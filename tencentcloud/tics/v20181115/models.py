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


class DescribeDomainInfoRequest(AbstractModel):
    """DescribeDomainInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 要查询的域名\n        :type Key: str\n        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。\n        :type Option: int\n        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainInfoResponse(AbstractModel):
    """DescribeDomainInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据\n        :type ReturnCode: int\n        :param Result: 判定结果，如：black、white、grey\n        :type Result: str\n        :param Confidence: 置信度，取值0-100\n        :type Confidence: int\n        :param ThreatTypes: 威胁类型。
botnet = 僵尸网络
trojan = 木马
ransomware = 勒索软件
worm = 蠕虫
dga = 域名生成算法
c2 = c&c
compromised = 失陷主机
dynamicIP = 动态IP
proxy = 代理
idc = idc 机房
whitelist = 白名单
tor = 暗网
miner = 挖矿
maleware site = 恶意站点
malware IP = 恶意IP
等等\n        :type ThreatTypes: list of str\n        :param Tags: 恶意标签，对应的团伙，家族等信息。\n        :type Tags: list of TagType\n        :param Intelligences: 对应的历史上的威胁情报事件\n        :type Intelligences: list of IntelligenceType\n        :param Context: 情报相关的上下文\n        :type Context: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeFileInfoRequest(AbstractModel):
    """DescribeFileInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 要查询文件的MD5\n        :type Key: str\n        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。\n        :type Option: int\n        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileInfoResponse(AbstractModel):
    """DescribeFileInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据\n        :type ReturnCode: int\n        :param Result: 判定结果，如：black、white、grey\n        :type Result: str\n        :param Confidence: 置信度，取值0-100\n        :type Confidence: int\n        :param FileInfo: 文件类型，文件hash
（md5,sha1,sha256）,文件大小等等文件
基础信息\n        :type FileInfo: list of FileInfoType\n        :param Tags: 恶意标签，对应的团伙，家族等信息。\n        :type Tags: list of TagType\n        :param Intelligences: 对应的历史上的威胁情报事件\n        :type Intelligences: list of IntelligenceType\n        :param Context: 情报相关的上下文\n        :type Context: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.FileInfo = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        if params.get("FileInfo") is not None:
            self.FileInfo = []
            for item in params.get("FileInfo"):
                obj = FileInfoType()
                obj._deserialize(item)
                self.FileInfo.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeIpInfoRequest(AbstractModel):
    """DescribeIpInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 要查询的IP\n        :type Key: str\n        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。\n        :type Option: int\n        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpInfoResponse(AbstractModel):
    """DescribeIpInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据\n        :type ReturnCode: int\n        :param Result: 判定结果，如：black、white、grey\n        :type Result: str\n        :param Confidence: 置信度，取值0-100\n        :type Confidence: int\n        :param ThreatTypes: 威胁类型。
botnet = 僵尸网络
trojan = 木马
ransomware = 勒索软件
worm = 蠕虫
dga = 域名生成算法
c2 = c&c
compromised = 失陷主机
dynamicIP = 动态IP
proxy = 代理
idc = idc 机房
whitelist = 白名单
tor = 暗网
miner = 挖矿
maleware site = 恶意站点
malware IP = 恶意IP
等等\n        :type ThreatTypes: list of str\n        :param Tags: 恶意标签，对应的团伙，家族等信息。\n        :type Tags: list of TagType\n        :param Intelligences: 对应的历史上的威胁情报事件\n        :type Intelligences: list of IntelligenceType\n        :param Context: 情报相关的上下文\n        :type Context: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeThreatInfoRequest(AbstractModel):
    """DescribeThreatInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Key: 查询对象，域名或IP\n        :type Key: str\n        :param Type: 查询类型，当前取值为domain或ip\n        :type Type: str\n        :param Option: 附加字段，是否返回上下文。当为0时不返回上下文，当为1时返回上下文。\n        :type Option: int\n        """
        self.Key = None
        self.Type = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeThreatInfoResponse(AbstractModel):
    """DescribeThreatInfo返回参数结构体

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有数据，0代表有数据，1代表没有数据\n        :type ReturnCode: int\n        :param Result: 判定结果，如：black、white、grey\n        :type Result: str\n        :param Confidence: 置信度，取值0-100\n        :type Confidence: int\n        :param ThreatTypes: 威胁类型。
botnet = 僵尸网络
trojan = 木马
ransomware = 勒索软件
worm = 蠕虫
dga = 域名生成算法
c2 = c&c
compromised = 失陷主机
dynamicIP = 动态IP
proxy = 代理
idc = idc 机房
whitelist = 白名单
tor = 暗网
miner = 挖矿
maleware site = 恶意站点
malware IP = 恶意IP
等等\n        :type ThreatTypes: list of str\n        :param Tags: 恶意标签，对应的团伙，家族等信息。\n        :type Tags: list of str\n        :param Status: 当前状态
active = 活跃
sinkholed = sinkholed
inactive = 不活跃
unknown = 未知
expired = 过期\n        :type Status: str\n        :param Context: 情报相关的上下文，参数option=1 的时候提供
每个数据默认为3 条\n        :type Context: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Status = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        self.Tags = params.get("Tags")
        self.Status = params.get("Status")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class FileInfoType(AbstractModel):
    """文件信息类型

    """

    def __init__(self):
        """
        :param DetectId: 判定渠道\n        :type DetectId: str\n        :param DetectPriority: 检测优先级\n        :type DetectPriority: str\n        :param EnginePriority: 引擎优先级\n        :type EnginePriority: str\n        :param FileExist: 样本是否存在\n        :type FileExist: str\n        :param FileForceUpload: 文件上传\n        :type FileForceUpload: str\n        :param FileSize: 文件大小\n        :type FileSize: str\n        :param FileupTime: 文件上传时间\n        :type FileupTime: str\n        :param FullVirusName: 病毒文件全名\n        :type FullVirusName: str\n        :param IdcPosition: IDC位置\n        :type IdcPosition: str\n        :param Md5Type: 文件md5值\n        :type Md5Type: str\n        :param PeExist: PE结构是否存在\n        :type PeExist: str\n        :param PeForceUpload: PE结构上传\n        :type PeForceUpload: str\n        :param SafeLevel: 安全性等级\n        :type SafeLevel: str\n        :param ScanModiTime: 扫描时间\n        :type ScanModiTime: str\n        :param SubdetectId: 子判定渠道\n        :type SubdetectId: str\n        :param UserDefName: 病毒名\n        :type UserDefName: str\n        :param VirusType: 病毒类型\n        :type VirusType: str\n        :param WhiteScore: 白名单分数\n        :type WhiteScore: str\n        """
        self.DetectId = None
        self.DetectPriority = None
        self.EnginePriority = None
        self.FileExist = None
        self.FileForceUpload = None
        self.FileSize = None
        self.FileupTime = None
        self.FullVirusName = None
        self.IdcPosition = None
        self.Md5Type = None
        self.PeExist = None
        self.PeForceUpload = None
        self.SafeLevel = None
        self.ScanModiTime = None
        self.SubdetectId = None
        self.UserDefName = None
        self.VirusType = None
        self.WhiteScore = None


    def _deserialize(self, params):
        self.DetectId = params.get("DetectId")
        self.DetectPriority = params.get("DetectPriority")
        self.EnginePriority = params.get("EnginePriority")
        self.FileExist = params.get("FileExist")
        self.FileForceUpload = params.get("FileForceUpload")
        self.FileSize = params.get("FileSize")
        self.FileupTime = params.get("FileupTime")
        self.FullVirusName = params.get("FullVirusName")
        self.IdcPosition = params.get("IdcPosition")
        self.Md5Type = params.get("Md5Type")
        self.PeExist = params.get("PeExist")
        self.PeForceUpload = params.get("PeForceUpload")
        self.SafeLevel = params.get("SafeLevel")
        self.ScanModiTime = params.get("ScanModiTime")
        self.SubdetectId = params.get("SubdetectId")
        self.UserDefName = params.get("UserDefName")
        self.VirusType = params.get("VirusType")
        self.WhiteScore = params.get("WhiteScore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntelligenceType(AbstractModel):
    """{ "source": "inergj_ai_predict", "stamp": "msraminer", "time": 1531994023 }

    """

    def __init__(self):
        """
        :param Source: 来源\n        :type Source: str\n        :param Stamp: 标记\n        :type Stamp: str\n        :param Time: 时间\n        :type Time: int\n        """
        self.Source = None
        self.Stamp = None
        self.Time = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Stamp = params.get("Stamp")
        self.Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagType(AbstractModel):
    """标签及对应的解释

    """

    def __init__(self):
        """
        :param Tag: 标签\n        :type Tag: str\n        :param Desc: 标签对应的中文解释\n        :type Desc: str\n        """
        self.Tag = None
        self.Desc = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        