import logging
import threading
from httpx import HTTPTransport

logger = logging.getLogger("tencentcloud_sdk_common")

class BasePreConnPool(HTTPTransport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._conn_producer = threading.Thread(target=self._conn_producer_loop)
        self._conn_producer.setDaemon(True)
        self._conn_producer.start()

    def _conn_producer_loop(self):
        while True:
            with self._pool._connections_lock:
                if len(self._pool._connections) < self._pool._max_connections:
                    conn = self._pool._create_connection()
                    conn.connect()
                    logger.debug(f"{self.__class__.__name__}: created a new conn")
                    self._pool._connections.append(conn)

class HTTPPreConnPool(BasePreConnPool):
    pass  # 实例化子类仅用于输出日志时与 HTTPSPreConnPool 有所区分，其他代码一致

class HTTPSPreConnPool(BasePreConnPool):
    pass  # 实例化子类仅用于输出日志时与 HTTPPreConnPool 有所区分，其他代码一致

class PreConnTransport(HTTPTransport):
    def __init__(self, pool_size, *args, **kwargs):
        self._pool_size = pool_size
        super().__init__(*args, **kwargs)
        self._init_pools()

    def _init_pools(self):
        self._http_pool = HTTPPreConnPool(max_connections=self._pool_size)
        self._https_pool = HTTPSPreConnPool(max_connections=self._pool_size)

    def handle_request(self, request):
        if request.url.scheme == "https":
            return self._https_pool.handle_request(request)
        elif request.url.scheme == "http":
            return self._http_pool.handle_request(request)
        raise NotImplementedError(f"Unsupported schema: {request.url.scheme}")

# Example usage
if __name__ == "__main__":
    from httpx import Client
    pre_conn_pool_size = 10
    client = (
        Client(transport=PreConnTransport(pool_size=pre_conn_pool_size))
        if pre_conn_pool_size > 0
        else Client()
    )
    response = client.get("https://www.example.com")
    print(response.status_code)
