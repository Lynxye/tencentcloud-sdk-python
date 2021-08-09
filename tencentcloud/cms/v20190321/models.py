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


class CodeDetail(AbstractModel):
    """从图片中检测到的二维码，可能为多个

    """

    def __init__(self):
        """
        :param CodePosition: 二维码在图片中的位置，由边界点的坐标表示\n        :type CodePosition: list of CodePosition\n        :param CodeCharset: 二维码文本的编码格式\n        :type CodeCharset: str\n        :param CodeText: 二维码的文本内容\n        :type CodeText: str\n        :param CodeType: 二维码的类型：1:ONED_BARCODE，2:QRCOD，3:WXCODE，4:PDF417，5:DATAMATRIX\n        :type CodeType: int\n        """
        self.CodePosition = None
        self.CodeCharset = None
        self.CodeText = None
        self.CodeType = None


    def _deserialize(self, params):
        if params.get("CodePosition") is not None:
            self.CodePosition = []
            for item in params.get("CodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self.CodePosition.append(obj)
        self.CodeCharset = params.get("CodeCharset")
        self.CodeText = params.get("CodeText")
        self.CodeType = params.get("CodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeDetect(AbstractModel):
    """图片二维码详情

    """

    def __init__(self):
        """
        :param ModerationDetail: 从图片中检测到的二维码，可能为多个\n        :type ModerationDetail: list of CodeDetail\n        :param ModerationCode: 检测是否成功，0：成功，-1：出错\n        :type ModerationCode: int\n        """
        self.ModerationDetail = None
        self.ModerationCode = None


    def _deserialize(self, params):
        if params.get("ModerationDetail") is not None:
            self.ModerationDetail = []
            for item in params.get("ModerationDetail"):
                obj = CodeDetail()
                obj._deserialize(item)
                self.ModerationDetail.append(obj)
        self.ModerationCode = params.get("ModerationCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodePosition(AbstractModel):
    """二维码在图片中的位置，由边界点的坐标表示

    """

    def __init__(self):
        """
        :param FloatX: 二维码边界点X轴坐标\n        :type FloatX: float\n        :param FloatY: 二维码边界点Y轴坐标\n        :type FloatY: float\n        """
        self.FloatX = None
        self.FloatY = None


    def _deserialize(self, params):
        self.FloatX = params.get("FloatX")
        self.FloatY = params.get("FloatY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标

    """

    def __init__(self):
        """
        :param Cx: 左上角横坐标\n        :type Cx: int\n        :param Cy: 左上角纵坐标\n        :type Cy: int\n        :param Height: 高度\n        :type Height: int\n        :param Width: 宽度\n        :type Width: int\n        """
        self.Cx = None
        self.Cy = None
        self.Height = None
        self.Width = None


    def _deserialize(self, params):
        self.Cx = params.get("Cx")
        self.Cy = params.get("Cy")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileSampleRequest(AbstractModel):
    """CreateFileSample请求参数结构体

    """

    def __init__(self):
        """
        :param Contents: 文件类型结构数组\n        :type Contents: list of FileSample\n        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
20105：广告引流\n        :type EvilType: int\n        :param FileType: image：图片\n        :type FileType: str\n        :param Label: 样本类型
1：黑库
2：白库\n        :type Label: int\n        """
        self.Contents = None
        self.EvilType = None
        self.FileType = None
        self.Label = None


    def _deserialize(self, params):
        if params.get("Contents") is not None:
            self.Contents = []
            for item in params.get("Contents"):
                obj = FileSample()
                obj._deserialize(item)
                self.Contents.append(obj)
        self.EvilType = params.get("EvilType")
        self.FileType = params.get("FileType")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFileSampleResponse(AbstractModel):
    """CreateFileSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class CreateTextSampleRequest(AbstractModel):
    """CreateTextSample请求参数结构体

    """

    def __init__(self):
        """
        :param Contents: 关键词数组\n        :type Contents: list of str\n        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐
20105：广告引流\n        :type EvilType: int\n        :param Label: 样本类型
1：黑库
2：白库\n        :type Label: int\n        :param Test: 测试修改参数\n        :type Test: str\n        """
        self.Contents = None
        self.EvilType = None
        self.Label = None
        self.Test = None


    def _deserialize(self, params):
        self.Contents = params.get("Contents")
        self.EvilType = params.get("EvilType")
        self.Label = params.get("Label")
        self.Test = params.get("Test")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTextSampleResponse(AbstractModel):
    """CreateTextSample返回参数结构体

    """

    def __init__(self):
        """
        :param ErrMsg: 操作样本失败时返回的错误信息示例：  "样本1":错误码，"样本2":错误码\n        :type ErrMsg: str\n        :param Progress: 任务状态
1：已完成
2：处理中\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ErrMsg = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMsg = params.get("ErrMsg")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class CustomResult(AbstractModel):
    """文本返回的自定义词库结果

    """

    def __init__(self):
        """
        :param Keywords: 命中的自定义关键词\n        :type Keywords: list of str\n        :param LibId: 自定义库id\n        :type LibId: str\n        :param LibName: 自定义词库名称\n        :type LibName: str\n        :param Type: 命中的自定义关键词的类型\n        :type Type: str\n        """
        self.Keywords = None
        self.LibId = None
        self.LibName = None
        self.Type = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileSampleRequest(AbstractModel):
    """DeleteFileSample请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 唯一标识数组\n        :type Ids: list of str\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFileSampleResponse(AbstractModel):
    """DeleteFileSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteTextSampleRequest(AbstractModel):
    """DeleteTextSample请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 唯一标识数组，目前暂时只支持单个删除\n        :type Ids: list of str\n        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTextSampleResponse(AbstractModel):
    """DeleteTextSample返回参数结构体

    """

    def __init__(self):
        """
        :param Progress: 任务状态
1：已完成
2：处理中\n        :type Progress: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeFileSampleRequest(AbstractModel):
    """DescribeFileSample请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过标签值进行筛选\n        :type Filters: list of Filter\n        :param Limit: 数量限制，默认为20，最大值为100\n        :type Limit: int\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc\n        :type OrderDirection: str\n        :param OrderField: 按某个字段排序，目前仅支持CreatedAt排序\n        :type OrderField: str\n        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderDirection = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderDirection = params.get("OrderDirection")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileSampleResponse(AbstractModel):
    """DescribeFileSample返回参数结构体

    """

    def __init__(self):
        """
        :param FileSampleSet: 符合要求的样本的信息\n        :type FileSampleSet: list of FileSampleInfo\n        :param TotalCount: 符合要求的样本的数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FileSampleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSampleSet") is not None:
            self.FileSampleSet = []
            for item in params.get("FileSampleSet"):
                obj = FileSampleInfo()
                obj._deserialize(item)
                self.FileSampleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTextSampleRequest(AbstractModel):
    """DescribeTextSample请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持通过标签值进行筛选\n        :type Filters: list of Filter\n        :param Limit: 数量限制，默认为20，最大值为100\n        :type Limit: int\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param OrderDirection: 升序（asc）还是降序（desc），默认：desc\n        :type OrderDirection: str\n        :param OrderField: 按某个字段排序，目前仅支持CreatedAt排序\n        :type OrderField: str\n        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderDirection = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderDirection = params.get("OrderDirection")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTextSampleResponse(AbstractModel):
    """DescribeTextSample返回参数结构体

    """

    def __init__(self):
        """
        :param TextSampleSet: 符合要求的样本的信息\n        :type TextSampleSet: list of TextSample\n        :param TotalCount: 符合要求的样本的数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TextSampleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextSampleSet") is not None:
            self.TextSampleSet = []
            for item in params.get("TextSampleSet"):
                obj = TextSample()
                obj._deserialize(item)
                self.TextSampleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetailResult(AbstractModel):
    """文本返回的详细结果

    """

    def __init__(self):
        """
        :param EvilLabel: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词\n        :type EvilLabel: str\n        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐\n        :type EvilType: int\n        :param Keywords: 该标签下命中的关键词\n        :type Keywords: list of str\n        :param Score: 该标签模型命中的分值\n        :type Score: int\n        """
        self.EvilLabel = None
        self.EvilType = None
        self.Keywords = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilLabel = params.get("EvilLabel")
        self.EvilType = params.get("EvilType")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Device(AbstractModel):
    """设备信息

    """

    def __init__(self):
        """
        :param DeviceId: 设备指纹ID\n        :type DeviceId: str\n        :param IDFA: IOS设备，Identifier For Advertising（广告标识符）\n        :type IDFA: str\n        :param IDFV: IOS设备，IDFV - Identifier For Vendor（应用开发商标识符）\n        :type IDFV: str\n        :param IMEI: 设备序列号\n        :type IMEI: str\n        :param IP: 用户IP\n        :type IP: str\n        :param Mac: Mac地址\n        :type Mac: str\n        :param TokenId: 设备指纹Token\n        :type TokenId: str\n        """
        self.DeviceId = None
        self.IDFA = None
        self.IDFV = None
        self.IMEI = None
        self.IP = None
        self.Mac = None
        self.TokenId = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.IDFA = params.get("IDFA")
        self.IDFV = params.get("IDFV")
        self.IMEI = params.get("IMEI")
        self.IP = params.get("IP")
        self.Mac = params.get("Mac")
        self.TokenId = params.get("TokenId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSample(AbstractModel):
    """文件类型样本

    """

    def __init__(self):
        """
        :param FileMd5: 文件md5\n        :type FileMd5: str\n        :param FileName: 文件名称\n        :type FileName: str\n        :param FileUrl: 文件url\n        :type FileUrl: str\n        :param CompressFileUrl: 文件压缩后云url\n        :type CompressFileUrl: str\n        """
        self.FileMd5 = None
        self.FileName = None
        self.FileUrl = None
        self.CompressFileUrl = None


    def _deserialize(self, params):
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        self.CompressFileUrl = params.get("CompressFileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileSampleInfo(AbstractModel):
    """文件样本返回信息

    """

    def __init__(self):
        """
        :param Code: 处理错误码\n        :type Code: int\n        :param CreatedAt: 创建时间戳\n        :type CreatedAt: int\n        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐\n        :type EvilType: int\n        :param FileMd5: 文件的md5\n        :type FileMd5: str\n        :param FileName: 文件名称\n        :type FileName: str\n        :param FileType: 文件类型\n        :type FileType: str\n        :param Id: 唯一标识\n        :type Id: str\n        :param Label: 样本类型
1：黑库
2：白库\n        :type Label: int\n        :param Status: 任务状态
1：添加完成
2：添加处理中
3：下载中
4：下载完成
5：上传完成
6：步骤完成\n        :type Status: int\n        :param CompressFileUrl: 文件压缩后云url\n        :type CompressFileUrl: str\n        :param FileUrl: 文件的url\n        :type FileUrl: str\n        """
        self.Code = None
        self.CreatedAt = None
        self.EvilType = None
        self.FileMd5 = None
        self.FileName = None
        self.FileType = None
        self.Id = None
        self.Label = None
        self.Status = None
        self.CompressFileUrl = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.CreatedAt = params.get("CreatedAt")
        self.EvilType = params.get("EvilType")
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Status = params.get("Status")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """筛选数据结构

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段\n        :type Name: str\n        :param Value: 需要过滤字段的值\n        :type Value: str\n        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageData(AbstractModel):
    """图片识别结果详情

    """

    def __init__(self):
        """
        :param EvilFlag: 是否恶意 0：正常 1：可疑\n        :type EvilFlag: int\n        :param EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
20103：性感
24001：暴恐\n        :type EvilType: int\n        :param CodeDetect: 图片二维码详情\n        :type CodeDetect: :class:`tencentcloud.cms.v20190321.models.CodeDetect`\n        :param HotDetect: 图片性感详情\n        :type HotDetect: :class:`tencentcloud.cms.v20190321.models.ImageHotDetect`\n        :param IllegalDetect: 图片违法详情\n        :type IllegalDetect: :class:`tencentcloud.cms.v20190321.models.ImageIllegalDetect`\n        :param LogoDetect: logo详情\n        :type LogoDetect: :class:`tencentcloud.cms.v20190321.models.LogoDetail`\n        :param OCRDetect: 图片OCR详情\n        :type OCRDetect: :class:`tencentcloud.cms.v20190321.models.OCRDetect`\n        :param PhoneDetect: 手机检测详情\n        :type PhoneDetect: :class:`tencentcloud.cms.v20190321.models.PhoneDetect`\n        :param PolityDetect: 图片涉政详情\n        :type PolityDetect: :class:`tencentcloud.cms.v20190321.models.ImagePolityDetect`\n        :param PornDetect: 图片涉黄详情\n        :type PornDetect: :class:`tencentcloud.cms.v20190321.models.ImagePornDetect`\n        :param Similar: 图片相似度详情\n        :type Similar: :class:`tencentcloud.cms.v20190321.models.Similar`\n        :param TerrorDetect: 图片暴恐详情\n        :type TerrorDetect: :class:`tencentcloud.cms.v20190321.models.ImageTerrorDetect`\n        """
        self.EvilFlag = None
        self.EvilType = None
        self.CodeDetect = None
        self.HotDetect = None
        self.IllegalDetect = None
        self.LogoDetect = None
        self.OCRDetect = None
        self.PhoneDetect = None
        self.PolityDetect = None
        self.PornDetect = None
        self.Similar = None
        self.TerrorDetect = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("CodeDetect") is not None:
            self.CodeDetect = CodeDetect()
            self.CodeDetect._deserialize(params.get("CodeDetect"))
        if params.get("HotDetect") is not None:
            self.HotDetect = ImageHotDetect()
            self.HotDetect._deserialize(params.get("HotDetect"))
        if params.get("IllegalDetect") is not None:
            self.IllegalDetect = ImageIllegalDetect()
            self.IllegalDetect._deserialize(params.get("IllegalDetect"))
        if params.get("LogoDetect") is not None:
            self.LogoDetect = LogoDetail()
            self.LogoDetect._deserialize(params.get("LogoDetect"))
        if params.get("OCRDetect") is not None:
            self.OCRDetect = OCRDetect()
            self.OCRDetect._deserialize(params.get("OCRDetect"))
        if params.get("PhoneDetect") is not None:
            self.PhoneDetect = PhoneDetect()
            self.PhoneDetect._deserialize(params.get("PhoneDetect"))
        if params.get("PolityDetect") is not None:
            self.PolityDetect = ImagePolityDetect()
            self.PolityDetect._deserialize(params.get("PolityDetect"))
        if params.get("PornDetect") is not None:
            self.PornDetect = ImagePornDetect()
            self.PornDetect._deserialize(params.get("PornDetect"))
        if params.get("Similar") is not None:
            self.Similar = Similar()
            self.Similar._deserialize(params.get("Similar"))
        if params.get("TerrorDetect") is not None:
            self.TerrorDetect = ImageTerrorDetect()
            self.TerrorDetect._deserialize(params.get("TerrorDetect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageHotDetect(AbstractModel):
    """图片性感详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
20103：性感\n        :type EvilType: int\n        :param HitFlag: 处置判定 0：正常 1：可疑\n        :type HitFlag: int\n        :param Keywords: 关键词明细\n        :type Keywords: list of str\n        :param Labels: 性感标签：性感特征中文描述\n        :type Labels: list of str\n        :param Score: 性感分：分值范围 0-100，分数越高性感倾向越明显\n        :type Score: int\n        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageIllegalDetect(AbstractModel):
    """图片违法详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常 
20006：涉毒违法\n        :type EvilType: int\n        :param HitFlag: 处置判定 0：正常 1：可疑\n        :type HitFlag: int\n        :param Keywords: 关键词明细\n        :type Keywords: list of str\n        :param Labels: 违法标签：返回违法特征中文描述，如赌桌，枪支\n        :type Labels: list of str\n        :param Score: 违法分：分值范围 0-100，分数越高违法倾向越明显\n        :type Score: int\n        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationRequest(AbstractModel):
    """ImageModeration请求参数结构体

    """

    def __init__(self):
        """
        :param FileContent: 文件内容 Base64,与FileUrl必须二填一\n        :type FileContent: str\n        :param FileMD5: 文件MD5值\n        :type FileMD5: str\n        :param FileUrl: 文件地址\n        :type FileUrl: str\n        """
        self.FileContent = None
        self.FileMD5 = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileMD5 = params.get("FileMD5")
        self.FileUrl = params.get("FileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 识别结果\n        :type Data: :class:`tencentcloud.cms.v20190321.models.ImageData`\n        :param BusinessCode: 业务返回码\n        :type BusinessCode: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.BusinessCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ImageData()
            self.Data._deserialize(params.get("Data"))
        self.BusinessCode = params.get("BusinessCode")
        self.RequestId = params.get("RequestId")


class ImagePolityDetect(AbstractModel):
    """图片涉政详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常 
20001：政治\n        :type EvilType: int\n        :param HitFlag: 处置判定  0：正常 1：可疑\n        :type HitFlag: int\n        :param PolityLogoDetail: 命中的logo标签信息\n        :type PolityLogoDetail: list of Logo\n        :param FaceNames: 命中的人脸名称\n        :type FaceNames: list of str\n        :param Keywords: 关键词明细\n        :type Keywords: list of str\n        :param PolityItems: 命中的政治物品名称\n        :type PolityItems: list of str\n        :param Score: 政治（人脸）分：分值范围 0-100，分数越高可疑程度越高\n        :type Score: int\n        """
        self.EvilType = None
        self.HitFlag = None
        self.PolityLogoDetail = None
        self.FaceNames = None
        self.Keywords = None
        self.PolityItems = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        if params.get("PolityLogoDetail") is not None:
            self.PolityLogoDetail = []
            for item in params.get("PolityLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self.PolityLogoDetail.append(obj)
        self.FaceNames = params.get("FaceNames")
        self.Keywords = params.get("Keywords")
        self.PolityItems = params.get("PolityItems")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImagePornDetect(AbstractModel):
    """图片涉黄详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
20002：色情\n        :type EvilType: int\n        :param HitFlag: 处置判定 0：正常 1：可疑\n        :type HitFlag: int\n        :param Keywords: 关键词明细\n        :type Keywords: list of str\n        :param Labels: 色情标签：色情特征中文描述\n        :type Labels: list of str\n        :param Score: 色情分：分值范围 0-100，分数越高色情倾向越明显\n        :type Score: int\n        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTerrorDetect(AbstractModel):
    """图片暴恐详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
24001：暴恐\n        :type EvilType: int\n        :param HitFlag: 处置判定 0：正常 1：可疑\n        :type HitFlag: int\n        :param Keywords: 关键词明细\n        :type Keywords: list of str\n        :param Labels: 暴恐标签：返回暴恐特征中文描述\n        :type Labels: list of str\n        :param Score: 暴恐分：分值范围0--100，分数越高暴恐倾向越明显\n        :type Score: int\n        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Logo(AbstractModel):
    """Logo

    """

    def __init__(self):
        """
        :param RrectF: logo图标坐标信息\n        :type RrectF: :class:`tencentcloud.cms.v20190321.models.RrectF`\n        :param Confidence: logo图标置信度\n        :type Confidence: float\n        :param Name: logo图标名称\n        :type Name: str\n        """
        self.RrectF = None
        self.Confidence = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("RrectF") is not None:
            self.RrectF = RrectF()
            self.RrectF._deserialize(params.get("RrectF"))
        self.Confidence = params.get("Confidence")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoDetail(AbstractModel):
    """LogoDetail

    """

    def __init__(self):
        """
        :param AppLogoDetail: 命中的Applogo详情\n        :type AppLogoDetail: list of Logo\n        """
        self.AppLogoDetail = None


    def _deserialize(self, params):
        if params.get("AppLogoDetail") is not None:
            self.AppLogoDetail = []
            for item in params.get("AppLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self.AppLogoDetail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualReviewContent(AbstractModel):
    """人审审核数据相关信息

    """

    def __init__(self):
        """
        :param BatchId: 审核批次号\n        :type BatchId: str\n        :param Content: 审核内容\n        :type Content: str\n        :param ContentId: 消息Id\n        :type ContentId: str\n        :param ContentType: 审核内容类型 1 图片 2 视频 3 文本 4 音频\n        :type ContentType: int\n        :param UserInfo: 用户信息\n        :type UserInfo: :class:`tencentcloud.cms.v20190321.models.User`\n        :param AutoDetailCode: 机器审核类型，与腾讯机器审核定义一致
100 正常
20001 政治
20002 色情
20006 违法
20007 谩骂
24001 暴恐
20105 广告
20103 性感\n        :type AutoDetailCode: int\n        :param AutoResult: 机器审核结果 0 放过 1 拦截\n        :type AutoResult: int\n        :param CallBackInfo: 回调信息标识，回传数据时原样返回\n        :type CallBackInfo: str\n        :param CreateTime: 创建时间 格式“2020-01-01 00:00:12”\n        :type CreateTime: str\n        :param Priority: 审核优先级，可选值 [1,2,3,4]，其中 1 最高，4 最低\n        :type Priority: int\n        :param Title: 标题\n        :type Title: str\n        """
        self.BatchId = None
        self.Content = None
        self.ContentId = None
        self.ContentType = None
        self.UserInfo = None
        self.AutoDetailCode = None
        self.AutoResult = None
        self.CallBackInfo = None
        self.CreateTime = None
        self.Priority = None
        self.Title = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.Content = params.get("Content")
        self.ContentId = params.get("ContentId")
        self.ContentType = params.get("ContentType")
        if params.get("UserInfo") is not None:
            self.UserInfo = User()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.AutoDetailCode = params.get("AutoDetailCode")
        self.AutoResult = params.get("AutoResult")
        self.CallBackInfo = params.get("CallBackInfo")
        self.CreateTime = params.get("CreateTime")
        self.Priority = params.get("Priority")
        self.Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualReviewData(AbstractModel):
    """人工审核接口返回结果，由ContentId和BatchId组成

    """

    def __init__(self):
        """
        :param BatchId: 人审内容批次号\n        :type BatchId: str\n        :param ContentId: 人审内容ID\n        :type ContentId: str\n        """
        self.BatchId = None
        self.ContentId = None


    def _deserialize(self, params):
        self.BatchId = params.get("BatchId")
        self.ContentId = params.get("ContentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualReviewRequest(AbstractModel):
    """ManualReview请求参数结构体

    """

    def __init__(self):
        """
        :param ReviewContent: 人工审核信息\n        :type ReviewContent: :class:`tencentcloud.cms.v20190321.models.ManualReviewContent`\n        """
        self.ReviewContent = None


    def _deserialize(self, params):
        if params.get("ReviewContent") is not None:
            self.ReviewContent = ManualReviewContent()
            self.ReviewContent._deserialize(params.get("ReviewContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualReviewResponse(AbstractModel):
    """ManualReview返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 人审接口同步响应结果\n        :type Data: :class:`tencentcloud.cms.v20190321.models.ManualReviewData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ManualReviewData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class OCRDetect(AbstractModel):
    """OCR识别结果详情

    """

    def __init__(self):
        """
        :param Item: 识别到的详细信息\n        :type Item: list of OCRItem\n        :param TextInfo: 识别到的文本信息\n        :type TextInfo: str\n        """
        self.Item = None
        self.TextInfo = None


    def _deserialize(self, params):
        if params.get("Item") is not None:
            self.Item = []
            for item in params.get("Item"):
                obj = OCRItem()
                obj._deserialize(item)
                self.Item.append(obj)
        self.TextInfo = params.get("TextInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OCRItem(AbstractModel):
    """OCR详情

    """

    def __init__(self):
        """
        :param TextPosition: 检测到的文本坐标信息\n        :type TextPosition: :class:`tencentcloud.cms.v20190321.models.Coordinate`\n        :param EvilLabel: 文本命中具体标签\n        :type EvilLabel: str\n        :param EvilType: 文本命中恶意违规类型\n        :type EvilType: int\n        :param Keywords: 文本命中违规的关键词\n        :type Keywords: list of str\n        :param Rate: 文本涉嫌违规分值\n        :type Rate: int\n        :param TextContent: 检测到的文本信息\n        :type TextContent: str\n        """
        self.TextPosition = None
        self.EvilLabel = None
        self.EvilType = None
        self.Keywords = None
        self.Rate = None
        self.TextContent = None


    def _deserialize(self, params):
        if params.get("TextPosition") is not None:
            self.TextPosition = Coordinate()
            self.TextPosition._deserialize(params.get("TextPosition"))
        self.EvilLabel = params.get("EvilLabel")
        self.EvilType = params.get("EvilType")
        self.Keywords = params.get("Keywords")
        self.Rate = params.get("Rate")
        self.TextContent = params.get("TextContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhoneDetect(AbstractModel):
    """手机模型识别检测

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常
21000：综合\n        :type EvilType: int\n        :param HitFlag: 处置判定 0：正常 1：可疑\n        :type HitFlag: int\n        :param Labels: 特征中文描述\n        :type Labels: list of str\n        :param Score: 分值范围 0-100，分数越高倾向越明显\n        :type Score: int\n        """
        self.EvilType = None
        self.HitFlag = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDetails(AbstractModel):
    """账号风险检测结果

    """

    def __init__(self):
        """
        :param Keywords: 预留字段，暂时不使用\n        :type Keywords: list of str\n        :param Label: 风险类别，RiskAccount，RiskIP, RiskIMEI\n        :type Label: str\n        :param Lable: 预留字段，暂时不用\n        :type Lable: str\n        :param Level: 风险等级，1:疑似，2：恶意\n        :type Level: int\n        """
        self.Keywords = None
        self.Label = None
        self.Lable = None
        self.Level = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.Label = params.get("Label")
        self.Lable = params.get("Lable")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RrectF(AbstractModel):
    """logo位置信息

    """

    def __init__(self):
        """
        :param Cx: logo横坐标\n        :type Cx: float\n        :param Cy: logo纵坐标\n        :type Cy: float\n        :param Height: logo图标高度\n        :type Height: float\n        :param Rotate: logo图标中心旋转度\n        :type Rotate: float\n        :param Width: logo图标宽度\n        :type Width: float\n        """
        self.Cx = None
        self.Cy = None
        self.Height = None
        self.Rotate = None
        self.Width = None


    def _deserialize(self, params):
        self.Cx = params.get("Cx")
        self.Cy = params.get("Cy")
        self.Height = params.get("Height")
        self.Rotate = params.get("Rotate")
        self.Width = params.get("Width")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Similar(AbstractModel):
    """相似度详情

    """

    def __init__(self):
        """
        :param EvilType: 恶意类型
100：正常 
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
24001：暴恐\n        :type EvilType: int\n        :param HitFlag: 处置判定 0：未匹配到 1：恶意 2：白样本\n        :type HitFlag: int\n        :param SeedUrl: 返回的种子url\n        :type SeedUrl: str\n        """
        self.EvilType = None
        self.HitFlag = None
        self.SeedUrl = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.SeedUrl = params.get("SeedUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextData(AbstractModel):
    """文本识别结果详情

    """

    def __init__(self):
        """
        :param EvilFlag: 是否恶意 0：正常 1：可疑\n        :type EvilFlag: int\n        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂
20105：广告引流 
24001：暴恐\n        :type EvilType: int\n        :param Common: 消息类公共相关参数\n        :type Common: :class:`tencentcloud.cms.v20190321.models.TextOutputComm`\n        :param CustomResult: 返回的自定义词库结果\n        :type CustomResult: list of CustomResult\n        :param DetailResult: 返回的详细结果\n        :type DetailResult: list of DetailResult\n        :param ID: 消息类ID信息\n        :type ID: :class:`tencentcloud.cms.v20190321.models.TextOutputID`\n        :param Res: 消息类输出结果\n        :type Res: :class:`tencentcloud.cms.v20190321.models.TextOutputRes`\n        :param RiskDetails: 账号风险检测结果\n        :type RiskDetails: list of RiskDetails\n        :param BizType: 最终使用的BizType\n        :type BizType: int\n        :param DataId: 和请求中的DataId一致，原样返回\n        :type DataId: str\n        :param EvilLabel: 恶意标签，Normal：正常，Polity：涉政，Porn：色情，Illegal：违法，Abuse：谩骂，Terror：暴恐，Ad：广告，Custom：自定义关键词\n        :type EvilLabel: str\n        :param Extra: 输出的其他信息，不同客户内容不同\n        :type Extra: str\n        :param Keywords: 命中的关键词\n        :type Keywords: list of str\n        :param Score: 命中的模型分值\n        :type Score: int\n        :param Suggestion: 建议值,Block：打击,Review：待复审,Normal：正常\n        :type Suggestion: str\n        """
        self.EvilFlag = None
        self.EvilType = None
        self.Common = None
        self.CustomResult = None
        self.DetailResult = None
        self.ID = None
        self.Res = None
        self.RiskDetails = None
        self.BizType = None
        self.DataId = None
        self.EvilLabel = None
        self.Extra = None
        self.Keywords = None
        self.Score = None
        self.Suggestion = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("Common") is not None:
            self.Common = TextOutputComm()
            self.Common._deserialize(params.get("Common"))
        if params.get("CustomResult") is not None:
            self.CustomResult = []
            for item in params.get("CustomResult"):
                obj = CustomResult()
                obj._deserialize(item)
                self.CustomResult.append(obj)
        if params.get("DetailResult") is not None:
            self.DetailResult = []
            for item in params.get("DetailResult"):
                obj = DetailResult()
                obj._deserialize(item)
                self.DetailResult.append(obj)
        if params.get("ID") is not None:
            self.ID = TextOutputID()
            self.ID._deserialize(params.get("ID"))
        if params.get("Res") is not None:
            self.Res = TextOutputRes()
            self.Res._deserialize(params.get("Res"))
        if params.get("RiskDetails") is not None:
            self.RiskDetails = []
            for item in params.get("RiskDetails"):
                obj = RiskDetails()
                obj._deserialize(item)
                self.RiskDetails.append(obj)
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        self.EvilLabel = params.get("EvilLabel")
        self.Extra = params.get("Extra")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")
        self.Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationRequest(AbstractModel):
    """TextModeration请求参数结构体

    """

    def __init__(self):
        """
        :param Content: 文本内容Base64编码。原文长度需小于15000字节，即5000个汉字以内。\n        :type Content: str\n        :param Device: 设备相关信息\n        :type Device: :class:`tencentcloud.cms.v20190321.models.Device`\n        :param User: 用户相关信息\n        :type User: :class:`tencentcloud.cms.v20190321.models.User`\n        :param BizType: 该字段用于标识业务场景。您可以在内容安全控制台创建对应的ID，配置不同的内容审核策略，通过接口调用，默认不填为0，后端使用默认策略\n        :type BizType: int\n        :param DataId: 数据ID，英文字母、下划线、-组成，不超过64个字符\n        :type DataId: str\n        :param SdkAppId: 业务应用ID\n        :type SdkAppId: int\n        """
        self.Content = None
        self.Device = None
        self.User = None
        self.BizType = None
        self.DataId = None
        self.SdkAppId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        if params.get("User") is not None:
            self.User = User()
            self.User._deserialize(params.get("User"))
        self.BizType = params.get("BizType")
        self.DataId = params.get("DataId")
        self.SdkAppId = params.get("SdkAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextModerationResponse(AbstractModel):
    """TextModeration返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 识别结果\n        :type Data: :class:`tencentcloud.cms.v20190321.models.TextData`\n        :param BusinessCode: 业务返回码\n        :type BusinessCode: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Data = None
        self.BusinessCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TextData()
            self.Data._deserialize(params.get("Data"))
        self.BusinessCode = params.get("BusinessCode")
        self.RequestId = params.get("RequestId")


class TextOutputComm(AbstractModel):
    """消息类输出公共参数

    """

    def __init__(self):
        """
        :param AppID: 接入业务的唯一ID\n        :type AppID: int\n        :param BUCtrlID: 接口唯一ID，旁路调用接口返回有该字段，标识唯一接口\n        :type BUCtrlID: int\n        :param SendTime: 消息发送时间\n        :type SendTime: int\n        :param Uin: 请求字段里的Common.Uin\n        :type Uin: int\n        """
        self.AppID = None
        self.BUCtrlID = None
        self.SendTime = None
        self.Uin = None


    def _deserialize(self, params):
        self.AppID = params.get("AppID")
        self.BUCtrlID = params.get("BUCtrlID")
        self.SendTime = params.get("SendTime")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextOutputID(AbstractModel):
    """消息类输出ID参数

    """

    def __init__(self):
        """
        :param MsgID: 接入业务的唯一ID\n        :type MsgID: str\n        :param Uin: 用户账号uin，对应请求协议里的Content.User.Uin。旁路结果有回带，串联结果无该字段\n        :type Uin: str\n        """
        self.MsgID = None
        self.Uin = None


    def _deserialize(self, params):
        self.MsgID = params.get("MsgID")
        self.Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextOutputRes(AbstractModel):
    """消息类输出结果参数

    """

    def __init__(self):
        """
        :param Operator: 操作人,信安处理人企业微信ID\n        :type Operator: str\n        :param ResultCode: 恶意操作码，
删除（1）， 通过（2）， 先审后发（100012）\n        :type ResultCode: int\n        :param ResultMsg: 操作结果备注说明\n        :type ResultMsg: str\n        :param ResultType: 恶意类型，广告（10001）， 政治（20001）， 色情（20002）， 社会事件（20004）， 暴力（20011）， 低俗（20012）， 违法犯罪（20006）， 欺诈（20008）， 版权（20013）， 谣言（20104）， 其他（21000）\n        :type ResultType: int\n        """
        self.Operator = None
        self.ResultCode = None
        self.ResultMsg = None
        self.ResultType = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.ResultCode = params.get("ResultCode")
        self.ResultMsg = params.get("ResultMsg")
        self.ResultType = params.get("ResultType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextSample(AbstractModel):
    """文字样本信息

    """

    def __init__(self):
        """
        :param Code: 处理错误码\n        :type Code: int\n        :param Content: 关键词\n        :type Content: str\n        :param CreatedAt: 创建时间戳\n        :type CreatedAt: int\n        :param EvilType: 恶意类型
100：正常
20001：政治
20002：色情 
20006：涉毒违法
20007：谩骂 
20105：广告引流 
24001：暴恐\n        :type EvilType: int\n        :param Id: 唯一标识\n        :type Id: str\n        :param Label: 样本类型
1：黑库
2：白库\n        :type Label: int\n        :param Status: 任务状态
1：已完成
2：处理中\n        :type Status: int\n        """
        self.Code = None
        self.Content = None
        self.CreatedAt = None
        self.EvilType = None
        self.Id = None
        self.Label = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Content = params.get("Content")
        self.CreatedAt = params.get("CreatedAt")
        self.EvilType = params.get("EvilType")
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """用户相关信息

    """

    def __init__(self):
        """
        :param AccountType: 账号类别，"1-微信uin 2-QQ号 3-微信群uin 4-qq群号 5-微信openid 6-QQopenid 7-其它string"\n        :type AccountType: int\n        :param Age: 年龄 默认0 未知\n        :type Age: int\n        :param Gender: 性别 默认0 未知 1 男性 2 女性\n        :type Gender: int\n        :param Level: 用户等级，默认0 未知 1 低 2 中 3 高\n        :type Level: int\n        :param Nickname: 用户昵称\n        :type Nickname: str\n        :param Phone: 手机号\n        :type Phone: str\n        :param UserId: 用户账号ID，如填写，会根据账号历史恶意情况，判定消息有害结果，特别是有利于可疑恶意情况下的辅助判断。账号可以填写微信uin、QQ号、微信openid、QQopenid、字符串等。该字段和账号类别确定唯一账号。\n        :type UserId: str\n        """
        self.AccountType = None
        self.Age = None
        self.Gender = None
        self.Level = None
        self.Nickname = None
        self.Phone = None
        self.UserId = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Age = params.get("Age")
        self.Gender = params.get("Gender")
        self.Level = params.get("Level")
        self.Nickname = params.get("Nickname")
        self.Phone = params.get("Phone")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        