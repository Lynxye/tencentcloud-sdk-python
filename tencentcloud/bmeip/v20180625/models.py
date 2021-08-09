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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class BindEipAclsRequest(AbstractModel):
    """BindEipAcls请求参数结构体

    """

    def __init__(self):
        """
        :param EipIdAclIdList: 待关联的 EIP 与 ACL关系列表\n        :type EipIdAclIdList: list of EipAclMap\n        """
        self.EipIdAclIdList = None


    def _deserialize(self, params):
        if params.get("EipIdAclIdList") is not None:
            self.EipIdAclIdList = []
            for item in params.get("EipIdAclIdList"):
                obj = EipAclMap()
                obj._deserialize(item)
                self.EipIdAclIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEipAclsResponse(AbstractModel):
    """BindEipAcls返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindHostedRequest(AbstractModel):
    """BindHosted请求参数结构体

    """

    def __init__(self):
        """
        :param EipId: Eip实例ID，可通过DescribeBmEip 接口返回字段中的 eipId获取。Eip和EipId参数必须要填写一个。\n        :type EipId: str\n        :param InstanceId: 托管机器实例ID\n        :type InstanceId: str\n        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindHostedResponse(AbstractModel):
    """BindHosted返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID，可以通过EipBmQueryTask查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindRsRequest(AbstractModel):
    """BindRs请求参数结构体

    """

    def __init__(self):
        """
        :param EipId: Eip实例ID\n        :type EipId: str\n        :param InstanceId: 物理服务器实例ID\n        :type InstanceId: str\n        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRsResponse(AbstractModel):
    """BindRs返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 绑定黑石物理机异步任务ID，可以通过DescribeEipTask查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindVpcIpRequest(AbstractModel):
    """BindVpcIp请求参数结构体

    """

    def __init__(self):
        """
        :param EipId: Eip实例ID\n        :type EipId: str\n        :param VpcId: EIP归属VpcId，例如vpc-k7j1t2x1\n        :type VpcId: str\n        :param VpcIp: 绑定的VPC内IP地址\n        :type VpcIp: str\n        """
        self.EipId = None
        self.VpcId = None
        self.VpcIp = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.VpcId = params.get("VpcId")
        self.VpcIp = params.get("VpcIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindVpcIpResponse(AbstractModel):
    """BindVpcIp返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: EIP绑定VPC网络IP异步任务ID，可以通过查询EIP任务状态查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateEipAclRequest(AbstractModel):
    """CreateEipAcl请求参数结构体

    """

    def __init__(self):
        """
        :param AclName: ACL 名称\n        :type AclName: str\n        :param Status: ACL 状态 0：无状态，1：有状态\n        :type Status: int\n        """
        self.AclName = None
        self.Status = None


    def _deserialize(self, params):
        self.AclName = params.get("AclName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEipAclResponse(AbstractModel):
    """CreateEipAcl返回参数结构体

    """

    def __init__(self):
        """
        :param AclId: ACL 实例 ID\n        :type AclId: str\n        :param Status: ACL 实例状态\n        :type Status: int\n        :param AclName: ACL 实例名称\n        :type AclName: str\n        :param CreatedAt: ACL 实例创建时间\n        :type CreatedAt: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AclId = None
        self.Status = None
        self.AclName = None
        self.CreatedAt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        self.Status = params.get("Status")
        self.AclName = params.get("AclName")
        self.CreatedAt = params.get("CreatedAt")
        self.RequestId = params.get("RequestId")


class CreateEipRequest(AbstractModel):
    """CreateEip请求参数结构体

    """

    def __init__(self):
        """
        :param GoodsNum: 申请数量，默认为1, 最大 20\n        :type GoodsNum: int\n        :param PayMode: EIP计费方式，flow-流量计费；bandwidth-带宽计费\n        :type PayMode: str\n        :param Bandwidth: 带宽设定值（只在带宽计费时生效）\n        :type Bandwidth: int\n        :param SetType: EIP模式，目前支持tunnel和fullnat\n        :type SetType: str\n        :param Exclusive: 是否使用独占集群，0：不使用，1：使用。默认为0\n        :type Exclusive: int\n        :param VpcId: EIP归属私有网络ID，例如vpc-k7j1t2x1\n        :type VpcId: str\n        :param IpList: 指定申请的IP列表\n        :type IpList: list of str\n        """
        self.GoodsNum = None
        self.PayMode = None
        self.Bandwidth = None
        self.SetType = None
        self.Exclusive = None
        self.VpcId = None
        self.IpList = None


    def _deserialize(self, params):
        self.GoodsNum = params.get("GoodsNum")
        self.PayMode = params.get("PayMode")
        self.Bandwidth = params.get("Bandwidth")
        self.SetType = params.get("SetType")
        self.Exclusive = params.get("Exclusive")
        self.VpcId = params.get("VpcId")
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEipResponse(AbstractModel):
    """CreateEip返回参数结构体

    """

    def __init__(self):
        """
        :param EipIds: EIP列表\n        :type EipIds: list of str\n        :param TaskId: 任务ID\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EipIds = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EipIds = params.get("EipIds")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteEipAclRequest(AbstractModel):
    """DeleteEipAcl请求参数结构体

    """

    def __init__(self):
        """
        :param AclId: 待删除的 ACL 实例 ID\n        :type AclId: str\n        """
        self.AclId = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEipAclResponse(AbstractModel):
    """DeleteEipAcl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEipRequest(AbstractModel):
    """DeleteEip请求参数结构体

    """

    def __init__(self):
        """
        :param EipIds: Eip实例ID列表\n        :type EipIds: list of str\n        """
        self.EipIds = None


    def _deserialize(self, params):
        self.EipIds = params.get("EipIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEipResponse(AbstractModel):
    """DeleteEip返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeEipAclsRequest(AbstractModel):
    """DescribeEipAcls请求参数结构体

    """

    def __init__(self):
        """
        :param AclName: ACL 名称，支持模糊查找\n        :type AclName: str\n        :param AclIds: ACL 实例 ID 列表，数组下标从 0 开始\n        :type AclIds: list of str\n        :param Offset: 分页参数。偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页参数。每一页的 EIPACL 列表数目\n        :type Limit: int\n        :param EipIds: EIP实例ID列表\n        :type EipIds: list of str\n        :param EipIps: EIP IP地址列表\n        :type EipIps: list of str\n        :param EipNames: EIP名称列表\n        :type EipNames: list of str\n        :param OrderField: 排序字段\n        :type OrderField: str\n        :param Order: 排序方式，取值：0:增序(默认)，1:降序\n        :type Order: int\n        :param AclNames: ACL名称列表，支持模糊查找\n        :type AclNames: list of str\n        """
        self.AclName = None
        self.AclIds = None
        self.Offset = None
        self.Limit = None
        self.EipIds = None
        self.EipIps = None
        self.EipNames = None
        self.OrderField = None
        self.Order = None
        self.AclNames = None


    def _deserialize(self, params):
        self.AclName = params.get("AclName")
        self.AclIds = params.get("AclIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EipIds = params.get("EipIds")
        self.EipIps = params.get("EipIps")
        self.EipNames = params.get("EipNames")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.AclNames = params.get("AclNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEipAclsResponse(AbstractModel):
    """DescribeEipAcls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回 EIPACL 列表总数\n        :type TotalCount: int\n        :param EipAclList: EIPACL列表\n        :type EipAclList: list of EipAcl\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.EipAclList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EipAclList") is not None:
            self.EipAclList = []
            for item in params.get("EipAclList"):
                obj = EipAcl()
                obj._deserialize(item)
                self.EipAclList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEipQuotaRequest(AbstractModel):
    """DescribeEipQuota请求参数结构体

    """


class DescribeEipQuotaResponse(AbstractModel):
    """DescribeEipQuota返回参数结构体

    """

    def __init__(self):
        """
        :param EipNumQuota: 能拥有的EIP个数的总配额，默认是100个\n        :type EipNumQuota: int\n        :param CurrentEipNum: 当前已使用的EIP个数，包括创建中、绑定中、已绑定、解绑中、未绑定几种状态的EIP个数总和\n        :type CurrentEipNum: int\n        :param DailyApplyCount: 当天申请EIP次数\n        :type DailyApplyCount: int\n        :param DailyApplyQuota: 每日申请EIP的次数限制\n        :type DailyApplyQuota: int\n        :param BatchApplyMax: BatchApplyMax\n        :type BatchApplyMax: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EipNumQuota = None
        self.CurrentEipNum = None
        self.DailyApplyCount = None
        self.DailyApplyQuota = None
        self.BatchApplyMax = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EipNumQuota = params.get("EipNumQuota")
        self.CurrentEipNum = params.get("CurrentEipNum")
        self.DailyApplyCount = params.get("DailyApplyCount")
        self.DailyApplyQuota = params.get("DailyApplyQuota")
        self.BatchApplyMax = params.get("BatchApplyMax")
        self.RequestId = params.get("RequestId")


class DescribeEipTaskRequest(AbstractModel):
    """DescribeEipTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: EIP查询任务ID\n        :type TaskId: int\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEipTaskResponse(AbstractModel):
    """DescribeEipTask返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 当前任务状态码：0-成功，1-失败，2-进行中\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeEipsRequest(AbstractModel):
    """DescribeEips请求参数结构体

    """

    def __init__(self):
        """
        :param EipIds: EIP实例ID列表\n        :type EipIds: list of str\n        :param Eips: EIP IP 列表\n        :type Eips: list of str\n        :param InstanceIds: 主机实例ID 列表\n        :type InstanceIds: list of str\n        :param SearchKey: EIP名称,模糊匹配\n        :type SearchKey: str\n        :param Status: 状态列表, 默认所有\n        :type Status: list of int\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回EIP数量，默认 20, 最大值 100\n        :type Limit: int\n        :param OrderField: 排序字段，支持： EipId,Eip,Status, InstanceId,CreatedAt\n        :type OrderField: str\n        :param Order: 排序方式 0:递增 1:递减(默认)\n        :type Order: int\n        :param PayMode: 计费模式,流量：flow，带宽：bandwidth\n        :type PayMode: str\n        :param VpcId: EIP归属VpcId，例如vpc-k7j1t2x1\n        :type VpcId: str\n        :param BindTypes: 绑定类型，-1：未绑定，0：物理机，1：nat网关，2：虚拟IP, 3:托管机器\n        :type BindTypes: list of int\n        :param ExclusiveTag: 独占标志，0：共享，1：独占\n        :type ExclusiveTag: int\n        :param AclId: EIP ACL实例ID\n        :type AclId: str\n        :param BindAcl: 搜索条件，是否绑定了EIP ACL， 0：未绑定，1：绑定\n        :type BindAcl: int\n        """
        self.EipIds = None
        self.Eips = None
        self.InstanceIds = None
        self.SearchKey = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.PayMode = None
        self.VpcId = None
        self.BindTypes = None
        self.ExclusiveTag = None
        self.AclId = None
        self.BindAcl = None


    def _deserialize(self, params):
        self.EipIds = params.get("EipIds")
        self.Eips = params.get("Eips")
        self.InstanceIds = params.get("InstanceIds")
        self.SearchKey = params.get("SearchKey")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.PayMode = params.get("PayMode")
        self.VpcId = params.get("VpcId")
        self.BindTypes = params.get("BindTypes")
        self.ExclusiveTag = params.get("ExclusiveTag")
        self.AclId = params.get("AclId")
        self.BindAcl = params.get("BindAcl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEipsResponse(AbstractModel):
    """DescribeEips返回参数结构体

    """

    def __init__(self):
        """
        :param EipSet: 返回EIP信息数组\n        :type EipSet: list of EipInfo\n        :param TotalCount: 返回EIP数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EipSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EipSet") is not None:
            self.EipSet = []
            for item in params.get("EipSet"):
                obj = EipInfo()
                obj._deserialize(item)
                self.EipSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class EipAcl(AbstractModel):
    """EipAcl信息

    """

    def __init__(self):
        """
        :param AclId: ACL 实例 ID。\n        :type AclId: str\n        :param AclName: ACL 实例名称\n        :type AclName: str\n        :param Status: ACL 状态。0：无状态，1：有状态\n        :type Status: str\n        :param CreatedAt: EIPACL 创建时间\n        :type CreatedAt: str\n        :param EipNum: EIPACL 已关联的 eip 数目\n        :type EipNum: int\n        :param OutRules: 出站规则\n        :type OutRules: list of EipAclRule\n        :param InRules: 入站规则\n        :type InRules: list of EipAclRule\n        """
        self.AclId = None
        self.AclName = None
        self.Status = None
        self.CreatedAt = None
        self.EipNum = None
        self.OutRules = None
        self.InRules = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        self.AclName = params.get("AclName")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.EipNum = params.get("EipNum")
        if params.get("OutRules") is not None:
            self.OutRules = []
            for item in params.get("OutRules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self.OutRules.append(obj)
        if params.get("InRules") is not None:
            self.InRules = []
            for item in params.get("InRules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self.InRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAclMap(AbstractModel):
    """eipid与aclid关联关系

    """

    def __init__(self):
        """
        :param EipId: EIP 实例 ID\n        :type EipId: str\n        :param AclId: ACL 实例 ID\n        :type AclId: str\n        """
        self.EipId = None
        self.AclId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.AclId = params.get("AclId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAclRule(AbstractModel):
    """eipacl规则

    """

    def __init__(self):
        """
        :param Ip: 源 IP\n        :type Ip: str\n        :param Port: 目标端口\n        :type Port: str\n        :param Protocol: 协议(TCP/UDP/ICMP/ANY)\n        :type Protocol: str\n        :param Action: 策略（accept/drop）\n        :type Action: str\n        :param Description: 备注\n        :type Description: str\n        """
        self.Ip = None
        self.Port = None
        self.Protocol = None
        self.Action = None
        self.Description = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.Action = params.get("Action")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipInfo(AbstractModel):
    """Eip信息

    """

    def __init__(self):
        """
        :param EipId: EIP实例ID\n        :type EipId: str\n        :param EipName: EIP名称\n        :type EipName: str\n        :param Eip: EIP地址\n        :type Eip: str\n        :param IspId: 运营商ID 0：电信； 1：联通； 2：移动； 3：教育网； 4：盈科； 5：BGP； 6：中国香港\n        :type IspId: int\n        :param Status: 状态 0：创建中； 1：绑定中； 2：已绑定； 3：解绑中； 4：未绑定； 6：下线中； 9：创建失败\n        :type Status: int\n        :param Arrears: 是否欠费隔离 1： 欠费隔离； 0： 正常。处在欠费隔离情况下的EIP不能进行任何管理操作。\n        :type Arrears: int\n        :param InstanceId: EIP所绑定的服务器实例ID，未绑定则为空\n        :type InstanceId: str\n        :param InstanceAlias: 服务器别名\n        :type InstanceAlias: str\n        :param FreeAt: EIP解绑时间\n        :type FreeAt: str\n        :param CreatedAt: EIP创建时间\n        :type CreatedAt: str\n        :param UpdatedAt: EIP更新时间\n        :type UpdatedAt: str\n        :param FreeSecond: EIP未绑定服务器时长（单位：秒）\n        :type FreeSecond: int\n        :param Type: EIP所绑定的资源类型，-1：未绑定资源；0：黑石物理机，字段对应unInstanceId；1：Nat网关，字段对应natUid；2：云服务器字段对应vpcIp; 3: 托管机器，字段对应HInstanceId, HInstanceAlias\n        :type Type: int\n        :param PayMode: EIP计费模式，"flow"：流量计费； "bandwidth"：带宽计费\n        :type PayMode: str\n        :param Bandwidth: EIP带宽计费模式下的带宽上限（单位：MB）\n        :type Bandwidth: int\n        :param LatestPayMode: 最近一次操作变更的EIP计费模式，"flow"：流量计费； "bandwidth"：带宽计费\n        :type LatestPayMode: str\n        :param LatestBandwidth: 最近一次操作变更的EIP计费模式对应的带宽上限值，仅在带宽计费模式下有效（单位：MB）\n        :type LatestBandwidth: int\n        :param VpcName: 私有网络名称\n        :type VpcName: str\n        :param NatId: EIP所绑定的NAT网关的数字ID，形如：1001,，未绑定则为空\n        :type NatId: int\n        :param NatUid: EIP所绑定的NAT网关实例ID，形如："nat-n47xxxxx"，未绑定则为空\n        :type NatUid: str\n        :param VpcIp: EIP所绑定的云服务器IP(托管或者云服务器的IP），形如："10.1.1.3"。 注意：IP资源需要通过bmvpc模块注册或者申请后才可以绑定eip，接口使用申请子网IP和注册子网IP：,未绑定则为空\n        :type VpcIp: str\n        :param VpcId: 私有网络实例ID\n        :type VpcId: str\n        :param Exclusive: 是否为独占类型EIP\n        :type Exclusive: int\n        :param VpcCidr: 私有网络的cidr\n        :type VpcCidr: str\n        :param AclId: EIP ACL实例ID\n        :type AclId: str\n        :param AclName: EIP ACL名称\n        :type AclName: str\n        :param HInstanceId: 托管机器实例ID\n        :type HInstanceId: str\n        :param HInstanceAlias: 托管机器别名\n        :type HInstanceAlias: str\n        """
        self.EipId = None
        self.EipName = None
        self.Eip = None
        self.IspId = None
        self.Status = None
        self.Arrears = None
        self.InstanceId = None
        self.InstanceAlias = None
        self.FreeAt = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.FreeSecond = None
        self.Type = None
        self.PayMode = None
        self.Bandwidth = None
        self.LatestPayMode = None
        self.LatestBandwidth = None
        self.VpcName = None
        self.NatId = None
        self.NatUid = None
        self.VpcIp = None
        self.VpcId = None
        self.Exclusive = None
        self.VpcCidr = None
        self.AclId = None
        self.AclName = None
        self.HInstanceId = None
        self.HInstanceAlias = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.EipName = params.get("EipName")
        self.Eip = params.get("Eip")
        self.IspId = params.get("IspId")
        self.Status = params.get("Status")
        self.Arrears = params.get("Arrears")
        self.InstanceId = params.get("InstanceId")
        self.InstanceAlias = params.get("InstanceAlias")
        self.FreeAt = params.get("FreeAt")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.FreeSecond = params.get("FreeSecond")
        self.Type = params.get("Type")
        self.PayMode = params.get("PayMode")
        self.Bandwidth = params.get("Bandwidth")
        self.LatestPayMode = params.get("LatestPayMode")
        self.LatestBandwidth = params.get("LatestBandwidth")
        self.VpcName = params.get("VpcName")
        self.NatId = params.get("NatId")
        self.NatUid = params.get("NatUid")
        self.VpcIp = params.get("VpcIp")
        self.VpcId = params.get("VpcId")
        self.Exclusive = params.get("Exclusive")
        self.VpcCidr = params.get("VpcCidr")
        self.AclId = params.get("AclId")
        self.AclName = params.get("AclName")
        self.HInstanceId = params.get("HInstanceId")
        self.HInstanceAlias = params.get("HInstanceAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipRsMap(AbstractModel):
    """EipId与InstanceId绑定关系

    """

    def __init__(self):
        """
        :param EipId: EIP实例 ID\n        :type EipId: str\n        :param InstanceId: 黑石物理机实例ID\n        :type InstanceId: str\n        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipAclRequest(AbstractModel):
    """ModifyEipAcl请求参数结构体

    """

    def __init__(self):
        """
        :param AclId: ACL 实例 ID\n        :type AclId: str\n        :param AclName: ACL 名称\n        :type AclName: str\n        :param Status: ACL 状态。0：无状态 1：有状态\n        :type Status: int\n        :param Type: 规则类型（in/out）。in：入站规则 out：出站规则\n        :type Type: str\n        :param Rules: ACL规则列表\n        :type Rules: list of EipAclRule\n        """
        self.AclId = None
        self.AclName = None
        self.Status = None
        self.Type = None
        self.Rules = None


    def _deserialize(self, params):
        self.AclId = params.get("AclId")
        self.AclName = params.get("AclName")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = EipAclRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipAclResponse(AbstractModel):
    """ModifyEipAcl返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEipChargeRequest(AbstractModel):
    """ModifyEipCharge请求参数结构体

    """

    def __init__(self):
        """
        :param PayMode: EIP计费方式，flow-流量计费；bandwidth-带宽计费\n        :type PayMode: str\n        :param EipIds: Eip实例ID列表\n        :type EipIds: list of str\n        :param Bandwidth: 带宽设定值（只在带宽计费时生效）\n        :type Bandwidth: int\n        """
        self.PayMode = None
        self.EipIds = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.PayMode = params.get("PayMode")
        self.EipIds = params.get("EipIds")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipChargeResponse(AbstractModel):
    """ModifyEipCharge返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 修改计费模式的异步任务ID，可以通过查询EIP任务状态查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyEipNameRequest(AbstractModel):
    """ModifyEipName请求参数结构体

    """

    def __init__(self):
        """
        :param EipId: Eip实例ID，可通过/v2/DescribeEip 接口返回字段中的 eipId获取\n        :type EipId: str\n        :param EipName: EIP 实例别名\n        :type EipName: str\n        """
        self.EipId = None
        self.EipName = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.EipName = params.get("EipName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEipNameResponse(AbstractModel):
    """ModifyEipName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindEipAclsRequest(AbstractModel):
    """UnbindEipAcls请求参数结构体

    """

    def __init__(self):
        """
        :param EipIdAclIdList: 待解关联的 EIP 与 ACL列表\n        :type EipIdAclIdList: list of EipAclMap\n        """
        self.EipIdAclIdList = None


    def _deserialize(self, params):
        if params.get("EipIdAclIdList") is not None:
            self.EipIdAclIdList = []
            for item in params.get("EipIdAclIdList"):
                obj = EipAclMap()
                obj._deserialize(item)
                self.EipIdAclIdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindEipAclsResponse(AbstractModel):
    """UnbindEipAcls返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindHostedRequest(AbstractModel):
    """UnbindHosted请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 托管机器实例ID\n        :type InstanceId: str\n        :param EipId: Eip实例ID，可通过DescribeBmEip 接口返回字段中的 eipId获取。Eip和EipId参数必须要填写一个。\n        :type EipId: str\n        :param Eip: 弹性IP。Eip和EipId参数必须要填写一个。\n        :type Eip: str\n        """
        self.InstanceId = None
        self.EipId = None
        self.Eip = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.EipId = params.get("EipId")
        self.Eip = params.get("Eip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindHostedResponse(AbstractModel):
    """UnbindHosted返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID，可以通过EipBmQueryTask查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindRsListRequest(AbstractModel):
    """UnbindRsList请求参数结构体

    """

    def __init__(self):
        """
        :param EipRsList: 物理机绑定的EIP列表\n        :type EipRsList: list of EipRsMap\n        """
        self.EipRsList = None


    def _deserialize(self, params):
        if params.get("EipRsList") is not None:
            self.EipRsList = []
            for item in params.get("EipRsList"):
                obj = EipRsMap()
                obj._deserialize(item)
                self.EipRsList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRsListResponse(AbstractModel):
    """UnbindRsList返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 解绑操作的异步任务ID，可以通过查询EIP任务状态查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindRsRequest(AbstractModel):
    """UnbindRs请求参数结构体

    """

    def __init__(self):
        """
        :param EipId: Eip实例ID\n        :type EipId: str\n        :param InstanceId: 物理服务器实例ID\n        :type InstanceId: str\n        """
        self.EipId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindRsResponse(AbstractModel):
    """UnbindRs返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 解绑操作的异步任务ID，可以通过查询EIP任务状态查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindVpcIpRequest(AbstractModel):
    """UnbindVpcIp请求参数结构体

    """

    def __init__(self):
        """
        :param EipId: Eip实例ID\n        :type EipId: str\n        :param VpcId: EIP归属VpcId，例如vpc-k7j1t2x1\n        :type VpcId: str\n        :param VpcIp: 绑定的VPC内IP地址\n        :type VpcIp: str\n        """
        self.EipId = None
        self.VpcId = None
        self.VpcIp = None


    def _deserialize(self, params):
        self.EipId = params.get("EipId")
        self.VpcId = params.get("VpcId")
        self.VpcIp = params.get("VpcIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindVpcIpResponse(AbstractModel):
    """UnbindVpcIp返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 绑定黑石物理机异步任务ID，可以通过查询EIP任务状态查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")