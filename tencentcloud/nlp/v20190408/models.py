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


class AnalyzeSentimentRequest(AbstractModel):
    """AnalyzeSentiment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（仅支持UTF-8格式，不超过200字）。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeSentimentResponse(AbstractModel):
    """AnalyzeSentiment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Positive: 正面情感概率。
        :type Positive: float
        :param _Neutral: 中性情感概率。
        :type Neutral: float
        :param _Negative: 负面情感概率。
        :type Negative: float
        :param _Sentiment: 情感分类结果：
positive：正面情感
negative：负面情感
neutral：中性、无情感
        :type Sentiment: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Positive = None
        self._Neutral = None
        self._Negative = None
        self._Sentiment = None
        self._RequestId = None

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Neutral(self):
        return self._Neutral

    @Neutral.setter
    def Neutral(self, Neutral):
        self._Neutral = Neutral

    @property
    def Negative(self):
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative

    @property
    def Sentiment(self):
        return self._Sentiment

    @Sentiment.setter
    def Sentiment(self, Sentiment):
        self._Sentiment = Sentiment

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Positive = params.get("Positive")
        self._Neutral = params.get("Neutral")
        self._Negative = params.get("Negative")
        self._Sentiment = params.get("Sentiment")
        self._RequestId = params.get("RequestId")


class BasicParticiple(AbstractModel):
    """基础粒度分词和词性标注的结果

    """

    def __init__(self):
        r"""
        :param _Word: 基础词。
        :type Word: str
        :param _BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param _Length: 基础词的长度。
        :type Length: int
        :param _Pos: 词性。
        :type Pos: str
        """
        self._Word = None
        self._BeginOffset = None
        self._Length = None
        self._Pos = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._Length = params.get("Length")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Category(AbstractModel):
    """分类详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 分类id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Label: 分类英文名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Name: 分类中文名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Score: 分类置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self._Id = None
        self._Label = None
        self._Name = None
        self._Score = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Label = params.get("Label")
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyContentRequest(AbstractModel):
    """ClassifyContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Title: 待分类的文章的标题（仅支持UTF-8格式，不超过100字符）。
        :type Title: str
        :param _Content: 待分类文章的内容, 每个元素对应一个段落。（仅支持UTF-8格式，文章内容长度总和不超过2000字符）
        :type Content: list of str
        """
        self._Title = None
        self._Content = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyContentResponse(AbstractModel):
    """ClassifyContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FirstClassification: 一级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
        :type FirstClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param _SecondClassification: 二级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
        :type SecondClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param _ThirdClassification: 三级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FirstClassification = None
        self._SecondClassification = None
        self._ThirdClassification = None
        self._RequestId = None

    @property
    def FirstClassification(self):
        return self._FirstClassification

    @FirstClassification.setter
    def FirstClassification(self, FirstClassification):
        self._FirstClassification = FirstClassification

    @property
    def SecondClassification(self):
        return self._SecondClassification

    @SecondClassification.setter
    def SecondClassification(self, SecondClassification):
        self._SecondClassification = SecondClassification

    @property
    def ThirdClassification(self):
        return self._ThirdClassification

    @ThirdClassification.setter
    def ThirdClassification(self, ThirdClassification):
        self._ThirdClassification = ThirdClassification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FirstClassification") is not None:
            self._FirstClassification = Category()
            self._FirstClassification._deserialize(params.get("FirstClassification"))
        if params.get("SecondClassification") is not None:
            self._SecondClassification = Category()
            self._SecondClassification._deserialize(params.get("SecondClassification"))
        if params.get("ThirdClassification") is not None:
            self._ThirdClassification = Category()
            self._ThirdClassification._deserialize(params.get("ThirdClassification"))
        self._RequestId = params.get("RequestId")


class ComposeCoupletRequest(AbstractModel):
    """ComposeCouplet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 生成对联的关键词。长度需>=2，当长度>2时，自动截取前两个字作为关键字。内容需为常用汉字（不含有数字、英文、韩语、日语、符号等等其他）。
        :type Text: str
        :param _TargetType: 返回的文本结果为繁体还是简体。0：简体；1：繁体。默认为0。
        :type TargetType: int
        """
        self._Text = None
        self._TargetType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeCoupletResponse(AbstractModel):
    """ComposeCouplet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopScroll: 横批。
        :type TopScroll: str
        :param _Content: 上联与下联。
        :type Content: list of str
        :param _RandomCause: 当对联随机生成时，展示随机生成原因。
        :type RandomCause: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopScroll = None
        self._Content = None
        self._RandomCause = None
        self._RequestId = None

    @property
    def TopScroll(self):
        return self._TopScroll

    @TopScroll.setter
    def TopScroll(self, TopScroll):
        self._TopScroll = TopScroll

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RandomCause(self):
        return self._RandomCause

    @RandomCause.setter
    def RandomCause(self, RandomCause):
        self._RandomCause = RandomCause

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopScroll = params.get("TopScroll")
        self._Content = params.get("Content")
        self._RandomCause = params.get("RandomCause")
        self._RequestId = params.get("RequestId")


class ComposePoetryRequest(AbstractModel):
    """ComposePoetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 生成诗词的关键词。
        :type Text: str
        :param _PoetryType: 生成诗词的类型。0：藏头或藏身；1：藏头；2：藏身。默认为0。
        :type PoetryType: int
        :param _Genre: 诗的体裁。0：五言律诗或七言律诗；5：五言律诗；7：七言律诗。默认为0。
        :type Genre: int
        """
        self._Text = None
        self._PoetryType = None
        self._Genre = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def PoetryType(self):
        return self._PoetryType

    @PoetryType.setter
    def PoetryType(self, PoetryType):
        self._PoetryType = PoetryType

    @property
    def Genre(self):
        return self._Genre

    @Genre.setter
    def Genre(self, Genre):
        self._Genre = Genre


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._PoetryType = params.get("PoetryType")
        self._Genre = params.get("Genre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposePoetryResponse(AbstractModel):
    """ComposePoetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Title: 诗题，即输入的生成诗词的关键词。
        :type Title: str
        :param _Content: 诗的内容。
        :type Content: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Title = None
        self._Content = None
        self._RequestId = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class CompoundParticiple(AbstractModel):
    """复合粒度分词和词性标注的结果。

    """

    def __init__(self):
        r"""
        :param _Word: 基础词。
        :type Word: str
        :param _BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param _Length: 基础词的长度。
        :type Length: int
        :param _Pos: 词性。
        :type Pos: str
        """
        self._Word = None
        self._BeginOffset = None
        self._Length = None
        self._Pos = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._Length = params.get("Length")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorrectionItem(AbstractModel):
    """纠错结果列表

    """

    def __init__(self):
        r"""
        :param _Order: 纠错句子的序号。
        :type Order: int
        :param _BeginOffset: 错误的起始位置，从0开始。
        :type BeginOffset: int
        :param _Len: 错误内容长度。
        :type Len: int
        :param _Word: 错误内容。
        :type Word: str
        :param _CorrectWord: 纠错结果，当为删除类错误时，结果为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectWord: list of str
        :param _CorrectionType: 纠错类型。0：替换；1：插入；2：删除。
        :type CorrectionType: int
        :param _Confidence: 纠错信息置信度。0：error；1：warning；error的置信度更高。（仅供参考）
        :type Confidence: int
        :param _DescriptionZh: 纠错信息中文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionZh: str
        :param _DescriptionEn: 纠错信息英文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionEn: str
        """
        self._Order = None
        self._BeginOffset = None
        self._Len = None
        self._Word = None
        self._CorrectWord = None
        self._CorrectionType = None
        self._Confidence = None
        self._DescriptionZh = None
        self._DescriptionEn = None

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Len(self):
        return self._Len

    @Len.setter
    def Len(self, Len):
        self._Len = Len

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def CorrectWord(self):
        return self._CorrectWord

    @CorrectWord.setter
    def CorrectWord(self, CorrectWord):
        self._CorrectWord = CorrectWord

    @property
    def CorrectionType(self):
        return self._CorrectionType

    @CorrectionType.setter
    def CorrectionType(self, CorrectionType):
        self._CorrectionType = CorrectionType

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def DescriptionZh(self):
        return self._DescriptionZh

    @DescriptionZh.setter
    def DescriptionZh(self, DescriptionZh):
        self._DescriptionZh = DescriptionZh

    @property
    def DescriptionEn(self):
        return self._DescriptionEn

    @DescriptionEn.setter
    def DescriptionEn(self, DescriptionEn):
        self._DescriptionEn = DescriptionEn


    def _deserialize(self, params):
        self._Order = params.get("Order")
        self._BeginOffset = params.get("BeginOffset")
        self._Len = params.get("Len")
        self._Word = params.get("Word")
        self._CorrectWord = params.get("CorrectWord")
        self._CorrectionType = params.get("CorrectionType")
        self._Confidence = params.get("Confidence")
        self._DescriptionZh = params.get("DescriptionZh")
        self._DescriptionEn = params.get("DescriptionEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Embellish(AbstractModel):
    """文本润色结果

    """

    def __init__(self):
        r"""
        :param _Text: 润色后的文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _EmbellishType: 润色类型。类型如下：
expansion：扩写
rewriting：改写
translation_m2a：从现代文改写为古文
translation_a2m：从古文改写为现代文


注意：此字段可能返回 null，表示取不到有效值。
        :type EmbellishType: str
        """
        self._Text = None
        self._EmbellishType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def EmbellishType(self):
        return self._EmbellishType

    @EmbellishType.setter
    def EmbellishType(self, EmbellishType):
        self._EmbellishType = EmbellishType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._EmbellishType = params.get("EmbellishType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Entity(AbstractModel):
    """实体识别结果。

    """

    def __init__(self):
        r"""
        :param _Word: 基础词。
        :type Word: str
        :param _BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param _Length: 基础词的长度。
        :type Length: int
        :param _Type: 实体类型的标准名字。
        :type Type: str
        :param _Name: 类型名字的自然语言表达。（中文或英文）
        :type Name: str
        """
        self._Word = None
        self._BeginOffset = None
        self._Length = None
        self._Type = None
        self._Name = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._Length = params.get("Length")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateSentenceSimilarityRequest(AbstractModel):
    """EvaluateSentenceSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SentencePairList: 待分析的句子对数组。句子对应不超过1对，仅支持中文文本，原句子与目标句子均应不超过500字符。
        :type SentencePairList: list of SentencePair
        """
        self._SentencePairList = None

    @property
    def SentencePairList(self):
        return self._SentencePairList

    @SentencePairList.setter
    def SentencePairList(self, SentencePairList):
        self._SentencePairList = SentencePairList


    def _deserialize(self, params):
        if params.get("SentencePairList") is not None:
            self._SentencePairList = []
            for item in params.get("SentencePairList"):
                obj = SentencePair()
                obj._deserialize(item)
                self._SentencePairList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateSentenceSimilarityResponse(AbstractModel):
    """EvaluateSentenceSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreList: 每个句子对的相似度分值。
        :type ScoreList: list of float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreList = None
        self._RequestId = None

    @property
    def ScoreList(self):
        return self._ScoreList

    @ScoreList.setter
    def ScoreList(self, ScoreList):
        self._ScoreList = ScoreList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScoreList = params.get("ScoreList")
        self._RequestId = params.get("RequestId")


class EvaluateWordSimilarityRequest(AbstractModel):
    """EvaluateWordSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceWord: 计算相似度的源词。（仅支持UTF-8格式，不超过10字符）

        :type SourceWord: str
        :param _TargetWord: 计算相似度的目标词。（仅支持UTF-8格式，不超过10字符）

        :type TargetWord: str
        """
        self._SourceWord = None
        self._TargetWord = None

    @property
    def SourceWord(self):
        return self._SourceWord

    @SourceWord.setter
    def SourceWord(self, SourceWord):
        self._SourceWord = SourceWord

    @property
    def TargetWord(self):
        return self._TargetWord

    @TargetWord.setter
    def TargetWord(self, TargetWord):
        self._TargetWord = TargetWord


    def _deserialize(self, params):
        self._SourceWord = params.get("SourceWord")
        self._TargetWord = params.get("TargetWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateWordSimilarityResponse(AbstractModel):
    """EvaluateWordSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Similarity: 词相似度分值。
        :type Similarity: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Similarity = None
        self._RequestId = None

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Similarity = params.get("Similarity")
        self._RequestId = params.get("RequestId")


class GenerateKeywordSentenceRequest(AbstractModel):
    """GenerateKeywordSentence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WordList: 生成句子的关键词，关键词个数需不超过4个，中文关键词长度应不超过10字符，英文关键词长度不超过3个单词。关键词中不可包含标点符号。
        :type WordList: list of str
        :param _Number: 返回生成句子的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param _Domain: 指定生成句子的领域，支持领域如下：
general：通用领域，支持中英文
academic：学术领域，仅支持英文
默认为general（通用领域）。
        :type Domain: str
        """
        self._WordList = None
        self._Number = None
        self._Domain = None

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._WordList = params.get("WordList")
        self._Number = params.get("Number")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateKeywordSentenceResponse(AbstractModel):
    """GenerateKeywordSentence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeywordSentenceList: 生成的句子列表。
        :type KeywordSentenceList: list of KeywordSentence
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeywordSentenceList = None
        self._RequestId = None

    @property
    def KeywordSentenceList(self):
        return self._KeywordSentenceList

    @KeywordSentenceList.setter
    def KeywordSentenceList(self, KeywordSentenceList):
        self._KeywordSentenceList = KeywordSentenceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeywordSentenceList") is not None:
            self._KeywordSentenceList = []
            for item in params.get("KeywordSentenceList"):
                obj = KeywordSentence()
                obj._deserialize(item)
                self._KeywordSentenceList.append(obj)
        self._RequestId = params.get("RequestId")


class KeywordSentence(AbstractModel):
    """通过关键词生成的句子信息

    """

    def __init__(self):
        r"""
        :param _TargetText: 通过关键词生成的句子。
        :type TargetText: str
        """
        self._TargetText = None

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseWordsRequest(AbstractModel):
    """ParseWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（支持中英文文本，不超过500字符）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseWordsResponse(AbstractModel):
    """ParseWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NormalText: 输入文本正则化的结果。（包括对英文文本中的开头和实体进行大写等）
        :type NormalText: str
        :param _BasicParticiples: 基础粒度分词和词性标注的结果。（请参见附录[词性表](https://cloud.tencent.com/document/product/271/36460)）
        :type BasicParticiples: list of BasicParticiple
        :param _CompoundParticiples: 复合粒度分词和词性标注的结果。（请参见附录[词性表](https://cloud.tencent.com/document/product/271/36460)）
        :type CompoundParticiples: list of CompoundParticiple
        :param _Entities: 实体识别结果。（请参见附录[实体类型数据](https://cloud.tencent.com/document/product/271/90592)）

        :type Entities: list of Entity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NormalText = None
        self._BasicParticiples = None
        self._CompoundParticiples = None
        self._Entities = None
        self._RequestId = None

    @property
    def NormalText(self):
        return self._NormalText

    @NormalText.setter
    def NormalText(self, NormalText):
        self._NormalText = NormalText

    @property
    def BasicParticiples(self):
        return self._BasicParticiples

    @BasicParticiples.setter
    def BasicParticiples(self, BasicParticiples):
        self._BasicParticiples = BasicParticiples

    @property
    def CompoundParticiples(self):
        return self._CompoundParticiples

    @CompoundParticiples.setter
    def CompoundParticiples(self, CompoundParticiples):
        self._CompoundParticiples = CompoundParticiples

    @property
    def Entities(self):
        return self._Entities

    @Entities.setter
    def Entities(self, Entities):
        self._Entities = Entities

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NormalText = params.get("NormalText")
        if params.get("BasicParticiples") is not None:
            self._BasicParticiples = []
            for item in params.get("BasicParticiples"):
                obj = BasicParticiple()
                obj._deserialize(item)
                self._BasicParticiples.append(obj)
        if params.get("CompoundParticiples") is not None:
            self._CompoundParticiples = []
            for item in params.get("CompoundParticiples"):
                obj = CompoundParticiple()
                obj._deserialize(item)
                self._CompoundParticiples.append(obj)
        if params.get("Entities") is not None:
            self._Entities = []
            for item in params.get("Entities"):
                obj = Entity()
                obj._deserialize(item)
                self._Entities.append(obj)
        self._RequestId = params.get("RequestId")


class RetrieveSimilarWordsRequest(AbstractModel):
    """RetrieveSimilarWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 输入的词语。（仅支持UTF-8格式，不超过10字符）
        :type Text: str
        :param _Number: 召回的相似词个数，取值范围为1-20。
        :type Number: int
        """
        self._Text = None
        self._Number = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveSimilarWordsResponse(AbstractModel):
    """RetrieveSimilarWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WordList: 召回的相似词数组。
        :type WordList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WordList = None
        self._RequestId = None

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WordList = params.get("WordList")
        self._RequestId = params.get("RequestId")


class SentenceCorrectionRequest(AbstractModel):
    """SentenceCorrection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TextList: 待纠错的句子列表。可以以数组方式在一次请求中填写多个待纠错的句子。文本统一使用utf-8格式编码，每个中文句子的长度不超过150字符，每个英文句子的长度不超过100个单词，且数组长度需小于30，即句子总数需少于30句。
        :type TextList: list of str
        """
        self._TextList = None

    @property
    def TextList(self):
        return self._TextList

    @TextList.setter
    def TextList(self, TextList):
        self._TextList = TextList


    def _deserialize(self, params):
        self._TextList = params.get("TextList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceCorrectionResponse(AbstractModel):
    """SentenceCorrection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorrectionList: 纠错结果列表。
（注意仅展示错误句子的纠错结果，若句子无错则不展示，若全部待纠错句子都被认为无错，则可能返回数组为空）
        :type CorrectionList: list of CorrectionItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorrectionList = None
        self._RequestId = None

    @property
    def CorrectionList(self):
        return self._CorrectionList

    @CorrectionList.setter
    def CorrectionList(self, CorrectionList):
        self._CorrectionList = CorrectionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CorrectionList") is not None:
            self._CorrectionList = []
            for item in params.get("CorrectionList"):
                obj = CorrectionItem()
                obj._deserialize(item)
                self._CorrectionList.append(obj)
        self._RequestId = params.get("RequestId")


class SentencePair(AbstractModel):
    """待分析的句子对

    """

    def __init__(self):
        r"""
        :param _SourceText: 需要与目标句子计算相似度的源句子。（仅支持UTF-8格式，不超过500字符）
        :type SourceText: str
        :param _TargetText: 目标句子。（仅支持UTF-8格式，不超过500字符）

        :type TargetText: str
        """
        self._SourceText = None
        self._TargetText = None

    @property
    def SourceText(self):
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TestingTextGenerationRequest(AbstractModel):
    """TestingTextGeneration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 会话内容,按对话时间从旧到新在数组中排列。
        :type Messages: list of TextGenerationMessage
        :param _Model: 模型名称，当前固定为TestingModel
        :type Model: str
        :param _QueryId: 会话id。
        :type QueryId: str
        :param _Temperature: 超参数temperature, 该参数用于控制生成文本中重复内容。取值区间为[0.0, 2.0], 非必要不建议使用, 不合理的取值会影响效果。默认为1.0。
        :type Temperature: float
        :param _TopP: 超参数top_p, 该参数用于控制生成文本的多样性。较小的"top_p"值会限制模型的选择范围，使生成的文本更加一致和确定性。较大的"top_p"值会扩大选择范围，使生成的文本更加多样化和随机。取值区间为[0.0, 1.0], 非必要不建议使用, 不合理的取值会影响效果。默认值为1.0。
        :type TopP: float
        :param _TopK: 超参数top_k,该参数用于控制生成文本的多样性和可控性，较小的"top_k"值会限制模型的选择范围，使生成的文本更加一致和确定性。较大的"top_k"值会扩大选择范围，使生成的文本更加多样化和随机。取值区间为[1, 100]，默认值 40。
        :type TopK: float
        :param _RepetitionPenalty: 重复惩罚项,该参数用于用于控制生成文本中重复内容。建议范围[1.0, 1.05]非必要不建议使用, 不合理的取值会影响效果。默认为1。
        :type RepetitionPenalty: float
        :param _OutputSeqLen: 输出结果最大tokens数量。取值区间为(0, 1024]。默认值为768。
        :type OutputSeqLen: int
        :param _MaxInputSeqLen: 输入文本的最大 tokens 数量。取值区间为(0, 1024]。默认值为256。
        :type MaxInputSeqLen: int
        """
        self._Messages = None
        self._Model = None
        self._QueryId = None
        self._Temperature = None
        self._TopP = None
        self._TopK = None
        self._RepetitionPenalty = None
        self._OutputSeqLen = None
        self._MaxInputSeqLen = None

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def QueryId(self):
        return self._QueryId

    @QueryId.setter
    def QueryId(self, QueryId):
        self._QueryId = QueryId

    @property
    def Temperature(self):
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def TopK(self):
        return self._TopK

    @TopK.setter
    def TopK(self, TopK):
        self._TopK = TopK

    @property
    def RepetitionPenalty(self):
        return self._RepetitionPenalty

    @RepetitionPenalty.setter
    def RepetitionPenalty(self, RepetitionPenalty):
        self._RepetitionPenalty = RepetitionPenalty

    @property
    def OutputSeqLen(self):
        return self._OutputSeqLen

    @OutputSeqLen.setter
    def OutputSeqLen(self, OutputSeqLen):
        self._OutputSeqLen = OutputSeqLen

    @property
    def MaxInputSeqLen(self):
        return self._MaxInputSeqLen

    @MaxInputSeqLen.setter
    def MaxInputSeqLen(self, MaxInputSeqLen):
        self._MaxInputSeqLen = MaxInputSeqLen


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = TextGenerationMessage()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Model = params.get("Model")
        self._QueryId = params.get("QueryId")
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        self._TopK = params.get("TopK")
        self._RepetitionPenalty = params.get("RepetitionPenalty")
        self._OutputSeqLen = params.get("OutputSeqLen")
        self._MaxInputSeqLen = params.get("MaxInputSeqLen")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TestingTextGenerationResponse(AbstractModel):
    """TestingTextGeneration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Choices: 结果
        :type Choices: list of TextGenerationChoices
        :param _Created: unix时间戳的字符串
        :type Created: int
        :param _Id: 会话id
        :type Id: str
        :param _Model: 模型名
        :type Model: str
        :param _Usage: token数量
        :type Usage: :class:`tencentcloud.nlp.v20190408.models.TextGenerationUsage`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Choices = None
        self._Created = None
        self._Id = None
        self._Model = None
        self._Usage = None
        self._RequestId = None

    @property
    def Choices(self):
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def Created(self):
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = TextGenerationChoices()
                obj._deserialize(item)
                self._Choices.append(obj)
        self._Created = params.get("Created")
        self._Id = params.get("Id")
        self._Model = params.get("Model")
        if params.get("Usage") is not None:
            self._Usage = TextGenerationUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class TextEmbellishRequest(AbstractModel):
    """TextEmbellish请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待润色的文本。中文文本长度需<=50字符；英文文本长度需<=30个单词。
        :type Text: str
        :param _SourceLang: 待润色文本的语言类型，支持语言如下：
zh：中文
en：英文
        :type SourceLang: str
        :param _Number: 返回润色结果的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param _Style: 控制润色类型，类型如下：
both：同时返回改写和扩写
expansion：扩写
rewriting：改写
m2a：从现代文改写为古文
a2m：从古文改写为现代文
默认为both。
        :type Style: str
        """
        self._Text = None
        self._SourceLang = None
        self._Number = None
        self._Style = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SourceLang(self):
        return self._SourceLang

    @SourceLang.setter
    def SourceLang(self, SourceLang):
        self._SourceLang = SourceLang

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SourceLang = params.get("SourceLang")
        self._Number = params.get("Number")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextEmbellishResponse(AbstractModel):
    """TextEmbellish返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EmbellishList: 润色结果列表。
        :type EmbellishList: list of Embellish
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EmbellishList = None
        self._RequestId = None

    @property
    def EmbellishList(self):
        return self._EmbellishList

    @EmbellishList.setter
    def EmbellishList(self, EmbellishList):
        self._EmbellishList = EmbellishList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EmbellishList") is not None:
            self._EmbellishList = []
            for item in params.get("EmbellishList"):
                obj = Embellish()
                obj._deserialize(item)
                self._EmbellishList.append(obj)
        self._RequestId = params.get("RequestId")


class TextGenerationChoices(AbstractModel):
    """TextGenerationChoices

    """

    def __init__(self):
        r"""
        :param _Message: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: :class:`tencentcloud.nlp.v20190408.models.TextGenerationMessage`
        """
        self._Message = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        if params.get("Message") is not None:
            self._Message = TextGenerationMessage()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextGenerationMessage(AbstractModel):
    """TextGenerationMessage

    """

    def __init__(self):
        r"""
        :param _Role: 角色支持 system, user, assistant。默认为user。
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _Content: 消息的内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextGenerationUsage(AbstractModel):
    """TextGenerationUsage

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入tokens数量
        :type PromptTokens: int
        :param _CompletionTokens: 输出tokens数量
        :type CompletionTokens: int
        :param _TotalTokens: 总token数量
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._CompletionTokens = params.get("CompletionTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWritingRequest(AbstractModel):
    """TextWriting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待续写的句子，文本统一使用utf-8格式编码，长度不超过200字符。
        :type Text: str
        :param _SourceLang: 待续写文本的语言类型，支持语言如下：
zh：中文
en：英文
        :type SourceLang: str
        :param _Number: 返回续写结果的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param _Domain: 指定续写领域，支持领域如下：
general：通用领域，支持中英文补全
academic：学术领域，仅支持英文补全
默认为general（通用领域）。
        :type Domain: str
        :param _Style: 指定续写风格，支持风格如下：
science_fiction：科幻
military_history：军事
xuanhuan_wuxia：武侠
urban_officialdom：职场
默认为xuanhuan_wuxia（武侠）。
        :type Style: str
        """
        self._Text = None
        self._SourceLang = None
        self._Number = None
        self._Domain = None
        self._Style = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SourceLang(self):
        return self._SourceLang

    @SourceLang.setter
    def SourceLang(self, SourceLang):
        self._SourceLang = SourceLang

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SourceLang = params.get("SourceLang")
        self._Number = params.get("Number")
        self._Domain = params.get("Domain")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWritingResponse(AbstractModel):
    """TextWriting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WritingList: 续写结果列表。
        :type WritingList: list of Writing
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WritingList = None
        self._RequestId = None

    @property
    def WritingList(self):
        return self._WritingList

    @WritingList.setter
    def WritingList(self, WritingList):
        self._WritingList = WritingList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WritingList") is not None:
            self._WritingList = []
            for item in params.get("WritingList"):
                obj = Writing()
                obj._deserialize(item)
                self._WritingList.append(obj)
        self._RequestId = params.get("RequestId")


class Writing(AbstractModel):
    """文本续写结果

    """

    def __init__(self):
        r"""
        :param _TargetText: 续写的文本。
        :type TargetText: str
        :param _PrefixText: 续写的前缀。
        :type PrefixText: str
        """
        self._TargetText = None
        self._PrefixText = None

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def PrefixText(self):
        return self._PrefixText

    @PrefixText.setter
    def PrefixText(self, PrefixText):
        self._PrefixText = PrefixText


    def _deserialize(self, params):
        self._TargetText = params.get("TargetText")
        self._PrefixText = params.get("PrefixText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        