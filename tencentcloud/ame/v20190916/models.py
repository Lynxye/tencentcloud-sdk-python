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


class Album(AbstractModel):
    """Album

    """

    def __init__(self):
        """
        :param AlbumName: 专辑名\n        :type AlbumName: str\n        :param ImagePathMap: 专辑图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImagePathMap: list of ImagePath\n        """
        self.AlbumName = None
        self.ImagePathMap = None


    def _deserialize(self, params):
        self.AlbumName = params.get("AlbumName")
        if params.get("ImagePathMap") is not None:
            self.ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self.ImagePathMap.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Artist(AbstractModel):
    """Artist

    """

    def __init__(self):
        """
        :param ArtistName: 歌手名\n        :type ArtistName: str\n        """
        self.ArtistName = None


    def _deserialize(self, params):
        self.ArtistName = params.get("ArtistName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthInfo(AbstractModel):
    """AuthInfo集合

    """

    def __init__(self):
        """
        :param SubjectName: 主体名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubjectName: str\n        :param ProjectName: 项目名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectName: str\n        :param AppScene: 应用场景\n        :type AppScene: int\n        :param AppRegion: 应用地域\n        :type AppRegion: int\n        :param AuthPeriod: 授权时间\n        :type AuthPeriod: int\n        :param Commercialization: 是否可商业化\n        :type Commercialization: int\n        :param Platform: 是否可跨平台\n        :type Platform: int\n        :param Id: 加密后Id\n        :type Id: str\n        """
        self.SubjectName = None
        self.ProjectName = None
        self.AppScene = None
        self.AppRegion = None
        self.AuthPeriod = None
        self.Commercialization = None
        self.Platform = None
        self.Id = None


    def _deserialize(self, params):
        self.SubjectName = params.get("SubjectName")
        self.ProjectName = params.get("ProjectName")
        self.AppScene = params.get("AppScene")
        self.AppRegion = params.get("AppRegion")
        self.AuthPeriod = params.get("AuthPeriod")
        self.Commercialization = params.get("Commercialization")
        self.Platform = params.get("Platform")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataInfo(AbstractModel):
    """数据信息

    """

    def __init__(self):
        """
        :param Name: Song Name\n        :type Name: str\n        :param Version: 歌曲版本\n        :type Version: str\n        :param Duration: 歌曲总时长（非试听时长）\n        :type Duration: str\n        :param AuditionBegin: 试听开始时间\n        :type AuditionBegin: int\n        :param AuditionEnd: 试听结束时间\n        :type AuditionEnd: int\n        """
        self.Name = None
        self.Version = None
        self.Duration = None
        self.AuditionBegin = None
        self.AuditionEnd = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Duration = params.get("Duration")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthInfoRequest(AbstractModel):
    """DescribeAuthInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量：Offset=Offset+Limit\n        :type Offset: int\n        :param Limit: 数据条数\n        :type Limit: int\n        :param Key: 搜索关键字\n        :type Key: str\n        """
        self.Offset = None
        self.Limit = None
        self.Key = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthInfoResponse(AbstractModel):
    """DescribeAuthInfo返回参数结构体

    """

    def __init__(self):
        """
        :param AuthInfo: 授权项目列表\n        :type AuthInfo: list of AuthInfo\n        :param TotalCount: 总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AuthInfo = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AuthInfo") is not None:
            self.AuthInfo = []
            for item in params.get("AuthInfo"):
                obj = AuthInfo()
                obj._deserialize(item)
                self.AuthInfo.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCloudMusicPurchasedRequest(AbstractModel):
    """DescribeCloudMusicPurchased请求参数结构体

    """

    def __init__(self):
        """
        :param AuthInfoId: 授权项目Id\n        :type AuthInfoId: str\n        """
        self.AuthInfoId = None


    def _deserialize(self, params):
        self.AuthInfoId = params.get("AuthInfoId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudMusicPurchasedResponse(AbstractModel):
    """DescribeCloudMusicPurchased返回参数结构体

    """

    def __init__(self):
        """
        :param MusicOpenDetail: 云音乐列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type MusicOpenDetail: list of MusicOpenDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MusicOpenDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MusicOpenDetail") is not None:
            self.MusicOpenDetail = []
            for item in params.get("MusicOpenDetail"):
                obj = MusicOpenDetail()
                obj._deserialize(item)
                self.MusicOpenDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCloudMusicRequest(AbstractModel):
    """DescribeCloudMusic请求参数结构体

    """

    def __init__(self):
        """
        :param MusicId: 歌曲Id\n        :type MusicId: str\n        :param MusicType: 歌曲类型，可选值有：
<li>MP3-128K-FTW：含有水印的试听资源；</li>
<li>MP3-320K-FTD-P：320kbps歌曲热门片段；</li>
<li>MP3-320K-FTD：320kbps已核验歌曲完整资源。</li>
默认为：MP3-128K-FTW\n        :type MusicType: str\n        """
        self.MusicId = None
        self.MusicType = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.MusicType = params.get("MusicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudMusicResponse(AbstractModel):
    """DescribeCloudMusic返回参数结构体

    """

    def __init__(self):
        """
        :param MusicId: 歌曲Id\n        :type MusicId: str\n        :param MusicName: 歌曲名称\n        :type MusicName: str\n        :param Duration: 歌曲时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type Duration: int\n        :param MusicUrl: 歌曲链接\n        :type MusicUrl: str\n        :param MusicImageUrl: 歌曲图片
注意：此字段可能返回 null，表示取不到有效值。\n        :type MusicImageUrl: str\n        :param Singers: 歌手列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Singers: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MusicId = None
        self.MusicName = None
        self.Duration = None
        self.MusicUrl = None
        self.MusicImageUrl = None
        self.Singers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.MusicName = params.get("MusicName")
        self.Duration = params.get("Duration")
        self.MusicUrl = params.get("MusicUrl")
        self.MusicImageUrl = params.get("MusicImageUrl")
        self.Singers = params.get("Singers")
        self.RequestId = params.get("RequestId")


class DescribeItemByIdRequest(AbstractModel):
    """DescribeItemById请求参数结构体

    """

    def __init__(self):
        """
        :param ItemIDs: 歌曲ID，目前暂不支持批量查询\n        :type ItemIDs: str\n        """
        self.ItemIDs = None


    def _deserialize(self, params):
        self.ItemIDs = params.get("ItemIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeItemByIdResponse(AbstractModel):
    """DescribeItemById返回参数结构体

    """

    def __init__(self):
        """
        :param Items: 歌曲信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Items: list of Item\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeItemsRequest(AbstractModel):
    """DescribeItems请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: offset (Default = 0)，(当前页-1) * Limit\n        :type Offset: int\n        :param Limit: 条数，必须大于0，最大值为30\n        :type Limit: int\n        :param CategoryId: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。\n        :type CategoryId: str\n        :param CategoryCode: （电台/歌单）ID，CategoryId和CategoryCode两个必传1个，可以从<a href="https://cloud.tencent.com/document/product/1155/40109">获取分类内容（Station）列表接口</a>中获取。\n        :type CategoryCode: str\n        """
        self.Offset = None
        self.Limit = None
        self.CategoryId = None
        self.CategoryCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CategoryId = params.get("CategoryId")
        self.CategoryCode = params.get("CategoryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeItemsResponse(AbstractModel):
    """DescribeItems返回参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移量\n        :type Offset: int\n        :param Size: 当前页歌曲数量\n        :type Size: int\n        :param Total: 总数据条数\n        :type Total: int\n        :param HaveMore: 剩余数量（total-offset-size），通过这个值判断是否
还有下一页\n        :type HaveMore: int\n        :param Items: Items 歌曲列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Items: list of Item\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Offset = None
        self.Size = None
        self.Total = None
        self.HaveMore = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        self.Total = params.get("Total")
        self.HaveMore = params.get("HaveMore")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKTVMusicDetailRequest(AbstractModel):
    """DescribeKTVMusicDetail请求参数结构体

    """

    def __init__(self):
        """
        :param MusicId: 曲目 Id\n        :type MusicId: str\n        """
        self.MusicId = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKTVMusicDetailResponse(AbstractModel):
    """DescribeKTVMusicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param KTVMusicBaseInfo: 歌曲基础信息\n        :type KTVMusicBaseInfo: :class:`tencentcloud.ame.v20190916.models.KTVMusicBaseInfo`\n        :param PlayToken: 播放凭证\n        :type PlayToken: str\n        :param LyricsUrl: 歌词下载地址\n        :type LyricsUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KTVMusicBaseInfo = None
        self.PlayToken = None
        self.LyricsUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KTVMusicBaseInfo") is not None:
            self.KTVMusicBaseInfo = KTVMusicBaseInfo()
            self.KTVMusicBaseInfo._deserialize(params.get("KTVMusicBaseInfo"))
        self.PlayToken = params.get("PlayToken")
        self.LyricsUrl = params.get("LyricsUrl")
        self.RequestId = params.get("RequestId")


class DescribeLyricRequest(AbstractModel):
    """DescribeLyric请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 歌曲ID\n        :type ItemId: str\n        :param SubItemType: 歌词格式，可选项，可不填写，目前填写只能填LRC-LRC。该字段为预留的扩展字段。后续如果不填，会返回歌曲的所有格式的歌词。如果填写某个正确的格式，则只返回该格式的歌词。\n        :type SubItemType: str\n        """
        self.ItemId = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.SubItemType = params.get("SubItemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLyricResponse(AbstractModel):
    """DescribeLyric返回参数结构体

    """

    def __init__(self):
        """
        :param Lyric: 歌词详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Lyric: :class:`tencentcloud.ame.v20190916.models.Lyric`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Lyric = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Lyric") is not None:
            self.Lyric = Lyric()
            self.Lyric._deserialize(params.get("Lyric"))
        self.RequestId = params.get("RequestId")


class DescribeMusicRequest(AbstractModel):
    """DescribeMusic请求参数结构体

    """

    def __init__(self):
        """
        :param ItemId: 歌曲ID\n        :type ItemId: str\n        :param IdentityId: 在应用前端播放音乐C端用户的唯一标识。无需是账户信息，用户唯一标识即可。\n        :type IdentityId: str\n        :param SubItemType: MP3-320K-FTD-P  为获取320kbps歌曲热门片段。
MP3-320K-FTD 为获取320kbps已核验歌曲完整资源。\n        :type SubItemType: str\n        :param Ssl: CDN URL Protocol:HTTP or HTTPS/SSL
Values:Y , N(default)\n        :type Ssl: str\n        """
        self.ItemId = None
        self.IdentityId = None
        self.SubItemType = None
        self.Ssl = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.IdentityId = params.get("IdentityId")
        self.SubItemType = params.get("SubItemType")
        self.Ssl = params.get("Ssl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMusicResponse(AbstractModel):
    """DescribeMusic返回参数结构体

    """

    def __init__(self):
        """
        :param Music: 音乐相关信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Music: :class:`tencentcloud.ame.v20190916.models.Music`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Music = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Music") is not None:
            self.Music = Music()
            self.Music._deserialize(params.get("Music"))
        self.RequestId = params.get("RequestId")


class DescribePackageItemsRequest(AbstractModel):
    """DescribePackageItems请求参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 订单id，从获取已购曲库包列表中获取\n        :type OrderId: str\n        :param Offset: 默认0，Offset=Offset+Length\n        :type Offset: int\n        :param Length: 默认20\n        :type Length: int\n        """
        self.OrderId = None
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackageItemsResponse(AbstractModel):
    """DescribePackageItems返回参数结构体

    """

    def __init__(self):
        """
        :param PackageItems: 已核销歌曲信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageItems: list of PackageItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PackageItems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PackageItems") is not None:
            self.PackageItems = []
            for item in params.get("PackageItems"):
                obj = PackageItem()
                obj._deserialize(item)
                self.PackageItems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePackagesRequest(AbstractModel):
    """DescribePackages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 默认0，Offset=Offset+Length\n        :type Offset: int\n        :param Length: 默认20\n        :type Length: int\n        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackagesResponse(AbstractModel):
    """DescribePackages返回参数结构体

    """

    def __init__(self):
        """
        :param Packages: 已购曲库包列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Packages: list of Package\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Packages = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Packages") is not None:
            self.Packages = []
            for item in params.get("Packages"):
                obj = Package()
                obj._deserialize(item)
                self.Packages.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStationsRequest(AbstractModel):
    """DescribeStations请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 条数，必须大于0\n        :type Limit: int\n        :param Offset: offset (Default = 0)，Offset=Offset+Limit\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStationsResponse(AbstractModel):
    """DescribeStations返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 总数量\n        :type Total: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        :param Size: 当前页station数量\n        :type Size: int\n        :param HaveMore: 剩余数量（total-offset-size），通过这个值判断是否还有下一页\n        :type HaveMore: int\n        :param Stations: Stations 素材库列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Stations: list of Station\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Total = None
        self.Offset = None
        self.Size = None
        self.HaveMore = None
        self.Stations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        self.HaveMore = params.get("HaveMore")
        if params.get("Stations") is not None:
            self.Stations = []
            for item in params.get("Stations"):
                obj = Station()
                obj._deserialize(item)
                self.Stations.append(obj)
        self.RequestId = params.get("RequestId")


class ImagePath(AbstractModel):
    """图片路径

    """

    def __init__(self):
        """
        :param Key: station图片大小及类别
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: station图片地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Item(AbstractModel):
    """歌曲信息

    """

    def __init__(self):
        """
        :param ItemID: Song ID\n        :type ItemID: str\n        :param DataInfo: Song info
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataInfo: :class:`tencentcloud.ame.v20190916.models.DataInfo`\n        :param Album: 专辑信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Album: :class:`tencentcloud.ame.v20190916.models.Album`\n        :param Artists: 多个歌手集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type Artists: list of Artist\n        :param Status: 歌曲状态，1:添加进购物车；2:核销进曲库包
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        """
        self.ItemID = None
        self.DataInfo = None
        self.Album = None
        self.Artists = None
        self.Status = None


    def _deserialize(self, params):
        self.ItemID = params.get("ItemID")
        if params.get("DataInfo") is not None:
            self.DataInfo = DataInfo()
            self.DataInfo._deserialize(params.get("DataInfo"))
        if params.get("Album") is not None:
            self.Album = Album()
            self.Album._deserialize(params.get("Album"))
        if params.get("Artists") is not None:
            self.Artists = []
            for item in params.get("Artists"):
                obj = Artist()
                obj._deserialize(item)
                self.Artists.append(obj)
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KTVMusicBaseInfo(AbstractModel):
    """KTV 曲目基础信息

    """

    def __init__(self):
        """
        :param MusicId: 歌曲 Id\n        :type MusicId: str\n        :param Name: 歌曲名称\n        :type Name: str\n        :param SingerSet: 演唱者列表\n        :type SingerSet: list of str\n        :param LyricistSet: 作词者列表\n        :type LyricistSet: list of str\n        :param ComposerSet: 作曲者列表\n        :type ComposerSet: list of str\n        :param TagSet: 标签列表\n        :type TagSet: list of str\n        :param Duration: 歌曲时长\n        :type Duration: int\n        """
        self.MusicId = None
        self.Name = None
        self.SingerSet = None
        self.LyricistSet = None
        self.ComposerSet = None
        self.TagSet = None
        self.Duration = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.Name = params.get("Name")
        self.SingerSet = params.get("SingerSet")
        self.LyricistSet = params.get("LyricistSet")
        self.ComposerSet = params.get("ComposerSet")
        self.TagSet = params.get("TagSet")
        self.Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Lyric(AbstractModel):
    """歌词信息

    """

    def __init__(self):
        """
        :param Url: 歌词cdn地址\n        :type Url: str\n        :param FileNameExt: 歌词后缀名\n        :type FileNameExt: str\n        :param SubItemType: 歌词类型\n        :type SubItemType: str\n        """
        self.Url = None
        self.FileNameExt = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileNameExt = params.get("FileNameExt")
        self.SubItemType = params.get("SubItemType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMusicOnShelvesRequest(AbstractModel):
    """ModifyMusicOnShelves请求参数结构体

    """

    def __init__(self):
        """
        :param MusicDetailInfos: 歌曲变更信息\n        :type MusicDetailInfos: :class:`tencentcloud.ame.v20190916.models.MusicDetailInfo`\n        :param AmeKey: ame对接资源方密钥\n        :type AmeKey: str\n        """
        self.MusicDetailInfos = None
        self.AmeKey = None


    def _deserialize(self, params):
        if params.get("MusicDetailInfos") is not None:
            self.MusicDetailInfos = MusicDetailInfo()
            self.MusicDetailInfos._deserialize(params.get("MusicDetailInfos"))
        self.AmeKey = params.get("AmeKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMusicOnShelvesResponse(AbstractModel):
    """ModifyMusicOnShelves返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Music(AbstractModel):
    """音乐详情

    """

    def __init__(self):
        """
        :param Url: 音乐播放链接相对路径，必须通过在正版曲库直通车控制台上登记的域名进行拼接。\n        :type Url: str\n        :param FileSize: 音频文件大小\n        :type FileSize: int\n        :param FileExtension: 音频文件类型\n        :type FileExtension: str\n        :param AuditionBegin: Song fragment start.试听片段开始时间，试听时长为auditionEnd-auditionBegin
Unit :ms\n        :type AuditionBegin: int\n        :param AuditionEnd: Song fragment end.试听片段结束时间, 试听时长为auditionEnd-auditionBegin
Unit :ms\n        :type AuditionEnd: int\n        :param FullUrl: 音乐播放链接全路径，前提是在正版曲库直通车控制台添加过域名，否则返回空字符。
如果添加过多个域名只返回第一个添加域名的播放全路径。\n        :type FullUrl: str\n        """
        self.Url = None
        self.FileSize = None
        self.FileExtension = None
        self.AuditionBegin = None
        self.AuditionEnd = None
        self.FullUrl = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileSize = params.get("FileSize")
        self.FileExtension = params.get("FileExtension")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")
        self.FullUrl = params.get("FullUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicDetailInfo(AbstractModel):
    """歌曲变更细节

    """

    def __init__(self):
        """
        :param MusicId: 资源方音乐Id\n        :type MusicId: str\n        :param AmeId: 资源方识别信息\n        :type AmeId: str\n        :param Tags: 分类标签\n        :type Tags: list of str\n        :param HitWords: 关键词\n        :type HitWords: list of str\n        :param Bpm: 节奏信息\n        :type Bpm: int\n        :param Score: 商业化权益\n        :type Score: float\n        :param Scene: 应用歌曲信息,1.图文/短视频,2.网络直播,3.网络电台FM,4.免费游戏,5.商业游戏,6.网店网站设计,7.广告营销,8.网络长视频\n        :type Scene: list of str\n        :param Region: 应用地域,1. 中国大陆,2. 中国含港澳台,3. 全球\n        :type Region: list of str\n        :param AuthPeriod: 授权时间,1. 1年, 5. 随片永久\n        :type AuthPeriod: str\n        :param Commercialization: 商业化授权，1. 支持商业化 ,2. 不支持商业化\n        :type Commercialization: str\n        :param Platform: 跨平台传播，1. 支持跨平台传播 ,2. 不支持跨平台传播\n        :type Platform: str\n        :param Channel: 传播渠道\n        :type Channel: str\n        """
        self.MusicId = None
        self.AmeId = None
        self.Tags = None
        self.HitWords = None
        self.Bpm = None
        self.Score = None
        self.Scene = None
        self.Region = None
        self.AuthPeriod = None
        self.Commercialization = None
        self.Platform = None
        self.Channel = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.AmeId = params.get("AmeId")
        self.Tags = params.get("Tags")
        self.HitWords = params.get("HitWords")
        self.Bpm = params.get("Bpm")
        self.Score = params.get("Score")
        self.Scene = params.get("Scene")
        self.Region = params.get("Region")
        self.AuthPeriod = params.get("AuthPeriod")
        self.Commercialization = params.get("Commercialization")
        self.Platform = params.get("Platform")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MusicOpenDetail(AbstractModel):
    """对外开放信息

    """

    def __init__(self):
        """
        :param MusicId: 音乐Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type MusicId: str\n        :param AlbumName: 专辑名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlbumName: str\n        :param AlbumImageUrl: 专辑图片路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlbumImageUrl: str\n        :param MusicName: 音乐名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type MusicName: str\n        :param MusicImageUrl: 音乐图片路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type MusicImageUrl: str\n        :param Singers: 歌手
注意：此字段可能返回 null，表示取不到有效值。\n        :type Singers: list of str\n        :param Duration: 播放时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type Duration: int\n        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of str\n        :param LyricUrl: 歌词url
注意：此字段可能返回 null，表示取不到有效值。\n        :type LyricUrl: str\n        """
        self.MusicId = None
        self.AlbumName = None
        self.AlbumImageUrl = None
        self.MusicName = None
        self.MusicImageUrl = None
        self.Singers = None
        self.Duration = None
        self.Tags = None
        self.LyricUrl = None


    def _deserialize(self, params):
        self.MusicId = params.get("MusicId")
        self.AlbumName = params.get("AlbumName")
        self.AlbumImageUrl = params.get("AlbumImageUrl")
        self.MusicName = params.get("MusicName")
        self.MusicImageUrl = params.get("MusicImageUrl")
        self.Singers = params.get("Singers")
        self.Duration = params.get("Duration")
        self.Tags = params.get("Tags")
        self.LyricUrl = params.get("LyricUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Package(AbstractModel):
    """曲库包信息

    """

    def __init__(self):
        """
        :param OrderId: 订单id\n        :type OrderId: str\n        :param Name: 曲库包名称\n        :type Name: str\n        :param AuthorizedArea: 授权地区-global: 全球  CN: 中国\n        :type AuthorizedArea: str\n        :param AuthorizedLimit: 授权次数\n        :type AuthorizedLimit: int\n        :param TermOfValidity: 套餐有效期，单位:天\n        :type TermOfValidity: int\n        :param Commercial: 0:不可商业化；1:可商业化\n        :type Commercial: int\n        :param PackagePrice: 套餐价格，单位：元\n        :type PackagePrice: float\n        :param EffectTime: 生效开始时间,格式yyyy-MM-dd HH:mm:ss\n        :type EffectTime: str\n        :param ExpireTime: 生效结束时间,格式yyyy-MM-dd HH:mm:ss\n        :type ExpireTime: str\n        :param UsedCount: 剩余授权次数\n        :type UsedCount: int\n        :param UseRanges: 曲库包用途信息\n        :type UseRanges: list of UseRange\n        """
        self.OrderId = None
        self.Name = None
        self.AuthorizedArea = None
        self.AuthorizedLimit = None
        self.TermOfValidity = None
        self.Commercial = None
        self.PackagePrice = None
        self.EffectTime = None
        self.ExpireTime = None
        self.UsedCount = None
        self.UseRanges = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Name = params.get("Name")
        self.AuthorizedArea = params.get("AuthorizedArea")
        self.AuthorizedLimit = params.get("AuthorizedLimit")
        self.TermOfValidity = params.get("TermOfValidity")
        self.Commercial = params.get("Commercial")
        self.PackagePrice = params.get("PackagePrice")
        self.EffectTime = params.get("EffectTime")
        self.ExpireTime = params.get("ExpireTime")
        self.UsedCount = params.get("UsedCount")
        if params.get("UseRanges") is not None:
            self.UseRanges = []
            for item in params.get("UseRanges"):
                obj = UseRange()
                obj._deserialize(item)
                self.UseRanges.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageItem(AbstractModel):
    """曲库包歌曲信息

    """

    def __init__(self):
        """
        :param OrderId: 订单id\n        :type OrderId: str\n        :param TrackName: 歌曲名\n        :type TrackName: str\n        :param ItemID: 歌曲ID\n        :type ItemID: str\n        :param Img: 专辑图片\n        :type Img: str\n        :param ArtistName: 歌手名\n        :type ArtistName: str\n        :param Duration: 歌曲时长\n        :type Duration: str\n        :param AuthorizedArea: 授权区域，global: 全球 CN: 中国\n        :type AuthorizedArea: str\n        """
        self.OrderId = None
        self.TrackName = None
        self.ItemID = None
        self.Img = None
        self.ArtistName = None
        self.Duration = None
        self.AuthorizedArea = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.TrackName = params.get("TrackName")
        self.ItemID = params.get("ItemID")
        self.Img = params.get("Img")
        self.ArtistName = params.get("ArtistName")
        self.Duration = params.get("Duration")
        self.AuthorizedArea = params.get("AuthorizedArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMusicOnTheShelvesRequest(AbstractModel):
    """PutMusicOnTheShelves请求参数结构体

    """

    def __init__(self):
        """
        :param MusicIds: 资源方歌曲Id\n        :type MusicIds: list of str\n        """
        self.MusicIds = None


    def _deserialize(self, params):
        self.MusicIds = params.get("MusicIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutMusicOnTheShelvesResponse(AbstractModel):
    """PutMusicOnTheShelves返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessNum: 操作成功数量\n        :type SuccessNum: int\n        :param FailedNum: 操作失败数量\n        :type FailedNum: int\n        :param FailedMusicIds: 失败歌曲Id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedMusicIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessNum = None
        self.FailedNum = None
        self.FailedMusicIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessNum = params.get("SuccessNum")
        self.FailedNum = params.get("FailedNum")
        self.FailedMusicIds = params.get("FailedMusicIds")
        self.RequestId = params.get("RequestId")


class ReportDataRequest(AbstractModel):
    """ReportData请求参数结构体

    """

    def __init__(self):
        """
        :param ReportData: 上报数据
注:reportData为客户端压缩后的上报数据进行16进制转换的字符串数据
压缩说明：
a) 上报的json格式字符串通过流的转换（ByteArrayInputStream, java.util.zip.GZIPOutputStream），获取到压缩后的字节数组。
b) 将压缩后的字节数组转成16进制字符串。

reportData由两部分数据组成：
1）report_type（上报类型）
2）data（歌曲上报数据）
不同的report_type对应的data数据结构不一样。

详细说明请参考文档reportdata.docx：
https://github.com/tencentyun/ame-documents\n        :type ReportData: str\n        """
        self.ReportData = None


    def _deserialize(self, params):
        self.ReportData = params.get("ReportData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportDataResponse(AbstractModel):
    """ReportData返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchKTVMusicsRequest(AbstractModel):
    """SearchKTVMusics请求参数结构体

    """

    def __init__(self):
        """
        :param KeyWord: 搜索关键词\n        :type KeyWord: str\n        :param Offset: 分页游标\n        :type Offset: int\n        :param Limit: 分页页长\n        :type Limit: int\n        """
        self.KeyWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.KeyWord = params.get("KeyWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchKTVMusicsResponse(AbstractModel):
    """SearchKTVMusics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总记录数\n        :type TotalCount: int\n        :param KTVMusicInfoSet: KTV 曲目列表\n        :type KTVMusicInfoSet: list of KTVMusicBaseInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.KTVMusicInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KTVMusicInfoSet") is not None:
            self.KTVMusicInfoSet = []
            for item in params.get("KTVMusicInfoSet"):
                obj = KTVMusicBaseInfo()
                obj._deserialize(item)
                self.KTVMusicInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class Station(AbstractModel):
    """分类内容

    """

    def __init__(self):
        """
        :param CategoryID: StationID\n        :type CategoryID: str\n        :param CategoryCode: Station MCCode
注意：此字段可能返回 null，表示取不到有效值。\n        :type CategoryCode: str\n        :param Name: Category Name
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Rank: Station的排序值，供参考（返回结果已按其升序）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rank: int\n        :param ImagePathMap: station图片集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImagePathMap: list of ImagePath\n        """
        self.CategoryID = None
        self.CategoryCode = None
        self.Name = None
        self.Rank = None
        self.ImagePathMap = None


    def _deserialize(self, params):
        self.CategoryID = params.get("CategoryID")
        self.CategoryCode = params.get("CategoryCode")
        self.Name = params.get("Name")
        self.Rank = params.get("Rank")
        if params.get("ImagePathMap") is not None:
            self.ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self.ImagePathMap.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelves(AbstractModel):
    """下架歌曲复合结构

    """

    def __init__(self):
        """
        :param MusicIds: 资源方对应音乐Id\n        :type MusicIds: str\n        :param SaleStatus: 当曲目临时下架时：已订购客户无影响，无需消息通知。当曲目封杀下架后，推送消息至已订购老客户，枚举值，判断是否上/下架
在售状态，0在售，1临时下架，2永久下架\n        :type SaleStatus: str\n        """
        self.MusicIds = None
        self.SaleStatus = None


    def _deserialize(self, params):
        self.MusicIds = params.get("MusicIds")
        self.SaleStatus = params.get("SaleStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelvesRequest(AbstractModel):
    """TakeMusicOffShelves请求参数结构体

    """

    def __init__(self):
        """
        :param TakeMusicOffShelves: 资源方下架必传结构\n        :type TakeMusicOffShelves: list of TakeMusicOffShelves\n        """
        self.TakeMusicOffShelves = None


    def _deserialize(self, params):
        if params.get("TakeMusicOffShelves") is not None:
            self.TakeMusicOffShelves = []
            for item in params.get("TakeMusicOffShelves"):
                obj = TakeMusicOffShelves()
                obj._deserialize(item)
                self.TakeMusicOffShelves.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TakeMusicOffShelvesResponse(AbstractModel):
    """TakeMusicOffShelves返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessNum: 返回成功数量\n        :type SuccessNum: int\n        :param FailedNum: 返回失败数量\n        :type FailedNum: int\n        :param FailedMusicIds: 返回失败歌曲musicId
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedMusicIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessNum = None
        self.FailedNum = None
        self.FailedMusicIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessNum = params.get("SuccessNum")
        self.FailedNum = params.get("FailedNum")
        self.FailedMusicIds = params.get("FailedMusicIds")
        self.RequestId = params.get("RequestId")


class UseRange(AbstractModel):
    """曲库包用途信息

    """

    def __init__(self):
        """
        :param UseRangeId: 用途id\n        :type UseRangeId: int\n        :param Name: 用途范围名称\n        :type Name: str\n        """
        self.UseRangeId = None
        self.Name = None


    def _deserialize(self, params):
        self.UseRangeId = params.get("UseRangeId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        