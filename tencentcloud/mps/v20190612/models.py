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


class AIAnalysisTemplateItem(AbstractModel):
    """AI 智能分析模板详情

    """

    def __init__(self):
        """
        :param Definition: 智能分析模板唯一标识。\n        :type Definition: int\n        :param Name: 智能分析模板名称。\n        :type Name: str\n        :param Comment: 智能分析模板描述信息。\n        :type Comment: str\n        :param ClassificationConfigure: 智能分类任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfo`\n        :param TagConfigure: 智能标签任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfo`\n        :param CoverConfigure: 智能封面任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfo`\n        :param FrameTagConfigure: 智能按帧标签任务控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfo`\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIRecognitionTemplateItem(AbstractModel):
    """视频内容识别模板详情

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。\n        :type Definition: int\n        :param Name: 视频内容识别模板名称。\n        :type Name: str\n        :param Comment: 视频内容识别模板描述信息。\n        :type Comment: str\n        :param FaceConfigure: 人脸识别控制参数。\n        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfo`\n        :param OcrFullTextConfigure: 文本全文识别控制参数。\n        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfo`\n        :param OcrWordsConfigure: 文本关键词识别控制参数。\n        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfo`\n        :param AsrFullTextConfigure: 语音全文识别控制参数。\n        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfo`\n        :param AsrWordsConfigure: 语音关键词识别控制参数。\n        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfo`\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActionConfigInfo(AbstractModel):
    """动作识别参数配置

    """

    def __init__(self):
        """
        :param Switch: 动作识别任务开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingInfoItem(AbstractModel):
    """转自适应码流信息

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流规格。\n        :type Definition: int\n        :param Package: 打包格式，可能为 HLS和 MPEG-DASH 两种。\n        :type Package: str\n        :param Path: 播放路径。\n        :type Path: str\n        :param Storage: 自适应码流文件的存储位置。\n        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        """
        self.Definition = None
        self.Package = None
        self.Path = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Package = params.get("Package")
        self.Path = params.get("Path")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTaskInput(AbstractModel):
    """对视频转自适应码流的输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流模板 ID。\n        :type Definition: int\n        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。\n        :type WatermarkSet: list of WatermarkInput\n        :param OutputStorage: 转自适应码流后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 转自适应码流后，manifest 文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}.{format}`。\n        :type OutputObjectPath: str\n        :param SubStreamObjectName: 转自适应码流后，子流文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}.{format}`。\n        :type SubStreamObjectName: str\n        :param SegmentObjectName: 转自适应码流（仅 HLS）后，分片文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_adaptiveDynamicStreaming_{definition}_{subStreamNumber}_{segmentNumber}.{format}`。\n        :type SegmentObjectName: str\n        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SubStreamObjectName = None
        self.SegmentObjectName = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SubStreamObjectName = params.get("SubStreamObjectName")
        self.SegmentObjectName = params.get("SegmentObjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveDynamicStreamingTemplate(AbstractModel):
    """转自适应码流模板详情

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流模板唯一标识。\n        :type Definition: int\n        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param Name: 转自适应码流模板名称。\n        :type Name: str\n        :param Comment: 转自适应码流模板描述信息。\n        :type Comment: str\n        :param Format: 转自适应码流格式，取值范围：
<li>HLS，</li>
<li>MPEG-DASH。</li>\n        :type Format: str\n        :param StreamInfos: 转自适应码流输入流参数信息，最多输入10路流。\n        :type StreamInfos: list of AdaptiveStreamTemplate\n        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>\n        :type DisableHigherVideoBitrate: int\n        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>\n        :type DisableHigherVideoResolution: int\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/266/11732#I)。\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Format = None
        self.StreamInfos = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdaptiveStreamTemplate(AbstractModel):
    """自适应转码流参数模板

    """

    def __init__(self):
        """
        :param Video: 视频参数信息。\n        :type Video: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`\n        :param Audio: 音频参数信息。\n        :type Audio: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`\n        :param RemoveAudio: 是否移除音频流，取值范围：
<li>0：否，</li>
<li>1：是。</li>\n        :type RemoveAudio: int\n        :param RemoveVideo: 是否移除视频流，取值范围：
<li>0：否，</li>
<li>1：是。</li>\n        :type RemoveVideo: int\n        """
        self.Video = None
        self.Audio = None
        self.RemoveAudio = None
        self.RemoveVideo = None


    def _deserialize(self, params):
        if params.get("Video") is not None:
            self.Video = VideoTemplateInfo()
            self.Video._deserialize(params.get("Video"))
        if params.get("Audio") is not None:
            self.Audio = AudioTemplateInfo()
            self.Audio._deserialize(params.get("Audio"))
        self.RemoveAudio = params.get("RemoveAudio")
        self.RemoveVideo = params.get("RemoveVideo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisResult(AbstractModel):
    """智能分析结果

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Classification：智能分类</li>
<li>Cover：智能封面</li>
<li>Tag：智能标签</li>
<li>FrameTag：智能按帧标签</li>
<li>Highlight：智能精彩集锦</li>\n        :type Type: str\n        :param ClassificationTask: 视频内容分析智能分类任务的查询结果，当任务类型为 Classification 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClassificationTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationResult`\n        :param CoverTask: 视频内容分析智能封面任务的查询结果，当任务类型为 Cover 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CoverTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverResult`\n        :param TagTask: 视频内容分析智能标签任务的查询结果，当任务类型为 Tag 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagResult`\n        :param FrameTagTask: 视频内容分析智能按帧标签任务的查询结果，当任务类型为 FrameTag 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrameTagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagResult`\n        """
        self.Type = None
        self.ClassificationTask = None
        self.CoverTask = None
        self.TagTask = None
        self.FrameTagTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ClassificationTask") is not None:
            self.ClassificationTask = AiAnalysisTaskClassificationResult()
            self.ClassificationTask._deserialize(params.get("ClassificationTask"))
        if params.get("CoverTask") is not None:
            self.CoverTask = AiAnalysisTaskCoverResult()
            self.CoverTask._deserialize(params.get("CoverTask"))
        if params.get("TagTask") is not None:
            self.TagTask = AiAnalysisTaskTagResult()
            self.TagTask._deserialize(params.get("TagTask"))
        if params.get("FrameTagTask") is not None:
            self.FrameTagTask = AiAnalysisTaskFrameTagResult()
            self.FrameTagTask._deserialize(params.get("FrameTagTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationInput(AbstractModel):
    """智能分类任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能分类模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationOutput(AbstractModel):
    """智能分类结果信息

    """

    def __init__(self):
        """
        :param ClassificationSet: 视频智能分类列表。\n        :type ClassificationSet: list of MediaAiAnalysisClassificationItem\n        """
        self.ClassificationSet = None


    def _deserialize(self, params):
        if params.get("ClassificationSet") is not None:
            self.ClassificationSet = []
            for item in params.get("ClassificationSet"):
                obj = MediaAiAnalysisClassificationItem()
                obj._deserialize(item)
                self.ClassificationSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskClassificationResult(AbstractModel):
    """智能分类任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 智能分类任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationInput`\n        :param Output: 智能分类任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskClassificationOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskClassificationInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskClassificationOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverInput(AbstractModel):
    """智能分类任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能封面模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverOutput(AbstractModel):
    """智能封面结果信息

    """

    def __init__(self):
        """
        :param CoverSet: 智能封面列表。\n        :type CoverSet: list of MediaAiAnalysisCoverItem\n        :param OutputStorage: 智能封面的存储位置。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        """
        self.CoverSet = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("CoverSet") is not None:
            self.CoverSet = []
            for item in params.get("CoverSet"):
                obj = MediaAiAnalysisCoverItem()
                obj._deserialize(item)
                self.CoverSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskCoverResult(AbstractModel):
    """智能封面结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 智能封面任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverInput`\n        :param Output: 智能封面任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskCoverInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskCoverOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagInput(AbstractModel):
    """智能按帧标签任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能按帧标签模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagOutput(AbstractModel):
    """智能按帧标签结果信息

    """

    def __init__(self):
        """
        :param SegmentSet: 视频按帧标签列表。\n        :type SegmentSet: list of MediaAiAnalysisFrameTagSegmentItem\n        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaAiAnalysisFrameTagSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskFrameTagResult(AbstractModel):
    """智能按帧标签结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 智能按帧标签任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagInput`\n        :param Output: 智能按帧标签任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskFrameTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskFrameTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskInput(AbstractModel):
    """AI 视频智能分析输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagInput(AbstractModel):
    """智能标签任务输入类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能标签模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagOutput(AbstractModel):
    """智能标签结果信息

    """

    def __init__(self):
        """
        :param TagSet: 视频智能标签列表。\n        :type TagSet: list of MediaAiAnalysisTagItem\n        """
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiAnalysisTaskTagResult(AbstractModel):
    """智能标签结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 智能标签任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagInput`\n        :param Output: 智能标签任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiAnalysisTaskTagInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiAnalysisTaskTagOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewResult(AbstractModel):
    """内容审核结果

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Porn：图片鉴黄</li>
<li>Terrorism：图片鉴恐</li>
<li>Political：图片鉴政</li>
<li>Porn.Asr：Asr 文字鉴黄</li>
<li>Porn.Ocr：Ocr 文字鉴黄</li>
<li>Political.Asr：Asr 文字鉴政</li>
<li>Political.Ocr：Ocr 文字鉴政</li>
<li>Terrorism.Ocr：Ocr 文字鉴恐</li>
<li>Prohibited.Asr：Asr 文字鉴违禁</li>
<li>Prohibited.Ocr：Ocr 文字鉴违禁</li>\n        :type Type: str\n        :param SampleRate: 采样频率，即对视频每秒截取进行审核的帧数。\n        :type SampleRate: float\n        :param Duration: 审核的视频时长，单位：秒。\n        :type Duration: float\n        :param PornTask: 视频内容审核智能画面鉴黄任务的查询结果，当任务类型为 Porn 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PornTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornResult`\n        :param TerrorismTask: 视频内容审核智能画面鉴恐任务的查询结果，当任务类型为 Terrorism 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerrorismTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskTerrorismResult`\n        :param PoliticalTask: 视频内容审核智能画面鉴政任务的查询结果，当任务类型为 Political 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PoliticalTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalResult`\n        :param PornAsrTask: 视频内容审核 Asr 文字鉴黄任务的查询结果，当任务类型为 Porn.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PornAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornAsrResult`\n        :param PornOcrTask: 视频内容审核 Ocr 文字鉴黄任务的查询结果，当任务类型为 Porn.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PornOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPornOcrResult`\n        :param PoliticalAsrTask: 视频内容审核 Asr 文字鉴政任务的查询结果，当任务类型为 Political.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PoliticalAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalAsrResult`\n        :param PoliticalOcrTask: 视频内容审核 Ocr 文字鉴政任务的查询结果，当任务类型为 Political.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PoliticalOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskPoliticalOcrResult`\n        :param TerrorismOcrTask: 视频内容审核 Ocr 文字鉴恐任务的查询结果，当任务类型为 Terrorism.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerrorismOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskTerrorismOcrResult`\n        :param ProhibitedAsrTask: 视频内容审核 Asr 文字鉴违禁任务的查询结果，当任务类型为 Prohibited.Asr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProhibitedAsrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskProhibitedAsrResult`\n        :param ProhibitedOcrTask: 视频内容审核 Ocr 文字鉴违禁任务的查询结果，当任务类型为 Prohibited.Ocr 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProhibitedOcrTask: :class:`tencentcloud.mps.v20190612.models.AiReviewTaskProhibitedOcrResult`\n        """
        self.Type = None
        self.SampleRate = None
        self.Duration = None
        self.PornTask = None
        self.TerrorismTask = None
        self.PoliticalTask = None
        self.PornAsrTask = None
        self.PornOcrTask = None
        self.PoliticalAsrTask = None
        self.PoliticalOcrTask = None
        self.TerrorismOcrTask = None
        self.ProhibitedAsrTask = None
        self.ProhibitedOcrTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SampleRate = params.get("SampleRate")
        self.Duration = params.get("Duration")
        if params.get("PornTask") is not None:
            self.PornTask = AiReviewTaskPornResult()
            self.PornTask._deserialize(params.get("PornTask"))
        if params.get("TerrorismTask") is not None:
            self.TerrorismTask = AiReviewTaskTerrorismResult()
            self.TerrorismTask._deserialize(params.get("TerrorismTask"))
        if params.get("PoliticalTask") is not None:
            self.PoliticalTask = AiReviewTaskPoliticalResult()
            self.PoliticalTask._deserialize(params.get("PoliticalTask"))
        if params.get("PornAsrTask") is not None:
            self.PornAsrTask = AiReviewTaskPornAsrResult()
            self.PornAsrTask._deserialize(params.get("PornAsrTask"))
        if params.get("PornOcrTask") is not None:
            self.PornOcrTask = AiReviewTaskPornOcrResult()
            self.PornOcrTask._deserialize(params.get("PornOcrTask"))
        if params.get("PoliticalAsrTask") is not None:
            self.PoliticalAsrTask = AiReviewTaskPoliticalAsrResult()
            self.PoliticalAsrTask._deserialize(params.get("PoliticalAsrTask"))
        if params.get("PoliticalOcrTask") is not None:
            self.PoliticalOcrTask = AiReviewTaskPoliticalOcrResult()
            self.PoliticalOcrTask._deserialize(params.get("PoliticalOcrTask"))
        if params.get("TerrorismOcrTask") is not None:
            self.TerrorismOcrTask = AiReviewTaskTerrorismOcrResult()
            self.TerrorismOcrTask._deserialize(params.get("TerrorismOcrTask"))
        if params.get("ProhibitedAsrTask") is not None:
            self.ProhibitedAsrTask = AiReviewTaskProhibitedAsrResult()
            self.ProhibitedAsrTask._deserialize(params.get("ProhibitedAsrTask"))
        if params.get("ProhibitedOcrTask") is not None:
            self.ProhibitedOcrTask = AiReviewTaskProhibitedOcrResult()
            self.ProhibitedOcrTask._deserialize(params.get("ProhibitedOcrTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiContentReviewTaskInput(AbstractModel):
    """智能内容审核任务类型

    """

    def __init__(self):
        """
        :param Definition: 视频内容审核模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionResult(AbstractModel):
    """智能识别结果。

    """

    def __init__(self):
        """
        :param Type: 任务的类型，取值范围：
<li>FaceRecognition：人脸识别，</li>
<li>AsrWordsRecognition：语音关键词识别，</li>
<li>OcrWordsRecognition：文本关键词识别，</li>
<li>AsrFullTextRecognition：语音全文识别，</li>
<li>OcrFullTextRecognition：文本全文识别。</li>\n        :type Type: str\n        :param FaceTask: 人脸识别结果，当 Type 为 
 FaceRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FaceTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResult`\n        :param AsrWordsTask: 语音关键词识别结果，当 Type 为
 AsrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AsrWordsTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResult`\n        :param AsrFullTextTask: 语音全文识别结果，当 Type 为
 AsrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AsrFullTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResult`\n        :param OcrWordsTask: 文本关键词识别结果，当 Type 为
 OcrWordsRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OcrWordsTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResult`\n        :param OcrFullTextTask: 文本全文识别结果，当 Type 为
 OcrFullTextRecognition 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OcrFullTextTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResult`\n        """
        self.Type = None
        self.FaceTask = None
        self.AsrWordsTask = None
        self.AsrFullTextTask = None
        self.OcrWordsTask = None
        self.OcrFullTextTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceTask") is not None:
            self.FaceTask = AiRecognitionTaskFaceResult()
            self.FaceTask._deserialize(params.get("FaceTask"))
        if params.get("AsrWordsTask") is not None:
            self.AsrWordsTask = AiRecognitionTaskAsrWordsResult()
            self.AsrWordsTask._deserialize(params.get("AsrWordsTask"))
        if params.get("AsrFullTextTask") is not None:
            self.AsrFullTextTask = AiRecognitionTaskAsrFullTextResult()
            self.AsrFullTextTask._deserialize(params.get("AsrFullTextTask"))
        if params.get("OcrWordsTask") is not None:
            self.OcrWordsTask = AiRecognitionTaskOcrWordsResult()
            self.OcrWordsTask._deserialize(params.get("OcrWordsTask"))
        if params.get("OcrFullTextTask") is not None:
            self.OcrFullTextTask = AiRecognitionTaskOcrFullTextResult()
            self.OcrFullTextTask._deserialize(params.get("OcrFullTextTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResult(AbstractModel):
    """语音全文识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 语音全文识别任务输入信息。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultInput`\n        :param Output: 语音全文识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrFullTextResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultInput(AbstractModel):
    """语音全文识别的输入。

    """

    def __init__(self):
        """
        :param Definition: 语音全文识别模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextResultOutput(AbstractModel):
    """语音全文识别结果。

    """

    def __init__(self):
        """
        :param SegmentSet: 语音全文识别片段列表。\n        :type SegmentSet: list of AiRecognitionTaskAsrFullTextSegmentItem\n        :param SubtitlePath: 字幕文件地址。\n        :type SubtitlePath: str\n        :param OutputStorage: 字幕文件存储位置。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        """
        self.SegmentSet = None
        self.SubtitlePath = None
        self.OutputStorage = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        self.SubtitlePath = params.get("SubtitlePath")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrFullTextSegmentItem(AbstractModel):
    """语音全文识别片段。

    """

    def __init__(self):
        """
        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Text: 识别文本。\n        :type Text: str\n        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResult(AbstractModel):
    """语音关键词识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 语音关键词识别任务输入信息。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultInput`\n        :param Output: 语音关键词识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskAsrWordsResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskAsrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskAsrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultInput(AbstractModel):
    """语音关键词识别输入。

    """

    def __init__(self):
        """
        :param Definition: 语音关键词识别模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultItem(AbstractModel):
    """语音关键词识别结果。

    """

    def __init__(self):
        """
        :param Word: 语音关键词。\n        :type Word: str\n        :param SegmentSet: 语音关键词出现的时间片段列表。\n        :type SegmentSet: list of AiRecognitionTaskAsrWordsSegmentItem\n        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskAsrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsResultOutput(AbstractModel):
    """语音关键词识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 语音关键词识别结果集。\n        :type ResultSet: list of AiRecognitionTaskAsrWordsResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskAsrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskAsrWordsSegmentItem(AbstractModel):
    """语音识别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResult(AbstractModel):
    """人脸识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 人脸识别任务输入信息。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResultInput`\n        :param Output: 人脸识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskFaceResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskFaceResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskFaceResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultInput(AbstractModel):
    """人脸识别输入。

    """

    def __init__(self):
        """
        :param Definition: 人脸识别模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultItem(AbstractModel):
    """人脸识别结果

    """

    def __init__(self):
        """
        :param Id: 人物唯一标识 ID。\n        :type Id: str\n        :param Type: 人物库类型，表示识别出的人物来自哪个人物库：
<li>Default：默认人物库；</li>
<li>UserDefine：用户自定义人物库。</li>\n        :type Type: str\n        :param Name: 人物名称。\n        :type Name: str\n        :param SegmentSet: 人物出现的片段结果集。\n        :type SegmentSet: list of AiRecognitionTaskFaceSegmentItem\n        """
        self.Id = None
        self.Type = None
        self.Name = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskFaceSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceResultOutput(AbstractModel):
    """智能人脸识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 智能人脸识别结果集。\n        :type ResultSet: list of AiRecognitionTaskFaceResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskFaceResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskFaceSegmentItem(AbstractModel):
    """人脸识别结果片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskInput(AbstractModel):
    """视频内容识别输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频智能识别模板 ID 。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResult(AbstractModel):
    """文本全文识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 文本全文识别任务输入信息。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultInput`\n        :param Output: 文本全文识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrFullTextResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrFullTextResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrFullTextResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultInput(AbstractModel):
    """文本全文识别输入。

    """

    def __init__(self):
        """
        :param Definition: 文本全文识别模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextResultOutput(AbstractModel):
    """文本全文识别输出。

    """

    def __init__(self):
        """
        :param SegmentSet: 文本全文识别结果集。\n        :type SegmentSet: list of AiRecognitionTaskOcrFullTextSegmentItem\n        """
        self.SegmentSet = None


    def _deserialize(self, params):
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentItem(AbstractModel):
    """文本全文识别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param TextSet: 识别片段结果集。\n        :type TextSet: list of AiRecognitionTaskOcrFullTextSegmentTextItem\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TextSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TextSet") is not None:
            self.TextSet = []
            for item in params.get("TextSet"):
                obj = AiRecognitionTaskOcrFullTextSegmentTextItem()
                obj._deserialize(item)
                self.TextSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrFullTextSegmentTextItem(AbstractModel):
    """文本全文识别片段。

    """

    def __init__(self):
        """
        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。\n        :type AreaCoordSet: list of int\n        :param Text: 识别文本。\n        :type Text: str\n        """
        self.Confidence = None
        self.AreaCoordSet = None
        self.Text = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResult(AbstractModel):
    """文本关键识别结果。

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 文本关键词识别任务输入信息。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultInput`\n        :param Output: 文本关键词识别任务输出信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskOcrWordsResultOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiRecognitionTaskOcrWordsResultInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiRecognitionTaskOcrWordsResultOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultInput(AbstractModel):
    """文本关键词识别输入。

    """

    def __init__(self):
        """
        :param Definition: 文本关键词识别模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultItem(AbstractModel):
    """文本关键词识别结果。

    """

    def __init__(self):
        """
        :param Word: 文本关键词。\n        :type Word: str\n        :param SegmentSet: 文本关键出现的片段列表。\n        :type SegmentSet: list of AiRecognitionTaskOcrWordsSegmentItem\n        """
        self.Word = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = AiRecognitionTaskOcrWordsSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsResultOutput(AbstractModel):
    """文本关键词识别输出。

    """

    def __init__(self):
        """
        :param ResultSet: 文本关键词识别结果集。\n        :type ResultSet: list of AiRecognitionTaskOcrWordsResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = AiRecognitionTaskOcrWordsResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiRecognitionTaskOcrWordsSegmentItem(AbstractModel):
    """文本识别片段。

    """

    def __init__(self):
        """
        :param StartTimeOffset: 识别片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 识别片段终止的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。\n        :type AreaCoordSet: list of int\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴政模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalAsrTaskOutput(AbstractModel):
    """Asr 文字涉政信息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉政、敏感评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Asr 文字涉政、敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Asr 文字有涉政、敏感嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴政任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴政模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalOcrTaskOutput(AbstractModel):
    """Ocr 文字涉政信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉政、敏感评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Ocr 文字涉政、敏感结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Ocr 文字有涉政、敏感嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskInput(AbstractModel):
    """内容审核鉴政任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴政模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPoliticalTaskOutput(AbstractModel):
    """涉政信息

    """

    def __init__(self):
        """
        :param Confidence: 视频涉政评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: 涉政结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param Label: 视频鉴政结果标签。内容审核模板[画面鉴政任务控制参数](https://cloud.tencent.com/document/api/862/37615#AiReviewPoliticalTaskOutput)里 LabelSet 参数与此参数取值范围的对应关系：
violation_photo：
<li>violation_photo：违规图标。</li>
其他（即 politician/entertainment/sport/entrepreneur/scholar/celebrity/military）：
<li>politician：政治人物。</li>\n        :type Label: str\n        :param SegmentSet: 有涉政嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewPoliticalSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewPoliticalSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴黄任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴黄模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornAsrTaskOutput(AbstractModel):
    """Asr 文字涉黄信息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉黄评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Asr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Asr 文字有涉黄嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴黄模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornOcrTaskOutput(AbstractModel):
    """Ocr 文字涉黄信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉黄评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Ocr 文字涉黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Ocr 文字有涉黄嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskInput(AbstractModel):
    """内容审核鉴黄任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴黄模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewPornTaskOutput(AbstractModel):
    """鉴黄结果信息

    """

    def __init__(self):
        """
        :param Confidence: 视频鉴黄评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: 鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param Label: 视频鉴黄结果标签，取值范围：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：亲密行为。</li>\n        :type Label: str\n        :param SegmentSet: 有涉黄嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskInput(AbstractModel):
    """内容审核 Asr 文字鉴违禁任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴违禁模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedAsrTaskOutput(AbstractModel):
    """Asr 文字涉违禁信息

    """

    def __init__(self):
        """
        :param Confidence: Asr 文字涉违禁评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Asr 文字涉违禁结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Asr 文字有涉违禁嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewAsrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewAsrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴违禁任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴违禁模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewProhibitedOcrTaskOutput(AbstractModel):
    """Ocr 文字涉违禁信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉违禁评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Ocr 文字涉违禁结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Ocr 文字有涉违禁嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Asr 文字鉴政任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskInput`\n        :param Output: 内容审核 Asr 文字鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalAsrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴政、敏感任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS，FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Ocr 文字鉴政任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskInput`\n        :param Output: 内容审核 Ocr 文字鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPoliticalResult(AbstractModel):
    """内容审核鉴政任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核鉴政任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalTaskInput`\n        :param Output: 内容审核鉴政任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPoliticalTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPoliticalTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPoliticalTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Asr 文字鉴黄任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornAsrTaskInput`\n        :param Output: 内容审核 Asr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornAsrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Ocr 文字鉴黄任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornOcrTaskInput`\n        :param Output: 内容审核 Ocr 文字鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskPornResult(AbstractModel):
    """内容审核鉴黄任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核鉴黄任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewPornTaskInput`\n        :param Output: 内容审核鉴黄任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewPornTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewPornTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewPornTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedAsrResult(AbstractModel):
    """内容审核 Asr 文字鉴任违禁务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Asr 文字鉴违禁任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskInput`\n        :param Output: 内容审核 Asr 文字鉴违禁任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedAsrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedAsrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedAsrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskProhibitedOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴任违禁务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Ocr 文字鉴违禁任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskInput`\n        :param Output: 内容审核 Ocr 文字鉴违禁任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewProhibitedOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewProhibitedOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewProhibitedOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismOcrResult(AbstractModel):
    """内容审核 Ocr 文字鉴恐任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核 Ocr 文字鉴恐任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskInput`\n        :param Output: 内容审核 Ocr 文字鉴恐任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismOcrTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismOcrTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismOcrTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTaskTerrorismResult(AbstractModel):
    """内容审核鉴恐任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 内容审核鉴恐任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismTaskInput`\n        :param Output: 内容审核鉴恐任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AiReviewTerrorismTaskOutput`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AiReviewTerrorismTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AiReviewTerrorismTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskInput(AbstractModel):
    """内容审核 Ocr 文字鉴恐任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴恐模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismOcrTaskOutput(AbstractModel):
    """Ocr 文字涉恐信息

    """

    def __init__(self):
        """
        :param Confidence: Ocr 文字涉恐评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: Ocr 文字涉恐结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param SegmentSet: Ocr 文字有涉恐嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewOcrTextSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewOcrTextSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskInput(AbstractModel):
    """内容审核鉴恐任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 鉴恐模板 ID。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiReviewTerrorismTaskOutput(AbstractModel):
    """暴恐信息

    """

    def __init__(self):
        """
        :param Confidence: 视频暴恐评分，分值为0到100。\n        :type Confidence: float\n        :param Suggestion: 暴恐结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param Label: 视频暴恐结果标签，取值范围：
<li>guns：武器枪支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部队。</li>
<li>bloody：血腥画面。</li>
<li>banners：暴恐旗帜。</li>
<li>militant：武装分子。</li>
<li>explosion：爆炸火灾。</li>
<li>terrorists：暴恐人物。</li>
<li>scenario：暴恐画面。</li>\n        :type Label: str\n        :param SegmentSet: 有暴恐嫌疑的视频片段列表。\n        :type SegmentSet: list of MediaContentReviewSegmentItem\n        """
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = MediaContentReviewSegmentItem()
                obj._deserialize(item)
                self.SegmentSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceInfo(AbstractModel):
    """AI 样本管理，人脸信息。

    """

    def __init__(self):
        """
        :param FaceId: 人脸图片 ID。\n        :type FaceId: str\n        :param Url: 人脸图片地址。\n        :type Url: str\n        """
        self.FaceId = None
        self.Url = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFaceOperation(AbstractModel):
    """AI 样本管理，人脸数据操作。

    """

    def __init__(self):
        """
        :param Type: 操作类型，可选值：add（添加）、delete（删除）、reset（重置）。重置操作将清空该人物已有人脸数据，并添加 FaceContents 指定人脸数据。\n        :type Type: str\n        :param FaceIds: 人脸 ID 集合，当 Type为delete 时，该字段必填。\n        :type FaceIds: list of str\n        :param FaceContents: 人脸图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串集合。
<li>当 Type为add 或 reset 时，该字段必填；</li>
<li>数组长度限制：5 张图片。</li>
注意：图片必须是单人像正面人脸较清晰的照片，像素不低于 200*200。\n        :type FaceContents: list of str\n        """
        self.Type = None
        self.FaceIds = None
        self.FaceContents = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.FaceIds = params.get("FaceIds")
        self.FaceContents = params.get("FaceContents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleFailFaceInfo(AbstractModel):
    """AI 样本管理，处理失败的人脸信息

    """

    def __init__(self):
        """
        :param Index: 对应入参 FaceContents 中错误图片下标，从 0 开始。\n        :type Index: int\n        :param ErrCode: 错误码，取值：
<li>0：成功；</li>
<li>其他：失败。</li>\n        :type ErrCode: int\n        :param Message: 错误描述。\n        :type Message: str\n        """
        self.Index = None
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.Index = params.get("Index")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSamplePerson(AbstractModel):
    """AI 样本管理，人物信息。

    """

    def __init__(self):
        """
        :param PersonId: 人物 ID。\n        :type PersonId: str\n        :param Name: 人物名称。\n        :type Name: str\n        :param Description: 人物描述。\n        :type Description: str\n        :param FaceInfoSet: 人脸信息。\n        :type FaceInfoSet: list of AiSampleFaceInfo\n        :param TagSet: 人物标签。\n        :type TagSet: list of str\n        :param UsageSet: 应用场景。\n        :type UsageSet: list of str\n        :param CreateTime: 创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.FaceInfoSet = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("FaceInfoSet") is not None:
            self.FaceInfoSet = []
            for item in params.get("FaceInfoSet"):
                obj = AiSampleFaceInfo()
                obj._deserialize(item)
                self.FaceInfoSet.append(obj)
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleTagOperation(AbstractModel):
    """AI 样本管理，标签操作。

    """

    def __init__(self):
        """
        :param Type: 操作类型，可选值：add（添加）、delete（删除）、reset（重置）。\n        :type Type: str\n        :param Tags: 标签，长度限制：128 个字符。\n        :type Tags: list of str\n        """
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWord(AbstractModel):
    """AI 样本管理，关键词输出信息。

    """

    def __init__(self):
        """
        :param Keyword: 关键词。\n        :type Keyword: str\n        :param TagSet: 关键词标签。\n        :type TagSet: list of str\n        :param UsageSet: 关键词应用场景。\n        :type UsageSet: list of str\n        :param CreateTime: 创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.Keyword = None
        self.TagSet = None
        self.UsageSet = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.TagSet = params.get("TagSet")
        self.UsageSet = params.get("UsageSet")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AiSampleWordInfo(AbstractModel):
    """AI 样本管理，关键词输入信息。

    """

    def __init__(self):
        """
        :param Keyword: 关键词，长度限制：20 个字符。\n        :type Keyword: str\n        :param Tags: 关键词标签
<li>数组长度限制：20 个标签；</li>
<li>单个标签长度限制：128 个字符。</li>\n        :type Tags: list of str\n        """
        self.Keyword = None
        self.Tags = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicTaskInput(AbstractModel):
    """转动图任务类型。

    """

    def __init__(self):
        """
        :param Definition: 视频转动图模板 ID。\n        :type Definition: int\n        :param StartTimeOffset: 动图在视频中的开始时间，单位为秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 动图在视频中的结束时间，单位为秒。\n        :type EndTimeOffset: float\n        :param OutputStorage: 转动图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 转动图后文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_animatedGraphic_{definition}.{format}`。\n        :type OutputObjectPath: str\n        """
        self.Definition = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnimatedGraphicsTemplate(AbstractModel):
    """转动图模板详情。

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。\n        :type Definition: int\n        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param Name: 转动图模板名称。\n        :type Name: str\n        :param Comment: 转动图模板描述。\n        :type Comment: str\n        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 动图格式。\n        :type Format: str\n        :param Fps: 帧率。\n        :type Fps: int\n        :param Quality: 图片质量。\n        :type Quality: float\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfo(AbstractModel):
    """语音全文识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音全文识别任务开关，可选值：
<li>ON：开启智能语音全文识别任务；</li>
<li>OFF：关闭智能语音全文识别任务。</li>\n        :type Switch: str\n        :param SubtitleFormat: 生成的字幕文件格式，不填或者填空字符串表示不生成字幕文件，可选值：
<li>vtt：生成 WebVTT 字幕文件。</li>\n        :type SubtitleFormat: str\n        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrFullTextConfigureInfoForUpdate(AbstractModel):
    """语音全文识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音全文识别任务开关，可选值：
<li>ON：开启智能语音全文识别任务；</li>
<li>OFF：关闭智能语音全文识别任务。</li>\n        :type Switch: str\n        :param SubtitleFormat: 生成的字幕文件格式，填空字符串表示不生成字幕文件，可选值：
<li>vtt：生成 WebVTT 字幕文件。</li>\n        :type SubtitleFormat: str\n        """
        self.Switch = None
        self.SubtitleFormat = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubtitleFormat = params.get("SubtitleFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfo(AbstractModel):
    """语音关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音关键词识别任务开关，可选值：
<li>ON：开启语音关键词识别任务；</li>
<li>OFF：关闭语音关键词识别任务。</li>\n        :type Switch: str\n        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsrWordsConfigureInfoForUpdate(AbstractModel):
    """语音关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音关键词识别任务开关，可选值：
<li>ON：开启语音关键词识别任务；</li>
<li>OFF：关闭语音关键词识别任务。</li>\n        :type Switch: str\n        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfo(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>\n        :type Codec: str\n        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。
当取值为 0，表示音频码率和原始音频保持一致。\n        :type Bitrate: int\n        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。\n        :type SampleRate: int\n        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
当媒体的封装格式是音频格式时（flac，ogg，mp3，m4a）时，声道数不允许设为立体声。
默认值：2。\n        :type AudioChannel: int\n        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfoForUpdate(AbstractModel):
    """音频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 音频流的编码格式。
当外层参数 Container 为 mp3 时，可选值为：
<li>libmp3lame。</li>
当外层参数 Container 为 ogg 或 flac 时，可选值为：
<li>flac。</li>
当外层参数 Container 为 m4a 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame；</li>
<li>ac3。</li>
当外层参数 Container 为 mp4 或 flv 时，可选值为：
<li>libfdk_aac：更适合 mp4；</li>
<li>libmp3lame：更适合 flv；</li>
<li>mp2。</li>
当外层参数 Container 为 hls 时，可选值为：
<li>libfdk_aac；</li>
<li>libmp3lame。</li>\n        :type Codec: str\n        :param Bitrate: 音频流的码率，取值范围：0 和 [26, 256]，单位：kbps。 当取值为 0，表示音频码率和原始音频保持一致。\n        :type Bitrate: int\n        :param SampleRate: 音频流的采样率，可选值：
<li>32000</li>
<li>44100</li>
<li>48000</li>
单位：Hz。\n        :type SampleRate: int\n        :param AudioChannel: 音频通道方式，可选值：
<li>1：单通道</li>
<li>2：双通道</li>
<li>6：立体声</li>
当媒体的封装格式是音频格式时（flac，ogg，mp3，m4a）时，声道数不允许设为立体声。\n        :type AudioChannel: int\n        """
        self.Codec = None
        self.Bitrate = None
        self.SampleRate = None
        self.AudioChannel = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Bitrate = params.get("Bitrate")
        self.SampleRate = params.get("SampleRate")
        self.AudioChannel = params.get("AudioChannel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfo(AbstractModel):
    """智能分类任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能分类任务开关，可选值：
<li>ON：开启智能分类任务；</li>
<li>OFF：关闭智能分类任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassificationConfigureInfoForUpdate(AbstractModel):
    """智能分类任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能分类任务开关，可选值：
<li>ON：开启智能分类任务；</li>
<li>OFF：关闭智能分类任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContentReviewTemplateItem(AbstractModel):
    """内容审核模板详情

    """

    def __init__(self):
        """
        :param Definition: 内容审核模板唯一标识。\n        :type Definition: int\n        :param Name: 内容审核模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 内容审核模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param PornConfigure: 鉴黄控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfo`\n        :param TerrorismConfigure: 鉴恐控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfo`\n        :param PoliticalConfigure: 鉴政控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfo`\n        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfo`\n        :param UserDefineConfigure: 用户自定义内容审核控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfo`\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosFileUploadTrigger(AbstractModel):
    """绑定到 COS 的输入规则。

    """

    def __init__(self):
        """
        :param Bucket: 工作流绑定的 COS Bucket 名，如 TopRankVideo-125xxx88。\n        :type Bucket: str\n        :param Region: 工作流绑定的 COS Bucket 所属园区，如 ap-chongiqng。\n        :type Region: str\n        :param Dir: 工作流绑定的输入路径目录，必须为绝对路径，即以 `/` 开头和结尾。如`/movie/201907/`，不填代表根目录`/`。\n        :type Dir: str\n        :param Formats: 工作流允许触发的文件格式列表，如 ["mp4", "flv", "mov"]。不填代表所有格式的文件都可以触发工作流。\n        :type Formats: list of str\n        """
        self.Bucket = None
        self.Region = None
        self.Dir = None
        self.Formats = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Dir = params.get("Dir")
        self.Formats = params.get("Formats")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosInputInfo(AbstractModel):
    """视频处理 COS 对象信息。

    """

    def __init__(self):
        """
        :param Bucket: 视频处理对象文件所在的 COS Bucket 名，如 TopRankVideo-125xxx88。\n        :type Bucket: str\n        :param Region: 视频处理对象文件所在的 COS Bucket 所属园区，如 ap-chongqing。\n        :type Region: str\n        :param Object: 视频处理对象文件的输入路径，如`/movie/201907/WildAnimal.mov`。\n        :type Object: str\n        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosOutputStorage(AbstractModel):
    """视频处理 COS 输出对象信息。

    """

    def __init__(self):
        """
        :param Bucket: 视频处理生成的文件输出的目标 Bucket 名，如 TopRankVideo-125xxx88。如果不填，表示继承上层。\n        :type Bucket: str\n        :param Region: 视频处理生成的文件输出的目标 Bucket 的园区，如 ap-chongqing。如果不填，表示继承上层。\n        :type Region: str\n        """
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfo(AbstractModel):
    """智能封面任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能封面任务开关，可选值：
<li>ON：开启智能封面任务；</li>
<li>OFF：关闭智能封面任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CoverConfigureInfoForUpdate(AbstractModel):
    """智能封面任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能封面任务开关，可选值：
<li>ON：开启智能封面任务；</li>
<li>OFF：关闭智能封面任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateRequest(AbstractModel):
    """CreateAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 视频内容分析模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 视频内容分析模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param ClassificationConfigure: 智能分类任务控制参数。\n        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfo`\n        :param TagConfigure: 智能标签任务控制参数。\n        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfo`\n        :param CoverConfigure: 智能封面任务控制参数。\n        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfo`\n        :param FrameTagConfigure: 智能按帧标签任务控制参数。\n        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfo`\n        """
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfo()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfo()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfo()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfo()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIAnalysisTemplateResponse(AbstractModel):
    """CreateAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAIRecognitionTemplateRequest(AbstractModel):
    """CreateAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 视频内容识别模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 视频内容识别模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param FaceConfigure: 人脸识别控制参数。\n        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfo`\n        :param OcrFullTextConfigure: 文本全文识别控制参数。\n        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfo`\n        :param OcrWordsConfigure: 文本关键词识别控制参数。\n        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfo`\n        :param AsrFullTextConfigure: 语音全文识别控制参数。\n        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfo`\n        :param AsrWordsConfigure: 语音关键词识别控制参数。\n        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfo`\n        """
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfo()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfo()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfo()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfo()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfo()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAIRecognitionTemplateResponse(AbstractModel):
    """CreateAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Format: 自适应转码格式，取值范围：
<li>HLS，</li>
<li>MPEG-DASH。</li>\n        :type Format: str\n        :param StreamInfos: 转自适应码流输出子流参数信息，最多输出10路子流。
注意：各个子流的帧率必须保持一致；如果不一致，采用第一个子流的帧率作为输出帧率。\n        :type StreamInfos: list of AdaptiveStreamTemplate\n        :param Name: 模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
默认为否。\n        :type DisableHigherVideoBitrate: int\n        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>
默认为否。\n        :type DisableHigherVideoResolution: int\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        """
        self.Format = None
        self.StreamInfos = None
        self.Name = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.Comment = None


    def _deserialize(self, params):
        self.Format = params.get("Format")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Name = params.get("Name")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """CreateAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 自适应转码模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateAnimatedGraphicsTemplateRequest(AbstractModel):
    """CreateAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。\n        :type Fps: int\n        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 动图格式，取值为 gif 和 webp。默认为 gif。\n        :type Format: str\n        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。\n        :type Quality: float\n        :param Name: 转动图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        """
        self.Fps = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Quality = None
        self.Name = None
        self.Comment = None


    def _deserialize(self, params):
        self.Fps = params.get("Fps")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Quality = params.get("Quality")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnimatedGraphicsTemplateResponse(AbstractModel):
    """CreateAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateContentReviewTemplateRequest(AbstractModel):
    """CreateContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 内容智能识别模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 内容智能识别模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param PornConfigure: 令人反感的信息的控制参数。\n        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfo`\n        :param TerrorismConfigure: 令人不安全的信息的控制参数。\n        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfo`\n        :param PoliticalConfigure: 令人不适宜的信息的控制参数。\n        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfo`\n        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此参数尚未支持。\n        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfo`\n        :param UserDefineConfigure: 用户自定义内容智能识别控制参数。\n        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfo`\n        """
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfo()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfo()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfo()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfo()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfo()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateContentReviewTemplateResponse(AbstractModel):
    """CreateContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 内容智能识别模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateImageSpriteTemplateRequest(AbstractModel):
    """CreateImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>\n        :type SampleType: str\n        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>\n        :type SampleInterval: int\n        :param RowCount: 雪碧图中小图的行数。\n        :type RowCount: int\n        :param ColumnCount: 雪碧图中小图的列数。\n        :type ColumnCount: int\n        :param Name: 雪碧图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。\n        :type FillType: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        """
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageSpriteTemplateResponse(AbstractModel):
    """CreateImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreatePersonSampleRequest(AbstractModel):
    """CreatePersonSample请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 素材名称，长度限制：20 个字符。\n        :type Name: str\n        :param Usages: 素材应用场景，可选值：
1. Recognition：用于内容识别，等价于 Recognition.Face。
2. Review：用于不适宜内容识别，等价于 Review.Face。
3. All：包含以上全部，等价于 1+2。\n        :type Usages: list of str\n        :param Description: 素材描述，长度限制：1024 个字符。\n        :type Description: str\n        :param FaceContents: 素材图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串，仅支持 jpeg、png 图片格式。数组长度限制：5 张图片。
注意：图片必须是单人像五官较清晰的照片，像素不低于 200*200。\n        :type FaceContents: list of str\n        :param Tags: 素材标签
<li>数组长度限制：20 个标签；</li>
<li>单个标签长度限制：128 个字符。</li>\n        :type Tags: list of str\n        """
        self.Name = None
        self.Usages = None
        self.Description = None
        self.FaceContents = None
        self.Tags = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usages = params.get("Usages")
        self.Description = params.get("Description")
        self.FaceContents = params.get("FaceContents")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePersonSampleResponse(AbstractModel):
    """CreatePersonSample返回参数结构体

    """

    def __init__(self):
        """
        :param Person: 素材信息。\n        :type Person: :class:`tencentcloud.mps.v20190612.models.AiSamplePerson`\n        :param FailFaceInfoSet: 处理失败的五官定位信息。\n        :type FailFaceInfoSet: list of AiSampleFailFaceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateSampleSnapshotTemplateRequest(AbstractModel):
    """CreateSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>\n        :type SampleType: str\n        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>\n        :type SampleInterval: int\n        :param Name: 采样截图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 图片格式，取值为 jpg 和 png。默认为 jpg。\n        :type Format: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。\n        :type FillType: str\n        """
        self.SampleType = None
        self.SampleInterval = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSampleSnapshotTemplateResponse(AbstractModel):
    """CreateSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 图片格式，取值可以为 jpg 和 png。默认为 jpg。\n        :type Format: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。\n        :type FillType: str\n        """
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """CreateSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 时间点截图模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateTranscodeTemplateRequest(AbstractModel):
    """CreateTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。\n        :type Container: str\n        :param Name: 转码模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。\n        :type RemoveVideo: int\n        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>
默认值：0。\n        :type RemoveAudio: int\n        :param VideoTemplate: 视频流配置参数，当 RemoveVideo 为 0，该字段必填。\n        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`\n        :param AudioTemplate: 音频流配置参数，当 RemoveAudio 为 0，该字段必填。\n        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`\n        :param TEHDConfig: 极速高清转码参数。\n        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`\n        """
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTranscodeTemplateResponse(AbstractModel):
    """CreateTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。\n        :type Definition: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.RequestId = params.get("RequestId")


class CreateWatermarkTemplateRequest(AbstractModel):
    """CreateWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 水印类型，可选值：
<li>image：图片水印；</li>
<li>text：文字水印；</li>
<li>svg：SVG 水印。</li>\n        :type Type: str\n        :param Name: 水印模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>
默认值：TopLeft。\n        :type CoordinateOrigin: str\n        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。\n        :type XPos: str\n        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。\n        :type YPos: str\n        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段必填且有效。\n        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInput`\n        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段必填且有效。\n        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`\n        :param SvgTemplate: SVG 水印模板，仅当 Type 为 svg，该字段必填且有效。\n        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`\n        """
        self.Type = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWatermarkTemplateResponse(AbstractModel):
    """CreateWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。\n        :type Definition: int\n        :param ImageUrl: 水印图片地址，仅当 Type 为 image，该字段有效。\n        :type ImageUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Definition = None
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class CreateWordSamplesRequest(AbstractModel):
    """CreateWordSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Usages: <b>关键词应用场景，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜内容识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜内容识别，等价于 3+4；
7. All：通过光学字符识别技术、音频识别技术，进行内容识别、不适宜内容识别，等价于 1+2+3+4。\n        :type Usages: list of str\n        :param Words: 关键词，数组长度限制：100。\n        :type Words: list of AiSampleWordInfo\n        """
        self.Usages = None
        self.Words = None


    def _deserialize(self, params):
        self.Usages = params.get("Usages")
        if params.get("Words") is not None:
            self.Words = []
            for item in params.get("Words"):
                obj = AiSampleWordInfo()
                obj._deserialize(item)
                self.Words.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWordSamplesResponse(AbstractModel):
    """CreateWordSamples返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWorkflowRequest(AbstractModel):
    """CreateWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。\n        :type WorkflowName: str\n        :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。\n        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`\n        :param OutputStorage: 视频处理的文件输出存储位置。不填则继承 Trigger 中的存储位置。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致。\n        :type OutputDir: str\n        :param MediaProcessTask: 视频处理类型任务参数。\n        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: 视频内容审核类型任务参数。\n        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: 视频内容分析类型任务参数。\n        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: 视频内容识别类型任务参数。\n        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`\n        :param TaskNotifyConfig: 任务的事件通知配置，不填代表不获取事件通知。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`\n        :param TaskPriority: 工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。\n        :type TaskPriority: int\n        """
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None


    def _deserialize(self, params):
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkflowResponse(AbstractModel):
    """CreateWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。\n        :type WorkflowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.WorkflowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.RequestId = params.get("RequestId")


class DeleteAIAnalysisTemplateRequest(AbstractModel):
    """DeleteAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIAnalysisTemplateResponse(AbstractModel):
    """DeleteAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAIRecognitionTemplateRequest(AbstractModel):
    """DeleteAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAIRecognitionTemplateResponse(AbstractModel):
    """DeleteAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 自适应转码模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """DeleteAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAnimatedGraphicsTemplateRequest(AbstractModel):
    """DeleteAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAnimatedGraphicsTemplateResponse(AbstractModel):
    """DeleteAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteContentReviewTemplateRequest(AbstractModel):
    """DeleteContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 内容智能识别模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteContentReviewTemplateResponse(AbstractModel):
    """DeleteContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageSpriteTemplateRequest(AbstractModel):
    """DeleteImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageSpriteTemplateResponse(AbstractModel):
    """DeleteImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePersonSampleRequest(AbstractModel):
    """DeletePersonSample请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 素材 ID。\n        :type PersonId: str\n        """
        self.PersonId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePersonSampleResponse(AbstractModel):
    """DeletePersonSample返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSampleSnapshotTemplateRequest(AbstractModel):
    """DeleteSampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSampleSnapshotTemplateResponse(AbstractModel):
    """DeleteSampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """DeleteSnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTranscodeTemplateRequest(AbstractModel):
    """DeleteTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTranscodeTemplateResponse(AbstractModel):
    """DeleteTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWatermarkTemplateRequest(AbstractModel):
    """DeleteWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。\n        :type Definition: int\n        """
        self.Definition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWatermarkTemplateResponse(AbstractModel):
    """DeleteWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordSamplesRequest(AbstractModel):
    """DeleteWordSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Keywords: 关键词，数组长度限制：100 个词。\n        :type Keywords: list of str\n        """
        self.Keywords = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWordSamplesResponse(AbstractModel):
    """DeleteWordSamples返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWorkflowRequest(AbstractModel):
    """DeleteWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。\n        :type WorkflowId: int\n        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWorkflowResponse(AbstractModel):
    """DeleteWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAIAnalysisTemplatesRequest(AbstractModel):
    """DescribeAIAnalysisTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 视频内容分析模板唯一标识过滤条件，数组长度限制：10。\n        :type Definitions: list of int\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIAnalysisTemplatesResponse(AbstractModel):
    """DescribeAIAnalysisTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param AIAnalysisTemplateSet: 视频内容分析模板详情列表。\n        :type AIAnalysisTemplateSet: list of AIAnalysisTemplateItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AIAnalysisTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIAnalysisTemplateSet") is not None:
            self.AIAnalysisTemplateSet = []
            for item in params.get("AIAnalysisTemplateSet"):
                obj = AIAnalysisTemplateItem()
                obj._deserialize(item)
                self.AIAnalysisTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAIRecognitionTemplatesRequest(AbstractModel):
    """DescribeAIRecognitionTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 视频内容识别模板唯一标识过滤条件，数组长度限制：10。\n        :type Definitions: list of int\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：50。\n        :type Limit: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAIRecognitionTemplatesResponse(AbstractModel):
    """DescribeAIRecognitionTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param AIRecognitionTemplateSet: 视频内容识别模板详情列表。\n        :type AIRecognitionTemplateSet: list of AIRecognitionTemplateItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AIRecognitionTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AIRecognitionTemplateSet") is not None:
            self.AIRecognitionTemplateSet = []
            for item in params.get("AIRecognitionTemplateSet"):
                obj = AIRecognitionTemplateItem()
                obj._deserialize(item)
                self.AIRecognitionTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAdaptiveDynamicStreamingTemplatesRequest(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转自适应码流模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int non-negative\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAdaptiveDynamicStreamingTemplatesResponse(AbstractModel):
    """DescribeAdaptiveDynamicStreamingTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param AdaptiveDynamicStreamingTemplateSet: 转自适应码流模板详情列表。\n        :type AdaptiveDynamicStreamingTemplateSet: list of AdaptiveDynamicStreamingTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AdaptiveDynamicStreamingTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AdaptiveDynamicStreamingTemplateSet") is not None:
            self.AdaptiveDynamicStreamingTemplateSet = []
            for item in params.get("AdaptiveDynamicStreamingTemplateSet"):
                obj = AdaptiveDynamicStreamingTemplate()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAnimatedGraphicsTemplatesRequest(AbstractModel):
    """DescribeAnimatedGraphicsTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转动图模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int non-negative\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAnimatedGraphicsTemplatesResponse(AbstractModel):
    """DescribeAnimatedGraphicsTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param AnimatedGraphicsTemplateSet: 转动图模板详情列表。\n        :type AnimatedGraphicsTemplateSet: list of AnimatedGraphicsTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AnimatedGraphicsTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AnimatedGraphicsTemplateSet") is not None:
            self.AnimatedGraphicsTemplateSet = []
            for item in params.get("AnimatedGraphicsTemplateSet"):
                obj = AnimatedGraphicsTemplate()
                obj._deserialize(item)
                self.AnimatedGraphicsTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeContentReviewTemplatesRequest(AbstractModel):
    """DescribeContentReviewTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 内容智能识别模板唯一标识过滤条件，数组长度限制：50。\n        :type Definitions: list of int\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：50。\n        :type Limit: int\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeContentReviewTemplatesResponse(AbstractModel):
    """DescribeContentReviewTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param ContentReviewTemplateSet: 内容审核模板详情列表。\n        :type ContentReviewTemplateSet: list of ContentReviewTemplateItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ContentReviewTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ContentReviewTemplateSet") is not None:
            self.ContentReviewTemplateSet = []
            for item in params.get("ContentReviewTemplateSet"):
                obj = ContentReviewTemplateItem()
                obj._deserialize(item)
                self.ContentReviewTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageSpriteTemplatesRequest(AbstractModel):
    """DescribeImageSpriteTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 雪碧图模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int non-negative\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSpriteTemplatesResponse(AbstractModel):
    """DescribeImageSpriteTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param ImageSpriteTemplateSet: 雪碧图模板详情列表。\n        :type ImageSpriteTemplateSet: list of ImageSpriteTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ImageSpriteTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSpriteTemplateSet") is not None:
            self.ImageSpriteTemplateSet = []
            for item in params.get("ImageSpriteTemplateSet"):
                obj = ImageSpriteTemplate()
                obj._deserialize(item)
                self.ImageSpriteTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMediaMetaDataRequest(AbstractModel):
    """DescribeMediaMetaData请求参数结构体

    """

    def __init__(self):
        """
        :param InputInfo: 需要获取元信息的文件输入信息。\n        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`\n        """
        self.InputInfo = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaMetaDataResponse(AbstractModel):
    """DescribeMediaMetaData返回参数结构体

    """

    def __init__(self):
        """
        :param MetaData: 媒体元信息。\n        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MetaData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.RequestId = params.get("RequestId")


class DescribePersonSamplesRequest(AbstractModel):
    """DescribePersonSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 拉取的素材类型，可选值：
<li>UserDefine：用户自定义素材库；</li>
<li>Default：系统默认素材库。</li>

默认值：UserDefine，拉取用户自定义素材库素材。
说明：如果是拉取系统默认素材库，只能使用素材名字或者素材 ID + 素材名字的方式进行拉取，且人脸图片只返回一张。\n        :type Type: str\n        :param PersonIds: 素材 ID，数组长度限制：100。\n        :type PersonIds: list of str\n        :param Names: 素材名称，数组长度限制：20。\n        :type Names: list of str\n        :param Tags: 素材标签，数组长度限制：20。\n        :type Tags: list of str\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：100，最大值：100。\n        :type Limit: int\n        """
        self.Type = None
        self.PersonIds = None
        self.Names = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PersonIds = params.get("PersonIds")
        self.Names = params.get("Names")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePersonSamplesResponse(AbstractModel):
    """DescribePersonSamples返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。\n        :type TotalCount: int\n        :param PersonSet: 素材信息。\n        :type PersonSet: list of AiSamplePerson\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = AiSamplePerson()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSampleSnapshotTemplatesRequest(AbstractModel):
    """DescribeSampleSnapshotTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 采样截图模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int non-negative\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSampleSnapshotTemplatesResponse(AbstractModel):
    """DescribeSampleSnapshotTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param SampleSnapshotTemplateSet: 采样截图模板详情列表。\n        :type SampleSnapshotTemplateSet: list of SampleSnapshotTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SampleSnapshotTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SampleSnapshotTemplateSet") is not None:
            self.SampleSnapshotTemplateSet = []
            for item in params.get("SampleSnapshotTemplateSet"):
                obj = SampleSnapshotTemplate()
                obj._deserialize(item)
                self.SampleSnapshotTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotByTimeOffsetTemplatesRequest(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 指定时间点截图模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int non-negative\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        """
        self.Definitions = None
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotByTimeOffsetTemplatesResponse(AbstractModel):
    """DescribeSnapshotByTimeOffsetTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param SnapshotByTimeOffsetTemplateSet: 指定时间点截图模板详情列表。\n        :type SnapshotByTimeOffsetTemplateSet: list of SnapshotByTimeOffsetTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SnapshotByTimeOffsetTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotByTimeOffsetTemplateSet") is not None:
            self.SnapshotByTimeOffsetTemplateSet = []
            for item in params.get("SnapshotByTimeOffsetTemplateSet"):
                obj = SnapshotByTimeOffsetTemplate()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务的任务 ID。\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，目前取值有：
<li>WorkflowTask：视频工作流处理任务。</li>
<li>EditMediaTask：视频编辑任务。</li>
<li>LiveStreamProcessTask：直播流处理任务。</li>\n        :type TaskType: str\n        :param Status: 任务状态，取值：
<li>WAITING：等待中；</li>
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>\n        :type Status: str\n        :param CreateTime: 任务的创建时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param BeginProcessTime: 任务开始执行的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type BeginProcessTime: str\n        :param FinishTime: 任务执行完毕的时间，采用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type FinishTime: str\n        :param WorkflowTask: 视频处理任务信息，仅当 TaskType 为 WorkflowTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type WorkflowTask: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`\n        :param EditMediaTask: 视频编辑任务信息，仅当 TaskType 为 EditMediaTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EditMediaTask: :class:`tencentcloud.mps.v20190612.models.EditMediaTask`\n        :param LiveStreamProcessTask: 直播流处理任务信息，仅当 TaskType 为 LiveStreamProcessTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LiveStreamProcessTask: :class:`tencentcloud.mps.v20190612.models.LiveStreamProcessTask`\n        :param TaskNotifyConfig: 任务的事件通知信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`\n        :param TasksPriority: 任务流的优先级，取值范围为 [-10, 10]。\n        :type TasksPriority: int\n        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。\n        :type SessionId: str\n        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。\n        :type SessionContext: str\n        :param ExtInfo: 扩展信息字段，仅用于特定场景。\n        :type ExtInfo: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskType = None
        self.Status = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None
        self.WorkflowTask = None
        self.EditMediaTask = None
        self.LiveStreamProcessTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None
        self.ExtInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        if params.get("WorkflowTask") is not None:
            self.WorkflowTask = WorkflowTask()
            self.WorkflowTask._deserialize(params.get("WorkflowTask"))
        if params.get("EditMediaTask") is not None:
            self.EditMediaTask = EditMediaTask()
            self.EditMediaTask._deserialize(params.get("EditMediaTask"))
        if params.get("LiveStreamProcessTask") is not None:
            self.LiveStreamProcessTask = LiveStreamProcessTask()
            self.LiveStreamProcessTask._deserialize(params.get("LiveStreamProcessTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.ExtInfo = params.get("ExtInfo")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 过滤条件：任务状态，可选值：WAITING（等待中）、PROCESSING（处理中）、FINISH（已完成）。\n        :type Status: str\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        :param ScrollToken: 翻页标识，分批拉取时使用：当单次请求无法拉取所有数据，接口将会返回 ScrollToken，下一次请求携带该 Token，将会从下一条记录开始获取。\n        :type ScrollToken: str\n        """
        self.Status = None
        self.Limit = None
        self.ScrollToken = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Limit = params.get("Limit")
        self.ScrollToken = params.get("ScrollToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskSet: 任务概要列表。\n        :type TaskSet: list of TaskSimpleInfo\n        :param ScrollToken: 翻页标识，当请求未返回所有数据，该字段表示下一条记录的 ID。当该字段为空字符串，说明已无更多数据。\n        :type ScrollToken: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskSet = None
        self.ScrollToken = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskSimpleInfo()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.ScrollToken = params.get("ScrollToken")
        self.RequestId = params.get("RequestId")


class DescribeTranscodeTemplatesRequest(AbstractModel):
    """DescribeTranscodeTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 转码模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int\n        :param Type: 模板类型过滤条件，可选值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式板；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式。</li>\n        :type ContainerType: str\n        :param TEHDType: 极速高清过滤条件，用于过滤普通转码或极速高清转码模板，可选值：
<li>Common：普通转码模板；</li>
<li>TEHD：极速高清模板。</li>\n        :type TEHDType: str\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        """
        self.Definitions = None
        self.Type = None
        self.ContainerType = None
        self.TEHDType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.ContainerType = params.get("ContainerType")
        self.TEHDType = params.get("TEHDType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeTemplatesResponse(AbstractModel):
    """DescribeTranscodeTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param TranscodeTemplateSet: 转码模板详情列表。\n        :type TranscodeTemplateSet: list of TranscodeTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TranscodeTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TranscodeTemplateSet") is not None:
            self.TranscodeTemplateSet = []
            for item in params.get("TranscodeTemplateSet"):
                obj = TranscodeTemplate()
                obj._deserialize(item)
                self.TranscodeTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWatermarkTemplatesRequest(AbstractModel):
    """DescribeWatermarkTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Definitions: 水印模板唯一标识过滤条件，数组长度限制：100。\n        :type Definitions: list of int\n        :param Type: 水印类型过滤条件，可选值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>\n        :type Type: str\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数
<li>默认值：10；</li>
<li>最大值：100。</li>\n        :type Limit: int\n        """
        self.Definitions = None
        self.Type = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Definitions = params.get("Definitions")
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWatermarkTemplatesResponse(AbstractModel):
    """DescribeWatermarkTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param WatermarkTemplateSet: 水印模板详情列表。\n        :type WatermarkTemplateSet: list of WatermarkTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WatermarkTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WatermarkTemplateSet") is not None:
            self.WatermarkTemplateSet = []
            for item in params.get("WatermarkTemplateSet"):
                obj = WatermarkTemplate()
                obj._deserialize(item)
                self.WatermarkTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWordSamplesRequest(AbstractModel):
    """DescribeWordSamples请求参数结构体

    """

    def __init__(self):
        """
        :param Keywords: 关键词过滤条件，数组长度限制：100 个词。\n        :type Keywords: list of str\n        :param Usages: <b>关键词应用场景过滤条件，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜内容的识别；
4. Review.Asr：通过音频识别技术，进行不适宜内容的识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜内容的识别，等价于 3+4；
可多选，元素间关系为 or，即关键词的应用场景包含该字段集合中任意元素的记录，均符合该条件。\n        :type Usages: list of str\n        :param Tags: 标签过滤条件，数组长度限制：20 个词。\n        :type Tags: list of str\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：100，最大值：100。\n        :type Limit: int\n        """
        self.Keywords = None
        self.Usages = None
        self.Tags = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Keywords = params.get("Keywords")
        self.Usages = params.get("Usages")
        self.Tags = params.get("Tags")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWordSamplesResponse(AbstractModel):
    """DescribeWordSamples返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的记录总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param WordSet: 关键词信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type WordSet: list of AiSampleWord\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WordSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordSet") is not None:
            self.WordSet = []
            for item in params.get("WordSet"):
                obj = AiSampleWord()
                obj._deserialize(item)
                self.WordSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkflowsRequest(AbstractModel):
    """DescribeWorkflows请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowIds: 工作流 ID 过滤条件，数组长度限制：100。\n        :type WorkflowIds: list of int\n        :param Status: 工作流状态，取值范围：
<li>Enabled：已启用，</li>
<li>Disabled：已禁用。</li>
不填此参数，则不区分工作流状态。\n        :type Status: str\n        :param Offset: 分页偏移量，默认值：0。\n        :type Offset: int\n        :param Limit: 返回记录条数，默认值：10，最大值：100。\n        :type Limit: int\n        """
        self.WorkflowIds = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.WorkflowIds = params.get("WorkflowIds")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkflowsResponse(AbstractModel):
    """DescribeWorkflows返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的记录总数。\n        :type TotalCount: int\n        :param WorkflowInfoSet: 工作流信息数组。\n        :type WorkflowInfoSet: list of WorkflowInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WorkflowInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WorkflowInfoSet") is not None:
            self.WorkflowInfoSet = []
            for item in params.get("WorkflowInfoSet"):
                obj = WorkflowInfo()
                obj._deserialize(item)
                self.WorkflowInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableWorkflowRequest(AbstractModel):
    """DisableWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。\n        :type WorkflowId: int\n        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWorkflowResponse(AbstractModel):
    """DisableWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditMediaFileInfo(AbstractModel):
    """编辑点播视频文件信息

    """

    def __init__(self):
        """
        :param InputInfo: 视频的输入信息。\n        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`\n        :param StartTimeOffset: 视频剪辑的起始时间偏移，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 视频剪辑的结束时间偏移，单位：秒。\n        :type EndTimeOffset: float\n        """
        self.InputInfo = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaOutputConfig(AbstractModel):
    """编辑视频的结果文件输出配置。

    """

    def __init__(self):
        """
        :param Container: 封装格式，可选值：mp4、hls、mov、flv、avi。默认是 mp4。\n        :type Container: str\n        """
        self.Container = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaRequest(AbstractModel):
    """EditMedia请求参数结构体

    """

    def __init__(self):
        """
        :param FileInfos: 输入的视频文件信息。\n        :type FileInfos: list of EditMediaFileInfo\n        :param OutputStorage: 视频处理输出文件的目标存储。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 视频处理输出文件的目标路径。\n        :type OutputObjectPath: str\n        :param OutputConfig: 编辑后生成的文件配置。\n        :type OutputConfig: :class:`tencentcloud.mps.v20190612.models.EditMediaOutputConfig`\n        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`\n        :param TasksPriority: 任务优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。\n        :type TasksPriority: int\n        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。\n        :type SessionId: str\n        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。\n        :type SessionContext: str\n        """
        self.FileInfos = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.OutputConfig = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("OutputConfig") is not None:
            self.OutputConfig = EditMediaOutputConfig()
            self.OutputConfig._deserialize(params.get("OutputConfig"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaResponse(AbstractModel):
    """EditMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 编辑视频的任务 ID，可以通过该 ID 查询编辑任务的状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class EditMediaTask(AbstractModel):
    """编辑视频任务信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。\n        :type TaskId: str\n        :param Status: 任务状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>\n        :type Status: str\n        :param ErrCode: 错误码
<li>0：成功；</li>
<li>其他值：失败。</li>\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 视频编辑任务的输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.EditMediaTaskInput`\n        :param Output: 视频编辑任务的输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.EditMediaTaskOutput`\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = EditMediaTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = EditMediaTaskOutput()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskInput(AbstractModel):
    """编辑视频任务的输入。

    """

    def __init__(self):
        """
        :param FileInfoSet: 输入的视频文件信息。\n        :type FileInfoSet: list of EditMediaFileInfo\n        """
        self.FileInfoSet = None


    def _deserialize(self, params):
        if params.get("FileInfoSet") is not None:
            self.FileInfoSet = []
            for item in params.get("FileInfoSet"):
                obj = EditMediaFileInfo()
                obj._deserialize(item)
                self.FileInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditMediaTaskOutput(AbstractModel):
    """编辑视频任务的输出

    """

    def __init__(self):
        """
        :param OutputStorage: 编辑后文件的目标存储。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param Path: 编辑后的视频文件路径。\n        :type Path: str\n        """
        self.OutputStorage = None
        self.Path = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWorkflowRequest(AbstractModel):
    """EnableWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。\n        :type WorkflowId: int\n        """
        self.WorkflowId = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWorkflowResponse(AbstractModel):
    """EnableWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExecuteFunctionRequest(AbstractModel):
    """ExecuteFunction请求参数结构体

    """

    def __init__(self):
        """
        :param FunctionName: 调用后端接口名称。\n        :type FunctionName: str\n        :param FunctionArg: 接口参数，具体参数格式调用时与后端协调。\n        :type FunctionArg: str\n        """
        self.FunctionName = None
        self.FunctionArg = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.FunctionArg = params.get("FunctionArg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteFunctionResponse(AbstractModel):
    """ExecuteFunction返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 处理结果打包后的字符串，具体与后台一同协调。\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ExpressionConfigInfo(AbstractModel):
    """表情识别参数配置

    """

    def __init__(self):
        """
        :param Switch: 表情识别任务开关，可选值：
<li>ON：开启；</li>
<li>OFF：关闭。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceConfigureInfo(AbstractModel):
    """人脸识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 人脸识别任务开关，可选值：
<li>ON：开启智能人脸识别任务；</li>
<li>OFF：关闭智能人脸识别任务。</li>\n        :type Switch: str\n        :param Score: 人脸识别过滤分数，当识别结果达到该分数以上，返回识别结果。默认 95 分。取值范围：0 - 100。\n        :type Score: float\n        :param DefaultLibraryLabelSet: 默认人物过滤标签，指定需要返回的默认人物的标签。如果未填或者为空，则全部默认人物结果都返回。标签可选值：
<li>entertainment：娱乐明星；</li>
<li>sport：体育明星；</li>
<li>politician：政治人物。</li>\n        :type DefaultLibraryLabelSet: list of str\n        :param UserDefineLibraryLabelSet: 用户自定义人物过滤标签，指定需要返回的用户自定义人物的标签。如果未填或者为空，则全部自定义人物结果都返回。
标签个数最多 100 个，每个标签长度最多 16 个字符。\n        :type UserDefineLibraryLabelSet: list of str\n        :param FaceLibrary: 人物库选择，可选值：
<li>Default：使用默认人物库；</li>
<li>UserDefine：使用用户自定义人物库。</li>
<li>All：同时使用默认人物库和用户自定义人物库。</li>
默认值：All，使用系统默认人物库及用户自定义人物库。\n        :type FaceLibrary: str\n        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FaceConfigureInfoForUpdate(AbstractModel):
    """人脸识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 人脸识别任务开关，可选值：
<li>ON：开启智能人脸识别任务；</li>
<li>OFF：关闭智能人脸识别任务。</li>\n        :type Switch: str\n        :param Score: 人脸识别过滤分数，当识别结果达到该分数以上，返回识别结果。取值范围：0-100。\n        :type Score: float\n        :param DefaultLibraryLabelSet: 默认人物过滤标签，指定需要返回的默认人物的标签。如果未填或者为空，则全部默认人物结果都返回。标签可选值：
<li>entertainment：娱乐明星；</li>
<li>sport：体育明星；</li>
<li>politician：政治人物。</li>\n        :type DefaultLibraryLabelSet: list of str\n        :param UserDefineLibraryLabelSet: 用户自定义人物过滤标签，指定需要返回的用户自定义人物的标签。如果未填或者为空，则全部自定义人物结果都返回。
标签个数最多 100 个，每个标签长度最多 16 个字符。\n        :type UserDefineLibraryLabelSet: list of str\n        :param FaceLibrary: 人物库选择，可选值：
<li>Default：使用默认人物库；</li>
<li>UserDefine：使用用户自定义人物库。</li>
<li>All：同时使用默认人物库和用户自定义人物库。</li>\n        :type FaceLibrary: str\n        """
        self.Switch = None
        self.Score = None
        self.DefaultLibraryLabelSet = None
        self.UserDefineLibraryLabelSet = None
        self.FaceLibrary = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Score = params.get("Score")
        self.DefaultLibraryLabelSet = params.get("DefaultLibraryLabelSet")
        self.UserDefineLibraryLabelSet = params.get("UserDefineLibraryLabelSet")
        self.FaceLibrary = params.get("FaceLibrary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfo(AbstractModel):
    """智能按帧标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能按帧标签任务开关，可选值：
<li>ON：开启智能按帧标签任务；</li>
<li>OFF：关闭智能按帧标签任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameTagConfigureInfoForUpdate(AbstractModel):
    """智能按帧标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能按帧标签任务开关，可选值：
<li>ON：开启智能按帧标签任务；</li>
<li>OFF：关闭智能按帧标签任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeadTailParameter(AbstractModel):
    """片头片尾参数

    """

    def __init__(self):
        """
        :param HeadSet: 片头列表。\n        :type HeadSet: list of MediaInputInfo\n        :param TailSet: 片尾列表。\n        :type TailSet: list of MediaInputInfo\n        """
        self.HeadSet = None
        self.TailSet = None


    def _deserialize(self, params):
        if params.get("HeadSet") is not None:
            self.HeadSet = []
            for item in params.get("HeadSet"):
                obj = MediaInputInfo()
                obj._deserialize(item)
                self.HeadSet.append(obj)
        if params.get("TailSet") is not None:
            self.TailSet = []
            for item in params.get("TailSet"):
                obj = MediaInputInfo()
                obj._deserialize(item)
                self.TailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTaskInput(AbstractModel):
    """对视频截雪碧图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板 ID。\n        :type Definition: int\n        :param OutputStorage: 截取雪碧图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 截取雪碧图后，雪碧图图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_imageSprite_{definition}_{number}.{format}`。\n        :type OutputObjectPath: str\n        :param WebVttObjectName: 截取雪碧图后，Web VTT 文件的输出路径，只能为相对路径。如果不填，则默认为相对路径：`{inputName}_imageSprite_{definition}.{format}`。\n        :type WebVttObjectName: str\n        :param ObjectNumberFormat: 截取雪碧图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`\n        """
        self.Definition = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.WebVttObjectName = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.WebVttObjectName = params.get("WebVttObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSpriteTemplate(AbstractModel):
    """雪碧图模板详情

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。\n        :type Definition: int\n        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param Name: 雪碧图模板名称。\n        :type Name: str\n        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param SampleType: 采样类型。\n        :type SampleType: str\n        :param SampleInterval: 采样间隔。\n        :type SampleInterval: int\n        :param RowCount: 雪碧图中小图的行数。\n        :type RowCount: int\n        :param ColumnCount: 雪碧图中小图的列数。\n        :type ColumnCount: int\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。\n        :type FillType: str\n        :param Comment: 模板描述信息。\n        :type Comment: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。\n        :type ImageContent: str\n        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。取值范围为[8, 4096]。</li>
默认值：10%。\n        :type Width: str\n        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。取值范围为0或[8, 4096]。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。\n        :type Height: str\n        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束（默认值）。</li>\n        :type RepeatType: str\n        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkInputForUpdate(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片 [Base64](https://tools.ietf.org/html/rfc4648) 编码后的字符串。支持 jpeg、png 图片格式。\n        :type ImageContent: str\n        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。取值范围为[8, 4096]。</li>\n        :type Width: str\n        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。取值范围为0或[8, 4096]。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。\n        :type Height: str\n        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束。</li>\n        :type RepeatType: str\n        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageContent = params.get("ImageContent")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageWatermarkTemplate(AbstractModel):
    """图片水印模板

    """

    def __init__(self):
        """
        :param ImageUrl: 水印图片地址。\n        :type ImageUrl: str\n        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>\n        :type Width: str\n        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；</li>
0px：表示 Height 按照 Width 对视频宽度的比例缩放。\n        :type Height: str\n        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束。</li>\n        :type RepeatType: str\n        """
        self.ImageUrl = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiRecognitionResultInfo(AbstractModel):
    """直播流 AI 识别结果

    """

    def __init__(self):
        """
        :param ResultSet: 内容识别结果列表。\n        :type ResultSet: list of LiveStreamAiRecognitionResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiRecognitionResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiRecognitionResultItem(AbstractModel):
    """直播流 AI 识别结果

    """

    def __init__(self):
        """
        :param Type: 结果的类型，取值范围：
<li>FaceRecognition：人脸识别，</li>
<li>AsrWordsRecognition：语音关键词识别，</li>
<li>OcrWordsRecognition：文本关键词识别，</li>
<li>AsrFullTextRecognition：语音全文识别，</li>
<li>OcrFullTextRecognition：文本全文识别。</li>\n        :type Type: str\n        :param FaceRecognitionResultSet: 人脸识别结果，当 Type 为
FaceRecognition 时有效。\n        :type FaceRecognitionResultSet: list of LiveStreamFaceRecognitionResult\n        :param AsrWordsRecognitionResultSet: 语音关键词识别结果，当 Type 为
AsrWordsRecognition 时有效。\n        :type AsrWordsRecognitionResultSet: list of LiveStreamAsrWordsRecognitionResult\n        :param OcrWordsRecognitionResultSet: 文本关键词识别结果，当 Type 为
OcrWordsRecognition 时有效。\n        :type OcrWordsRecognitionResultSet: list of LiveStreamOcrWordsRecognitionResult\n        :param AsrFullTextRecognitionResultSet: 语音全文识别结果，当 Type 为
AsrFullTextRecognition 时有效。\n        :type AsrFullTextRecognitionResultSet: list of LiveStreamAsrFullTextRecognitionResult\n        :param OcrFullTextRecognitionResultSet: 文本全文识别结果，当 Type 为
OcrFullTextRecognition 时有效。\n        :type OcrFullTextRecognitionResultSet: list of LiveStreamOcrFullTextRecognitionResult\n        """
        self.Type = None
        self.FaceRecognitionResultSet = None
        self.AsrWordsRecognitionResultSet = None
        self.OcrWordsRecognitionResultSet = None
        self.AsrFullTextRecognitionResultSet = None
        self.OcrFullTextRecognitionResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("FaceRecognitionResultSet") is not None:
            self.FaceRecognitionResultSet = []
            for item in params.get("FaceRecognitionResultSet"):
                obj = LiveStreamFaceRecognitionResult()
                obj._deserialize(item)
                self.FaceRecognitionResultSet.append(obj)
        if params.get("AsrWordsRecognitionResultSet") is not None:
            self.AsrWordsRecognitionResultSet = []
            for item in params.get("AsrWordsRecognitionResultSet"):
                obj = LiveStreamAsrWordsRecognitionResult()
                obj._deserialize(item)
                self.AsrWordsRecognitionResultSet.append(obj)
        if params.get("OcrWordsRecognitionResultSet") is not None:
            self.OcrWordsRecognitionResultSet = []
            for item in params.get("OcrWordsRecognitionResultSet"):
                obj = LiveStreamOcrWordsRecognitionResult()
                obj._deserialize(item)
                self.OcrWordsRecognitionResultSet.append(obj)
        if params.get("AsrFullTextRecognitionResultSet") is not None:
            self.AsrFullTextRecognitionResultSet = []
            for item in params.get("AsrFullTextRecognitionResultSet"):
                obj = LiveStreamAsrFullTextRecognitionResult()
                obj._deserialize(item)
                self.AsrFullTextRecognitionResultSet.append(obj)
        if params.get("OcrFullTextRecognitionResultSet") is not None:
            self.OcrFullTextRecognitionResultSet = []
            for item in params.get("OcrFullTextRecognitionResultSet"):
                obj = LiveStreamOcrFullTextRecognitionResult()
                obj._deserialize(item)
                self.OcrFullTextRecognitionResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImagePoliticalResult(AbstractModel):
    """直播 AI 内容审核图片鉴政结果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 嫌疑片段涉政分数。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>\n        :type Suggestion: str\n        :param Label: 视频鉴政结果标签，取值范围：
<li>politician：政治人物。</li>
<li>violation_photo：违规图标。</li>\n        :type Label: str\n        :param Name: 涉政人物、违规图标名字。\n        :type Name: str\n        :param AreaCoordSet: 涉政人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。\n        :type AreaCoordSet: list of int\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。\n        :type Url: str\n        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type PicUrlExpireTime: str\n        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Name = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Name = params.get("Name")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImagePornResult(AbstractModel):
    """直播 AI 内容审核图片鉴黄结果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 嫌疑片段涉黄分数。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>\n        :type Suggestion: str\n        :param Label: 视频鉴黄结果标签，取值范围：
<li>porn：色情。</li>
<li>sexy：性感。</li>
<li>vulgar：低俗。</li>
<li>intimacy：亲密行为。</li>\n        :type Label: str\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。\n        :type Url: str\n        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type PicUrlExpireTime: str\n        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewImageTerrorismResult(AbstractModel):
    """直播 AI 内容审核图片鉴恐结果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 嫌疑片段涉恐分数。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段鉴恐结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>\n        :type Suggestion: str\n        :param Label: 视频暴恐结果标签，取值范围：
<li>guns：武器枪支。</li>
<li>crowd：人群聚集。</li>
<li>police：警察部队。</li>
<li>bloody：血腥画面。</li>
<li>banners：暴恐旗帜。</li>
<li>militant：武装分子。</li>
<li>explosion：爆炸火灾。</li>
<li>terrorists：暴恐人物。</li>\n        :type Label: str\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。\n        :type Url: str\n        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type PicUrlExpireTime: str\n        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewResultInfo(AbstractModel):
    """直播流 AI 审核结果

    """

    def __init__(self):
        """
        :param ResultSet: 内容审核结果列表。\n        :type ResultSet: list of LiveStreamAiReviewResultItem\n        """
        self.ResultSet = None


    def _deserialize(self, params):
        if params.get("ResultSet") is not None:
            self.ResultSet = []
            for item in params.get("ResultSet"):
                obj = LiveStreamAiReviewResultItem()
                obj._deserialize(item)
                self.ResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewResultItem(AbstractModel):
    """直播流 AI 审核结果

    """

    def __init__(self):
        """
        :param Type: 审核结果的类型，可以取的值有：
<li>ImagePorn：图片鉴黄</li>
<li>ImageTerrorism：图片鉴恐</li>
<li>ImagePolitical：图片鉴政</li>
<li>PornVoice：声音鉴黄</li>\n        :type Type: str\n        :param ImagePornResultSet: 图片鉴黄的结果，当 Type 为 ImagePorn 时有效。\n        :type ImagePornResultSet: list of LiveStreamAiReviewImagePornResult\n        :param ImageTerrorismResultSet: 图片鉴恐的结果，当 Type 为 ImageTerrorism 时有效。\n        :type ImageTerrorismResultSet: list of LiveStreamAiReviewImageTerrorismResult\n        :param ImagePoliticalResultSet: 图片鉴政的结果，当 Type 为 ImagePolitical 时有效。\n        :type ImagePoliticalResultSet: list of LiveStreamAiReviewImagePoliticalResult\n        :param VoicePornResultSet: 声音鉴黄的结果，当 Type 为 PornVoice 时有效。\n        :type VoicePornResultSet: list of LiveStreamAiReviewVoicePornResult\n        """
        self.Type = None
        self.ImagePornResultSet = None
        self.ImageTerrorismResultSet = None
        self.ImagePoliticalResultSet = None
        self.VoicePornResultSet = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("ImagePornResultSet") is not None:
            self.ImagePornResultSet = []
            for item in params.get("ImagePornResultSet"):
                obj = LiveStreamAiReviewImagePornResult()
                obj._deserialize(item)
                self.ImagePornResultSet.append(obj)
        if params.get("ImageTerrorismResultSet") is not None:
            self.ImageTerrorismResultSet = []
            for item in params.get("ImageTerrorismResultSet"):
                obj = LiveStreamAiReviewImageTerrorismResult()
                obj._deserialize(item)
                self.ImageTerrorismResultSet.append(obj)
        if params.get("ImagePoliticalResultSet") is not None:
            self.ImagePoliticalResultSet = []
            for item in params.get("ImagePoliticalResultSet"):
                obj = LiveStreamAiReviewImagePoliticalResult()
                obj._deserialize(item)
                self.ImagePoliticalResultSet.append(obj)
        if params.get("VoicePornResultSet") is not None:
            self.VoicePornResultSet = []
            for item in params.get("VoicePornResultSet"):
                obj = LiveStreamAiReviewVoicePornResult()
                obj._deserialize(item)
                self.VoicePornResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAiReviewVoicePornResult(AbstractModel):
    """直播 AI 内容审核声音鉴黄结果

    """

    def __init__(self):
        """
        :param StartPtsTime: 嫌疑片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 嫌疑片段结束的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 嫌疑片段涉黄分数。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass</li>
<li>review</li>
<li>block</li>\n        :type Suggestion: str\n        :param Label: 视频鉴黄结果标签，取值范围：
<li>sexual_moan：呻吟。</li>\n        :type Label: str\n        """
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.Suggestion = None
        self.Label = None


    def _deserialize(self, params):
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAsrFullTextRecognitionResult(AbstractModel):
    """直播识别 Asr 全文识别

    """

    def __init__(self):
        """
        :param Text: 识别文本。\n        :type Text: str\n        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamAsrWordsRecognitionResult(AbstractModel):
    """直播 AI Asr 单词识别结果

    """

    def __init__(self):
        """
        :param Word: 语音关键词。\n        :type Word: str\n        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamFaceRecognitionResult(AbstractModel):
    """直播 AI 人脸识别结果

    """

    def __init__(self):
        """
        :param Id: 人物唯一标识 ID。\n        :type Id: str\n        :param Name: 人物名称。\n        :type Name: str\n        :param Type: 人物库类型，表示识别出的人物来自哪个人物库：
<li>Default：默认人物库；</li><li>UserDefine：用户自定义人物库。</li>\n        :type Type: str\n        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。\n        :type AreaCoordSet: list of int\n        """
        self.Id = None
        self.Name = None
        self.Type = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamOcrFullTextRecognitionResult(AbstractModel):
    """直播识别 Ocr 全文识别

    """

    def __init__(self):
        """
        :param Text: 语音文本。\n        :type Text: str\n        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param AreaCoordSet: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。\n        :type AreaCoordSet: list of int\n        """
        self.Text = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoordSet = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoordSet = params.get("AreaCoordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamOcrWordsRecognitionResult(AbstractModel):
    """直播 AI Ocr 单词识别结果

    """

    def __init__(self):
        """
        :param Word: 文本关键词。\n        :type Word: str\n        :param StartPtsTime: 识别片段起始的 PTS 时间，单位：秒。\n        :type StartPtsTime: float\n        :param EndPtsTime: 识别片段终止的 PTS 时间，单位：秒。\n        :type EndPtsTime: float\n        :param Confidence: 识别片段置信度。取值：0~100。\n        :type Confidence: float\n        :param AreaCoords: 识别结果的区域坐标。数组包含 4 个元素 [x1,y1,x2,y2]，依次表示区域左上点、右下点的横纵坐标。\n        :type AreaCoords: list of int\n        """
        self.Word = None
        self.StartPtsTime = None
        self.EndPtsTime = None
        self.Confidence = None
        self.AreaCoords = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.StartPtsTime = params.get("StartPtsTime")
        self.EndPtsTime = params.get("EndPtsTime")
        self.Confidence = params.get("Confidence")
        self.AreaCoords = params.get("AreaCoords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamProcessErrorInfo(AbstractModel):
    """直播流处理错误信息

    """

    def __init__(self):
        """
        :param ErrCode: 错误码：
<li>0表示没有错误；</li>
<li>非0表示错误，请参考 Message 错误信息。</li>\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        """
        self.ErrCode = None
        self.Message = None


    def _deserialize(self, params):
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamProcessTask(AbstractModel):
    """直播处理任务信息

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务 ID。\n        :type TaskId: str\n        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>\n        :type Status: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Url: 直播流 URL。\n        :type Url: str\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.Url = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveStreamTaskNotifyConfig(AbstractModel):
    """任务处理的事件通知配置。

    """

    def __init__(self):
        """
        :param CmqModel: CMQ 的模型，有 Queue 和 Topic 两种，目前仅支持 Queue。\n        :type CmqModel: str\n        :param CmqRegion: CMQ 的园区，如 sh，bj 等。\n        :type CmqRegion: str\n        :param QueueName: 当模型为 Queue 时有效，表示接收事件通知的 CMQ 的队列名。\n        :type QueueName: str\n        :param TopicName: 当模型为 Topic 时有效，表示接收事件通知的 CMQ 的主题名。\n        :type TopicName: str\n        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskRequest(AbstractModel):
    """ManageTask请求参数结构体

    """

    def __init__(self):
        """
        :param OperationType: 操作类型，取值范围：
<ul>
<li>Abort：终止任务。使用说明：
<ul><li>若 [任务类型](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 为直播流处理任务（LiveStreamProcessTask），支持终止 [任务状态](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 为等待中（WAITING）或处理中（PROCESSING）的任务；</li>
<li>否则，对于其他 [任务类型](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0)，只支持终止 [任务状态](/document/product/862/37614#3.-.E8.BE.93.E5.87.BA.E5.8F.82.E6.95.B0) 为等待中（WAITING）的任务。</li></ul>
</li></ul>\n        :type OperationType: str\n        :param TaskId: 视频处理的任务 ID。\n        :type TaskId: str\n        """
        self.OperationType = None
        self.TaskId = None


    def _deserialize(self, params):
        self.OperationType = params.get("OperationType")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageTaskResponse(AbstractModel):
    """ManageTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MediaAiAnalysisClassificationItem(AbstractModel):
    """智能分类结果

    """

    def __init__(self):
        """
        :param Classification: 智能分类的类别名称。\n        :type Classification: str\n        :param Confidence: 智能分类的可信度，取值范围是 0 到 100。\n        :type Confidence: float\n        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisCoverItem(AbstractModel):
    """智能封面信息

    """

    def __init__(self):
        """
        :param CoverPath: 智能封面存储路径。\n        :type CoverPath: str\n        :param Confidence: 智能封面的可信度，取值范围是 0 到 100。\n        :type Confidence: float\n        """
        self.CoverPath = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverPath = params.get("CoverPath")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagItem(AbstractModel):
    """智能按帧标签结果信息

    """

    def __init__(self):
        """
        :param Tag: 按帧标签名称。\n        :type Tag: str\n        :param CategorySet: 按帧标签名称的分类列表，CategorySet.N 表示第 N+1级分类。
比如 Tag 为“塔楼”时，CategorySet 包含两个元素：CategorySet.0 为“场景”，CategorySet.1为 “建筑”，表示按帧标签为“塔楼”，且第1级分类是“场景”，第2级分类是“建筑”。\n        :type CategorySet: list of str\n        :param Confidence: 按帧标签的可信度，取值范围是 0 到 100。\n        :type Confidence: float\n        """
        self.Tag = None
        self.CategorySet = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.CategorySet = params.get("CategorySet")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisFrameTagSegmentItem(AbstractModel):
    """按帧标签片段列表

    """

    def __init__(self):
        """
        :param StartTimeOffset: 按帧标签起始的偏移时间。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 按帧标签结束的偏移时间。\n        :type EndTimeOffset: float\n        :param TagSet: 时间片段内的标签列表。\n        :type TagSet: list of MediaAiAnalysisFrameTagItem\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.TagSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = MediaAiAnalysisFrameTagItem()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAiAnalysisTagItem(AbstractModel):
    """智能标签结果信息

    """

    def __init__(self):
        """
        :param Tag: 标签名称。\n        :type Tag: str\n        :param Confidence: 标签的可信度，取值范围是 0 到 100。\n        :type Confidence: float\n        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAnimatedGraphicsItem(AbstractModel):
    """视频转动图结果信息

    """

    def __init__(self):
        """
        :param Storage: 转动图文件的存储位置。\n        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param Path: 转动图的文件路径。\n        :type Path: str\n        :param Definition: 转动图模板 ID，参见[转动图参数模板](https://cloud.tencent.com/document/product/862/37042#.E9.A2.84.E7.BD.AE.E8.BD.AC.E5.8A.A8.E5.9B.BE.E6.A8.A1.E6.9D.BF)。\n        :type Definition: int\n        :param Container: 动图格式，如 gif。\n        :type Container: str\n        :param Height: 动图的高度，单位：px。\n        :type Height: int\n        :param Width: 动图的宽度，单位：px。\n        :type Width: int\n        :param Bitrate: 动图码率，单位：bps。\n        :type Bitrate: int\n        :param Size: 动图大小，单位：字节。\n        :type Size: int\n        :param Md5: 动图的md5值。\n        :type Md5: str\n        :param StartTimeOffset: 动图在视频中的起始时间偏移，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 动图在视频中的结束时间偏移，单位：秒。\n        :type EndTimeOffset: float\n        """
        self.Storage = None
        self.Path = None
        self.Definition = None
        self.Container = None
        self.Height = None
        self.Width = None
        self.Bitrate = None
        self.Size = None
        self.Md5 = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Bitrate = params.get("Bitrate")
        self.Size = params.get("Size")
        self.Md5 = params.get("Md5")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaAudioStreamItem(AbstractModel):
    """点播文件音频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 音频流的码率，单位：bps。\n        :type Bitrate: int\n        :param SamplingRate: 音频流的采样率，单位：hz。\n        :type SamplingRate: int\n        :param Codec: 音频流的编码格式，例如 aac。\n        :type Codec: str\n        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewAsrTextSegmentItem(AbstractModel):
    """内容审核 Asr 文字审核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段置信度。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param KeywordSet: 嫌疑关键词列表。\n        :type KeywordSet: list of str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewOcrTextSegmentItem(AbstractModel):
    """内容审核 Ocr 文字审核嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段置信度。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段审核结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param KeywordSet: 嫌疑关键词列表。\n        :type KeywordSet: list of str\n        :param AreaCoordSet: 嫌疑文字出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。\n        :type AreaCoordSet: list of int\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
PicUrlExpireTime 时间点后图片将被删除）。\n        :type Url: str\n        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type PicUrlExpireTime: str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.KeywordSet = None
        self.AreaCoordSet = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.KeywordSet = params.get("KeywordSet")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewPoliticalSegmentItem(AbstractModel):
    """内容审核涉政嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段涉政分数。\n        :type Confidence: float\n        :param Suggestion: 嫌疑片段鉴政结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param Name: 涉政人物、违规图标名字。\n        :type Name: str\n        :param Label: 嫌疑片段鉴政结果标签。内容审核模板[画面鉴政任务控制参数](https://cloud.tencent.com/document/api/862/37615#PoliticalImgReviewTemplateInfo)里 LabelSet 参数与此参数取值范围的对应关系：
violation_photo：
<li>violation_photo：违规图标。</li>
politician：
<li>nation_politician：国家领导人；</li>
<li>province_politician: 省部级领导人；</li>
<li>bureau_politician：厅局级领导人；</li>
<li>county_politician：县处级领导人；</li>
<li>rural_politician：乡科级领导人；</li>
<li>sensitive_politician：敏感政治人物；</li>
<li>foreign_politician：国外领导人。</li>
entertainment：
<li>sensitive_entertainment：敏感娱乐人物。</li>
sport：
<li>sensitive_sport：敏感体育人物。</li>
entrepreneur：
<li>sensitive_entrepreneur：敏感商业人物。</li>
scholar：
<li>sensitive_scholar：敏感教育学者。</li>
celebrity：
<li>sensitive_celebrity：敏感知名人物；</li>
<li>historical_celebrity：历史知名人物。</li>
military：
<li>sensitive_military：敏感军事人物。</li>\n        :type Label: str\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。\n        :type Url: str\n        :param AreaCoordSet: 涉政人物、违规图标出现的区域坐标 (像素级)，[x1, y1, x2, y2]，即左上角坐标、右下角坐标。\n        :type AreaCoordSet: list of int\n        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type PicUrlExpireTime: str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Suggestion = None
        self.Name = None
        self.Label = None
        self.Url = None
        self.AreaCoordSet = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.Url = params.get("Url")
        self.AreaCoordSet = params.get("AreaCoordSet")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaContentReviewSegmentItem(AbstractModel):
    """内容审核涉黄/暴恐嫌疑片段

    """

    def __init__(self):
        """
        :param StartTimeOffset: 嫌疑片段起始的偏移时间，单位：秒。\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 嫌疑片段结束的偏移时间，单位：秒。\n        :type EndTimeOffset: float\n        :param Confidence: 嫌疑片段涉黄分数。\n        :type Confidence: float\n        :param Label: 嫌疑片段鉴黄结果标签。\n        :type Label: str\n        :param Suggestion: 嫌疑片段鉴黄结果建议，取值范围：
<li>pass。</li>
<li>review。</li>
<li>block。</li>\n        :type Suggestion: str\n        :param Url: 嫌疑图片 URL （图片不会永久存储，到达
 PicUrlExpireTime 时间点后图片将被删除）。\n        :type Url: str\n        :param PicUrlExpireTime: 嫌疑图片 URL 失效时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type PicUrlExpireTime: str\n        """
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.Confidence = None
        self.Label = None
        self.Suggestion = None
        self.Url = None
        self.PicUrlExpireTime = None


    def _deserialize(self, params):
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        self.Confidence = params.get("Confidence")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Url = params.get("Url")
        self.PicUrlExpireTime = params.get("PicUrlExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaImageSpriteItem(AbstractModel):
    """雪碧图信息

    """

    def __init__(self):
        """
        :param Definition: 雪碧图规格，参见[雪碧图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF)。\n        :type Definition: int\n        :param Height: 雪碧图小图的高度。\n        :type Height: int\n        :param Width: 雪碧图小图的宽度。\n        :type Width: int\n        :param TotalCount: 每一张雪碧图大图里小图的数量。\n        :type TotalCount: int\n        :param ImagePathSet: 每一张雪碧图大图的路径。\n        :type ImagePathSet: list of str\n        :param WebVttPath: 雪碧图子图位置与时间关系的 WebVtt 文件路径。WebVtt 文件表明了各个雪碧图小图对应的时间点，以及在雪碧大图里的坐标位置，一般被播放器用于实现预览。\n        :type WebVttPath: str\n        :param Storage: 雪碧图文件的存储位置。\n        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        """
        self.Definition = None
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImagePathSet = None
        self.WebVttPath = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImagePathSet = params.get("ImagePathSet")
        self.WebVttPath = params.get("WebVttPath")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInputInfo(AbstractModel):
    """视频处理的输入对象信息。

    """

    def __init__(self):
        """
        :param Type: 输入来源对象的类型，支持 COS 和 URL 两种。\n        :type Type: str\n        :param CosInputInfo: 当 Type 为 COS 时有效，则该项为必填，表示视频处理 COS 对象信息。\n        :type CosInputInfo: :class:`tencentcloud.mps.v20190612.models.CosInputInfo`\n        :param UrlInputInfo: 当 Type 为 URL 时有效，则该项为必填，表示视频处理 URL 对象信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UrlInputInfo: :class:`tencentcloud.mps.v20190612.models.UrlInputInfo`\n        """
        self.Type = None
        self.CosInputInfo = None
        self.UrlInputInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInputInfo") is not None:
            self.CosInputInfo = CosInputInfo()
            self.CosInputInfo._deserialize(params.get("CosInputInfo"))
        if params.get("UrlInputInfo") is not None:
            self.UrlInputInfo = UrlInputInfo()
            self.UrlInputInfo._deserialize(params.get("UrlInputInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaMetaData(AbstractModel):
    """点播媒体文件元信息

    """

    def __init__(self):
        """
        :param Size: 上传的媒体文件大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。\n        :type Size: int\n        :param Container: 容器类型，例如 m4a，mp4 等。\n        :type Container: str\n        :param Bitrate: 视频流码率平均值与音频流码率平均值之和，单位：bps。\n        :type Bitrate: int\n        :param Height: 视频流高度的最大值，单位：px。\n        :type Height: int\n        :param Width: 视频流宽度的最大值，单位：px。\n        :type Width: int\n        :param Duration: 视频时长，单位：秒。\n        :type Duration: float\n        :param Rotate: 视频拍摄时的选择角度，单位：度。\n        :type Rotate: int\n        :param VideoStreamSet: 视频流信息。\n        :type VideoStreamSet: list of MediaVideoStreamItem\n        :param AudioStreamSet: 音频流信息。\n        :type AudioStreamSet: list of MediaAudioStreamItem\n        :param VideoDuration: 视频时长，单位：秒。\n        :type VideoDuration: float\n        :param AudioDuration: 音频时长，单位：秒。\n        :type AudioDuration: float\n        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamSet = None
        self.AudioStreamSet = None
        self.VideoDuration = None
        self.AudioDuration = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        self.VideoDuration = params.get("VideoDuration")
        self.AudioDuration = params.get("AudioDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAdaptiveDynamicStreamingResult(AbstractModel):
    """对视频转自适应码流任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 对视频转自适应码流任务的输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AdaptiveDynamicStreamingTaskInput`\n        :param Output: 对视频转自适应码流任务的输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.AdaptiveDynamicStreamingInfoItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AdaptiveDynamicStreamingTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = AdaptiveDynamicStreamingInfoItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskAnimatedGraphicResult(AbstractModel):
    """转动图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 转动图任务的输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.AnimatedGraphicTaskInput`\n        :param Output: 转动图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaAnimatedGraphicsItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = AnimatedGraphicTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaAnimatedGraphicsItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskImageSpriteResult(AbstractModel):
    """对视频截雪碧图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 对视频截雪碧图任务的输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.ImageSpriteTaskInput`\n        :param Output: 对视频截雪碧图任务的输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaImageSpriteItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = ImageSpriteTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaImageSpriteItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskInput(AbstractModel):
    """视频处理任务类型

    """

    def __init__(self):
        """
        :param TranscodeTaskSet: 视频转码任务列表。\n        :type TranscodeTaskSet: list of TranscodeTaskInput\n        :param AnimatedGraphicTaskSet: 视频转动图任务列表。\n        :type AnimatedGraphicTaskSet: list of AnimatedGraphicTaskInput\n        :param SnapshotByTimeOffsetTaskSet: 对视频按时间点截图任务列表。\n        :type SnapshotByTimeOffsetTaskSet: list of SnapshotByTimeOffsetTaskInput\n        :param SampleSnapshotTaskSet: 对视频采样截图任务列表。\n        :type SampleSnapshotTaskSet: list of SampleSnapshotTaskInput\n        :param ImageSpriteTaskSet: 对视频截雪碧图任务列表。\n        :type ImageSpriteTaskSet: list of ImageSpriteTaskInput\n        :param AdaptiveDynamicStreamingTaskSet: 转自适应码流任务列表。\n        :type AdaptiveDynamicStreamingTaskSet: list of AdaptiveDynamicStreamingTaskInput\n        """
        self.TranscodeTaskSet = None
        self.AnimatedGraphicTaskSet = None
        self.SnapshotByTimeOffsetTaskSet = None
        self.SampleSnapshotTaskSet = None
        self.ImageSpriteTaskSet = None
        self.AdaptiveDynamicStreamingTaskSet = None


    def _deserialize(self, params):
        if params.get("TranscodeTaskSet") is not None:
            self.TranscodeTaskSet = []
            for item in params.get("TranscodeTaskSet"):
                obj = TranscodeTaskInput()
                obj._deserialize(item)
                self.TranscodeTaskSet.append(obj)
        if params.get("AnimatedGraphicTaskSet") is not None:
            self.AnimatedGraphicTaskSet = []
            for item in params.get("AnimatedGraphicTaskSet"):
                obj = AnimatedGraphicTaskInput()
                obj._deserialize(item)
                self.AnimatedGraphicTaskSet.append(obj)
        if params.get("SnapshotByTimeOffsetTaskSet") is not None:
            self.SnapshotByTimeOffsetTaskSet = []
            for item in params.get("SnapshotByTimeOffsetTaskSet"):
                obj = SnapshotByTimeOffsetTaskInput()
                obj._deserialize(item)
                self.SnapshotByTimeOffsetTaskSet.append(obj)
        if params.get("SampleSnapshotTaskSet") is not None:
            self.SampleSnapshotTaskSet = []
            for item in params.get("SampleSnapshotTaskSet"):
                obj = SampleSnapshotTaskInput()
                obj._deserialize(item)
                self.SampleSnapshotTaskSet.append(obj)
        if params.get("ImageSpriteTaskSet") is not None:
            self.ImageSpriteTaskSet = []
            for item in params.get("ImageSpriteTaskSet"):
                obj = ImageSpriteTaskInput()
                obj._deserialize(item)
                self.ImageSpriteTaskSet.append(obj)
        if params.get("AdaptiveDynamicStreamingTaskSet") is not None:
            self.AdaptiveDynamicStreamingTaskSet = []
            for item in params.get("AdaptiveDynamicStreamingTaskSet"):
                obj = AdaptiveDynamicStreamingTaskInput()
                obj._deserialize(item)
                self.AdaptiveDynamicStreamingTaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskResult(AbstractModel):
    """任务查询结果类型

    """

    def __init__(self):
        """
        :param Type: 任务的类型，可以取的值有：
<li>Transcode：转码</li>
<li>AnimatedGraphics：转动图</li>
<li>SnapshotByTimeOffset：时间点截图</li>
<li>SampleSnapshot：采样截图</li>
<li>ImageSprites：雪碧图</li>
<li>CoverBySnapshot：截图做封面</li>
<li>AdaptiveDynamicStreaming：自适应码流</li>\n        :type Type: str\n        :param TranscodeTask: 视频转码任务的查询结果，当任务类型为 Transcode 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TranscodeTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskTranscodeResult`\n        :param AnimatedGraphicTask: 视频转动图任务的查询结果，当任务类型为 AnimatedGraphics 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AnimatedGraphicTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAnimatedGraphicResult`\n        :param SnapshotByTimeOffsetTask: 对视频按时间点截图任务的查询结果，当任务类型为 SnapshotByTimeOffset 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SnapshotByTimeOffsetTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSnapshotByTimeOffsetResult`\n        :param SampleSnapshotTask: 对视频采样截图任务的查询结果，当任务类型为 SampleSnapshot 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SampleSnapshotTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskSampleSnapshotResult`\n        :param ImageSpriteTask: 对视频截雪碧图任务的查询结果，当任务类型为 ImageSprite 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageSpriteTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskImageSpriteResult`\n        :param AdaptiveDynamicStreamingTask: 转自适应码流任务查询结果，当任务类型为 AdaptiveDynamicStreaming 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdaptiveDynamicStreamingTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskAdaptiveDynamicStreamingResult`\n        """
        self.Type = None
        self.TranscodeTask = None
        self.AnimatedGraphicTask = None
        self.SnapshotByTimeOffsetTask = None
        self.SampleSnapshotTask = None
        self.ImageSpriteTask = None
        self.AdaptiveDynamicStreamingTask = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("TranscodeTask") is not None:
            self.TranscodeTask = MediaProcessTaskTranscodeResult()
            self.TranscodeTask._deserialize(params.get("TranscodeTask"))
        if params.get("AnimatedGraphicTask") is not None:
            self.AnimatedGraphicTask = MediaProcessTaskAnimatedGraphicResult()
            self.AnimatedGraphicTask._deserialize(params.get("AnimatedGraphicTask"))
        if params.get("SnapshotByTimeOffsetTask") is not None:
            self.SnapshotByTimeOffsetTask = MediaProcessTaskSnapshotByTimeOffsetResult()
            self.SnapshotByTimeOffsetTask._deserialize(params.get("SnapshotByTimeOffsetTask"))
        if params.get("SampleSnapshotTask") is not None:
            self.SampleSnapshotTask = MediaProcessTaskSampleSnapshotResult()
            self.SampleSnapshotTask._deserialize(params.get("SampleSnapshotTask"))
        if params.get("ImageSpriteTask") is not None:
            self.ImageSpriteTask = MediaProcessTaskImageSpriteResult()
            self.ImageSpriteTask._deserialize(params.get("ImageSpriteTask"))
        if params.get("AdaptiveDynamicStreamingTask") is not None:
            self.AdaptiveDynamicStreamingTask = MediaProcessTaskAdaptiveDynamicStreamingResult()
            self.AdaptiveDynamicStreamingTask._deserialize(params.get("AdaptiveDynamicStreamingTask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSampleSnapshotResult(AbstractModel):
    """对视频做采样截图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 对视频做采样截图任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.SampleSnapshotTaskInput`\n        :param Output: 对视频做采样截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSampleSnapshotItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SampleSnapshotTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSampleSnapshotItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskSnapshotByTimeOffsetResult(AbstractModel):
    """对视频按指定时间点截图任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 对视频按指定时间点截图任务输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.SnapshotByTimeOffsetTaskInput`\n        :param Output: 对视频按指定时间点截图任务输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaSnapshotByTimeOffsetItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = SnapshotByTimeOffsetTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaSnapshotByTimeOffsetItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaProcessTaskTranscodeResult(AbstractModel):
    """转码任务结果类型

    """

    def __init__(self):
        """
        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。\n        :type Status: str\n        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [视频处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。\n        :type ErrCodeExt: str\n        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。\n        :type ErrCode: int\n        :param Message: 错误信息。\n        :type Message: str\n        :param Input: 转码任务的输入。\n        :type Input: :class:`tencentcloud.mps.v20190612.models.TranscodeTaskInput`\n        :param Output: 转码任务的输出。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Output: :class:`tencentcloud.mps.v20190612.models.MediaTranscodeItem`\n        """
        self.Status = None
        self.ErrCodeExt = None
        self.ErrCode = None
        self.Message = None
        self.Input = None
        self.Output = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCodeExt = params.get("ErrCodeExt")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("Input") is not None:
            self.Input = TranscodeTaskInput()
            self.Input._deserialize(params.get("Input"))
        if params.get("Output") is not None:
            self.Output = MediaTranscodeItem()
            self.Output._deserialize(params.get("Output"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSampleSnapshotItem(AbstractModel):
    """采样截图信息

    """

    def __init__(self):
        """
        :param Definition: 采样截图规格 ID，参见[采样截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。\n        :type Definition: int\n        :param SampleType: 采样方式，取值范围：
<li>Percent：根据百分比间隔采样。</li>
<li>Time：根据时间间隔采样。</li>\n        :type SampleType: str\n        :param Interval: 采样间隔
<li>当 SampleType 为 Percent 时，该值表示多少百分比一张图。</li>
<li>当 SampleType 为 Time 时，该值表示多少时间间隔一张图，单位秒， 第一张图均为视频首帧。</li>\n        :type Interval: int\n        :param Storage: 截图后文件的存储位置。\n        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param ImagePathSet: 生成的截图 path 列表。\n        :type ImagePathSet: list of str\n        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。\n        :type WaterMarkDefinition: list of int\n        """
        self.Definition = None
        self.SampleType = None
        self.Interval = None
        self.Storage = None
        self.ImagePathSet = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.SampleType = params.get("SampleType")
        self.Interval = params.get("Interval")
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        self.ImagePathSet = params.get("ImagePathSet")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimeOffsetItem(AbstractModel):
    """点播文件指定时间点截图信息

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图规格，参见[指定时间点截图参数模板](https://cloud.tencent.com/document/product/266/33480#.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)。\n        :type Definition: int\n        :param PicInfoSet: 同一规格的截图信息集合，每个元素代表一张截图。\n        :type PicInfoSet: list of MediaSnapshotByTimePicInfoItem\n        :param Storage: 指定时间点截图文件的存储位置。\n        :type Storage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        """
        self.Definition = None
        self.PicInfoSet = None
        self.Storage = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("PicInfoSet") is not None:
            self.PicInfoSet = []
            for item in params.get("PicInfoSet"):
                obj = MediaSnapshotByTimePicInfoItem()
                obj._deserialize(item)
                self.PicInfoSet.append(obj)
        if params.get("Storage") is not None:
            self.Storage = TaskOutputStorage()
            self.Storage._deserialize(params.get("Storage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaSnapshotByTimePicInfoItem(AbstractModel):
    """指定时间点截图信息

    """

    def __init__(self):
        """
        :param TimeOffset: 该张截图对应视频文件中的时间偏移，单位为<font color=red>毫秒</font>。\n        :type TimeOffset: float\n        :param Path: 该张截图的路径。\n        :type Path: str\n        :param WaterMarkDefinition: 截图如果被打上了水印，被打水印的模板 ID 列表。\n        :type WaterMarkDefinition: list of int\n        """
        self.TimeOffset = None
        self.Path = None
        self.WaterMarkDefinition = None


    def _deserialize(self, params):
        self.TimeOffset = params.get("TimeOffset")
        self.Path = params.get("Path")
        self.WaterMarkDefinition = params.get("WaterMarkDefinition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaTranscodeItem(AbstractModel):
    """转码信息

    """

    def __init__(self):
        """
        :param OutputStorage: 转码后文件的目标存储。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param Path: 转码后的视频文件路径。\n        :type Path: str\n        :param Definition: 转码规格 ID，参见[转码参数模板](https://cloud.tencent.com/document/product/862/37042)。\n        :type Definition: int\n        :param Bitrate: 视频流码率平均值与音频流码率平均值之和， 单位：bps。\n        :type Bitrate: int\n        :param Height: 视频流高度的最大值，单位：px。\n        :type Height: int\n        :param Width: 视频流宽度的最大值，单位：px。\n        :type Width: int\n        :param Size: 媒体文件总大小（视频为 HLS 时，大小是 m3u8 和 ts 文件大小的总和），单位：字节。\n        :type Size: int\n        :param Duration: 视频时长，单位：秒。\n        :type Duration: float\n        :param Container: 容器类型，例如 m4a，mp4 等。\n        :type Container: str\n        :param Md5: 视频的 md5 值。\n        :type Md5: str\n        :param AudioStreamSet: 音频流信息。\n        :type AudioStreamSet: list of MediaAudioStreamItem\n        :param VideoStreamSet: 视频流信息。\n        :type VideoStreamSet: list of MediaVideoStreamItem\n        """
        self.OutputStorage = None
        self.Path = None
        self.Definition = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Size = None
        self.Duration = None
        self.Container = None
        self.Md5 = None
        self.AudioStreamSet = None
        self.VideoStreamSet = None


    def _deserialize(self, params):
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.Path = params.get("Path")
        self.Definition = params.get("Definition")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Size = params.get("Size")
        self.Duration = params.get("Duration")
        self.Container = params.get("Container")
        self.Md5 = params.get("Md5")
        if params.get("AudioStreamSet") is not None:
            self.AudioStreamSet = []
            for item in params.get("AudioStreamSet"):
                obj = MediaAudioStreamItem()
                obj._deserialize(item)
                self.AudioStreamSet.append(obj)
        if params.get("VideoStreamSet") is not None:
            self.VideoStreamSet = []
            for item in params.get("VideoStreamSet"):
                obj = MediaVideoStreamItem()
                obj._deserialize(item)
                self.VideoStreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaVideoStreamItem(AbstractModel):
    """点播文件视频流信息

    """

    def __init__(self):
        """
        :param Bitrate: 视频流的码率，单位：bps。\n        :type Bitrate: int\n        :param Height: 视频流的高度，单位：px。\n        :type Height: int\n        :param Width: 视频流的宽度，单位：px。\n        :type Width: int\n        :param Codec: 视频流的编码格式，例如 h264。\n        :type Codec: str\n        :param Fps: 帧率，单位：hz。\n        :type Fps: int\n        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateRequest(AbstractModel):
    """ModifyAIAnalysisTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容分析模板唯一标识。\n        :type Definition: int\n        :param Name: 视频内容分析模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 视频内容分析模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param ClassificationConfigure: 智能分类任务控制参数。\n        :type ClassificationConfigure: :class:`tencentcloud.mps.v20190612.models.ClassificationConfigureInfoForUpdate`\n        :param TagConfigure: 智能标签任务控制参数。\n        :type TagConfigure: :class:`tencentcloud.mps.v20190612.models.TagConfigureInfoForUpdate`\n        :param CoverConfigure: 智能封面任务控制参数。\n        :type CoverConfigure: :class:`tencentcloud.mps.v20190612.models.CoverConfigureInfoForUpdate`\n        :param FrameTagConfigure: 智能按帧标签任务控制参数。\n        :type FrameTagConfigure: :class:`tencentcloud.mps.v20190612.models.FrameTagConfigureInfoForUpdate`\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.ClassificationConfigure = None
        self.TagConfigure = None
        self.CoverConfigure = None
        self.FrameTagConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("ClassificationConfigure") is not None:
            self.ClassificationConfigure = ClassificationConfigureInfoForUpdate()
            self.ClassificationConfigure._deserialize(params.get("ClassificationConfigure"))
        if params.get("TagConfigure") is not None:
            self.TagConfigure = TagConfigureInfoForUpdate()
            self.TagConfigure._deserialize(params.get("TagConfigure"))
        if params.get("CoverConfigure") is not None:
            self.CoverConfigure = CoverConfigureInfoForUpdate()
            self.CoverConfigure._deserialize(params.get("CoverConfigure"))
        if params.get("FrameTagConfigure") is not None:
            self.FrameTagConfigure = FrameTagConfigureInfoForUpdate()
            self.FrameTagConfigure._deserialize(params.get("FrameTagConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIAnalysisTemplateResponse(AbstractModel):
    """ModifyAIAnalysisTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAIRecognitionTemplateRequest(AbstractModel):
    """ModifyAIRecognitionTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 视频内容识别模板唯一标识。\n        :type Definition: int\n        :param Name: 视频内容识别模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 视频内容识别模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param FaceConfigure: 人脸识别控制参数。\n        :type FaceConfigure: :class:`tencentcloud.mps.v20190612.models.FaceConfigureInfoForUpdate`\n        :param OcrFullTextConfigure: 文本全文识别控制参数。\n        :type OcrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.OcrFullTextConfigureInfoForUpdate`\n        :param OcrWordsConfigure: 文本关键词识别控制参数。\n        :type OcrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.OcrWordsConfigureInfoForUpdate`\n        :param AsrFullTextConfigure: 语音全文识别控制参数。\n        :type AsrFullTextConfigure: :class:`tencentcloud.mps.v20190612.models.AsrFullTextConfigureInfoForUpdate`\n        :param AsrWordsConfigure: 语音关键词识别控制参数。\n        :type AsrWordsConfigure: :class:`tencentcloud.mps.v20190612.models.AsrWordsConfigureInfoForUpdate`\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.FaceConfigure = None
        self.OcrFullTextConfigure = None
        self.OcrWordsConfigure = None
        self.AsrFullTextConfigure = None
        self.AsrWordsConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("FaceConfigure") is not None:
            self.FaceConfigure = FaceConfigureInfoForUpdate()
            self.FaceConfigure._deserialize(params.get("FaceConfigure"))
        if params.get("OcrFullTextConfigure") is not None:
            self.OcrFullTextConfigure = OcrFullTextConfigureInfoForUpdate()
            self.OcrFullTextConfigure._deserialize(params.get("OcrFullTextConfigure"))
        if params.get("OcrWordsConfigure") is not None:
            self.OcrWordsConfigure = OcrWordsConfigureInfoForUpdate()
            self.OcrWordsConfigure._deserialize(params.get("OcrWordsConfigure"))
        if params.get("AsrFullTextConfigure") is not None:
            self.AsrFullTextConfigure = AsrFullTextConfigureInfoForUpdate()
            self.AsrFullTextConfigure._deserialize(params.get("AsrFullTextConfigure"))
        if params.get("AsrWordsConfigure") is not None:
            self.AsrWordsConfigure = AsrWordsConfigureInfoForUpdate()
            self.AsrWordsConfigure._deserialize(params.get("AsrWordsConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAIRecognitionTemplateResponse(AbstractModel):
    """ModifyAIRecognitionTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAdaptiveDynamicStreamingTemplateRequest(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转自适应码流模板唯一标识。\n        :type Definition: int\n        :param Name: 模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Format: 转自适应码流格式，取值范围：
<li>HLS，</li>
<li>MPEG-DASH。</li>\n        :type Format: str\n        :param DisableHigherVideoBitrate: 是否禁止视频低码率转高码率，取值范围：
<li>0：否，</li>
<li>1：是。</li>\n        :type DisableHigherVideoBitrate: int\n        :param DisableHigherVideoResolution: 是否禁止视频分辨率转高分辨率，取值范围：
<li>0：否，</li>
<li>1：是。</li>\n        :type DisableHigherVideoResolution: int\n        :param StreamInfos: 转自适应码流输入流参数信息，最多输入10路流。
注意：各个流的帧率必须保持一致；如果不一致，采用第一个流的帧率作为输出帧率。\n        :type StreamInfos: list of AdaptiveStreamTemplate\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        """
        self.Definition = None
        self.Name = None
        self.Format = None
        self.DisableHigherVideoBitrate = None
        self.DisableHigherVideoResolution = None
        self.StreamInfos = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Format = params.get("Format")
        self.DisableHigherVideoBitrate = params.get("DisableHigherVideoBitrate")
        self.DisableHigherVideoResolution = params.get("DisableHigherVideoResolution")
        if params.get("StreamInfos") is not None:
            self.StreamInfos = []
            for item in params.get("StreamInfos"):
                obj = AdaptiveStreamTemplate()
                obj._deserialize(item)
                self.StreamInfos.append(obj)
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAdaptiveDynamicStreamingTemplateResponse(AbstractModel):
    """ModifyAdaptiveDynamicStreamingTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAnimatedGraphicsTemplateRequest(AbstractModel):
    """ModifyAnimatedGraphicsTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转动图模板唯一标识。\n        :type Definition: int\n        :param Name: 转动图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 动图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 动图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 动图格式，取值为 gif 和 webp。\n        :type Format: str\n        :param Fps: 帧率，取值范围：[1, 30]，单位：Hz。\n        :type Fps: int\n        :param Quality: 图片质量，取值范围：[1, 100]，默认值为 75。\n        :type Quality: float\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Fps = None
        self.Quality = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Fps = params.get("Fps")
        self.Quality = params.get("Quality")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAnimatedGraphicsTemplateResponse(AbstractModel):
    """ModifyAnimatedGraphicsTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyContentReviewTemplateRequest(AbstractModel):
    """ModifyContentReviewTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 内容智能识别模板唯一标识。\n        :type Definition: int\n        :param Name: 内容智能识别模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 内容智能识别模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param PornConfigure: 令人反感的信息的控制参数。\n        :type PornConfigure: :class:`tencentcloud.mps.v20190612.models.PornConfigureInfoForUpdate`\n        :param TerrorismConfigure: 令人不安全的信息的控制参数。\n        :type TerrorismConfigure: :class:`tencentcloud.mps.v20190612.models.TerrorismConfigureInfoForUpdate`\n        :param PoliticalConfigure: 令人不适宜的控制参数。\n        :type PoliticalConfigure: :class:`tencentcloud.mps.v20190612.models.PoliticalConfigureInfoForUpdate`\n        :param ProhibitedConfigure: 违禁控制参数。违禁内容包括：
<li>谩骂；</li>
<li>涉毒违法。</li>
注意：此参数尚未支持。\n        :type ProhibitedConfigure: :class:`tencentcloud.mps.v20190612.models.ProhibitedConfigureInfoForUpdate`\n        :param UserDefineConfigure: 用户自定义内容智能识别控制参数。\n        :type UserDefineConfigure: :class:`tencentcloud.mps.v20190612.models.UserDefineConfigureInfoForUpdate`\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.PornConfigure = None
        self.TerrorismConfigure = None
        self.PoliticalConfigure = None
        self.ProhibitedConfigure = None
        self.UserDefineConfigure = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        if params.get("PornConfigure") is not None:
            self.PornConfigure = PornConfigureInfoForUpdate()
            self.PornConfigure._deserialize(params.get("PornConfigure"))
        if params.get("TerrorismConfigure") is not None:
            self.TerrorismConfigure = TerrorismConfigureInfoForUpdate()
            self.TerrorismConfigure._deserialize(params.get("TerrorismConfigure"))
        if params.get("PoliticalConfigure") is not None:
            self.PoliticalConfigure = PoliticalConfigureInfoForUpdate()
            self.PoliticalConfigure._deserialize(params.get("PoliticalConfigure"))
        if params.get("ProhibitedConfigure") is not None:
            self.ProhibitedConfigure = ProhibitedConfigureInfoForUpdate()
            self.ProhibitedConfigure._deserialize(params.get("ProhibitedConfigure"))
        if params.get("UserDefineConfigure") is not None:
            self.UserDefineConfigure = UserDefineConfigureInfoForUpdate()
            self.UserDefineConfigure._deserialize(params.get("UserDefineConfigure"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyContentReviewTemplateResponse(AbstractModel):
    """ModifyContentReviewTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSpriteTemplateRequest(AbstractModel):
    """ModifyImageSpriteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 雪碧图模板唯一标识。\n        :type Definition: int\n        :param Name: 雪碧图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 雪碧图中小图的宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 雪碧图中小图的高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param SampleType: 采样类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>\n        :type SampleType: str\n        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>\n        :type SampleInterval: int\n        :param RowCount: 雪碧图中小图的行数。\n        :type RowCount: int\n        :param ColumnCount: 雪碧图中小图的列数。\n        :type ColumnCount: int\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
默认值：black 。\n        :type FillType: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.RowCount = None
        self.ColumnCount = None
        self.FillType = None
        self.Comment = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.RowCount = params.get("RowCount")
        self.ColumnCount = params.get("ColumnCount")
        self.FillType = params.get("FillType")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageSpriteTemplateResponse(AbstractModel):
    """ModifyImageSpriteTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonSampleRequest(AbstractModel):
    """ModifyPersonSample请求参数结构体

    """

    def __init__(self):
        """
        :param PersonId: 素材 ID。\n        :type PersonId: str\n        :param Name: 名称，长度限制：128 个字符。\n        :type Name: str\n        :param Description: 描述，长度限制：1024 个字符。\n        :type Description: str\n        :param Usages: 素材应用场景，可选值：
1. Recognition：用于内容识别，等价于 Recognition.Face。
2. Review：用于不适宜的内容识别，等价于 Review.Face。
3. All：用于内容识别、不适宜的内容识别，等价于 1+2。\n        :type Usages: list of str\n        :param FaceOperationInfo: 五官操作信息。\n        :type FaceOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleFaceOperation`\n        :param TagOperationInfo: 标签操作信息。\n        :type TagOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleTagOperation`\n        """
        self.PersonId = None
        self.Name = None
        self.Description = None
        self.Usages = None
        self.FaceOperationInfo = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Usages = params.get("Usages")
        if params.get("FaceOperationInfo") is not None:
            self.FaceOperationInfo = AiSampleFaceOperation()
            self.FaceOperationInfo._deserialize(params.get("FaceOperationInfo"))
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPersonSampleResponse(AbstractModel):
    """ModifyPersonSample返回参数结构体

    """

    def __init__(self):
        """
        :param Person: 素材信息。\n        :type Person: :class:`tencentcloud.mps.v20190612.models.AiSamplePerson`\n        :param FailFaceInfoSet: 处理失败的五官信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailFaceInfoSet: list of AiSampleFailFaceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Person = None
        self.FailFaceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Person") is not None:
            self.Person = AiSamplePerson()
            self.Person._deserialize(params.get("Person"))
        if params.get("FailFaceInfoSet") is not None:
            self.FailFaceInfoSet = []
            for item in params.get("FailFaceInfoSet"):
                obj = AiSampleFailFaceInfo()
                obj._deserialize(item)
                self.FailFaceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifySampleSnapshotTemplateRequest(AbstractModel):
    """ModifySampleSnapshotTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。\n        :type Definition: int\n        :param Name: 采样截图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param SampleType: 采样截图类型，取值：
<li>Percent：按百分比。</li>
<li>Time：按时间间隔。</li>\n        :type SampleType: str\n        :param SampleInterval: 采样间隔。
<li>当 SampleType 为 Percent 时，指定采样间隔的百分比。</li>
<li>当 SampleType 为 Time 时，指定采样间隔的时间，单位为秒。</li>\n        :type SampleInterval: int\n        :param Format: 图片格式，取值为 jpg 和 png。\n        :type Format: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。\n        :type FillType: str\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.SampleType = None
        self.SampleInterval = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySampleSnapshotTemplateResponse(AbstractModel):
    """ModifySampleSnapshotTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotByTimeOffsetTemplateRequest(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板唯一标识。\n        :type Definition: int\n        :param Name: 指定时间点截图模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 图片格式，取值可以为 jpg 和 png。\n        :type Format: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。\n        :type FillType: str\n        """
        self.Definition = None
        self.Name = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.Comment = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.Comment = params.get("Comment")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySnapshotByTimeOffsetTemplateResponse(AbstractModel):
    """ModifySnapshotByTimeOffsetTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTranscodeTemplateRequest(AbstractModel):
    """ModifyTranscodeTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。\n        :type Definition: int\n        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。\n        :type Container: str\n        :param Name: 转码模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param RemoveVideo: 是否去除视频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>\n        :type RemoveVideo: int\n        :param RemoveAudio: 是否去除音频数据，可选值：
<li>0：保留</li>
<li>1：去除</li>\n        :type RemoveAudio: int\n        :param VideoTemplate: 视频流配置参数。\n        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`\n        :param AudioTemplate: 音频流配置参数。\n        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`\n        :param TEHDConfig: 极速高清转码参数。\n        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`\n        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTranscodeTemplateResponse(AbstractModel):
    """ModifyTranscodeTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWatermarkTemplateRequest(AbstractModel):
    """ModifyWatermarkTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。\n        :type Definition: int\n        :param Name: 水印模板名称，长度限制：64 个字符。\n        :type Name: str\n        :param Comment: 模板描述信息，长度限制：256 个字符。\n        :type Comment: str\n        :param CoordinateOrigin: 原点位置，可选值：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>TopRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>BottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>BottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下角。</li>\n        :type CoordinateOrigin: str\n        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>\n        :type XPos: str\n        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>\n        :type YPos: str\n        :param ImageTemplate: 图片水印模板，该字段仅对图片水印模板有效。\n        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkInputForUpdate`\n        :param TextTemplate: 文字水印模板，该字段仅对文字水印模板有效。\n        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInputForUpdate`\n        :param SvgTemplate: SVG水印模板，当 Type 为 svg，该字段必填。当 Type 为 image 或 text，该字段无效。\n        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInputForUpdate`\n        """
        self.Definition = None
        self.Name = None
        self.Comment = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkInputForUpdate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInputForUpdate()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInputForUpdate()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWatermarkTemplateResponse(AbstractModel):
    """ModifyWatermarkTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param ImageUrl: 图片水印地址，仅当 ImageTemplate.ImageContent 非空，该字段有效。\n        :type ImageUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageUrl = params.get("ImageUrl")
        self.RequestId = params.get("RequestId")


class ModifyWordSampleRequest(AbstractModel):
    """ModifyWordSample请求参数结构体

    """

    def __init__(self):
        """
        :param Keyword: 关键词，长度限制：128 个字符。\n        :type Keyword: str\n        :param Usages: <b>关键词应用场景，可选值：</b>
1. Recognition.Ocr：通过光学字符识别技术，进行内容识别；
2. Recognition.Asr：通过音频识别技术，进行内容识别；
3. Review.Ocr：通过光学字符识别技术，进行不适宜的内容识别；
4. Review.Asr：通过音频识别技术，进行不适宜的音频识别；
<b>可合并简写为：</b>
5. Recognition：通过光学字符识别技术、音频识别技术，进行内容识别，等价于 1+2；
6. Review：通过光学字符识别技术、音频识别技术，进行不适宜的内容识别，等价于 3+4；
7. All：包含以上全部，等价于 1+2+3+4。\n        :type Usages: list of str\n        :param TagOperationInfo: 标签操作信息。\n        :type TagOperationInfo: :class:`tencentcloud.mps.v20190612.models.AiSampleTagOperation`\n        """
        self.Keyword = None
        self.Usages = None
        self.TagOperationInfo = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.Usages = params.get("Usages")
        if params.get("TagOperationInfo") is not None:
            self.TagOperationInfo = AiSampleTagOperation()
            self.TagOperationInfo._deserialize(params.get("TagOperationInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWordSampleResponse(AbstractModel):
    """ModifyWordSample返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MosaicInput(AbstractModel):
    """视频处理任务中的马赛克参数类型

    """

    def __init__(self):
        """
        :param CoordinateOrigin: 原点位置，目前仅支持：
<li>TopLeft：表示坐标原点位于视频图像左上角，马赛克原点为图片或文字的左上角。</li>
默认值：TopLeft。\n        :type CoordinateOrigin: str\n        :param XPos: 马赛克原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。\n        :type XPos: str\n        :param YPos: 马赛克原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。\n        :type YPos: str\n        :param Width: 马赛克的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。\n        :type Width: str\n        :param Height: 马赛克的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示马赛克 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示马赛克 Height 单位为像素，如 100px 表示 Height 为 100 像素。</li>
默认值：10%。\n        :type Height: str\n        :param StartTimeOffset: 马赛克的起始时间偏移，单位：秒。不填或填0，表示马赛克从画面出现时开始显现。
<li>不填或填0，表示马赛克从画面开始就出现；</li>
<li>当数值大于0时（假设为 n），表示马赛克从画面开始的第 n 秒出现；</li>
<li>当数值小于0时（假设为 -n），表示马赛克从离画面结束 n 秒前开始出现。</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 马赛克的结束时间偏移，单位：秒。
<li>不填或填0，表示马赛克持续到画面结束；</li>
<li>当数值大于0时（假设为 n），表示马赛克持续到第 n 秒时消失；</li>
<li>当数值小于0时（假设为 -n），表示马赛克持续到离画面结束 n 秒前消失。</li>\n        :type EndTimeOffset: float\n        """
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.Width = None
        self.Height = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NumberFormat(AbstractModel):
    """输出文件名的`{number}`变量的规则。

    """

    def __init__(self):
        """
        :param InitialValue: `{number}`变量的起始值，默认为0。\n        :type InitialValue: int\n        :param Increment: `{number}`变量的增长步长，默认为1。\n        :type Increment: int\n        :param MinLength: `{number}`变量的最小长度，不足时补占位符。默认为1。\n        :type MinLength: int\n        :param PlaceHolder: `{number}`变量的长度不足时，补充的占位符。默认为"0"。\n        :type PlaceHolder: str\n        """
        self.InitialValue = None
        self.Increment = None
        self.MinLength = None
        self.PlaceHolder = None


    def _deserialize(self, params):
        self.InitialValue = params.get("InitialValue")
        self.Increment = params.get("Increment")
        self.MinLength = params.get("MinLength")
        self.PlaceHolder = params.get("PlaceHolder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfo(AbstractModel):
    """文本全文本识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本全文识别任务开关，可选值：
<li>ON：开启智能文本全文识别任务；</li>
<li>OFF：关闭智能文本全文识别任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrFullTextConfigureInfoForUpdate(AbstractModel):
    """文本全文本识别任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本全文识别任务开关，可选值：
<li>ON：开启智能文本全文识别任务；</li>
<li>OFF：关闭智能文本全文识别任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfo(AbstractModel):
    """文本关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本关键词识别任务开关，可选值：
<li>ON：开启文本关键词识别任务；</li>
<li>OFF：关闭文本关键词识别任务。</li>\n        :type Switch: str\n        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OcrWordsConfigureInfoForUpdate(AbstractModel):
    """文本关键词识别控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本关键词识别任务开关，可选值：
<li>ON：开启文本关键词识别任务；</li>
<li>OFF：关闭文本关键词识别任务。</li>\n        :type Switch: str\n        :param LabelSet: 关键词过滤标签，指定需要返回的关键词的标签。如果未填或者为空，则全部结果都返回。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        """
        self.Switch = None
        self.LabelSet = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverrideTranscodeParameter(AbstractModel):
    """自定义转码的规格参数。用于覆盖模板中对应参数值。

    """

    def __init__(self):
        """
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。\n        :type Container: str\n        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>\n        :type RemoveVideo: int\n        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>\n        :type RemoveAudio: int\n        :param VideoTemplate: 视频流配置参数。\n        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfoForUpdate`\n        :param AudioTemplate: 音频流配置参数。\n        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfoForUpdate`\n        :param TEHDConfig: 极速高清转码参数。\n        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfigForUpdate`\n        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfoForUpdate()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfoForUpdate()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfigForUpdate()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseLiveStreamProcessNotificationRequest(AbstractModel):
    """ParseLiveStreamProcessNotification请求参数结构体

    """

    def __init__(self):
        """
        :param Content: 从 CMQ 获取到的直播流事件通知内容。\n        :type Content: str\n        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseLiveStreamProcessNotificationResponse(AbstractModel):
    """ParseLiveStreamProcessNotification返回参数结构体

    """

    def __init__(self):
        """
        :param NotificationType: 直播流处理结果类型，包含：
<li>AiReviewResult：内容审核结果；</li>
<li>AiRecognitionResult：内容识别结果；</li>
<li>ProcessEof：直播流处理结束。</li>\n        :type NotificationType: str\n        :param TaskId: 视频处理任务 ID。\n        :type TaskId: str\n        :param ProcessEofInfo: 直播流处理错误信息，当 NotificationType 为 ProcessEof 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProcessEofInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamProcessErrorInfo`\n        :param AiReviewResultInfo: 内容审核结果，当 NotificationType 为 AiReviewResult 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AiReviewResultInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamAiReviewResultInfo`\n        :param AiRecognitionResultInfo: 内容识别结果，当 NotificationType 为 AiRecognitionResult 时有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AiRecognitionResultInfo: :class:`tencentcloud.mps.v20190612.models.LiveStreamAiRecognitionResultInfo`\n        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。\n        :type SessionId: str\n        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。\n        :type SessionContext: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NotificationType = None
        self.TaskId = None
        self.ProcessEofInfo = None
        self.AiReviewResultInfo = None
        self.AiRecognitionResultInfo = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NotificationType = params.get("NotificationType")
        self.TaskId = params.get("TaskId")
        if params.get("ProcessEofInfo") is not None:
            self.ProcessEofInfo = LiveStreamProcessErrorInfo()
            self.ProcessEofInfo._deserialize(params.get("ProcessEofInfo"))
        if params.get("AiReviewResultInfo") is not None:
            self.AiReviewResultInfo = LiveStreamAiReviewResultInfo()
            self.AiReviewResultInfo._deserialize(params.get("AiReviewResultInfo"))
        if params.get("AiRecognitionResultInfo") is not None:
            self.AiRecognitionResultInfo = LiveStreamAiRecognitionResultInfo()
            self.AiRecognitionResultInfo._deserialize(params.get("AiRecognitionResultInfo"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class ParseNotificationRequest(AbstractModel):
    """ParseNotification请求参数结构体

    """

    def __init__(self):
        """
        :param Content: 从 CMQ 获取到的事件通知内容。\n        :type Content: str\n        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseNotificationResponse(AbstractModel):
    """ParseNotification返回参数结构体

    """

    def __init__(self):
        """
        :param EventType: 支持事件类型，目前取值有：
<li>WorkflowTask：视频工作流处理任务。</li>
<li>EditMediaTask：视频编辑任务。</li>\n        :type EventType: str\n        :param WorkflowTaskEvent: 视频处理任务信息，仅当 TaskType 为 WorkflowTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type WorkflowTaskEvent: :class:`tencentcloud.mps.v20190612.models.WorkflowTask`\n        :param EditMediaTaskEvent: 视频编辑任务信息，仅当 TaskType 为 EditMediaTask，该字段有值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EditMediaTaskEvent: :class:`tencentcloud.mps.v20190612.models.EditMediaTask`\n        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长50个字符，不带或者带空字符串表示不做去重。\n        :type SessionId: str\n        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长1000个字符。\n        :type SessionContext: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EventType = None
        self.WorkflowTaskEvent = None
        self.EditMediaTaskEvent = None
        self.SessionId = None
        self.SessionContext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EventType = params.get("EventType")
        if params.get("WorkflowTaskEvent") is not None:
            self.WorkflowTaskEvent = WorkflowTask()
            self.WorkflowTaskEvent._deserialize(params.get("WorkflowTaskEvent"))
        if params.get("EditMediaTaskEvent") is not None:
            self.EditMediaTaskEvent = EditMediaTask()
            self.EditMediaTaskEvent._deserialize(params.get("EditMediaTaskEvent"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        self.RequestId = params.get("RequestId")


class PoliticalAsrReviewTemplateInfo(AbstractModel):
    """语音鉴政任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音鉴政任务开关，可选值：
<li>ON：开启语音鉴政任务；</li>
<li>OFF：关闭语音鉴政任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音鉴政任务开关，可选值：
<li>ON：开启语音鉴政任务；</li>
<li>OFF：关闭语音鉴政任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfo(AbstractModel):
    """鉴政任务控制参数

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴政控制参数。\n        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfo`\n        :param AsrReviewInfo: 语音鉴政控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfo`\n        :param OcrReviewInfo: 文本鉴政控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfo`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalConfigureInfoForUpdate(AbstractModel):
    """鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴政控制参数。\n        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalImgReviewTemplateInfoForUpdate`\n        :param AsrReviewInfo: 语音鉴政控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalAsrReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: 文本鉴政控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PoliticalOcrReviewTemplateInfoForUpdate`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PoliticalImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PoliticalAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PoliticalOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfo(AbstractModel):
    """画面鉴政任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 画面鉴政任务开关，可选值：
<li>ON：开启画面鉴政任务；</li>
<li>OFF：关闭画面鉴政任务。</li>\n        :type Switch: str\n        :param LabelSet: 画面鉴政过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>violation_photo：违规图标；</li>
<li>politician：政治人物；</li>
<li>entertainment：娱乐人物；</li>
<li>sport：体育人物；</li>
<li>entrepreneur：商业人物；</li>
<li>scholar：教育学者；</li>
<li>celebrity：知名人物；</li>
<li>military：军事人物。</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 97 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 95 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 画面鉴政任务开关，可选值：
<li>ON：开启画面鉴政任务；</li>
<li>OFF：关闭画面鉴政任务。</li>\n        :type Switch: str\n        :param LabelSet: 画面鉴政过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>violation_photo：违规图标；</li>
<li>politician：政治人物；</li>
<li>entertainment：娱乐人物；</li>
<li>sport：体育人物；</li>
<li>entrepreneur：商业人物；</li>
<li>scholar：教育学者；</li>
<li>celebrity：知名人物；</li>
<li>military：军事人物。</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfo(AbstractModel):
    """文本鉴政任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴政任务开关，可选值：
<li>ON：开启文本鉴政任务；</li>
<li>OFF：关闭文本鉴政任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PoliticalOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴政任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本鉴政任务开关，可选值：
<li>ON：开启文本鉴政任务；</li>
<li>OFF：关闭文本鉴政任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfo(AbstractModel):
    """语音鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音鉴黄任务开关，可选值：
<li>ON：开启语音鉴黄任务；</li>
<li>OFF：关闭语音鉴黄任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 语音鉴黄任务开关，可选值：
<li>ON：开启语音鉴黄任务；</li>
<li>OFF：关闭语音鉴黄任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfo(AbstractModel):
    """鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴黄控制参数。\n        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornImgReviewTemplateInfo`\n        :param AsrReviewInfo: 语音鉴黄控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornAsrReviewTemplateInfo`\n        :param OcrReviewInfo: 文本鉴黄控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornOcrReviewTemplateInfo`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornConfigureInfoForUpdate(AbstractModel):
    """鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴黄控制参数。\n        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornImgReviewTemplateInfoForUpdate`\n        :param AsrReviewInfo: 语音鉴黄控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornAsrReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: 文本鉴黄控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.PornOcrReviewTemplateInfoForUpdate`\n        """
        self.ImgReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = PornImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = PornAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = PornOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfo(AbstractModel):
    """画面鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 画面鉴黄任务开关，可选值：
<li>ON：开启画面鉴黄任务；</li>
<li>OFF：关闭画面鉴黄任务。</li>\n        :type Switch: str\n        :param LabelSet: 画面鉴黄过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：亲密行为；</li>
<li>sexy：性感。</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 90 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 0 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 画面鉴黄任务开关，可选值：
<li>ON：开启画面鉴黄任务；</li>
<li>OFF：关闭画面鉴黄任务。</li>\n        :type Switch: str\n        :param LabelSet: 画面鉴黄过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>porn：色情；</li>
<li>vulgar：低俗；</li>
<li>intimacy：亲密行为；</li>
<li>sexy：性感。</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfo(AbstractModel):
    """文本鉴黄任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴黄任务开关，可选值：
<li>ON：开启文本鉴黄任务；</li>
<li>OFF：关闭文本鉴黄任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PornOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴黄任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 文本鉴黄任务开关，可选值：
<li>ON：开启文本鉴黄任务；</li>
<li>OFF：关闭文本鉴黄任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessLiveStreamRequest(AbstractModel):
    """ProcessLiveStream请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 直播流 URL（必须是直播文件地址，支持 rtmp，hls 和 flv 等）。\n        :type Url: str\n        :param TaskNotifyConfig: 任务的事件通知信息，用于指定直播流处理的结果。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.LiveStreamTaskNotifyConfig`\n        :param OutputStorage: 直播流处理输出文件的目标存储。如处理有文件输出，该参数为必填项。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputDir: 直播流处理生成的文件输出的目标目录，如`/movie/201909/`，如果不填为 `/` 目录。\n        :type OutputDir: str\n        :param AiContentReviewTask: 视频内容审核类型任务参数。\n        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`\n        :param AiRecognitionTask: 视频内容识别类型任务参数。\n        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`\n        :param SessionId: 用于去重的识别码，如果七天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。\n        :type SessionId: str\n        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。\n        :type SessionContext: str\n        """
        self.Url = None
        self.TaskNotifyConfig = None
        self.OutputStorage = None
        self.OutputDir = None
        self.AiContentReviewTask = None
        self.AiRecognitionTask = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = LiveStreamTaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessLiveStreamResponse(AbstractModel):
    """ProcessLiveStream返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProcessMediaRequest(AbstractModel):
    """ProcessMedia请求参数结构体

    """

    def __init__(self):
        """
        :param InputInfo: 视频处理的文件输入信息。\n        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`\n        :param OutputStorage: 视频处理输出文件的目标存储。不填则继承 InputInfo 中的存储位置。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与 InputInfo 中文件所在的目录一致。\n        :type OutputDir: str\n        :param MediaProcessTask: 视频处理类型任务参数。\n        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: 视频内容审核类型任务参数。\n        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: 视频内容分析类型任务参数。\n        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: 视频内容识别类型任务参数。\n        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`\n        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`\n        :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。\n        :type TasksPriority: int\n        :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。\n        :type SessionId: str\n        :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。\n        :type SessionContext: str\n        """
        self.InputInfo = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TasksPriority = None
        self.SessionId = None
        self.SessionContext = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TasksPriority = params.get("TasksPriority")
        self.SessionId = params.get("SessionId")
        self.SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessMediaResponse(AbstractModel):
    """ProcessMedia返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProhibitedAsrReviewTemplateInfo(AbstractModel):
    """语音违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音违禁任务开关，可选值：
<li>ON：开启语音违禁任务；</li>
<li>OFF：关闭语音违禁任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedAsrReviewTemplateInfoForUpdate(AbstractModel):
    """语音违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 语音违禁任务开关，可选值：
<li>ON：开启语音违禁任务；</li>
<li>OFF：关闭语音违禁任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfo(AbstractModel):
    """违禁任务控制参数

    """

    def __init__(self):
        """
        :param AsrReviewInfo: 语音违禁控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfo`\n        :param OcrReviewInfo: 文本违禁控制参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfo`\n        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedConfigureInfoForUpdate(AbstractModel):
    """违禁任务控制参数

    """

    def __init__(self):
        """
        :param AsrReviewInfo: 语音违禁控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedAsrReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: 文本违禁控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.ProhibitedOcrReviewTemplateInfoForUpdate`\n        """
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = ProhibitedAsrReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = ProhibitedOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfo(AbstractModel):
    """文本违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本违禁任务开关，可选值：
<li>ON：开启文本违禁任务；</li>
<li>OFF：关闭文本违禁任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProhibitedOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本违禁任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本违禁任务开关，可选值：
<li>ON：开启文本违禁任务；</li>
<li>OFF：关闭文本违禁任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawImageWatermarkInput(AbstractModel):
    """图片水印模板输入参数

    """

    def __init__(self):
        """
        :param ImageContent: 水印图片的输入内容。支持 jpeg、png 图片格式。\n        :type ImageContent: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`\n        :param Width: 水印的宽度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Width 为视频宽度的百分比大小，如 10% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素。</li>
默认值：10%。\n        :type Width: str\n        :param Height: 水印的高度。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 Height 为视频高度的百分比大小，如 10% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素。</li>
默认值：0px，表示 Height 按照原始水印图片的宽高比缩放。\n        :type Height: str\n        :param RepeatType: 水印重复类型。使用场景：水印为动态图像。取值范围：
<li>once：动态水印播放完后，不再出现；</li>
<li>repeat_last_frame：水印播放完后，停留在最后一帧；</li>
<li>repeat：水印循环播放，直到视频结束（默认值）。</li>\n        :type RepeatType: str\n        """
        self.ImageContent = None
        self.Width = None
        self.Height = None
        self.RepeatType = None


    def _deserialize(self, params):
        if params.get("ImageContent") is not None:
            self.ImageContent = MediaInputInfo()
            self.ImageContent._deserialize(params.get("ImageContent"))
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.RepeatType = params.get("RepeatType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawTranscodeParameter(AbstractModel):
    """自定义转码的规格参数。

    """

    def __init__(self):
        """
        :param Container: 封装格式，可选值：mp4、flv、hls、mp3、flac、ogg、m4a。其中，mp3、flac、ogg、m4a 为纯音频文件。\n        :type Container: str\n        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。\n        :type RemoveVideo: int\n        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>
默认值：0。\n        :type RemoveAudio: int\n        :param VideoTemplate: 视频流配置参数，当 RemoveVideo 为 0，该字段必填。\n        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`\n        :param AudioTemplate: 音频流配置参数，当 RemoveAudio 为 0，该字段必填。\n        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`\n        :param TEHDConfig: 极速高清转码参数。\n        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`\n        """
        self.Container = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None


    def _deserialize(self, params):
        self.Container = params.get("Container")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RawWatermarkParameter(AbstractModel):
    """自定义水印规格参数。

    """

    def __init__(self):
        """
        :param Type: 水印类型，可选值：
<li>image：图片水印。</li>\n        :type Type: str\n        :param CoordinateOrigin: 原点位置，目前仅支持：
<li>TopLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角。</li>
默认值：TopLeft。\n        :type CoordinateOrigin: str\n        :param XPos: 水印原点距离视频图像坐标原点的水平位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 XPos 为视频宽度指定百分比，如 10% 表示 XPos 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 XPos 为指定像素，如 100px 表示 XPos 为 100 像素。</li>
默认值：0px。\n        :type XPos: str\n        :param YPos: 水印原点距离视频图像坐标原点的垂直位置。支持 %、px 两种格式：
<li>当字符串以 % 结尾，表示水印 YPos 为视频高度指定百分比，如 10% 表示 YPos 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 YPos 为指定像素，如 100px 表示 YPos 为 100 像素。</li>
默认值：0px。\n        :type YPos: str\n        :param ImageTemplate: 图片水印模板，当 Type 为 image，该字段必填。当 Type 为 text，该字段无效。\n        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.RawImageWatermarkInput`\n        """
        self.Type = None
        self.CoordinateOrigin = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = RawImageWatermarkInput()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMediaForZhiXueRequest(AbstractModel):
    """RecognizeMediaForZhiXue请求参数结构体

    """

    def __init__(self):
        """
        :param InputInfo: 输入媒体文件存储信息。\n        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`\n        :param ExpressionConfig: 表情识别参数配置。默认开启。\n        :type ExpressionConfig: :class:`tencentcloud.mps.v20190612.models.ExpressionConfigInfo`\n        :param ActionConfig: 动作识别参数配置。默认开启。\n        :type ActionConfig: :class:`tencentcloud.mps.v20190612.models.ActionConfigInfo`\n        """
        self.InputInfo = None
        self.ExpressionConfig = None
        self.ActionConfig = None


    def _deserialize(self, params):
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("ExpressionConfig") is not None:
            self.ExpressionConfig = ExpressionConfigInfo()
            self.ExpressionConfig._deserialize(params.get("ExpressionConfig"))
        if params.get("ActionConfig") is not None:
            self.ActionConfig = ActionConfigInfo()
            self.ActionConfig._deserialize(params.get("ActionConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognizeMediaForZhiXueResponse(AbstractModel):
    """RecognizeMediaForZhiXue返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID，可以通过该 ID 查询任务状态和结果。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetWorkflowRequest(AbstractModel):
    """ResetWorkflow请求参数结构体

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。\n        :type WorkflowId: int\n        :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。\n        :type WorkflowName: str\n        :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。\n        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`\n        :param OutputStorage: 视频处理的文件输出配置。不填则继承 Trigger 中的存储位置。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致，即`{inputDir}`。\n        :type OutputDir: str\n        :param MediaProcessTask: 视频处理类型任务参数。\n        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: 视频内容审核类型任务参数。\n        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: 视频内容分析类型任务参数。\n        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: 视频内容识别类型任务参数。\n        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`\n        :param TaskPriority: 工作流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。\n        :type TaskPriority: int\n        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`\n        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Trigger = None
        self.OutputStorage = None
        self.OutputDir = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskPriority = None
        self.TaskNotifyConfig = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputDir = params.get("OutputDir")
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        self.TaskPriority = params.get("TaskPriority")
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetWorkflowResponse(AbstractModel):
    """ResetWorkflow返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SampleSnapshotTaskInput(AbstractModel):
    """对视频做采样截图任务输入参数类型。

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板 ID。\n        :type Definition: int\n        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。\n        :type WatermarkSet: list of WatermarkInput\n        :param OutputStorage: 采样截图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 采样截图后图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_sampleSnapshot_{definition}_{number}.{format}`。\n        :type OutputObjectPath: str\n        :param ObjectNumberFormat: 采样截图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`\n        """
        self.Definition = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SampleSnapshotTemplate(AbstractModel):
    """采样截图模板详情

    """

    def __init__(self):
        """
        :param Definition: 采样截图模板唯一标识。\n        :type Definition: int\n        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param Name: 采样截图模板名称。\n        :type Name: str\n        :param Comment: 模板描述信息。\n        :type Comment: str\n        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 图片格式。\n        :type Format: str\n        :param SampleType: 采样截图类型。\n        :type SampleType: str\n        :param SampleInterval: 采样间隔。\n        :type SampleInterval: int\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。\n        :type FillType: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.SampleType = None
        self.SampleInterval = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.SampleType = params.get("SampleType")
        self.SampleInterval = params.get("SampleInterval")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTaskInput(AbstractModel):
    """对视频按指定时间点截图任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 指定时间点截图模板 ID。\n        :type Definition: int\n        :param ExtTimeOffsetSet: 截图时间点列表，时间点支持 s、% 两种格式：
<li>当字符串以 s 结尾，表示时间点单位为秒，如 3.5s 表示时间点为第3.5秒；</li>
<li>当字符串以 % 结尾，表示时间点为视频时长的百分比大小，如10%表示时间点为视频前第10%的时间。</li>\n        :type ExtTimeOffsetSet: list of str\n        :param TimeOffsetSet: 截图时间点列表，单位为<font color=red>秒</font>。此参数已不再建议使用，建议您使用 ExtTimeOffsetSet 参数。\n        :type TimeOffsetSet: list of float\n        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。\n        :type WatermarkSet: list of WatermarkInput\n        :param OutputStorage: 时间点截图后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 时间点截图后图片文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_snapshotByTimeOffset_{definition}_{number}.{format}`。\n        :type OutputObjectPath: str\n        :param ObjectNumberFormat: 时间点截图后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`\n        """
        self.Definition = None
        self.ExtTimeOffsetSet = None
        self.TimeOffsetSet = None
        self.WatermarkSet = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.ObjectNumberFormat = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.ExtTimeOffsetSet = params.get("ExtTimeOffsetSet")
        self.TimeOffsetSet = params.get("TimeOffsetSet")
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotByTimeOffsetTemplate(AbstractModel):
    """时间点截图模板详情

    """

    def __init__(self):
        """
        :param Definition: 时间点截图模板唯一标识。\n        :type Definition: int\n        :param Type: 模板类型，取值范围：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param Name: 时间点截图模板名称。\n        :type Name: str\n        :param Comment: 模板描述信息。\n        :type Comment: str\n        :param Width: 截图宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 截图高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Format: 图片格式。\n        :type Format: str\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>black：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>black：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊。</li>
默认值：black 。\n        :type FillType: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.Width = None
        self.Height = None
        self.ResolutionAdaptive = None
        self.Format = None
        self.CreateTime = None
        self.UpdateTime = None
        self.FillType = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Format = params.get("Format")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.FillType = params.get("FillType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInput(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        """
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。\n        :type Width: str\n        :param Height: 水印的高度，支持 px，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。</li>
默认值为 0px。\n        :type Height: str\n        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SvgWatermarkInputForUpdate(AbstractModel):
    """SVG水印模板输入参数

    """

    def __init__(self):
        """
        :param Width: 水印的宽度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Width 单位为像素，如 100px 表示 Width 为 100 像素；当填 0px 且
 Height 不为 0px 时，表示水印的宽度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的宽度取原始 SVG 图像的宽度；</li>
<li>当字符串以 W% 结尾，表示水印 Width 为视频宽度的百分比大小，如 10W% 表示 Width 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Width 为视频高度的百分比大小，如 10H% 表示 Width 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Width 为视频短边的百分比大小，如 10S% 表示 Width 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Width 为视频长边的百分比大小，如 10L% 表示 Width 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 W%。</li>
默认值为 10W%。\n        :type Width: str\n        :param Height: 水印的高度，支持 px，%，W%，H%，S%，L% 六种格式：
<li>当字符串以 px 结尾，表示水印 Height 单位为像素，如 100px 表示 Height 为 100 像素；当填 0px 且
 Width 不为 0px 时，表示水印的高度按原始 SVG 图像等比缩放；当 Width、Height 都填 0px 时，表示水印的高度取原始 SVG 图像的高度；</li>
<li>当字符串以 W% 结尾，表示水印 Height 为视频宽度的百分比大小，如 10W% 表示 Height 为视频宽度的 10%；</li>
<li>当字符串以 H% 结尾，表示水印 Height 为视频高度的百分比大小，如 10H% 表示 Height 为视频高度的 10%；</li>
<li>当字符串以 S% 结尾，表示水印 Height 为视频短边的百分比大小，如 10S% 表示 Height 为视频短边的 10%；</li>
<li>当字符串以 L% 结尾，表示水印 Height 为视频长边的百分比大小，如 10L% 表示 Height 为视频长边的 10%；</li>
<li>当字符串以 % 结尾时，含义同 H%。
默认值为 0px。\n        :type Height: str\n        """
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfig(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        """
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不启用极速高清。\n        :type Type: str\n        :param MaxVideoBitrate: 视频码率上限，当 Type 指定了极速高清类型时有效。
不填或填0表示不设视频码率上限。\n        :type MaxVideoBitrate: int\n        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TEHDConfigForUpdate(AbstractModel):
    """极速高清参数配置。

    """

    def __init__(self):
        """
        :param Type: 极速高清类型，可选值：
<li>TEHD-100：极速高清-100。</li>
不填代表不修改。\n        :type Type: str\n        :param MaxVideoBitrate: 视频码率上限，不填代表不修改。\n        :type MaxVideoBitrate: int\n        """
        self.Type = None
        self.MaxVideoBitrate = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MaxVideoBitrate = params.get("MaxVideoBitrate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfo(AbstractModel):
    """智能标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能标签任务开关，可选值：
<li>ON：开启智能标签任务；</li>
<li>OFF：关闭智能标签任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagConfigureInfoForUpdate(AbstractModel):
    """智能标签任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 智能标签任务开关，可选值：
<li>ON：开启智能标签任务；</li>
<li>OFF：关闭智能标签任务。</li>\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskNotifyConfig(AbstractModel):
    """任务的事件通知配置。

    """

    def __init__(self):
        """
        :param CmqModel: CMQ 的模型，有 Queue 和 Topic 两种，目前仅支持 Queue。\n        :type CmqModel: str\n        :param CmqRegion: CMQ 的园区，如 sh，bj 等。\n        :type CmqRegion: str\n        :param QueueName: 当模型为 Queue 时有效，表示接收事件通知的 CMQ 的队列名。\n        :type QueueName: str\n        :param TopicName: 当模型为 Topic 时有效，表示接收事件通知的 CMQ 的主题名。\n        :type TopicName: str\n        :param NotifyMode: 工作流通知的模式，可取值有 Finish 和 Change，不填代表 Finish。\n        :type NotifyMode: str\n        :param NotifyType: 通知类型，默认CMQ，指定URL时HTTP回调推送到 NotifyUrl 指定的地址。\n        :type NotifyType: str\n        :param NotifyUrl: HTTP回调地址，NotifyType为URL时必填。\n        :type NotifyUrl: str\n        """
        self.CmqModel = None
        self.CmqRegion = None
        self.QueueName = None
        self.TopicName = None
        self.NotifyMode = None
        self.NotifyType = None
        self.NotifyUrl = None


    def _deserialize(self, params):
        self.CmqModel = params.get("CmqModel")
        self.CmqRegion = params.get("CmqRegion")
        self.QueueName = params.get("QueueName")
        self.TopicName = params.get("TopicName")
        self.NotifyMode = params.get("NotifyMode")
        self.NotifyType = params.get("NotifyType")
        self.NotifyUrl = params.get("NotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutputStorage(AbstractModel):
    """视频处理输出对象信息。

    """

    def __init__(self):
        """
        :param Type: 视频处理输出对象存储位置的类型，现在仅支持 COS。\n        :type Type: str\n        :param CosOutputStorage: 当 Type 为 COS 时有效，则该项为必填，表示视频处理 COS 输出位置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosOutputStorage: :class:`tencentcloud.mps.v20190612.models.CosOutputStorage`\n        """
        self.Type = None
        self.CosOutputStorage = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosOutputStorage") is not None:
            self.CosOutputStorage = CosOutputStorage()
            self.CosOutputStorage._deserialize(params.get("CosOutputStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskSimpleInfo(AbstractModel):
    """任务概要信息

    """

    def __init__(self):
        """
        :param TaskId: 任务 ID。\n        :type TaskId: str\n        :param TaskType: 任务类型，包含：
<li> WorkflowTask：工作流处理任务；</li>
<li> EditMediaTask：视频编辑任务；</li>
<li> LiveProcessTask：直播处理任务。</li>\n        :type TaskType: str\n        :param CreateTime: 任务创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param BeginProcessTime: 任务开始执行时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。若任务尚未开始，该字段为：0000-00-00T00:00:00Z。\n        :type BeginProcessTime: str\n        :param FinishTime: 任务结束时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。若任务尚未完成，该字段为：0000-00-00T00:00:00Z。\n        :type FinishTime: str\n        """
        self.TaskId = None
        self.TaskType = None
        self.CreateTime = None
        self.BeginProcessTime = None
        self.FinishTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.CreateTime = params.get("CreateTime")
        self.BeginProcessTime = params.get("BeginProcessTime")
        self.FinishTime = params.get("FinishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfo(AbstractModel):
    """鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴恐任务控制参数。\n        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfo`\n        :param OcrReviewInfo: 文本鉴恐任务控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfo`\n        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfo()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismConfigureInfoForUpdate(AbstractModel):
    """鉴恐任务控制参数。

    """

    def __init__(self):
        """
        :param ImgReviewInfo: 画面鉴恐任务控制参数。\n        :type ImgReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismImgReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: 文本鉴恐任务控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.TerrorismOcrReviewTemplateInfoForUpdate`\n        """
        self.ImgReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("ImgReviewInfo") is not None:
            self.ImgReviewInfo = TerrorismImgReviewTemplateInfoForUpdate()
            self.ImgReviewInfo._deserialize(params.get("ImgReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = TerrorismOcrReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfo(AbstractModel):
    """画面鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 画面鉴恐任务开关，可选值：
<li>ON：开启画面鉴恐任务；</li>
<li>OFF：关闭画面鉴恐任务。</li>\n        :type Switch: str\n        :param LabelSet: 画面鉴恐过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>guns：武器枪支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥画面；</li>
<li>police：警察部队；</li>
<li>banners：暴恐旗帜；</li>
<li>militant：武装分子；</li>
<li>explosion：爆炸火灾；</li>
<li>terrorists：暴恐人物；</li>
<li>scenario：暴恐画面。</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 90 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 80 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismImgReviewTemplateInfoForUpdate(AbstractModel):
    """画面鉴恐任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 画面鉴恐任务开关，可选值：
<li>ON：开启画面鉴恐任务；</li>
<li>OFF：关闭画面鉴恐任务。</li>\n        :type Switch: str\n        :param LabelSet: 画面鉴恐过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回，可选值为：
<li>guns：武器枪支；</li>
<li>crowd：人群聚集；</li>
<li>bloody：血腥画面；</li>
<li>police：警察部队；</li>
<li>banners：暴恐旗帜；</li>
<li>militant：武装分子；</li>
<li>explosion：爆炸火灾；</li>
<li>terrorists：暴恐人物；</li>
<li>scenario：暴恐画面。</li>\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfo(AbstractModel):
    """文本鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴恐任务开关，可选值：
<li>ON：开启文本鉴恐任务；</li>
<li>OFF：关闭文本鉴恐任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerrorismOcrReviewTemplateInfoForUpdate(AbstractModel):
    """文本鉴恐任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 文本鉴恐任务开关，可选值：
<li>ON：开启文本鉴恐任务；</li>
<li>OFF：关闭文本鉴恐任务。</li>\n        :type Switch: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInput(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>\n        :type FontType: str\n        :param FontSize: 字体大小，格式：Npx，N 为数值。\n        :type FontSize: str\n        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。\n        :type FontColor: str\n        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>
默认值：1。\n        :type FontAlpha: float\n        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWatermarkTemplateInputForUpdate(AbstractModel):
    """文字水印模板

    """

    def __init__(self):
        """
        :param FontType: 字体类型，目前可以支持两种：
<li>simkai.ttf：可以支持中文和英文；</li>
<li>arial.ttf：仅支持英文。</li>\n        :type FontType: str\n        :param FontSize: 字体大小，格式：Npx，N 为数值。\n        :type FontSize: str\n        :param FontColor: 字体颜色，格式：0xRRGGBB，默认值：0xFFFFFF（白色）。\n        :type FontColor: str\n        :param FontAlpha: 文字透明度，取值范围：(0, 1]
<li>0：完全透明</li>
<li>1：完全不透明</li>\n        :type FontAlpha: float\n        """
        self.FontType = None
        self.FontSize = None
        self.FontColor = None
        self.FontAlpha = None


    def _deserialize(self, params):
        self.FontType = params.get("FontType")
        self.FontSize = params.get("FontSize")
        self.FontColor = params.get("FontColor")
        self.FontAlpha = params.get("FontAlpha")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTaskInput(AbstractModel):
    """转码任务输入参数类型

    """

    def __init__(self):
        """
        :param Definition: 视频转码模板 ID。\n        :type Definition: int\n        :param RawParameter: 视频转码自定义参数，当 Definition 填 0 时有效。
该参数用于高度定制场景，建议您优先使用 Definition 指定转码参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RawParameter: :class:`tencentcloud.mps.v20190612.models.RawTranscodeParameter`\n        :param OverrideParameter: 视频转码自定义参数，当 Definition 不填 0 时有效。
当填写了该结构中的部分转码参数时，将使用填写的参数覆盖转码模板中的参数。
该参数用于高度定制场景，建议您仅使用 Definition 指定转码参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OverrideParameter: :class:`tencentcloud.mps.v20190612.models.OverrideTranscodeParameter`\n        :param WatermarkSet: 水印列表，支持多张图片或文字水印，最大可支持 10 张。
注意：此字段可能返回 null，表示取不到有效值。\n        :type WatermarkSet: list of WatermarkInput\n        :param MosaicSet: 马赛克列表，最大可支持 10 张。\n        :type MosaicSet: list of MosaicInput\n        :param StartTimeOffset: 转码后的视频的起始时间偏移，单位：秒。
<li>不填或填0，表示转码后的视频从原始视频的起始位置开始；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频从原始视频的第 n 秒位置开始；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频从原始视频结束 n 秒前的位置开始。</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 转码后视频的终止时间偏移，单位：秒。
<li>不填或填0，表示转码后的视频持续到原始视频的末尾终止；</li>
<li>当数值大于0时（假设为 n），表示转码后的视频持续到原始视频第 n 秒时终止；</li>
<li>当数值小于0时（假设为 -n），表示转码后的视频持续到原始视频结束 n 秒前终止。</li>\n        :type EndTimeOffset: float\n        :param OutputStorage: 转码后文件的目标存储，不填则继承上层的 OutputStorage 值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param OutputObjectPath: 转码后主文件的输出路径，可以为相对路径或者绝对路径。如果不填，则默认为相对路径：`{inputName}_transcode_{definition}.{format}`。\n        :type OutputObjectPath: str\n        :param SegmentObjectName: 转码后分片文件的输出路径（转码 HLS 时 ts 的路径），只能为相对路径。如果不填，则默认为：`{inputName}_transcode_{definition}_{number}.{format}`。\n        :type SegmentObjectName: str\n        :param ObjectNumberFormat: 转码后输出路径中的`{number}`变量的规则。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ObjectNumberFormat: :class:`tencentcloud.mps.v20190612.models.NumberFormat`\n        :param HeadTailParameter: 片头片尾参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeadTailParameter: :class:`tencentcloud.mps.v20190612.models.HeadTailParameter`\n        """
        self.Definition = None
        self.RawParameter = None
        self.OverrideParameter = None
        self.WatermarkSet = None
        self.MosaicSet = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None
        self.OutputStorage = None
        self.OutputObjectPath = None
        self.SegmentObjectName = None
        self.ObjectNumberFormat = None
        self.HeadTailParameter = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawTranscodeParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        if params.get("OverrideParameter") is not None:
            self.OverrideParameter = OverrideTranscodeParameter()
            self.OverrideParameter._deserialize(params.get("OverrideParameter"))
        if params.get("WatermarkSet") is not None:
            self.WatermarkSet = []
            for item in params.get("WatermarkSet"):
                obj = WatermarkInput()
                obj._deserialize(item)
                self.WatermarkSet.append(obj)
        if params.get("MosaicSet") is not None:
            self.MosaicSet = []
            for item in params.get("MosaicSet"):
                obj = MosaicInput()
                obj._deserialize(item)
                self.MosaicSet.append(obj)
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        self.OutputObjectPath = params.get("OutputObjectPath")
        self.SegmentObjectName = params.get("SegmentObjectName")
        if params.get("ObjectNumberFormat") is not None:
            self.ObjectNumberFormat = NumberFormat()
            self.ObjectNumberFormat._deserialize(params.get("ObjectNumberFormat"))
        if params.get("HeadTailParameter") is not None:
            self.HeadTailParameter = HeadTailParameter()
            self.HeadTailParameter._deserialize(params.get("HeadTailParameter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTemplate(AbstractModel):
    """转码模板详情

    """

    def __init__(self):
        """
        :param Definition: 转码模板唯一标识。\n        :type Definition: str\n        :param Container: 封装格式，取值：mp4、flv、hls、mp3、flac、ogg。\n        :type Container: str\n        :param Name: 转码模板名称。\n        :type Name: str\n        :param Comment: 模板描述信息。\n        :type Comment: str\n        :param Type: 模板类型，取值：
<li>Preset：系统预置模板；</li>
<li>Custom：用户自定义模板。</li>\n        :type Type: str\n        :param RemoveVideo: 是否去除视频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>\n        :type RemoveVideo: int\n        :param RemoveAudio: 是否去除音频数据，取值：
<li>0：保留；</li>
<li>1：去除。</li>\n        :type RemoveAudio: int\n        :param VideoTemplate: 视频流配置参数，仅当 RemoveVideo 为 0，该字段有效。\n        :type VideoTemplate: :class:`tencentcloud.mps.v20190612.models.VideoTemplateInfo`\n        :param AudioTemplate: 音频流配置参数，仅当 RemoveAudio 为 0，该字段有效 。\n        :type AudioTemplate: :class:`tencentcloud.mps.v20190612.models.AudioTemplateInfo`\n        :param TEHDConfig: 极速高清转码参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TEHDConfig: :class:`tencentcloud.mps.v20190612.models.TEHDConfig`\n        :param ContainerType: 封装格式过滤条件，可选值：
<li>Video：视频格式，可以同时包含视频流和音频流的封装格式；</li>
<li>PureAudio：纯音频格式，只能包含音频流的封装格式板。</li>\n        :type ContainerType: str\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.Definition = None
        self.Container = None
        self.Name = None
        self.Comment = None
        self.Type = None
        self.RemoveVideo = None
        self.RemoveAudio = None
        self.VideoTemplate = None
        self.AudioTemplate = None
        self.TEHDConfig = None
        self.ContainerType = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Container = params.get("Container")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.Type = params.get("Type")
        self.RemoveVideo = params.get("RemoveVideo")
        self.RemoveAudio = params.get("RemoveAudio")
        if params.get("VideoTemplate") is not None:
            self.VideoTemplate = VideoTemplateInfo()
            self.VideoTemplate._deserialize(params.get("VideoTemplate"))
        if params.get("AudioTemplate") is not None:
            self.AudioTemplate = AudioTemplateInfo()
            self.AudioTemplate._deserialize(params.get("AudioTemplate"))
        if params.get("TEHDConfig") is not None:
            self.TEHDConfig = TEHDConfig()
            self.TEHDConfig._deserialize(params.get("TEHDConfig"))
        self.ContainerType = params.get("ContainerType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlInputInfo(AbstractModel):
    """视频处理 URL 对象信息。

    """

    def __init__(self):
        """
        :param Url: 视频的 URL。\n        :type Url: str\n        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfo(AbstractModel):
    """用户自定义语音审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定语音审核任务开关，可选值：
<li>ON：开启自定义语音审核任务；</li>
<li>OFF：关闭自定义语音审核任务。</li>\n        :type Switch: str\n        :param LabelSet: 用户自定义语音过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义语音关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineAsrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义语音审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定语音审核任务开关，可选值：
<li>ON：开启自定义语音审核任务；</li>
<li>OFF：关闭自定义语音审核任务。</li>\n        :type Switch: str\n        :param LabelSet: 用户自定义语音过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义语音关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfo(AbstractModel):
    """用户自定义审核任务控制参数

    """

    def __init__(self):
        """
        :param FaceReviewInfo: 用户自定义人物审核控制参数。\n        :type FaceReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfo`\n        :param AsrReviewInfo: 用户自定义语音审核控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfo`\n        :param OcrReviewInfo: 用户自定义文本审核控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfo`\n        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfo()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfo()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfo()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineConfigureInfoForUpdate(AbstractModel):
    """用户自定义审核任务控制参数。

    """

    def __init__(self):
        """
        :param FaceReviewInfo: 用户自定义人物审核控制参数。\n        :type FaceReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineFaceReviewTemplateInfoForUpdate`\n        :param AsrReviewInfo: 用户自定义语音审核控制参数。\n        :type AsrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineAsrTextReviewTemplateInfoForUpdate`\n        :param OcrReviewInfo: 用户自定义文本审核控制参数。\n        :type OcrReviewInfo: :class:`tencentcloud.mps.v20190612.models.UserDefineOcrTextReviewTemplateInfoForUpdate`\n        """
        self.FaceReviewInfo = None
        self.AsrReviewInfo = None
        self.OcrReviewInfo = None


    def _deserialize(self, params):
        if params.get("FaceReviewInfo") is not None:
            self.FaceReviewInfo = UserDefineFaceReviewTemplateInfoForUpdate()
            self.FaceReviewInfo._deserialize(params.get("FaceReviewInfo"))
        if params.get("AsrReviewInfo") is not None:
            self.AsrReviewInfo = UserDefineAsrTextReviewTemplateInfoForUpdate()
            self.AsrReviewInfo._deserialize(params.get("AsrReviewInfo"))
        if params.get("OcrReviewInfo") is not None:
            self.OcrReviewInfo = UserDefineOcrTextReviewTemplateInfoForUpdate()
            self.OcrReviewInfo._deserialize(params.get("OcrReviewInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfo(AbstractModel):
    """用户自定义人物审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定义人物审核任务开关，可选值：
<li>ON：开启自定义人物审核任务；</li>
<li>OFF：关闭自定义人物审核任务。</li>\n        :type Switch: str\n        :param LabelSet: 用户自定义人物过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义人物库的时，需要添加对应人物标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 97 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 95 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineFaceReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义人物审核任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 用户自定义人物审核任务开关，可选值：
<li>ON：开启自定义人物审核任务；</li>
<li>OFF：关闭自定义人物审核任务。</li>\n        :type Switch: str\n        :param LabelSet: 用户自定义人物过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义人物库的时，需要添加对应人物标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfo(AbstractModel):
    """用户自定义文本审核任务控制参数

    """

    def __init__(self):
        """
        :param Switch: 用户自定文本审核任务开关，可选值：
<li>ON：开启自定义文本审核任务；</li>
<li>OFF：关闭自定义文本审核任务。</li>\n        :type Switch: str\n        :param LabelSet: 用户自定义文本过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义文本关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: list of str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规，不填默认为 100 分。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核，不填默认为 75 分。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefineOcrTextReviewTemplateInfoForUpdate(AbstractModel):
    """用户自定义文本审核任务控制参数。

    """

    def __init__(self):
        """
        :param Switch: 用户自定文本审核任务开关，可选值：
<li>ON：开启自定义文本审核任务；</li>
<li>OFF：关闭自定义文本审核任务。</li>\n        :type Switch: str\n        :param LabelSet: 用户自定义文本过滤标签，审核结果包含选择的标签则返回结果，如果过滤标签为空，则审核结果全部返回。如果要使用标签过滤功能，添加自定义文本关键词素材时需要添加对应标签。
标签个数最多 10 个，每个标签长度最多 16 个字符。\n        :type LabelSet: str\n        :param BlockConfidence: 判定涉嫌违规的分数阈值，当智能审核达到该分数以上，认为涉嫌违规。取值范围：0~100。\n        :type BlockConfidence: int\n        :param ReviewConfidence: 判定需人工复核是否违规的分数阈值，当智能审核达到该分数以上，认为需人工复核。取值范围：0~100。\n        :type ReviewConfidence: int\n        """
        self.Switch = None
        self.LabelSet = None
        self.BlockConfidence = None
        self.ReviewConfidence = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.LabelSet = params.get("LabelSet")
        self.BlockConfidence = params.get("BlockConfidence")
        self.ReviewConfidence = params.get("ReviewConfidence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfo(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
<li>av1：AOMedia Video 1 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。av1 编码容器目前只支持 mp4 。\n        :type Codec: str\n        :param Fps: 视频帧率，取值范围：[0, 100]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。\n        :type Fps: int\n        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。\n        :type Bitrate: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>
默认值：open。\n        :type ResolutionAdaptive: str\n        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Width: int\n        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>
默认值：0。\n        :type Height: int\n        :param Gop: 关键帧 I 帧之间的间隔，取值范围：0 和 [1, 100000]，单位：帧数。
当填 0 或不填时，系统将自动设置 gop 长度。\n        :type Gop: int\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊填充。</li>
默认值：black 。\n        :type FillType: str\n        :param Vcrf: 视频恒定码率控制因子，取值范围为[1, 51]。
如果指定该参数，将使用 CRF 的码率控制方式做转码（视频码率将不再生效）。
如果没有特殊需求，不建议指定该参数。\n        :type Vcrf: int\n        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None
        self.Vcrf = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfoForUpdate(AbstractModel):
    """视频流配置参数

    """

    def __init__(self):
        """
        :param Codec: 视频流的编码格式，可选值：
<li>libx264：H.264 编码</li>
<li>libx265：H.265 编码</li>
<li>av1：AOMedia Video 1 编码</li>
目前 H.265 编码必须指定分辨率，并且需要在 640*480 以内。av1 编码容器目前只支持 mp4 。\n        :type Codec: str\n        :param Fps: 视频帧率，取值范围：[0, 100]，单位：Hz。
当取值为 0，表示帧率和原始视频保持一致。\n        :type Fps: int\n        :param Bitrate: 视频流的码率，取值范围：0 和 [128, 35000]，单位：kbps。
当取值为 0，表示视频码率和原始视频保持一致。\n        :type Bitrate: int\n        :param ResolutionAdaptive: 分辨率自适应，可选值：
<li>open：开启，此时，Width 代表视频的长边，Height 表示视频的短边；</li>
<li>close：关闭，此时，Width 代表视频的宽度，Height 表示视频的高度。</li>\n        :type ResolutionAdaptive: str\n        :param Width: 视频流宽度（或长边）的最大值，取值范围：0 和 [128, 4096]，单位：px。
<li>当 Width、Height 均为 0，则分辨率同源；</li>
<li>当 Width 为 0，Height 非 0，则 Width 按比例缩放；</li>
<li>当 Width 非 0，Height 为 0，则 Height 按比例缩放；</li>
<li>当 Width、Height 均非 0，则分辨率按用户指定。</li>\n        :type Width: int\n        :param Height: 视频流高度（或短边）的最大值，取值范围：0 和 [128, 4096]，单位：px。\n        :type Height: int\n        :param Gop: 关键帧 I 帧之间的间隔，取值范围：0 和 [1, 100000]，单位：帧数。当填 0 时，系统将自动设置 gop 长度。\n        :type Gop: int\n        :param FillType: 填充方式，当视频流配置宽高参数与原始视频的宽高比不一致时，对转码的处理方式，即为“填充”。可选填充方式：
<li> stretch：拉伸，对每一帧进行拉伸，填满整个画面，可能导致转码后的视频被“压扁“或者“拉长“；</li>
<li>black：留黑，保持视频宽高比不变，边缘剩余部分使用黑色填充。</li>
<li>white：留白，保持视频宽高比不变，边缘剩余部分使用白色填充。</li>
<li>gauss：高斯模糊，保持视频宽高比不变，边缘剩余部分使用高斯模糊填充。</li>\n        :type FillType: str\n        :param Vcrf: 视频恒定码率控制因子。取值范围为[0, 51]，填0表示禁用该参数。
如果没有特殊需求，不建议指定该参数。\n        :type Vcrf: int\n        """
        self.Codec = None
        self.Fps = None
        self.Bitrate = None
        self.ResolutionAdaptive = None
        self.Width = None
        self.Height = None
        self.Gop = None
        self.FillType = None
        self.Vcrf = None


    def _deserialize(self, params):
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")
        self.Bitrate = params.get("Bitrate")
        self.ResolutionAdaptive = params.get("ResolutionAdaptive")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Gop = params.get("Gop")
        self.FillType = params.get("FillType")
        self.Vcrf = params.get("Vcrf")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkInput(AbstractModel):
    """视频处理任务中的水印参数类型

    """

    def __init__(self):
        """
        :param Definition: 水印模板 ID。\n        :type Definition: int\n        :param RawParameter: 水印自定义参数，当 Definition 填 0 时有效。
该参数用于高度定制场景，建议您优先使用 Definition 指定水印参数。
水印自定义参数不支持截图打水印。\n        :type RawParameter: :class:`tencentcloud.mps.v20190612.models.RawWatermarkParameter`\n        :param TextContent: 文字内容，长度不超过100个字符。仅当水印类型为文字水印时填写。
文字水印不支持截图打水印。\n        :type TextContent: str\n        :param SvgContent: SVG 内容。长度不超过 2000000 个字符。仅当水印类型为 SVG 水印时填写。
SVG 水印不支持截图打水印。\n        :type SvgContent: str\n        :param StartTimeOffset: 水印的起始时间偏移，单位：秒。不填或填0，表示水印从画面出现时开始显现。
<li>不填或填0，表示水印从画面开始就出现；</li>
<li>当数值大于0时（假设为 n），表示水印从画面开始的第 n 秒出现；</li>
<li>当数值小于0时（假设为 -n），表示水印从离画面结束 n 秒前开始出现。</li>\n        :type StartTimeOffset: float\n        :param EndTimeOffset: 水印的结束时间偏移，单位：秒。
<li>不填或填0，表示水印持续到画面结束；</li>
<li>当数值大于0时（假设为 n），表示水印持续到第 n 秒时消失；</li>
<li>当数值小于0时（假设为 -n），表示水印持续到离画面结束 n 秒前消失。</li>\n        :type EndTimeOffset: float\n        """
        self.Definition = None
        self.RawParameter = None
        self.TextContent = None
        self.SvgContent = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        if params.get("RawParameter") is not None:
            self.RawParameter = RawWatermarkParameter()
            self.RawParameter._deserialize(params.get("RawParameter"))
        self.TextContent = params.get("TextContent")
        self.SvgContent = params.get("SvgContent")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WatermarkTemplate(AbstractModel):
    """水印模板详情

    """

    def __init__(self):
        """
        :param Definition: 水印模板唯一标识。\n        :type Definition: int\n        :param Type: 水印类型，取值：
<li>image：图片水印；</li>
<li>text：文字水印。</li>\n        :type Type: str\n        :param Name: 水印模板名称。\n        :type Name: str\n        :param Comment: 模板描述信息。\n        :type Comment: str\n        :param XPos: 水印图片原点距离视频图像原点的水平位置。
<li>当字符串以 % 结尾，表示水印 Left 为视频宽度指定百分比的位置，如 10% 表示 Left 为视频宽度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Left 为视频宽度指定像素的位置，如 100px 表示 Left 为 100 像素。</li>\n        :type XPos: str\n        :param YPos: 水印图片原点距离视频图像原点的垂直位置。
<li>当字符串以 % 结尾，表示水印 Top 为视频高度指定百分比的位置，如 10% 表示 Top 为视频高度的 10%；</li>
<li>当字符串以 px 结尾，表示水印 Top 为视频高度指定像素的位置，如 100px 表示 Top 为 100 像素。</li>\n        :type YPos: str\n        :param ImageTemplate: 图片水印模板，仅当 Type 为 image，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageTemplate: :class:`tencentcloud.mps.v20190612.models.ImageWatermarkTemplate`\n        :param TextTemplate: 文字水印模板，仅当 Type 为 text，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TextTemplate: :class:`tencentcloud.mps.v20190612.models.TextWatermarkTemplateInput`\n        :param SvgTemplate: SVG 水印模板，当 Type 为 svg，该字段有效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SvgTemplate: :class:`tencentcloud.mps.v20190612.models.SvgWatermarkInput`\n        :param CreateTime: 模板创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 模板最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        :param CoordinateOrigin: 原点位置，可选值：
<li>topLeft：表示坐标原点位于视频图像左上角，水印原点为图片或文字的左上角；</li>
<li>topRight：表示坐标原点位于视频图像的右上角，水印原点为图片或文字的右上角；</li>
<li>bottomLeft：表示坐标原点位于视频图像的左下角，水印原点为图片或文字的左下角；</li>
<li>bottomRight：表示坐标原点位于视频图像的右下角，水印原点为图片或文字的右下。；</li>\n        :type CoordinateOrigin: str\n        """
        self.Definition = None
        self.Type = None
        self.Name = None
        self.Comment = None
        self.XPos = None
        self.YPos = None
        self.ImageTemplate = None
        self.TextTemplate = None
        self.SvgTemplate = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CoordinateOrigin = None


    def _deserialize(self, params):
        self.Definition = params.get("Definition")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.Comment = params.get("Comment")
        self.XPos = params.get("XPos")
        self.YPos = params.get("YPos")
        if params.get("ImageTemplate") is not None:
            self.ImageTemplate = ImageWatermarkTemplate()
            self.ImageTemplate._deserialize(params.get("ImageTemplate"))
        if params.get("TextTemplate") is not None:
            self.TextTemplate = TextWatermarkTemplateInput()
            self.TextTemplate._deserialize(params.get("TextTemplate"))
        if params.get("SvgTemplate") is not None:
            self.SvgTemplate = SvgWatermarkInput()
            self.SvgTemplate._deserialize(params.get("SvgTemplate"))
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CoordinateOrigin = params.get("CoordinateOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowInfo(AbstractModel):
    """工作流信息详情。

    """

    def __init__(self):
        """
        :param WorkflowId: 工作流 ID。\n        :type WorkflowId: int\n        :param WorkflowName: 工作流名称。\n        :type WorkflowName: str\n        :param Status: 工作流状态，取值范围：
<li>Enabled：已启用，</li>
<li>Disabled：已禁用。</li>\n        :type Status: str\n        :param Trigger: 工作流绑定的输入规则，当上传视频命中该规则到该对象时即触发工作流。\n        :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`\n        :param OutputStorage: 视频处理的文件输出存储位置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`\n        :param MediaProcessTask: 视频处理类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`\n        :param AiContentReviewTask: 视频内容审核类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`\n        :param AiAnalysisTask: 视频内容分析类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`\n        :param AiRecognitionTask: 视频内容识别类型任务参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`\n        :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`\n        :param TaskPriority: 任务流的优先级，数值越大优先级越高，取值范围是 -10 到 10，不填代表 0。\n        :type TaskPriority: int\n        :param OutputDir: 视频处理生成的文件输出的目标目录，如`/movie/201907/`。\n        :type OutputDir: str\n        :param CreateTime: 工作流创建时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type CreateTime: str\n        :param UpdateTime: 工作流最后修改时间，使用 [ISO 日期格式](https://cloud.tencent.com/document/product/862/37710#52)。\n        :type UpdateTime: str\n        """
        self.WorkflowId = None
        self.WorkflowName = None
        self.Status = None
        self.Trigger = None
        self.OutputStorage = None
        self.MediaProcessTask = None
        self.AiContentReviewTask = None
        self.AiAnalysisTask = None
        self.AiRecognitionTask = None
        self.TaskNotifyConfig = None
        self.TaskPriority = None
        self.OutputDir = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.WorkflowId = params.get("WorkflowId")
        self.WorkflowName = params.get("WorkflowName")
        self.Status = params.get("Status")
        if params.get("Trigger") is not None:
            self.Trigger = WorkflowTrigger()
            self.Trigger._deserialize(params.get("Trigger"))
        if params.get("OutputStorage") is not None:
            self.OutputStorage = TaskOutputStorage()
            self.OutputStorage._deserialize(params.get("OutputStorage"))
        if params.get("MediaProcessTask") is not None:
            self.MediaProcessTask = MediaProcessTaskInput()
            self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
        if params.get("AiContentReviewTask") is not None:
            self.AiContentReviewTask = AiContentReviewTaskInput()
            self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
        if params.get("AiAnalysisTask") is not None:
            self.AiAnalysisTask = AiAnalysisTaskInput()
            self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
        if params.get("AiRecognitionTask") is not None:
            self.AiRecognitionTask = AiRecognitionTaskInput()
            self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
        if params.get("TaskNotifyConfig") is not None:
            self.TaskNotifyConfig = TaskNotifyConfig()
            self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
        self.TaskPriority = params.get("TaskPriority")
        self.OutputDir = params.get("OutputDir")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTask(AbstractModel):
    """视频处理任务信息

    """

    def __init__(self):
        """
        :param TaskId: 视频处理任务 ID。\n        :type TaskId: str\n        :param Status: 任务流状态，取值：
<li>PROCESSING：处理中；</li>
<li>FINISH：已完成。</li>\n        :type Status: str\n        :param ErrCode: 已弃用，请使用各个具体任务的 ErrCode。\n        :type ErrCode: int\n        :param Message: 已弃用，请使用各个具体任务的 Message。\n        :type Message: str\n        :param InputInfo: 视频处理的目标文件信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`\n        :param MetaData: 原始视频的元信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`\n        :param MediaProcessResultSet: 视频处理任务的执行状态与结果。\n        :type MediaProcessResultSet: list of MediaProcessTaskResult\n        :param AiContentReviewResultSet: 视频内容审核任务的执行状态与结果。\n        :type AiContentReviewResultSet: list of AiContentReviewResult\n        :param AiAnalysisResultSet: 视频内容分析任务的执行状态与结果。\n        :type AiAnalysisResultSet: list of AiAnalysisResult\n        :param AiRecognitionResultSet: 视频内容识别任务的执行状态与结果。\n        :type AiRecognitionResultSet: list of AiRecognitionResult\n        """
        self.TaskId = None
        self.Status = None
        self.ErrCode = None
        self.Message = None
        self.InputInfo = None
        self.MetaData = None
        self.MediaProcessResultSet = None
        self.AiContentReviewResultSet = None
        self.AiAnalysisResultSet = None
        self.AiRecognitionResultSet = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.Message = params.get("Message")
        if params.get("InputInfo") is not None:
            self.InputInfo = MediaInputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("MediaProcessResultSet") is not None:
            self.MediaProcessResultSet = []
            for item in params.get("MediaProcessResultSet"):
                obj = MediaProcessTaskResult()
                obj._deserialize(item)
                self.MediaProcessResultSet.append(obj)
        if params.get("AiContentReviewResultSet") is not None:
            self.AiContentReviewResultSet = []
            for item in params.get("AiContentReviewResultSet"):
                obj = AiContentReviewResult()
                obj._deserialize(item)
                self.AiContentReviewResultSet.append(obj)
        if params.get("AiAnalysisResultSet") is not None:
            self.AiAnalysisResultSet = []
            for item in params.get("AiAnalysisResultSet"):
                obj = AiAnalysisResult()
                obj._deserialize(item)
                self.AiAnalysisResultSet.append(obj)
        if params.get("AiRecognitionResultSet") is not None:
            self.AiRecognitionResultSet = []
            for item in params.get("AiRecognitionResultSet"):
                obj = AiRecognitionResult()
                obj._deserialize(item)
                self.AiRecognitionResultSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkflowTrigger(AbstractModel):
    """输入规则，当上传视频命中该规则时，即触发工作流。

    """

    def __init__(self):
        """
        :param Type: 触发器的类型，目前仅支持 CosFileUpload。\n        :type Type: str\n        :param CosFileUploadTrigger: 当 Type 为 CosFileUpload 时必填且有效，为 COS 触发规则。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosFileUploadTrigger: :class:`tencentcloud.mps.v20190612.models.CosFileUploadTrigger`\n        """
        self.Type = None
        self.CosFileUploadTrigger = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosFileUploadTrigger") is not None:
            self.CosFileUploadTrigger = CosFileUploadTrigger()
            self.CosFileUploadTrigger._deserialize(params.get("CosFileUploadTrigger"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        