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


class DeleteCertRequest(AbstractModel):
    """DeleteCert请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 证书 ID，即通过 GetList 拿到的证书列表的 ID 字段。\n        :type Id: str\n        :param ModuleType: 模块名称，应填 ssl。\n        :type ModuleType: str\n        """
        self.Id = None
        self.ModuleType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ModuleType = params.get("ModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertResponse(AbstractModel):
    """DeleteCert返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCertListRequest(AbstractModel):
    """DescribeCertList请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleType: 模块名称，应填 ssl。\n        :type ModuleType: str\n        :param Offset: 页数，默认第一页。\n        :type Offset: int\n        :param Limit: 每页条数，默认每页20条。\n        :type Limit: int\n        :param SearchKey: 搜索关键字。\n        :type SearchKey: str\n        :param CertType: 证书类型（目前支持:CA=客户端证书,SVR=服务器证书）。\n        :type CertType: str\n        :param Id: 证书ID。\n        :type Id: str\n        :param WithCert: 是否同时获取证书内容。\n        :type WithCert: str\n        :param AltDomain: 如传，则只返回可以给该域名使用的证书。\n        :type AltDomain: str\n        """
        self.ModuleType = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertType = None
        self.Id = None
        self.WithCert = None
        self.AltDomain = None


    def _deserialize(self, params):
        self.ModuleType = params.get("ModuleType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertType = params.get("CertType")
        self.Id = params.get("Id")
        self.WithCert = params.get("WithCert")
        self.AltDomain = params.get("AltDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertListResponse(AbstractModel):
    """DescribeCertList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数量。\n        :type TotalCount: int\n        :param CertificateSet: 列表。\n        :type CertificateSet: list of SSLCertificate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.CertificateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CertificateSet") is not None:
            self.CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = SSLCertificate()
                obj._deserialize(item)
                self.CertificateSet.append(obj)
        self.RequestId = params.get("RequestId")


class SSLCertificate(AbstractModel):
    """获取证书列表（SSLCertificate）返回参数键为 CertificateSet 的内容。

    """

    def __init__(self):
        """
        :param OwnerUin: 所属账户
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: str\n        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: str\n        :param From: 证书来源：trustasia = 亚洲诚信， upload = 用户上传
注意：此字段可能返回 null，表示取不到有效值。\n        :type From: str\n        :param Type: 证书类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param CertType: 证书类型（目前支持：CA = 客户端证书，SVR = 服务器证书）
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertType: str\n        :param ProductZhName: 证书办法者名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductZhName: str\n        :param Domain: 主域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param Alias: 别名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        :param Status: 状态值 0：审核中，1：已通过，2：审核失败，3：已过期，4：已添加云解析记录，5：OV/EV 证书，待提交资料，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。\n        :type VulnerabilityStatus: str\n        :param StatusMsg: 状态信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusMsg: str\n        :param VerifyType: 验证类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyType: str\n        :param CertBeginTime: 证书生效时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertBeginTime: str\n        :param CertEndTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertEndTime: str\n        :param ValidityPeriod: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValidityPeriod: str\n        :param InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type InsertTime: str\n        :param ProjectInfo: 项目信息，ProjectId：项目ID，OwnerUin：项目所属的 uin（默认项目为0），Name：项目名称，CreatorUin：创建项目的 uin，CreateTime：项目创建时间，Info：项目说明
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectInfo: :class:`tencentcloud.wss.v20180426.models.SSLProjectInfo`\n        :param Id: 证书ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        :param SubjectAltName: 证书包含的多个域名（包含主域名）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubjectAltName: list of str\n        :param TypeName: 证书类型名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeName: str\n        :param StatusName: 状态名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusName: str\n        :param IsVip: 是否为 VIP 客户
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVip: bool\n        :param IsDv: 是否我 DV 版证书
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDv: bool\n        :param IsWildcard: 是否为泛域名证书
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsWildcard: bool\n        :param IsVulnerability: 是否启用了漏洞扫描功能
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVulnerability: bool\n        :param Cert: 证书
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cert: str\n        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.Type = None
        self.CertType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.VulnerabilityStatus = None
        self.StatusMsg = None
        self.VerifyType = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.ProjectInfo = None
        self.Id = None
        self.SubjectAltName = None
        self.TypeName = None
        self.StatusName = None
        self.IsVip = None
        self.IsDv = None
        self.IsWildcard = None
        self.IsVulnerability = None
        self.Cert = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.Type = params.get("Type")
        self.CertType = params.get("CertType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        if params.get("ProjectInfo") is not None:
            self.ProjectInfo = SSLProjectInfo()
            self.ProjectInfo._deserialize(params.get("ProjectInfo"))
        self.Id = params.get("Id")
        self.SubjectAltName = params.get("SubjectAltName")
        self.TypeName = params.get("TypeName")
        self.StatusName = params.get("StatusName")
        self.IsVip = params.get("IsVip")
        self.IsDv = params.get("IsDv")
        self.IsWildcard = params.get("IsWildcard")
        self.IsVulnerability = params.get("IsVulnerability")
        self.Cert = params.get("Cert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SSLProjectInfo(AbstractModel):
    """获取证书列表接口（SSLProjectInfo）出参键为CertificateSet下的元素ProjectIno详情

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: str\n        :param OwnerUin: 项目所属的 uin（默认项目为0）
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: int\n        :param Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param CreatorUin: 创建项目的 uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatorUin: int\n        :param CreateTime: 项目创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Info: 项目说明
注意：此字段可能返回 null，表示取不到有效值。\n        :type Info: str\n        """
        self.ProjectId = None
        self.OwnerUin = None
        self.Name = None
        self.CreatorUin = None
        self.CreateTime = None
        self.Info = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.OwnerUin = params.get("OwnerUin")
        self.Name = params.get("Name")
        self.CreatorUin = params.get("CreatorUin")
        self.CreateTime = params.get("CreateTime")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertRequest(AbstractModel):
    """UploadCert请求参数结构体

    """

    def __init__(self):
        """
        :param Cert: 证书内容。\n        :type Cert: str\n        :param CertType: 证书类型（目前支持：CA 为客户端证书，SVR 为服务器证书）。\n        :type CertType: str\n        :param ProjectId: 项目ID，详见用户指南的 [项目与标签](https://cloud.tencent.com/document/product/598/32738)。\n        :type ProjectId: str\n        :param ModuleType: 模块名称，应填 ssl。\n        :type ModuleType: str\n        :param Key: 证书私钥，certType=SVR 时必填。\n        :type Key: str\n        :param Alias: 证书备注。\n        :type Alias: str\n        """
        self.Cert = None
        self.CertType = None
        self.ProjectId = None
        self.ModuleType = None
        self.Key = None
        self.Alias = None


    def _deserialize(self, params):
        self.Cert = params.get("Cert")
        self.CertType = params.get("CertType")
        self.ProjectId = params.get("ProjectId")
        self.ModuleType = params.get("ModuleType")
        self.Key = params.get("Key")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertResponse(AbstractModel):
    """UploadCert返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 证书ID。\n        :type Id: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")