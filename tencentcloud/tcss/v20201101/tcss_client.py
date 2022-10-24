# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tcss.v20201101 import models


class TcssClient(AbstractClient):
    _apiVersion = '2020-11-01'
    _endpoint = 'tcss.tencentcloudapi.com'
    _service = 'tcss'


    def AddAndPublishNetworkFirewallPolicyDetail(self, request):
        """容器网络创建网络策略添加并发布任务

        :param request: Request instance for AddAndPublishNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAndPublishNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddAndPublishNetworkFirewallPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddAndPublishNetworkFirewallPolicyYamlDetail(self, request):
        """容器网络创建Yaml网络策略并发布任务

        :param request: Request instance for AddAndPublishNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAndPublishNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddAndPublishNetworkFirewallPolicyYamlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddAssetImageRegistryRegistryDetail(self, request):
        """新增单个镜像仓库详细信息

        :param request: Request instance for AddAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddComplianceAssetPolicySetToWhitelist(self, request):
        """新增安全合规忽略(资产+检测项列表)列表，不显示指定的检查项包含的资产内容
        参考的AddCompliancePolicyItemToWhitelist，除输入字段外，其它应该是一致的，如果有不同可能是定义的不对

        :param request: Request instance for AddComplianceAssetPolicySetToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddComplianceAssetPolicySetToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddComplianceAssetPolicySetToWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddComplianceAssetPolicySetToWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddComplianceAssetPolicySetToWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddCompliancePolicyAssetSetToWhitelist(self, request):
        """新增安全合规忽略(检测项+资产)列表，不显示指定的检查项包含的资产内容
        参考的AddCompliancePolicyItemToWhitelist，除输入字段外，其它应该是一致的，如果有不同可能是定义的不对

        :param request: Request instance for AddCompliancePolicyAssetSetToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyAssetSetToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyAssetSetToWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCompliancePolicyAssetSetToWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCompliancePolicyAssetSetToWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddCompliancePolicyItemToWhitelist(self, request):
        """将指定的检测项添加到白名单中，不显示未通过结果。

        :param request: Request instance for AddCompliancePolicyItemToWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyItemToWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddCompliancePolicyItemToWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddCompliancePolicyItemToWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddCompliancePolicyItemToWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditAbnormalProcessRule(self, request):
        """添加编辑运行时异常进程策略

        :param request: Request instance for AddEditAbnormalProcessRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditAbnormalProcessRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditAbnormalProcessRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditAbnormalProcessRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditAbnormalProcessRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditAccessControlRule(self, request):
        """添加编辑运行时访问控制策略

        :param request: Request instance for AddEditAccessControlRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditAccessControlRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditAccessControlRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditAccessControlRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditAccessControlRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditImageAutoAuthorizedRule(self, request):
        """新增或编辑本地镜像自动授权规则

        :param request: Request instance for AddEditImageAutoAuthorizedRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditImageAutoAuthorizedRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditImageAutoAuthorizedRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditImageAutoAuthorizedRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditImageAutoAuthorizedRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditReverseShellWhiteList(self, request):
        """添加编辑运行时反弹shell白名单

        :param request: Request instance for AddEditReverseShellWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditReverseShellWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditReverseShellWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditReverseShellWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditReverseShellWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditRiskSyscallWhiteList(self, request):
        """添加编辑运行时高危系统调用白名单

        :param request: Request instance for AddEditRiskSyscallWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditRiskSyscallWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditRiskSyscallWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditRiskSyscallWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditRiskSyscallWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEditWarningRules(self, request):
        """添加编辑告警策略

        :param request: Request instance for AddEditWarningRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEditWarningRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEditWarningRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEditWarningRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEditWarningRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddEscapeWhiteList(self, request):
        """新增逃逸白名单

        :param request: Request instance for AddEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddEscapeWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddIgnoreVul(self, request):
        """新增漏洞扫描忽略漏洞

        :param request: Request instance for AddIgnoreVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddIgnoreVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddIgnoreVul", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddIgnoreVulResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddNetworkFirewallPolicyDetail(self, request):
        """容器网络创建网络策略添加任务

        :param request: Request instance for AddNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddNetworkFirewallPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddNetworkFirewallPolicyYamlDetail(self, request):
        """容器网络创建Yaml网络策略添加任务

        :param request: Request instance for AddNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.AddNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddNetworkFirewallPolicyYamlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckNetworkFirewallPolicyYaml(self, request):
        """容器网络创建检查Yaml网络策略任务

        :param request: Request instance for CheckNetworkFirewallPolicyYaml.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CheckNetworkFirewallPolicyYamlRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CheckNetworkFirewallPolicyYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckNetworkFirewallPolicyYaml", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckNetworkFirewallPolicyYamlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckRepeatAssetImageRegistry(self, request):
        """检查单个镜像仓库名是否重复

        :param request: Request instance for CheckRepeatAssetImageRegistry.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CheckRepeatAssetImageRegistryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CheckRepeatAssetImageRegistryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckRepeatAssetImageRegistry", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckRepeatAssetImageRegistryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ConfirmNetworkFirewallPolicy(self, request):
        """容器网络创建网络策略确认任务

        :param request: Request instance for ConfirmNetworkFirewallPolicy.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ConfirmNetworkFirewallPolicyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ConfirmNetworkFirewallPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmNetworkFirewallPolicy", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ConfirmNetworkFirewallPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageRegistryScanTask(self, request):
        """镜像仓库创建镜像扫描任务

        :param request: Request instance for CreateAssetImageRegistryScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageRegistryScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageRegistryScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageRegistryScanTaskOneKey(self, request):
        """镜像仓库创建镜像一键扫描任务

        :param request: Request instance for CreateAssetImageRegistryScanTaskOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageRegistryScanTaskOneKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageRegistryScanTaskOneKey", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageRegistryScanTaskOneKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageScanSetting(self, request):
        """添加容器安全镜像扫描设置

        :param request: Request instance for CreateAssetImageScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageScanSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageScanTask(self, request):
        """容器安全创建镜像扫描任务

        :param request: Request instance for CreateAssetImageScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssetImageVirusExportJob(self, request):
        """创建本地镜像木马列表导出任务

        :param request: Request instance for CreateAssetImageVirusExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageVirusExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateAssetImageVirusExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetImageVirusExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetImageVirusExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCheckComponent(self, request):
        """安装检查组件，创建防护容器

        :param request: Request instance for CreateCheckComponent.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateCheckComponentRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateCheckComponentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCheckComponent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCheckComponentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateClusterCheckTask(self, request):
        """创建集群检查任务，用户检查用户的集群相关风险项

        :param request: Request instance for CreateClusterCheckTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateClusterCheckTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateClusterCheckTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterCheckTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterCheckTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateComplianceTask(self, request):
        """创建合规检查任务，在资产级别触发重新检测时使用。

        :param request: Request instance for CreateComplianceTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateComplianceTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateComplianceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComplianceTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateComplianceTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateComponentExportJob(self, request):
        """查询本地镜像组件列表导出

        :param request: Request instance for CreateComponentExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateComponentExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateComponentExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateComponentExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateComponentExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDefenceVulExportJob(self, request):
        """创建支持防御的漏洞导出任务

        :param request: Request instance for CreateDefenceVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateDefenceVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateDefenceVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefenceVulExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefenceVulExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateEmergencyVulExportJob(self, request):
        """创建应急漏洞导出任务

        :param request: Request instance for CreateEmergencyVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateEmergencyVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateEmergencyVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmergencyVulExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmergencyVulExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateEscapeEventsExportJob(self, request):
        """创建逃逸事件导出异步任务

        :param request: Request instance for CreateEscapeEventsExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeEventsExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeEventsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEscapeEventsExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEscapeEventsExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateEscapeWhiteListExportJob(self, request):
        """创建逃逸白名单导出任务

        :param request: Request instance for CreateEscapeWhiteListExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeWhiteListExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateEscapeWhiteListExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEscapeWhiteListExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEscapeWhiteListExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExportComplianceStatusListJob(self, request):
        """创建一个导出安全合规信息的任务

        :param request: Request instance for CreateExportComplianceStatusListJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateExportComplianceStatusListJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateExportComplianceStatusListJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExportComplianceStatusListJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateExportComplianceStatusListJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHostExportJob(self, request):
        """创建主机列表导出任务

        :param request: Request instance for CreateHostExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateHostExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateHostExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHostExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImageExportJob(self, request):
        """创建镜像导出任务

        :param request: Request instance for CreateImageExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateImageExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateImageExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImageExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkFirewallClusterRefresh(self, request):
        """容器网络集群下发刷新任务

        :param request: Request instance for CreateNetworkFirewallClusterRefresh.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallClusterRefreshRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallClusterRefreshResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallClusterRefresh", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkFirewallClusterRefreshResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkFirewallPolicyDiscover(self, request):
        """容器网络集群网络策略创建自动发现任务

        :param request: Request instance for CreateNetworkFirewallPolicyDiscover.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPolicyDiscoverRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPolicyDiscoverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallPolicyDiscover", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkFirewallPolicyDiscoverResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkFirewallPublish(self, request):
        """容器网络创建网络策略发布任务

        :param request: Request instance for CreateNetworkFirewallPublish.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPublishRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallPublishResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallPublish", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkFirewallPublishResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkFirewallUndoPublish(self, request):
        """容器网络创建网络策略撤销任务

        :param request: Request instance for CreateNetworkFirewallUndoPublish.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallUndoPublishRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateNetworkFirewallUndoPublishResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkFirewallUndoPublish", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkFirewallUndoPublishResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOrModifyPostPayCores(self, request):
        """CreateOrModifyPostPayCores  创建或者编辑弹性计费上限

        :param request: Request instance for CreateOrModifyPostPayCores.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateOrModifyPostPayCoresRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateOrModifyPostPayCoresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrModifyPostPayCores", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateOrModifyPostPayCoresResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProcessEventsExportJob(self, request):
        """创建异常进程事件导出异步任务

        :param request: Request instance for CreateProcessEventsExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateProcessEventsExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateProcessEventsExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProcessEventsExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProcessEventsExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRefreshTask(self, request):
        """下发刷新任务，会刷新资产信息

        :param request: Request instance for CreateRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRefreshTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRefreshTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSearchTemplate(self, request):
        """添加检索模板

        :param request: Request instance for CreateSearchTemplate.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateSearchTemplateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSearchTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSystemVulExportJob(self, request):
        """创建系统漏洞导出任务

        :param request: Request instance for CreateSystemVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateSystemVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateSystemVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSystemVulExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSystemVulExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVirusScanAgain(self, request):
        """运行时文件查杀重新检测

        :param request: Request instance for CreateVirusScanAgain.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanAgainRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVirusScanAgain", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVirusScanAgainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVirusScanTask(self, request):
        """运行时文件查杀一键扫描

        :param request: Request instance for CreateVirusScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVirusScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVirusScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVirusScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVulContainerExportJob(self, request):
        """创建受漏洞影响的容器导出任务

        :param request: Request instance for CreateVulContainerExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulContainerExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulContainerExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulContainerExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulContainerExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVulDefenceEventExportJob(self, request):
        """创建漏洞防御导出任务

        :param request: Request instance for CreateVulDefenceEventExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceEventExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceEventExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulDefenceEventExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulDefenceEventExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVulDefenceHostExportJob(self, request):
        """创建漏洞防御主机导出任务

        :param request: Request instance for CreateVulDefenceHostExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceHostExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulDefenceHostExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulDefenceHostExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulDefenceHostExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVulExportJob(self, request):
        """查询本地镜像漏洞列表导出

        :param request: Request instance for CreateVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVulImageExportJob(self, request):
        """创建受漏洞影响的镜像导出任务

        :param request: Request instance for CreateVulImageExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulImageExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulImageExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulImageExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulImageExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVulScanTask(self, request):
        """创建漏洞扫描任务

        :param request: Request instance for CreateVulScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateVulScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateVulScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWebVulExportJob(self, request):
        """创建web漏洞导出任务

        :param request: Request instance for CreateWebVulExportJob.
        :type request: :class:`tencentcloud.tcss.v20201101.models.CreateWebVulExportJobRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.CreateWebVulExportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWebVulExportJob", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWebVulExportJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAbnormalProcessRules(self, request):
        """删除运行异常进程策略

        :param request: Request instance for DeleteAbnormalProcessRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteAbnormalProcessRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteAbnormalProcessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAbnormalProcessRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAbnormalProcessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccessControlRules(self, request):
        """删除运行访问控制策略

        :param request: Request instance for DeleteAccessControlRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteAccessControlRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteAccessControlRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccessControlRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessControlRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteComplianceAssetPolicySetFromWhitelist(self, request):
        """移除安全合规忽略(资产+检测项)列表，不显示指定的检查项包含的资产内容
        参考的AddCompliancePolicyAssetSetToWhitelist，除输入字段外，其它应该是一致的，如果有不同可能是定义的不对

        :param request: Request instance for DeleteComplianceAssetPolicySetFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteComplianceAssetPolicySetFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteComplianceAssetPolicySetFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteComplianceAssetPolicySetFromWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteComplianceAssetPolicySetFromWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCompliancePolicyAssetSetFromWhitelist(self, request):
        """新增安全合规忽略(检测项+资产)列表，不显示指定的检查项包含的资产内容

        :param request: Request instance for DeleteCompliancePolicyAssetSetFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyAssetSetFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyAssetSetFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompliancePolicyAssetSetFromWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCompliancePolicyAssetSetFromWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCompliancePolicyItemFromWhitelist(self, request):
        """从白名单中删除将指定的检测项。

        :param request: Request instance for DeleteCompliancePolicyItemFromWhitelist.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyItemFromWhitelistRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteCompliancePolicyItemFromWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCompliancePolicyItemFromWhitelist", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCompliancePolicyItemFromWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteEscapeWhiteList(self, request):
        """删除逃逸白名单

        :param request: Request instance for DeleteEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEscapeWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIgnoreVul(self, request):
        """取消漏洞扫描忽略漏洞

        :param request: Request instance for DeleteIgnoreVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteIgnoreVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIgnoreVul", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIgnoreVulResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMachine(self, request):
        """卸载Agent客户端

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachine", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMachineResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetworkFirewallPolicyDetail(self, request):
        """容器网络创建网络策略删除任务

        :param request: Request instance for DeleteNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkFirewallPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteReverseShellEvents(self, request):
        """删除运行时反弹shell事件

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteReverseShellWhiteLists(self, request):
        """删除运行时反弹shell白名单

        :param request: Request instance for DeleteReverseShellWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteReverseShellWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellWhiteLists", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReverseShellWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRiskSyscallEvents(self, request):
        """删除运行时高危系统调用事件

        :param request: Request instance for DeleteRiskSyscallEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskSyscallEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRiskSyscallEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRiskSyscallWhiteLists(self, request):
        """删除运行时高危系统调用白名单

        :param request: Request instance for DeleteRiskSyscallWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteRiskSyscallWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRiskSyscallWhiteLists", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRiskSyscallWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSearchTemplate(self, request):
        """删除检索模板

        :param request: Request instance for DeleteSearchTemplate.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DeleteSearchTemplateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DeleteSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSearchTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSearchTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeABTestConfig(self, request):
        """获取用户当前灰度配置

        :param request: Request instance for DescribeABTestConfig.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeABTestConfigRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeABTestConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeABTestConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeABTestConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessDetail(self, request):
        """查询运行时异常进程事件详细信息

        :param request: Request instance for DescribeAbnormalProcessDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessEventTendency(self, request):
        """查询待处理异常进程事件趋势

        :param request: Request instance for DescribeAbnormalProcessEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessEventTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessEventTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessEvents(self, request):
        """查询运行时异常进程事件列表信息

        :param request: Request instance for DescribeAbnormalProcessEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessEventsExport(self, request):
        """查询运行时异常进程事件列表信息导出

        :param request: Request instance for DescribeAbnormalProcessEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessEventsExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessLevelSummary(self, request):
        """统计异常进程各威胁等级待处理事件数

        :param request: Request instance for DescribeAbnormalProcessLevelSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessLevelSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessLevelSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessLevelSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessLevelSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessRuleDetail(self, request):
        """查询运行时异常策略详细信息

        :param request: Request instance for DescribeAbnormalProcessRuleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRuleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessRules(self, request):
        """查询运行时异常进程策略列表信息

        :param request: Request instance for DescribeAbnormalProcessRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAbnormalProcessRulesExport(self, request):
        """查询运行时异常进程策略列表信息导出

        :param request: Request instance for DescribeAbnormalProcessRulesExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAbnormalProcessRulesExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAbnormalProcessRulesExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAbnormalProcessRulesExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlDetail(self, request):
        """查询运行时访问控制事件的详细信息

        :param request: Request instance for DescribeAccessControlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlEvents(self, request):
        """查询运行时访问控制事件列表

        :param request: Request instance for DescribeAccessControlEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlEventsExport(self, request):
        """查询运行时访问控制事件列表导出

        :param request: Request instance for DescribeAccessControlEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlEventsExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlRuleDetail(self, request):
        """查询运行时访问控制策略详细信息

        :param request: Request instance for DescribeAccessControlRuleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRuleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlRuleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlRuleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlRules(self, request):
        """查询运行访问控制策略列表信息

        :param request: Request instance for DescribeAccessControlRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessControlRulesExport(self, request):
        """查询运行时访问控制策略列表导出

        :param request: Request instance for DescribeAccessControlRulesExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAccessControlRulesExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessControlRulesExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessControlRulesExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAffectedClusterCount(self, request):
        """获取受影响的集群数量，返回数量

        :param request: Request instance for DescribeAffectedClusterCount.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedClusterCountRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedClusterCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAffectedClusterCount", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAffectedClusterCountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAffectedNodeList(self, request):
        """查询节点类型的影响范围，返回节点列表

        :param request: Request instance for DescribeAffectedNodeList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedNodeListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedNodeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAffectedNodeList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAffectedNodeListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAffectedWorkloadList(self, request):
        """查询workload类型的影响范围，返回workload列表

        :param request: Request instance for DescribeAffectedWorkloadList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedWorkloadListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAffectedWorkloadListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAffectedWorkloadList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAffectedWorkloadListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentDaemonSetCmd(self, request):
        """查询平行容器安装命令

        :param request: Request instance for DescribeAgentDaemonSetCmd.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentDaemonSetCmdRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentDaemonSetCmdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentDaemonSetCmd", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentDaemonSetCmdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAgentInstallCommand(self, request):
        """查询agent安装命令

        :param request: Request instance for DescribeAgentInstallCommand.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentInstallCommandRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAgentInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstallCommand", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAgentInstallCommandResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetAppServiceList(self, request):
        """容器安全查询app服务列表

        :param request: Request instance for DescribeAssetAppServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetAppServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetAppServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppServiceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetAppServiceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetComponentList(self, request):
        """容器安全搜索查询容器组件列表

        :param request: Request instance for DescribeAssetComponentList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetComponentListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetComponentList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetComponentListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetContainerDetail(self, request):
        """查询容器详细信息

        :param request: Request instance for DescribeAssetContainerDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetContainerDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetContainerDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetContainerList(self, request):
        """搜索查询容器列表

        :param request: Request instance for DescribeAssetContainerList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetContainerList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetContainerListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetDBServiceList(self, request):
        """容器安全查询db服务列表

        :param request: Request instance for DescribeAssetDBServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetDBServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetDBServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDBServiceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetDBServiceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetHostDetail(self, request):
        """查询主机详细信息

        :param request: Request instance for DescribeAssetHostDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetHostDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetHostList(self, request):
        """容器安全搜索查询主机列表

        :param request: Request instance for DescribeAssetHostList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetHostListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageBindRuleInfo(self, request):
        """镜像绑定规则列表信息，包含运行时访问控制和异常进程公用

        :param request: Request instance for DescribeAssetImageBindRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageBindRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageBindRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageBindRuleInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageBindRuleInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageDetail(self, request):
        """查询镜像详细信息

        :param request: Request instance for DescribeAssetImageDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageHostList(self, request):
        """容器安全查询镜像关联主机

        :param request: Request instance for DescribeAssetImageHostList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageHostListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageHostList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageHostListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageList(self, request):
        """容器安全搜索查询镜像列表

        :param request: Request instance for DescribeAssetImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageListExport(self, request):
        """容器安全搜索查询镜像列表导出

        :param request: Request instance for DescribeAssetImageListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryAssetStatus(self, request):
        """查看镜像仓库资产更新进度状态

        :param request: Request instance for DescribeAssetImageRegistryAssetStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryAssetStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryAssetStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryAssetStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryAssetStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryDetail(self, request):
        """镜像仓库镜像仓库列表详情

        :param request: Request instance for DescribeAssetImageRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryList(self, request):
        """镜像仓库镜像仓库列表

        :param request: Request instance for DescribeAssetImageRegistryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryListExport(self, request):
        """镜像仓库镜像列表导出

        :param request: Request instance for DescribeAssetImageRegistryListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRegistryDetail(self, request):
        """查看单个镜像仓库详细信息

        :param request: Request instance for DescribeAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRegistryList(self, request):
        """镜像仓库仓库列表

        :param request: Request instance for DescribeAssetImageRegistryRegistryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRegistryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRegistryList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRegistryListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRiskInfoList(self, request):
        """镜像仓库查询镜像高危行为列表

        :param request: Request instance for DescribeAssetImageRegistryRiskInfoList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskInfoListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRiskInfoList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRiskInfoListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryRiskListExport(self, request):
        """镜像仓库敏感信息列表导出

        :param request: Request instance for DescribeAssetImageRegistryRiskListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryRiskListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryRiskListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryRiskListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryScanStatusOneKey(self, request):
        """镜像仓库查询一键镜像扫描状态

        :param request: Request instance for DescribeAssetImageRegistryScanStatusOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryScanStatusOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryScanStatusOneKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryScanStatusOneKey", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryScanStatusOneKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistrySummary(self, request):
        """镜像仓库查询镜像统计信息

        :param request: Request instance for DescribeAssetImageRegistrySummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistrySummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistrySummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistrySummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistrySummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVirusList(self, request):
        """镜像仓库查询木马病毒列表

        :param request: Request instance for DescribeAssetImageRegistryVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVirusList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVirusListExport(self, request):
        """镜像仓库木马信息列表导出

        :param request: Request instance for DescribeAssetImageRegistryVirusListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVirusListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVirusListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVirusListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVulList(self, request):
        """镜像仓库查询镜像漏洞列表

        :param request: Request instance for DescribeAssetImageRegistryVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVulList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRegistryVulListExport(self, request):
        """镜像仓库漏洞列表导出

        :param request: Request instance for DescribeAssetImageRegistryVulListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRegistryVulListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRegistryVulListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRegistryVulListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRiskList(self, request):
        """容器安全查询镜像风险列表

        :param request: Request instance for DescribeAssetImageRiskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRiskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRiskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageRiskListExport(self, request):
        """容器安全搜索查询镜像风险列表导出

        :param request: Request instance for DescribeAssetImageRiskListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageRiskListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageRiskListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageRiskListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageScanSetting(self, request):
        """获取镜像扫描设置信息

        :param request: Request instance for DescribeAssetImageScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageScanSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageScanStatus(self, request):
        """容器安全查询镜像扫描状态

        :param request: Request instance for DescribeAssetImageScanStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageScanStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageScanStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageScanTask(self, request):
        """查询正在一键扫描的镜像扫描taskid

        :param request: Request instance for DescribeAssetImageScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageSimpleList(self, request):
        """容器安全搜索查询镜像简略信息列表

        :param request: Request instance for DescribeAssetImageSimpleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageSimpleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageSimpleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageSimpleList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageSimpleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVirusList(self, request):
        """容器安全查询镜像病毒列表

        :param request: Request instance for DescribeAssetImageVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVirusList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVirusListExport(self, request):
        """容器安全搜索查询镜像木马列表导出

        :param request: Request instance for DescribeAssetImageVirusListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVirusListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVirusListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVirusListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVulList(self, request):
        """容器安全查询镜像漏洞列表

        :param request: Request instance for DescribeAssetImageVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVulList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetImageVulListExport(self, request):
        """容器安全搜索查询镜像漏洞列表导出

        :param request: Request instance for DescribeAssetImageVulListExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetImageVulListExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetImageVulListExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetImageVulListExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetPortList(self, request):
        """容器安全搜索查询端口占用列表

        :param request: Request instance for DescribeAssetPortList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetPortListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetPortListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetPortListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetProcessList(self, request):
        """容器安全搜索查询进程列表

        :param request: Request instance for DescribeAssetProcessList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetProcessListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetProcessListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetSummary(self, request):
        """查询账户容器、镜像等统计信息

        :param request: Request instance for DescribeAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetSyncLastTime(self, request):
        """查询资产同步最近时间

        :param request: Request instance for DescribeAssetSyncLastTime.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSyncLastTimeRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetSyncLastTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSyncLastTime", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetSyncLastTimeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssetWebServiceList(self, request):
        """容器安全查询web服务列表

        :param request: Request instance for DescribeAssetWebServiceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetWebServiceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAssetWebServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetWebServiceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoAuthorizedRuleHost(self, request):
        """查询自动授权规则授权范围主机信息

        :param request: Request instance for DescribeAutoAuthorizedRuleHost.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeAutoAuthorizedRuleHostRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeAutoAuthorizedRuleHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoAuthorizedRuleHost", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoAuthorizedRuleHostResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCheckItemList(self, request):
        """查询所有检查项接口，返回总数和检查项列表

        :param request: Request instance for DescribeCheckItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCheckItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCheckItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCheckItemList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCheckItemListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterDetail(self, request):
        """查询单个集群的详细信息

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterSummary(self, request):
        """查询用户集群资产总览

        :param request: Request instance for DescribeClusterSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeClusterSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceAssetDetailInfo(self, request):
        """查询某个资产的详情

        :param request: Request instance for DescribeComplianceAssetDetailInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetDetailInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceAssetDetailInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetDetailInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceAssetList(self, request):
        """查询某类资产的列表

        :param request: Request instance for DescribeComplianceAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceAssetList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceAssetPolicyItemList(self, request):
        """查询某资产下的检测项列表

        :param request: Request instance for DescribeComplianceAssetPolicyItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetPolicyItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceAssetPolicyItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceAssetPolicyItemList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceAssetPolicyItemListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompliancePeriodTaskList(self, request):
        """查询合规检测的定时任务列表

        :param request: Request instance for DescribeCompliancePeriodTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePeriodTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePeriodTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePeriodTaskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCompliancePeriodTaskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompliancePolicyItemAffectedAssetList(self, request):
        """按照 检测项 → 资产 的两级层次展开的第二层级：资产层级。

        :param request: Request instance for DescribeCompliancePolicyItemAffectedAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePolicyItemAffectedAssetList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCompliancePolicyItemAffectedAssetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCompliancePolicyItemAffectedSummary(self, request):
        """按照 检测项 → 资产 的两级层次展开的第一层级：检测项层级。

        :param request: Request instance for DescribeCompliancePolicyItemAffectedSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeCompliancePolicyItemAffectedSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompliancePolicyItemAffectedSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCompliancePolicyItemAffectedSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceScanFailedAssetList(self, request):
        """按照 资产 → 检测项 二层结构展示的信息。这里查询第一层 资产的通过率汇总信息。

        :param request: Request instance for DescribeComplianceScanFailedAssetList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceScanFailedAssetListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceScanFailedAssetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceScanFailedAssetList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceScanFailedAssetListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceTaskAssetSummary(self, request):
        """查询上次任务的资产通过率汇总信息

        :param request: Request instance for DescribeComplianceTaskAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceTaskAssetSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceTaskAssetSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceTaskPolicyItemSummaryList(self, request):
        """查询最近一次任务发现的检测项的汇总信息列表，按照 检测项 → 资产 的两级层次展开。

        :param request: Request instance for DescribeComplianceTaskPolicyItemSummaryList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskPolicyItemSummaryListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceTaskPolicyItemSummaryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceTaskPolicyItemSummaryList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceTaskPolicyItemSummaryListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeComplianceWhitelistItemList(self, request):
        """查询白名单列表

        :param request: Request instance for DescribeComplianceWhitelistItemList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceWhitelistItemListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeComplianceWhitelistItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComplianceWhitelistItemList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComplianceWhitelistItemListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContainerAssetSummary(self, request):
        """查询容器资产概览信息

        :param request: Request instance for DescribeContainerAssetSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerAssetSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerAssetSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerAssetSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerAssetSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContainerSecEventSummary(self, request):
        """查询容器安全未处理事件信息

        :param request: Request instance for DescribeContainerSecEventSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerSecEventSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeContainerSecEventSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerSecEventSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerSecEventSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeESAggregations(self, request):
        """获取ES字段聚合结果

        :param request: Request instance for DescribeESAggregations.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeESAggregationsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeESAggregationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESAggregations", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeESAggregationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeESHits(self, request):
        """获取ES查询文档列表

        :param request: Request instance for DescribeESHits.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeESHitsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeESHitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESHits", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeESHitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEmergencyVulList(self, request):
        """查询应急漏洞列表

        :param request: Request instance for DescribeEmergencyVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEmergencyVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEmergencyVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyVulList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEmergencyVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventDetail(self, request):
        """DescribeEscapeEventDetail  查询容器逃逸事件详情

        :param request: Request instance for DescribeEscapeEventDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventInfo(self, request):
        """DescribeEscapeEventInfo 查询容器逃逸事件列表

        :param request: Request instance for DescribeEscapeEventInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventTendency(self, request):
        """查询待处理逃逸事件趋势

        :param request: Request instance for DescribeEscapeEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventTypeSummary(self, request):
        """统计容器逃逸各事件类型和待处理事件数

        :param request: Request instance for DescribeEscapeEventTypeSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTypeSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventTypeSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventTypeSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventTypeSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeEventsExport(self, request):
        """DescribeEscapeEventsExport  查询容器逃逸事件列表导出

        :param request: Request instance for DescribeEscapeEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeEventsExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeRuleInfo(self, request):
        """DescribeEscapeRuleInfo 查询容器逃逸扫描规则信息

        :param request: Request instance for DescribeEscapeRuleInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeRuleInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeRuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeRuleInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeRuleInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeSafeState(self, request):
        """DescribeEscapeSafeState 查询容器逃逸安全状态

        :param request: Request instance for DescribeEscapeSafeState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeSafeStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeSafeStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeSafeState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeSafeStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEscapeWhiteList(self, request):
        """查询逃逸白名单

        :param request: Request instance for DescribeEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEscapeWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExportJobResult(self, request):
        """查询导出任务的结果

        :param request: Request instance for DescribeExportJobResult.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobResultRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeExportJobResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportJobResult", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExportJobResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageAuthorizedInfo(self, request):
        """DescribeImageAuthorizedInfo  查询镜像授权信息

        :param request: Request instance for DescribeImageAuthorizedInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAuthorizedInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAuthorizedInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAuthorizedInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageAuthorizedInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageAutoAuthorizedLogList(self, request):
        """查询镜像自动授权结果列表

        :param request: Request instance for DescribeImageAutoAuthorizedLogList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedLogListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAutoAuthorizedLogList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageAutoAuthorizedLogListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageAutoAuthorizedRule(self, request):
        """查询本地镜像自动授权规则

        :param request: Request instance for DescribeImageAutoAuthorizedRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAutoAuthorizedRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageAutoAuthorizedRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageAutoAuthorizedTaskList(self, request):
        """查询镜像自动授权任务列表

        :param request: Request instance for DescribeImageAutoAuthorizedTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageAutoAuthorizedTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAutoAuthorizedTaskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageAutoAuthorizedTaskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageComponentList(self, request):
        """查询本地镜像组件列表

        :param request: Request instance for DescribeImageComponentList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageComponentListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageComponentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageComponentList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageComponentListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRegistryNamespaceList(self, request):
        """查询用户镜像仓库下的项目名称列表

        :param request: Request instance for DescribeImageRegistryNamespaceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryNamespaceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryNamespaceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRegistryNamespaceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRegistryTimingScanTask(self, request):
        """镜像仓库查看定时任务

        :param request: Request instance for DescribeImageRegistryTimingScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryTimingScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRegistryTimingScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRegistryTimingScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRegistryTimingScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRiskSummary(self, request):
        """查询本地镜像风险概览

        :param request: Request instance for DescribeImageRiskSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRiskSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRiskSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageRiskTendency(self, request):
        """查询容器安全本地镜像风险趋势

        :param request: Request instance for DescribeImageRiskTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageRiskTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageRiskTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRiskTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageSimpleList(self, request):
        """DescribeImageSimpleList 查询全部镜像列表

        :param request: Request instance for DescribeImageSimpleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeImageSimpleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeImageSimpleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageSimpleList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSimpleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIndexList(self, request):
        """获取索引列表

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeIndexListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIndexListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInspectionReport(self, request):
        """查询检查报告

        :param request: Request instance for DescribeInspectionReport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeInspectionReportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeInspectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInspectionReport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInspectionReportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogStorageStatistic(self, request):
        """获取日志检索容量使用统计

        :param request: Request instance for DescribeLogStorageStatistic.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeLogStorageStatisticRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeLogStorageStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageStatistic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogStorageStatisticResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallAuditRecord(self, request):
        """查询集群策略审计列表

        :param request: Request instance for DescribeNetworkFirewallAuditRecord.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallAuditRecordRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallAuditRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallAuditRecord", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallAuditRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallClusterList(self, request):
        """查询集群策略列表

        :param request: Request instance for DescribeNetworkFirewallClusterList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallClusterList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallClusterListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallClusterRefreshStatus(self, request):
        """容器网络查询资产任务进度

        :param request: Request instance for DescribeNetworkFirewallClusterRefreshStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterRefreshStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallClusterRefreshStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallClusterRefreshStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallClusterRefreshStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallNamespaceLabelList(self, request):
        """查询集群网络空间标签列表

        :param request: Request instance for DescribeNetworkFirewallNamespaceLabelList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallNamespaceLabelListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallNamespaceLabelListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallNamespaceLabelList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallNamespaceLabelListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallNamespaceList(self, request):
        """查询集群网络空间列表

        :param request: Request instance for DescribeNetworkFirewallNamespaceList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallNamespaceListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallNamespaceList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallNamespaceListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallPodLabelsList(self, request):
        """查询集群网络pod标签

        :param request: Request instance for DescribeNetworkFirewallPodLabelsList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPodLabelsListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPodLabelsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPodLabelsList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallPodLabelsListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallPolicyDetail(self, request):
        """容器网络集群查看策略详情

        :param request: Request instance for DescribeNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallPolicyDiscover(self, request):
        """容器网络查询网络策略自动发现任务进度

        :param request: Request instance for DescribeNetworkFirewallPolicyDiscover.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDiscoverRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyDiscoverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyDiscover", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallPolicyDiscoverResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallPolicyList(self, request):
        """查询集群网络策略列表

        :param request: Request instance for DescribeNetworkFirewallPolicyList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallPolicyListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallPolicyStatus(self, request):
        """容器网络查询网络策略策略执行状态

        :param request: Request instance for DescribeNetworkFirewallPolicyStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallPolicyStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkFirewallPolicyYamlDetail(self, request):
        """容器网络集群查看Yaml网络策略详情

        :param request: Request instance for DescribeNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkFirewallPolicyYamlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNewestVul(self, request):
        """查询最新披露漏洞列表

        :param request: Request instance for DescribeNewestVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeNewestVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeNewestVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNewestVul", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNewestVulResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePostPayDetail(self, request):
        """DescribePostPayDetail  查询后付费详情

        :param request: Request instance for DescribePostPayDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePostPayDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePostPayDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostPayDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePostPayDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProVersionInfo(self, request):
        """DescribeProVersionInfo  查询专业版需购买信息

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProVersionInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePromotionActivity(self, request):
        """查询促销活动

        :param request: Request instance for DescribePromotionActivity.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePromotionActivityRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePromotionActivityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePromotionActivity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePromotionActivityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePublicKey(self, request):
        """获取公钥

        :param request: Request instance for DescribePublicKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePublicKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePublicKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicKey", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePurchaseStateInfo(self, request):
        """DescribePurchaseStateInfo 查询容器安全服务已购买信息

        :param request: Request instance for DescribePurchaseStateInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribePurchaseStateInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribePurchaseStateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePurchaseStateInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePurchaseStateInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRefreshTask(self, request):
        """查询刷新任务

        :param request: Request instance for DescribeRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRefreshTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRefreshTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellDetail(self, request):
        """查询运行时反弹shell事件详细信息

        :param request: Request instance for DescribeReverseShellDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellEvents(self, request):
        """查询运行时反弹shell事件列表信息

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellEventsExport(self, request):
        """查询运行时反弹shell事件列表信息导出

        :param request: Request instance for DescribeReverseShellEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEventsExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellWhiteListDetail(self, request):
        """查询运行时反弹shell白名单详细信息

        :param request: Request instance for DescribeReverseShellWhiteListDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellWhiteListDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellWhiteListDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReverseShellWhiteLists(self, request):
        """查询运行时运行时反弹shell白名单列表信息

        :param request: Request instance for DescribeReverseShellWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeReverseShellWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellWhiteLists", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReverseShellWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskList(self, request):
        """查询最近一次任务发现的风险项的信息列表，支持根据特殊字段进行过滤

        :param request: Request instance for DescribeRiskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallDetail(self, request):
        """查询高危系统调用事件详细信息

        :param request: Request instance for DescribeRiskSyscallDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallEvents(self, request):
        """查询运行时运行时高危系统调用列表信息

        :param request: Request instance for DescribeRiskSyscallEvents.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallEvents", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallEventsExport(self, request):
        """运行时高危系统调用列表导出

        :param request: Request instance for DescribeRiskSyscallEventsExport.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsExportRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallEventsExportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallEventsExport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallEventsExportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallNames(self, request):
        """查询运行时高危系统调用系统名称列表

        :param request: Request instance for DescribeRiskSyscallNames.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallNamesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallNames", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallNamesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallWhiteListDetail(self, request):
        """查询运行时高危系统调用白名单详细信息

        :param request: Request instance for DescribeRiskSyscallWhiteListDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallWhiteListDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallWhiteListDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRiskSyscallWhiteLists(self, request):
        """查询运行时高危系统调用白名单列表信息

        :param request: Request instance for DescribeRiskSyscallWhiteLists.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeRiskSyscallWhiteListsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskSyscallWhiteLists", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRiskSyscallWhiteListsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScanIgnoreVulList(self, request):
        """查询扫描忽略的漏洞列表

        :param request: Request instance for DescribeScanIgnoreVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeScanIgnoreVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeScanIgnoreVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanIgnoreVulList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanIgnoreVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSearchExportList(self, request):
        """导出ES查询文档列表

        :param request: Request instance for DescribeSearchExportList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchExportListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchExportListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchExportList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSearchExportListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSearchLogs(self, request):
        """获取历史搜索记录

        :param request: Request instance for DescribeSearchLogs.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchLogsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchLogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSearchLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSearchTemplates(self, request):
        """获取快速检索列表

        :param request: Request instance for DescribeSearchTemplates.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchTemplatesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSearchTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSearchTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecEventsTendency(self, request):
        """查询容器运行时安全事件趋势

        :param request: Request instance for DescribeSecEventsTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecEventsTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecEventsTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecEventsTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecEventsTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogAlertMsg(self, request):
        """查询安全日志告警信息

        :param request: Request instance for DescribeSecLogAlertMsg.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogAlertMsgRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogAlertMsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogAlertMsg", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogAlertMsgResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogCleanSettingInfo(self, request):
        """查询安全日志清理设置详情

        :param request: Request instance for DescribeSecLogCleanSettingInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogCleanSettingInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogCleanSettingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogCleanSettingInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogCleanSettingInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogDeliveryClsOptions(self, request):
        """查询安全日志投递cls可选项

        :param request: Request instance for DescribeSecLogDeliveryClsOptions.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsOptionsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryClsOptions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogDeliveryClsOptionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogDeliveryClsSetting(self, request):
        """查询安全日志投递Cls配置

        :param request: Request instance for DescribeSecLogDeliveryClsSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryClsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryClsSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogDeliveryClsSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogDeliveryKafkaOptions(self, request):
        """查询安全日志投递kafka可选项

        :param request: Request instance for DescribeSecLogDeliveryKafkaOptions.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaOptionsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryKafkaOptions", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogDeliveryKafkaOptionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogDeliveryKafkaSetting(self, request):
        """查询安全日志投递kafka配置

        :param request: Request instance for DescribeSecLogDeliveryKafkaSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogDeliveryKafkaSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogDeliveryKafkaSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogDeliveryKafkaSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogJoinObjectList(self, request):
        """查询安全日志接入对象列表

        :param request: Request instance for DescribeSecLogJoinObjectList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinObjectListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinObjectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogJoinObjectList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogJoinObjectListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogJoinTypeList(self, request):
        """查询安全日志接入列表

        :param request: Request instance for DescribeSecLogJoinTypeList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinTypeListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogJoinTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogJoinTypeList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogJoinTypeListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogKafkaUIN(self, request):
        """查询安全日志KafkaUIN

        :param request: Request instance for DescribeSecLogKafkaUIN.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogKafkaUINRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogKafkaUINResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogKafkaUIN", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogKafkaUINResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecLogVasInfo(self, request):
        """查询安全日志商品信息

        :param request: Request instance for DescribeSecLogVasInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogVasInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSecLogVasInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecLogVasInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecLogVasInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSupportDefenceVul(self, request):
        """查询支持防御的漏洞列表

        :param request: Request instance for DescribeSupportDefenceVul.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSupportDefenceVulRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSupportDefenceVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportDefenceVul", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSupportDefenceVulResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSystemVulList(self, request):
        """查询系统漏洞列表

        :param request: Request instance for DescribeSystemVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeSystemVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeSystemVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemVulList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSystemVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResultSummary(self, request):
        """查询检查结果总览，返回受影响的节点数量，返回7天的数据，总共7个

        :param request: Request instance for DescribeTaskResultSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeTaskResultSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeTaskResultSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResultSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTcssSummary(self, request):
        """查询容器安全概览信息

        :param request: Request instance for DescribeTcssSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeTcssSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeTcssSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTcssSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTcssSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUnauthorizedCoresTendency(self, request):
        """查询当天未授权核数趋势

        :param request: Request instance for DescribeUnauthorizedCoresTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUnauthorizedCoresTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUnauthorizedCoresTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnauthorizedCoresTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnauthorizedCoresTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUnfinishRefreshTask(self, request):
        """查询未完成的刷新资产任务信息

        :param request: Request instance for DescribeUnfinishRefreshTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUnfinishRefreshTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUnfinishRefreshTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnfinishRefreshTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnfinishRefreshTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserCluster(self, request):
        """安全概览和集群安全页进入调用该接口，查询用户集群相关信息。

        :param request: Request instance for DescribeUserCluster.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeUserClusterRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeUserClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeValueAddedSrvInfo(self, request):
        """DescribeValueAddedSrvInfo查询增值服务需购买信息

        :param request: Request instance for DescribeValueAddedSrvInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeValueAddedSrvInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeValueAddedSrvInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeValueAddedSrvInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeValueAddedSrvInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusAutoIsolateSampleDetail(self, request):
        """查询木马自动隔离样本详情

        :param request: Request instance for DescribeVirusAutoIsolateSampleDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSampleDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusAutoIsolateSampleDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusAutoIsolateSampleDownloadURL(self, request):
        """查询木马自动隔离样本下载链接

        :param request: Request instance for DescribeVirusAutoIsolateSampleDownloadURL.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDownloadURLRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSampleDownloadURL", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusAutoIsolateSampleDownloadURLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusAutoIsolateSampleList(self, request):
        """查询木马自动隔离样本列表

        :param request: Request instance for DescribeVirusAutoIsolateSampleList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSampleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSampleList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusAutoIsolateSampleListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusAutoIsolateSetting(self, request):
        """查询木马自动隔离设置

        :param request: Request instance for DescribeVirusAutoIsolateSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusAutoIsolateSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusAutoIsolateSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusAutoIsolateSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusDetail(self, request):
        """运行时查询木马文件信息

        :param request: Request instance for DescribeVirusDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusEventTendency(self, request):
        """查询木马事件趋势

        :param request: Request instance for DescribeVirusEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusEventTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusEventTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusList(self, request):
        """查询运行时文件查杀事件列表

        :param request: Request instance for DescribeVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusManualScanEstimateTimeout(self, request):
        """查询木马一键检测预估超时时间

        :param request: Request instance for DescribeVirusManualScanEstimateTimeout.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusManualScanEstimateTimeoutRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusManualScanEstimateTimeoutResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusManualScanEstimateTimeout", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusManualScanEstimateTimeoutResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusMonitorSetting(self, request):
        """运行时查询文件查杀实时监控设置

        :param request: Request instance for DescribeVirusMonitorSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusMonitorSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusMonitorSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusMonitorSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusMonitorSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusSampleDownloadUrl(self, request):
        """查询木马样本下载url

        :param request: Request instance for DescribeVirusSampleDownloadUrl.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSampleDownloadUrlRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSampleDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusSampleDownloadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusSampleDownloadUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusScanSetting(self, request):
        """运行时查询文件查杀设置

        :param request: Request instance for DescribeVirusScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusScanSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusScanTaskStatus(self, request):
        """运行时查询文件查杀任务状态

        :param request: Request instance for DescribeVirusScanTaskStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusScanTaskStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusScanTimeoutSetting(self, request):
        """运行时文件扫描超时设置查询

        :param request: Request instance for DescribeVirusScanTimeoutSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTimeoutSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusScanTimeoutSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusScanTimeoutSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusScanTimeoutSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusSummary(self, request):
        """运行时查询木马概览信息

        :param request: Request instance for DescribeVirusSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVirusTaskList(self, request):
        """运行时查询文件查杀任务列表

        :param request: Request instance for DescribeVirusTaskList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusTaskListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVirusTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVirusTaskList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVirusTaskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulContainerList(self, request):
        """查询受漏洞的容器列表

        :param request: Request instance for DescribeVulContainerList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulContainerListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulContainerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulContainerList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulContainerListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDefenceEvent(self, request):
        """查询漏洞防御事件列表

        :param request: Request instance for DescribeVulDefenceEvent.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDefenceEventResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDefenceEventDetail(self, request):
        """查询漏洞防御事件详情

        :param request: Request instance for DescribeVulDefenceEventDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEventDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDefenceEventDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDefenceEventTendency(self, request):
        """查询漏洞防御攻击事件趋势

        :param request: Request instance for DescribeVulDefenceEventTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceEventTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceEventTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDefenceEventTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDefenceHost(self, request):
        """查询漏洞防御的主机列表

        :param request: Request instance for DescribeVulDefenceHost.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceHostRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceHost", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDefenceHostResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDefencePlugin(self, request):
        """查询漏洞防御插件列表

        :param request: Request instance for DescribeVulDefencePlugin.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefencePluginRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefencePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefencePlugin", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDefencePluginResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDefenceSetting(self, request):
        """查询漏洞防御设置信息

        :param request: Request instance for DescribeVulDefenceSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDefenceSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDefenceSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDefenceSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulDetail(self, request):
        """查询漏洞详情

        :param request: Request instance for DescribeVulDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulIgnoreLocalImageList(self, request):
        """查询漏洞扫描忽略的本地镜像列表

        :param request: Request instance for DescribeVulIgnoreLocalImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreLocalImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreLocalImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulIgnoreLocalImageList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulIgnoreLocalImageListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulIgnoreRegistryImageList(self, request):
        """查询漏洞扫描忽略的仓库镜像列表

        :param request: Request instance for DescribeVulIgnoreRegistryImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreRegistryImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulIgnoreRegistryImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulIgnoreRegistryImageList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulIgnoreRegistryImageListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulImageList(self, request):
        """查询漏洞影响的镜像列表

        :param request: Request instance for DescribeVulImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulImageList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulImageListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulImageSummary(self, request):
        """查询漏洞镜像统计

        :param request: Request instance for DescribeVulImageSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulImageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulImageSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulImageSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulLevelImageSummary(self, request):
        """查询应急漏洞各威胁等级统计镜像数

        :param request: Request instance for DescribeVulLevelImageSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelImageSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelImageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelImageSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulLevelImageSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulLevelSummary(self, request):
        """查询漏洞各威胁等级统计数

        :param request: Request instance for DescribeVulLevelSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulLevelSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulLevelSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulScanAuthorizedImageSummary(self, request):
        """统计漏洞扫描页已授权和未扫描镜像数

        :param request: Request instance for DescribeVulScanAuthorizedImageSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanAuthorizedImageSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanAuthorizedImageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanAuthorizedImageSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulScanAuthorizedImageSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulScanInfo(self, request):
        """查询漏洞扫描任务信息

        :param request: Request instance for DescribeVulScanInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulScanInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulScanLocalImageList(self, request):
        """查询漏洞扫描任务的本地镜像列表

        :param request: Request instance for DescribeVulScanLocalImageList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanLocalImageListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulScanLocalImageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulScanLocalImageList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulScanLocalImageListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulSummary(self, request):
        """查询漏洞风险统计概览

        :param request: Request instance for DescribeVulSummary.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulSummaryRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulSummary", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulTendency(self, request):
        """查询本地镜像、仓库镜像中严重&高危的漏洞趋势

        :param request: Request instance for DescribeVulTendency.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTendencyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTendencyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTendency", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulTendencyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVulTopRanking(self, request):
        """查询漏洞Top排名列表

        :param request: Request instance for DescribeVulTopRanking.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTopRankingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeVulTopRankingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTopRanking", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulTopRankingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWarningRules(self, request):
        """获取告警策略列表

        :param request: Request instance for DescribeWarningRules.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeWarningRulesRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeWarningRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningRules", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWarningRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWebVulList(self, request):
        """查询web应用漏洞列表

        :param request: Request instance for DescribeWebVulList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.DescribeWebVulListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.DescribeWebVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebVulList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWebVulListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportVirusList(self, request):
        """运行时文件查杀事件列表导出

        :param request: Request instance for ExportVirusList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ExportVirusListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ExportVirusListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVirusList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVirusListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InitializeUserComplianceEnvironment(self, request):
        """为客户初始化合规基线的使用环境，创建必要的数据和选项。

        :param request: Request instance for InitializeUserComplianceEnvironment.
        :type request: :class:`tencentcloud.tcss.v20201101.models.InitializeUserComplianceEnvironmentRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.InitializeUserComplianceEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitializeUserComplianceEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitializeUserComplianceEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAbnormalProcessRuleStatus(self, request):
        """修改运行时异常进程策略的开启关闭状态

        :param request: Request instance for ModifyAbnormalProcessRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAbnormalProcessRuleStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAbnormalProcessRuleStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAbnormalProcessStatus(self, request):
        """修改异常进程事件的状态信息

        :param request: Request instance for ModifyAbnormalProcessStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAbnormalProcessStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAbnormalProcessStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAbnormalProcessStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessControlRuleStatus(self, request):
        """修改运行时访问控制策略的状态，启用或者禁用

        :param request: Request instance for ModifyAccessControlRuleStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlRuleStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlRuleStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessControlRuleStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessControlRuleStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessControlStatus(self, request):
        """修改运行时访问控制事件状态信息

        :param request: Request instance for ModifyAccessControlStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAccessControlStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessControlStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessControlStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAsset(self, request):
        """容器安全主机资产刷新

        :param request: Request instance for ModifyAsset.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAsset", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssetImageRegistryScanStop(self, request):
        """镜像仓库停止镜像扫描任务

        :param request: Request instance for ModifyAssetImageRegistryScanStop.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetImageRegistryScanStop", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetImageRegistryScanStopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssetImageRegistryScanStopOneKey(self, request):
        """镜像仓库停止镜像一键扫描任务

        :param request: Request instance for ModifyAssetImageRegistryScanStopOneKey.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopOneKeyRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageRegistryScanStopOneKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetImageRegistryScanStopOneKey", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetImageRegistryScanStopOneKeyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssetImageScanStop(self, request):
        """容器安全停止镜像扫描

        :param request: Request instance for ModifyAssetImageScanStop.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageScanStopRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyAssetImageScanStopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssetImageScanStop", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssetImageScanStopResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCompliancePeriodTask(self, request):
        """修改定时任务的设置，包括检测周期、开启/禁用合规基准。

        :param request: Request instance for ModifyCompliancePeriodTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyCompliancePeriodTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyCompliancePeriodTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCompliancePeriodTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCompliancePeriodTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyContainerNetStatus(self, request):
        """隔离容器网络状态

        :param request: Request instance for ModifyContainerNetStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyContainerNetStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyContainerNetStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyContainerNetStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerNetStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEscapeEventStatus(self, request):
        """ModifyEscapeEventStatus  修改容器逃逸扫描事件状态

        :param request: Request instance for ModifyEscapeEventStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeEventStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEscapeEventStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEscapeEventStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEscapeRule(self, request):
        """ModifyEscapeRule  修改容器逃逸扫描规则信息

        :param request: Request instance for ModifyEscapeRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEscapeRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEscapeRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEscapeWhiteList(self, request):
        """修改逃逸白名单

        :param request: Request instance for ModifyEscapeWhiteList.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeWhiteListRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyEscapeWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEscapeWhiteList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEscapeWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyImageAuthorized(self, request):
        """批量授权镜像扫描V2.0

        :param request: Request instance for ModifyImageAuthorized.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyImageAuthorizedRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyImageAuthorizedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageAuthorized", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageAuthorizedResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyReverseShellStatus(self, request):
        """修改反弹shell事件的状态信息

        :param request: Request instance for ModifyReverseShellStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyReverseShellStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyReverseShellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReverseShellStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyReverseShellStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRiskSyscallStatus(self, request):
        """修改高危系统调用事件的状态信息

        :param request: Request instance for ModifyRiskSyscallStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyRiskSyscallStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyRiskSyscallStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRiskSyscallStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRiskSyscallStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecLogCleanSettingInfo(self, request):
        """修改安全日志清理设置信息

        :param request: Request instance for ModifySecLogCleanSettingInfo.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogCleanSettingInfoRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogCleanSettingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogCleanSettingInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecLogCleanSettingInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecLogDeliveryClsSetting(self, request):
        """更新安全日志-日志投递cls配置

        :param request: Request instance for ModifySecLogDeliveryClsSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryClsSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryClsSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogDeliveryClsSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecLogDeliveryClsSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecLogDeliveryKafkaSetting(self, request):
        """更新安全日志投递kafka设置

        :param request: Request instance for ModifySecLogDeliveryKafkaSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryKafkaSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogDeliveryKafkaSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogDeliveryKafkaSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecLogDeliveryKafkaSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecLogJoinObjects(self, request):
        """修改安全日志接入对象

        :param request: Request instance for ModifySecLogJoinObjects.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinObjectsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogJoinObjects", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecLogJoinObjectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecLogJoinState(self, request):
        """修改安全日志接入状态

        :param request: Request instance for ModifySecLogJoinState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogJoinStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogJoinState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecLogJoinStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecLogKafkaUIN(self, request):
        """修改安全日志kafkaUIN

        :param request: Request instance for ModifySecLogKafkaUIN.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogKafkaUINRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifySecLogKafkaUINResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecLogKafkaUIN", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecLogKafkaUINResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusAutoIsolateExampleSwitch(self, request):
        """修改木马自动隔离样本开关

        :param request: Request instance for ModifyVirusAutoIsolateExampleSwitch.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateExampleSwitchRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateExampleSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusAutoIsolateExampleSwitch", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusAutoIsolateExampleSwitchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusAutoIsolateSetting(self, request):
        """修改木马自动隔离设置

        :param request: Request instance for ModifyVirusAutoIsolateSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusAutoIsolateSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusAutoIsolateSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusAutoIsolateSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusFileStatus(self, request):
        """运行时更新木马文件事件状态

        :param request: Request instance for ModifyVirusFileStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusFileStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusFileStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusFileStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusFileStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusMonitorSetting(self, request):
        """运行时更新文件查杀实时监控设置

        :param request: Request instance for ModifyVirusMonitorSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusMonitorSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusMonitorSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusMonitorSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusMonitorSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusScanSetting(self, request):
        """运行时更新文件查杀设置

        :param request: Request instance for ModifyVirusScanSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusScanSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusScanSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVirusScanTimeoutSetting(self, request):
        """运行时文件扫描超时设置

        :param request: Request instance for ModifyVirusScanTimeoutSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanTimeoutSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVirusScanTimeoutSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVirusScanTimeoutSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVirusScanTimeoutSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVulDefenceEventStatus(self, request):
        """修改漏洞防御事件状态

        :param request: Request instance for ModifyVulDefenceEventStatus.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceEventStatusRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulDefenceEventStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVulDefenceEventStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVulDefenceSetting(self, request):
        """编辑漏洞防御设置

        :param request: Request instance for ModifyVulDefenceSetting.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceSettingRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ModifyVulDefenceSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVulDefenceSetting", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVulDefenceSettingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenTcssTrial(self, request):
        """开通容器安全服务试用

        :param request: Request instance for OpenTcssTrial.
        :type request: :class:`tencentcloud.tcss.v20201101.models.OpenTcssTrialRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.OpenTcssTrialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenTcssTrial", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenTcssTrialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveAssetImageRegistryRegistryDetail(self, request):
        """删除单个镜像仓库详细信息

        :param request: Request instance for RemoveAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.RemoveAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.RemoveAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewImageAuthorizeState(self, request):
        """RenewImageAuthorizeState   授权镜像扫描

        :param request: Request instance for RenewImageAuthorizeState.
        :type request: :class:`tencentcloud.tcss.v20201101.models.RenewImageAuthorizeStateRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.RenewImageAuthorizeStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewImageAuthorizeState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewImageAuthorizeStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetSecLogTopicConfig(self, request):
        """重置安全日志主题设置

        :param request: Request instance for ResetSecLogTopicConfig.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ResetSecLogTopicConfigRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ResetSecLogTopicConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetSecLogTopicConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetSecLogTopicConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanComplianceAssets(self, request):
        """重新检测选定的资产

        :param request: Request instance for ScanComplianceAssets.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanComplianceAssets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanComplianceAssetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanComplianceAssetsByPolicyItem(self, request):
        """用指定的检测项重新检测选定的资产，返回创建的合规检查任务的ID。

        :param request: Request instance for ScanComplianceAssetsByPolicyItem.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsByPolicyItemRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceAssetsByPolicyItemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanComplianceAssetsByPolicyItem", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanComplianceAssetsByPolicyItemResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanCompliancePolicyItems(self, request):
        """重新检测选的检测项下的所有资产，返回创建的合规检查任务的ID。

        :param request: Request instance for ScanCompliancePolicyItems.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanCompliancePolicyItemsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanCompliancePolicyItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanCompliancePolicyItems", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanCompliancePolicyItemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScanComplianceScanFailedAssets(self, request):
        """重新检测选定的检测失败的资产下的所有失败的检测项，返回创建的合规检查任务的ID。

        :param request: Request instance for ScanComplianceScanFailedAssets.
        :type request: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceScanFailedAssetsRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.ScanComplianceScanFailedAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanComplianceScanFailedAssets", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanComplianceScanFailedAssetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetCheckMode(self, request):
        """设置检测模式和自动检查

        :param request: Request instance for SetCheckMode.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SetCheckModeRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SetCheckModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCheckMode", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCheckModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopVirusScanTask(self, request):
        """运行时停止木马查杀任务

        :param request: Request instance for StopVirusScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.StopVirusScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.StopVirusScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVirusScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopVirusScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopVulScanTask(self, request):
        """停止漏洞扫描任务

        :param request: Request instance for StopVulScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.StopVulScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.StopVulScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopVulScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopVulScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchImageAutoAuthorizedRule(self, request):
        """编辑本地镜像自动授权开关

        :param request: Request instance for SwitchImageAutoAuthorizedRule.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SwitchImageAutoAuthorizedRuleRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SwitchImageAutoAuthorizedRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchImageAutoAuthorizedRule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchImageAutoAuthorizedRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncAssetImageRegistryAsset(self, request):
        """镜像仓库资产刷新

        :param request: Request instance for SyncAssetImageRegistryAsset.
        :type request: :class:`tencentcloud.tcss.v20201101.models.SyncAssetImageRegistryAssetRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.SyncAssetImageRegistryAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncAssetImageRegistryAsset", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncAssetImageRegistryAssetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAndPublishNetworkFirewallPolicyDetail(self, request):
        """容器网络创建网络策略更新并发布任务

        :param request: Request instance for UpdateAndPublishNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAndPublishNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAndPublishNetworkFirewallPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAndPublishNetworkFirewallPolicyYamlDetail(self, request):
        """容器网络更新Yaml网络策略并发布任务

        :param request: Request instance for UpdateAndPublishNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAndPublishNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAndPublishNetworkFirewallPolicyYamlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAssetImageRegistryRegistryDetail(self, request):
        """更新单个镜像仓库详细信息

        :param request: Request instance for UpdateAssetImageRegistryRegistryDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateAssetImageRegistryRegistryDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateAssetImageRegistryRegistryDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAssetImageRegistryRegistryDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAssetImageRegistryRegistryDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateImageRegistryTimingScanTask(self, request):
        """镜像仓库更新定时任务

        :param request: Request instance for UpdateImageRegistryTimingScanTask.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateImageRegistryTimingScanTaskRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateImageRegistryTimingScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateImageRegistryTimingScanTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateImageRegistryTimingScanTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateNetworkFirewallPolicyDetail(self, request):
        """容器网络创建网络策略更新任务

        :param request: Request instance for UpdateNetworkFirewallPolicyDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNetworkFirewallPolicyDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNetworkFirewallPolicyDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateNetworkFirewallPolicyYamlDetail(self, request):
        """容器网络更新Yaml网络策略任务

        :param request: Request instance for UpdateNetworkFirewallPolicyYamlDetail.
        :type request: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyYamlDetailRequest`
        :rtype: :class:`tencentcloud.tcss.v20201101.models.UpdateNetworkFirewallPolicyYamlDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNetworkFirewallPolicyYamlDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNetworkFirewallPolicyYamlDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)