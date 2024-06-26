#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
from typing import Union

import httpx
import certifi

from urllib.parse import urlparse

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

logger = logging.getLogger("tencentcloud_sdk_common")


def _get_proxy_from_env(host, varname="HTTPS_PROXY"):
    no_proxy = os.environ.get("NO_PROXY") or os.environ.get("no_proxy")
    if no_proxy and host in no_proxy:
        return None
    return os.environ.get(varname.lower()) or os.environ.get(varname.upper())


class ProxyConnection:
    def __init__(
            self,
            host: str,
            timeout: int = 60,
            proxy: Union[str, None] = None,
            certification: Union[str, None] = None,
            is_http: bool = False,
            pre_conn_pool_size: int = 0,
    ):
        self.request_host = host

        proxy = proxy or _get_proxy_from_env(host, varname="HTTP_PROXY" if is_http else "HTTPS_PROXY")
        client_kwargs = {
            # Implicitly disable loading CA bundle from the SSL_CERT_FILE and SSL_CERT_DIR env vars
            "verify": certifi.where() if certification is None else certification,
            "timeout": timeout,
            "proxy": {"http": proxy, "https": proxy} if proxy else None,
        }

        if certification:
            pass
        if pre_conn_pool_size > 0:
            client_kwargs["limits"] = httpx.Limits(max_keepalive_connections=pre_conn_pool_size)
        
        self._client = httpx.Client(**client_kwargs)
        self._async_client = httpx.AsyncClient(**client_kwargs)

    def request(self, method: str, url: str, body=None, headers: dict=None):
        if headers is None:
            headers = {}
        headers.setdefault("Host", self.request_host)
        return self._client.request(
            method=method, url=url, data=body, headers=headers
        )
    
    async def async_request(self, method: str, url: str, body=None, headers: dict=None):
        if headers is None:
            headers = {}
        headers.setdefault("Host", self.request_host)
        return await self._async_client.request(
            method=method, url=url, data=body, headers=headers
        )

class ApiRequest:
    def __init__(self, host, req_timeout=60, debug=False, proxy=None, is_http=False, certification=None,
                 pre_conn_pool_size=0):
        self.conn = ProxyConnection(host, timeout=req_timeout, proxy=proxy, certification=certification,
                                    is_http=is_http, pre_conn_pool_size=pre_conn_pool_size)
        self.is_http = is_http
        self.host = host
        self.req_timeout = req_timeout
        self.keep_alive = False
        self.debug = debug
        self.request_size = 0
        self.response_size = 0

    def _handle_host(self, host):
        url = urlparse(host)
        if not url.hostname:
            if self.is_http:
                return "http://" + host
            else:
                return "https://" + host
        return host

    def set_req_timeout(self, req_timeout):
        self.req_timeout = req_timeout

    def is_keep_alive(self):
        return self.keep_alive

    def set_keep_alive(self, flag=True):
        self.keep_alive = flag

    def set_debug(self, debug):
        self.debug = debug

    def _request(self, req_inter):
        url = self._handle_host(req_inter.host)
        if self.keep_alive:
            req_inter.header["Connection"] = "Keep-Alive"
        logger.debug("SendRequest: %s" % req_inter)
        if req_inter.method == 'GET':
            req_inter_url = '%s?%s' % (url, req_inter.data)
            return self.conn.request(req_inter.method, req_inter_url,
                                     None, req_inter.header)
        elif req_inter.method == 'POST':
            return self.conn.request(req_inter.method, url,
                                     req_inter.data, req_inter.header)
        raise TencentCloudSDKException(
                "ClientParamsError", 'Method only support (GET, POST)')
        
    async def _async_request(self, req_inter):
        url = self._handle_host(req_inter.host)
        if self.keep_alive:
            req_inter.header["Connection"] = "Keep-Alive"
        logger.debug("SendRequest: %s" % req_inter)
        if req_inter.method == 'GET':
            req_inter_url = '%s?%s' % (url, req_inter.data)
            return await self.conn.async_request(req_inter.method, req_inter_url,
                                                 None, req_inter.header)
        elif req_inter.method == 'POST':
            return await self.conn.async_request(req_inter.method, url,
                                                 req_inter.data, req_inter.header)
        raise TencentCloudSDKException(
                "ClientParamsError", 'Method only support (GET, POST)')
        

    def send_request(self, req_inter):
        try:
            http_resp = self._request(req_inter)
        except Exception as e:
            raise TencentCloudSDKException("ClientNetworkError", str(e)) from e
        return http_resp
    
    async def async_send_request(self, req_inter):
        try:
            http_resp = await self._async_request(req_inter)
        except Exception as e:
            raise TencentCloudSDKException("ClientNetworkError", str(e)) from e
        return http_resp


class RequestInternal(object):
    def __init__(self, host="", method="", uri="", header=None, data=""):
        if header is None:
            header = {}
        self.host = host
        self.method = method
        self.uri = uri
        self.header = header
        self.data = data

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("Host: %s\nMethod: %s\nUri: %s\nHeader: %s\nData: %s\n"
                % (self.host, self.method, self.uri, headers, self.data))


class ResponsePrettyFormatter(object):
    def __init__(self, resp, format_body=True, delimiter="\n"):
        self._resp = resp
        self._format_body = format_body
        self._delimiter = delimiter

    def __str__(self):
        lines = ['%s %d %s' % (self.str_ver(self._resp.raw.version), self._resp.status_code, self._resp.reason)]
        for k, v in self._resp.headers.items():
            lines.append('%s: %s' % (k, v))
        if self._format_body:
            lines.append('')
            lines.append(self._resp.text)
        return self._delimiter.join(lines)

    @staticmethod
    def str_ver(ver):
        if ver == 10:
            return "HTTP/1.0"
        elif ver == 11:
            return "HTTP/1.1"
        elif ver == 20:
            return "HTTP/2.0"
        else:
            return str(ver)
