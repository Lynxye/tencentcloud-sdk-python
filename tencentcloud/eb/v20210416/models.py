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


class APIGWParams(AbstractModel):
    """APIGWParams描述

    """

    def __init__(self):
        r"""
        :param _Protocol: HTTPS
        :type Protocol: str
        :param _Method: POST
        :type Method: str
        """
        self._Protocol = None
        self._Method = None

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRuleRequest(AbstractModel):
    """CheckRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Event: Event信息
        :type Event: str
        :param _EventPattern: EventPattern信息
        :type EventPattern: str
        """
        self._Event = None
        self._EventPattern = None

    @property
    def Event(self):
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern


    def _deserialize(self, params):
        self._Event = params.get("Event")
        self._EventPattern = params.get("EventPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckRuleResponse(AbstractModel):
    """CheckRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CheckTransformationRequest(AbstractModel):
    """CheckTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Input: 待处理的json字符串
        :type Input: str
        :param _Transformations: 一个转换规则列表
        :type Transformations: list of Transformation
        """
        self._Input = None
        self._Transformations = None

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations


    def _deserialize(self, params):
        self._Input = params.get("Input")
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckTransformationResponse(AbstractModel):
    """CheckTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Output: 经过Transformations处理之后的数据
        :type Output: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Output = None
        self._RequestId = None

    @property
    def Output(self):
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Output = params.get("Output")
        self._RequestId = params.get("RequestId")


class CkafkaDeliveryParams(AbstractModel):
    """用来描述需要投递到kafka topic的参数

    """

    def __init__(self):
        r"""
        :param _TopicName: ckafka topic name
        :type TopicName: str
        :param _ResourceDescription: ckafka资源qcs六段式
        :type ResourceDescription: str
        """
        self._TopicName = None
        self._ResourceDescription = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def ResourceDescription(self):
        return self._ResourceDescription

    @ResourceDescription.setter
    def ResourceDescription(self, ResourceDescription):
        self._ResourceDescription = ResourceDescription


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._ResourceDescription = params.get("ResourceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaParams(AbstractModel):
    """Ckafka 连接器参数

    """

    def __init__(self):
        r"""
        :param _Offset: kafka offset
        :type Offset: str
        :param _TopicName: ckafka  topic
        :type TopicName: str
        """
        self._Offset = None
        self._TopicName = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CkafkaTargetParams(AbstractModel):
    """用来描述ckafka投递目标

    """

    def __init__(self):
        r"""
        :param _TopicName: 要投递到的ckafka topic
        :type TopicName: str
        :param _RetryPolicy: 重试策略
        :type RetryPolicy: :class:`tencentcloud.eb.v20210416.models.RetryPolicy`
        """
        self._TopicName = None
        self._RetryPolicy = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def RetryPolicy(self):
        return self._RetryPolicy

    @RetryPolicy.setter
    def RetryPolicy(self, RetryPolicy):
        self._RetryPolicy = RetryPolicy


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        if params.get("RetryPolicy") is not None:
            self._RetryPolicy = RetryPolicy()
            self._RetryPolicy._deserialize(params.get("RetryPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Connection(AbstractModel):
    """Connection信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态
        :type Status: str
        :param _ModTime: 更新时间
        :type ModTime: str
        :param _Enable: 使能开关
        :type Enable: bool
        :param _Description: 描述
        :type Description: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _ConnectionId: 连接器ID
        :type ConnectionId: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _ConnectionDescription: 连接器描述
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param _ConnectionName: 连接器名称
        :type ConnectionName: str
        :param _Type: 类型
        :type Type: str
        """
        self._Status = None
        self._ModTime = None
        self._Enable = None
        self._Description = None
        self._AddTime = None
        self._ConnectionId = None
        self._EventBusId = None
        self._ConnectionDescription = None
        self._ConnectionName = None
        self._Type = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ConnectionDescription(self):
        return self._ConnectionDescription

    @ConnectionDescription.setter
    def ConnectionDescription(self, ConnectionDescription):
        self._ConnectionDescription = ConnectionDescription

    @property
    def ConnectionName(self):
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ModTime = params.get("ModTime")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._ConnectionId = params.get("ConnectionId")
        self._EventBusId = params.get("EventBusId")
        if params.get("ConnectionDescription") is not None:
            self._ConnectionDescription = ConnectionDescription()
            self._ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self._ConnectionName = params.get("ConnectionName")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionBrief(AbstractModel):
    """连接器基础信息

    """

    def __init__(self):
        r"""
        :param _Type: 连接器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 连接器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Type = None
        self._Status = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionDescription(AbstractModel):
    """ConnectionDescription描述

    """

    def __init__(self):
        r"""
        :param _ResourceDescription: 资源qcs六段式，更多参考 [资源六段式](https://cloud.tencent.com/document/product/598/10606)
        :type ResourceDescription: str
        :param _APIGWParams: apigw参数
注意：此字段可能返回 null，表示取不到有效值。
        :type APIGWParams: :class:`tencentcloud.eb.v20210416.models.APIGWParams`
        :param _CkafkaParams: ckafka参数
注意：此字段可能返回 null，表示取不到有效值。
        :type CkafkaParams: :class:`tencentcloud.eb.v20210416.models.CkafkaParams`
        :param _DTSParams: data transfer service (DTS)参数
注意：此字段可能返回 null，表示取不到有效值。
        :type DTSParams: :class:`tencentcloud.eb.v20210416.models.DTSParams`
        """
        self._ResourceDescription = None
        self._APIGWParams = None
        self._CkafkaParams = None
        self._DTSParams = None

    @property
    def ResourceDescription(self):
        return self._ResourceDescription

    @ResourceDescription.setter
    def ResourceDescription(self, ResourceDescription):
        self._ResourceDescription = ResourceDescription

    @property
    def APIGWParams(self):
        return self._APIGWParams

    @APIGWParams.setter
    def APIGWParams(self, APIGWParams):
        self._APIGWParams = APIGWParams

    @property
    def CkafkaParams(self):
        return self._CkafkaParams

    @CkafkaParams.setter
    def CkafkaParams(self, CkafkaParams):
        self._CkafkaParams = CkafkaParams

    @property
    def DTSParams(self):
        return self._DTSParams

    @DTSParams.setter
    def DTSParams(self, DTSParams):
        self._DTSParams = DTSParams


    def _deserialize(self, params):
        self._ResourceDescription = params.get("ResourceDescription")
        if params.get("APIGWParams") is not None:
            self._APIGWParams = APIGWParams()
            self._APIGWParams._deserialize(params.get("APIGWParams"))
        if params.get("CkafkaParams") is not None:
            self._CkafkaParams = CkafkaParams()
            self._CkafkaParams._deserialize(params.get("CkafkaParams"))
        if params.get("DTSParams") is not None:
            self._DTSParams = DTSParams()
            self._DTSParams._deserialize(params.get("DTSParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionRequest(AbstractModel):
    """CreateConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectionDescription: 连接器描述
        :type ConnectionDescription: :class:`tencentcloud.eb.v20210416.models.ConnectionDescription`
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _ConnectionName: 连接器名称
        :type ConnectionName: str
        :param _Description: 描述
        :type Description: str
        :param _Enable: 使能开关
        :type Enable: bool
        :param _Type: 类型
        :type Type: str
        """
        self._ConnectionDescription = None
        self._EventBusId = None
        self._ConnectionName = None
        self._Description = None
        self._Enable = None
        self._Type = None

    @property
    def ConnectionDescription(self):
        return self._ConnectionDescription

    @ConnectionDescription.setter
    def ConnectionDescription(self, ConnectionDescription):
        self._ConnectionDescription = ConnectionDescription

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ConnectionName(self):
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("ConnectionDescription") is not None:
            self._ConnectionDescription = ConnectionDescription()
            self._ConnectionDescription._deserialize(params.get("ConnectionDescription"))
        self._EventBusId = params.get("EventBusId")
        self._ConnectionName = params.get("ConnectionName")
        self._Description = params.get("Description")
        self._Enable = params.get("Enable")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConnectionResponse(AbstractModel):
    """CreateConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectionId: 连接器ID
        :type ConnectionId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConnectionId = None
        self._RequestId = None

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConnectionId = params.get("ConnectionId")
        self._RequestId = params.get("RequestId")


class CreateEventBusRequest(AbstractModel):
    """CreateEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type EventBusName: str
        :param _Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        :param _SaveDays: EB存储时长
        :type SaveDays: int
        :param _EnableStore: EB是否开启存储
        :type EnableStore: bool
        """
        self._EventBusName = None
        self._Description = None
        self._SaveDays = None
        self._EnableStore = None

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SaveDays(self):
        return self._SaveDays

    @SaveDays.setter
    def SaveDays(self, SaveDays):
        self._SaveDays = SaveDays

    @property
    def EnableStore(self):
        return self._EnableStore

    @EnableStore.setter
    def EnableStore(self, EnableStore):
        self._EnableStore = EnableStore


    def _deserialize(self, params):
        self._EventBusName = params.get("EventBusName")
        self._Description = params.get("Description")
        self._SaveDays = params.get("SaveDays")
        self._EnableStore = params.get("EnableStore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEventBusResponse(AbstractModel):
    """CreateEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventBusId = None
        self._RequestId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventPattern: 参考：[事件模式](https://cloud.tencent.com/document/product/1359/56084)
        :type EventPattern: str
        :param _EventBusId: 事件集ID。
        :type EventBusId: str
        :param _RuleName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type RuleName: str
        :param _Enable: 使能开关。
        :type Enable: bool
        :param _Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        """
        self._EventPattern = None
        self._EventBusId = None
        self._RuleName = None
        self._Enable = None
        self._Description = None

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._EventPattern = params.get("EventPattern")
        self._EventBusId = params.get("EventBusId")
        self._RuleName = params.get("RuleName")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 事件规则ID
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateTargetRequest(AbstractModel):
    """CreateTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Type: 目标类型
        :type Type: str
        :param _TargetDescription: 目标描述
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param _RuleId: 事件规则ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._Type = None
        self._TargetDescription = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TargetDescription(self):
        return self._TargetDescription

    @TargetDescription.setter
    def TargetDescription(self, TargetDescription):
        self._TargetDescription = TargetDescription

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._Type = params.get("Type")
        if params.get("TargetDescription") is not None:
            self._TargetDescription = TargetDescription()
            self._TargetDescription._deserialize(params.get("TargetDescription"))
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetResponse(AbstractModel):
    """CreateTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetId: 目标ID
        :type TargetId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetId = None
        self._RequestId = None

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._RequestId = params.get("RequestId")


class CreateTransformationRequest(AbstractModel):
    """CreateTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件总线 id
        :type EventBusId: str
        :param _RuleId: 规则id
        :type RuleId: str
        :param _Transformations: 一个转换规则列表，当前仅限定一个
        :type Transformations: list of Transformation
        """
        self._EventBusId = None
        self._RuleId = None
        self._Transformations = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTransformationResponse(AbstractModel):
    """CreateTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TransformationId: 生成的转换器id
        :type TransformationId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TransformationId = None
        self._RequestId = None

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TransformationId = params.get("TransformationId")
        self._RequestId = params.get("RequestId")


class DTSParams(AbstractModel):
    """Data Transfer Service参数

    """


class DeadLetterConfig(AbstractModel):
    """rule对应的dlq配置

    """

    def __init__(self):
        r"""
        :param _DisposeMethod: 支持dlq、丢弃、忽略错误继续传递三种模式, 分别对应: DLQ,DROP,IGNORE_ERROR
        :type DisposeMethod: str
        :param _CkafkaDeliveryParams: 设置了DLQ方式后,此选项必填. 错误消息会被投递到对应的kafka topic中
注意：此字段可能返回 null，表示取不到有效值。
        :type CkafkaDeliveryParams: :class:`tencentcloud.eb.v20210416.models.CkafkaDeliveryParams`
        """
        self._DisposeMethod = None
        self._CkafkaDeliveryParams = None

    @property
    def DisposeMethod(self):
        return self._DisposeMethod

    @DisposeMethod.setter
    def DisposeMethod(self, DisposeMethod):
        self._DisposeMethod = DisposeMethod

    @property
    def CkafkaDeliveryParams(self):
        return self._CkafkaDeliveryParams

    @CkafkaDeliveryParams.setter
    def CkafkaDeliveryParams(self, CkafkaDeliveryParams):
        self._CkafkaDeliveryParams = CkafkaDeliveryParams


    def _deserialize(self, params):
        self._DisposeMethod = params.get("DisposeMethod")
        if params.get("CkafkaDeliveryParams") is not None:
            self._CkafkaDeliveryParams = CkafkaDeliveryParams()
            self._CkafkaDeliveryParams._deserialize(params.get("CkafkaDeliveryParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionRequest(AbstractModel):
    """DeleteConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectionId: 连接器ID
        :type ConnectionId: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        """
        self._ConnectionId = None
        self._EventBusId = None

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        self._ConnectionId = params.get("ConnectionId")
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConnectionResponse(AbstractModel):
    """DeleteConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteEventBusRequest(AbstractModel):
    """DeleteEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        """
        self._EventBusId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEventBusResponse(AbstractModel):
    """DeleteEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleId: 事件规则ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTargetRequest(AbstractModel):
    """DeleteTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _TargetId: 事件目标ID
        :type TargetId: str
        :param _RuleId: 事件规则ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._TargetId = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._TargetId = params.get("TargetId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetResponse(AbstractModel):
    """DeleteTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTransformationRequest(AbstractModel):
    """DeleteTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _TransformationId: 转换器id
        :type TransformationId: str
        """
        self._EventBusId = None
        self._RuleId = None
        self._TransformationId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTransformationResponse(AbstractModel):
    """DeleteTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeLogTagValueRequest(AbstractModel):
    """DescribeLogTagValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _GroupField: 聚合字段
        :type GroupField: str
        :param _Page: 页数
        :type Page: int
        :param _Limit: 每页数据大小
        :type Limit: int
        :param _Filter: 筛选条件
        :type Filter: list of LogFilter
        """
        self._StartTime = None
        self._EndTime = None
        self._EventBusId = None
        self._GroupField = None
        self._Page = None
        self._Limit = None
        self._Filter = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def GroupField(self):
        return self._GroupField

    @GroupField.setter
    def GroupField(self, GroupField):
        self._GroupField = GroupField

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._EventBusId = params.get("EventBusId")
        self._GroupField = params.get("GroupField")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = LogFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogTagValueResponse(AbstractModel):
    """DescribeLogTagValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 索引检索维度值
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Results = params.get("Results")
        self._RequestId = params.get("RequestId")


class ESTargetParams(AbstractModel):
    """描述Es规则目标

    """

    def __init__(self):
        r"""
        :param _NetMode: 网络连接类型
        :type NetMode: str
        :param _IndexPrefix: 索引前缀
        :type IndexPrefix: str
        :param _RotationInterval: es日志轮换粒度
        :type RotationInterval: str
        :param _OutputMode: DTS事件配置
        :type OutputMode: str
        :param _IndexSuffixMode: DTS索引配置
        :type IndexSuffixMode: str
        :param _IndexTemplateType: es模版类型
        :type IndexTemplateType: str
        """
        self._NetMode = None
        self._IndexPrefix = None
        self._RotationInterval = None
        self._OutputMode = None
        self._IndexSuffixMode = None
        self._IndexTemplateType = None

    @property
    def NetMode(self):
        return self._NetMode

    @NetMode.setter
    def NetMode(self, NetMode):
        self._NetMode = NetMode

    @property
    def IndexPrefix(self):
        return self._IndexPrefix

    @IndexPrefix.setter
    def IndexPrefix(self, IndexPrefix):
        self._IndexPrefix = IndexPrefix

    @property
    def RotationInterval(self):
        return self._RotationInterval

    @RotationInterval.setter
    def RotationInterval(self, RotationInterval):
        self._RotationInterval = RotationInterval

    @property
    def OutputMode(self):
        return self._OutputMode

    @OutputMode.setter
    def OutputMode(self, OutputMode):
        self._OutputMode = OutputMode

    @property
    def IndexSuffixMode(self):
        return self._IndexSuffixMode

    @IndexSuffixMode.setter
    def IndexSuffixMode(self, IndexSuffixMode):
        self._IndexSuffixMode = IndexSuffixMode

    @property
    def IndexTemplateType(self):
        return self._IndexTemplateType

    @IndexTemplateType.setter
    def IndexTemplateType(self, IndexTemplateType):
        self._IndexTemplateType = IndexTemplateType


    def _deserialize(self, params):
        self._NetMode = params.get("NetMode")
        self._IndexPrefix = params.get("IndexPrefix")
        self._RotationInterval = params.get("RotationInterval")
        self._OutputMode = params.get("OutputMode")
        self._IndexSuffixMode = params.get("IndexSuffixMode")
        self._IndexTemplateType = params.get("IndexTemplateType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EtlFilter(AbstractModel):
    """描述如何过滤数据

    """

    def __init__(self):
        r"""
        :param _Filter: 语法Rule规则保持一致
        :type Filter: str
        """
        self._Filter = None

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """eb event信息

    """

    def __init__(self):
        r"""
        :param _Source: 事件源的信息,新产品上报必须符合EB的规范
        :type Source: str
        :param _Data: 事件数据，内容由创建事件的系统来控制，当前datacontenttype仅支持application/json;charset=utf-8，所以该字段是json字符串
        :type Data: str
        :param _Type: 事件类型，可自定义，选填。云服务默认写 COS:Created:PostObject，用“：”分割类型字段
        :type Type: str
        :param _Subject: 事件来源详细描述，可自定义，选填。云服务默认为标准qcs资源表示语法：qcs::dts:ap-guangzhou:appid/uin:xxx
        :type Subject: str
        :param _Time: 事件发生的毫秒时间戳，
time.Now().UnixNano()/1e6
        :type Time: int
        """
        self._Source = None
        self._Data = None
        self._Type = None
        self._Subject = None
        self._Time = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Subject(self):
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Data = params.get("Data")
        self._Type = params.get("Type")
        self._Subject = params.get("Subject")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventBus(AbstractModel):
    """事件集信息

    """

    def __init__(self):
        r"""
        :param _ModTime: 更新时间
        :type ModTime: str
        :param _Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _EventBusName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type EventBusName: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Type: 事件集类型
        :type Type: str
        :param _PayMode: 计费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _ConnectionBriefs: 连接器基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectionBriefs: list of ConnectionBrief
        :param _TargetBriefs: 目标简要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetBriefs: list of TargetBrief
        """
        self._ModTime = None
        self._Description = None
        self._AddTime = None
        self._EventBusName = None
        self._EventBusId = None
        self._Type = None
        self._PayMode = None
        self._ConnectionBriefs = None
        self._TargetBriefs = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ConnectionBriefs(self):
        return self._ConnectionBriefs

    @ConnectionBriefs.setter
    def ConnectionBriefs(self, ConnectionBriefs):
        self._ConnectionBriefs = ConnectionBriefs

    @property
    def TargetBriefs(self):
        return self._TargetBriefs

    @TargetBriefs.setter
    def TargetBriefs(self, TargetBriefs):
        self._TargetBriefs = TargetBriefs


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._Description = params.get("Description")
        self._AddTime = params.get("AddTime")
        self._EventBusName = params.get("EventBusName")
        self._EventBusId = params.get("EventBusId")
        self._Type = params.get("Type")
        self._PayMode = params.get("PayMode")
        if params.get("ConnectionBriefs") is not None:
            self._ConnectionBriefs = []
            for item in params.get("ConnectionBriefs"):
                obj = ConnectionBrief()
                obj._deserialize(item)
                self._ConnectionBriefs.append(obj)
        if params.get("TargetBriefs") is not None:
            self._TargetBriefs = []
            for item in params.get("TargetBriefs"):
                obj = TargetBrief()
                obj._deserialize(item)
                self._TargetBriefs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Extraction(AbstractModel):
    """描述如何提取数据

    """

    def __init__(self):
        r"""
        :param _ExtractionInputPath: JsonPath, 不指定则使用默认值$.
        :type ExtractionInputPath: str
        :param _Format: 取值: TEXT/JSON
        :type Format: str
        :param _TextParams: 仅在Text需要传递
注意：此字段可能返回 null，表示取不到有效值。
        :type TextParams: :class:`tencentcloud.eb.v20210416.models.TextParams`
        """
        self._ExtractionInputPath = None
        self._Format = None
        self._TextParams = None

    @property
    def ExtractionInputPath(self):
        return self._ExtractionInputPath

    @ExtractionInputPath.setter
    def ExtractionInputPath(self, ExtractionInputPath):
        self._ExtractionInputPath = ExtractionInputPath

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TextParams(self):
        return self._TextParams

    @TextParams.setter
    def TextParams(self, TextParams):
        self._TextParams = TextParams


    def _deserialize(self, params):
        self._ExtractionInputPath = params.get("ExtractionInputPath")
        self._Format = params.get("Format")
        if params.get("TextParams") is not None:
            self._TextParams = TextParams()
            self._TextParams._deserialize(params.get("TextParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    * 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    * 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        :param _Name: 过滤键的名称。
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusRequest(AbstractModel):
    """GetEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        """
        self._EventBusId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEventBusResponse(AbstractModel):
    """GetEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModTime: 更新时间
        :type ModTime: str
        :param _Description: 事件集描述
        :type Description: str
        :param _ClsTopicId: 日志主题ID
        :type ClsTopicId: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _ClsLogsetId: 日志集ID
        :type ClsLogsetId: str
        :param _EventBusName: 事件集名称
        :type EventBusName: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Type: （已废弃）事件集类型
        :type Type: str
        :param _PayMode: 计费模式
        :type PayMode: str
        :param _SaveDays: EB日志存储时长
注意：此字段可能返回 null，表示取不到有效值。
        :type SaveDays: int
        :param _LogTopicId: EB日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        :param _EnableStore: 是否开启存储
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableStore: bool
        :param _LinkMode: 消息序列，是否有序
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkMode: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModTime = None
        self._Description = None
        self._ClsTopicId = None
        self._AddTime = None
        self._ClsLogsetId = None
        self._EventBusName = None
        self._EventBusId = None
        self._Type = None
        self._PayMode = None
        self._SaveDays = None
        self._LogTopicId = None
        self._EnableStore = None
        self._LinkMode = None
        self._RequestId = None

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ClsTopicId(self):
        return self._ClsTopicId

    @ClsTopicId.setter
    def ClsTopicId(self, ClsTopicId):
        self._ClsTopicId = ClsTopicId

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ClsLogsetId(self):
        return self._ClsLogsetId

    @ClsLogsetId.setter
    def ClsLogsetId(self, ClsLogsetId):
        self._ClsLogsetId = ClsLogsetId

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def SaveDays(self):
        return self._SaveDays

    @SaveDays.setter
    def SaveDays(self, SaveDays):
        self._SaveDays = SaveDays

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def EnableStore(self):
        return self._EnableStore

    @EnableStore.setter
    def EnableStore(self, EnableStore):
        self._EnableStore = EnableStore

    @property
    def LinkMode(self):
        return self._LinkMode

    @LinkMode.setter
    def LinkMode(self, LinkMode):
        self._LinkMode = LinkMode

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ModTime = params.get("ModTime")
        self._Description = params.get("Description")
        self._ClsTopicId = params.get("ClsTopicId")
        self._AddTime = params.get("AddTime")
        self._ClsLogsetId = params.get("ClsLogsetId")
        self._EventBusName = params.get("EventBusName")
        self._EventBusId = params.get("EventBusId")
        self._Type = params.get("Type")
        self._PayMode = params.get("PayMode")
        self._SaveDays = params.get("SaveDays")
        self._LogTopicId = params.get("LogTopicId")
        self._EnableStore = params.get("EnableStore")
        self._LinkMode = params.get("LinkMode")
        self._RequestId = params.get("RequestId")


class GetRuleRequest(AbstractModel):
    """GetRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleId: 事件规则ID
        :type RuleId: str
        """
        self._EventBusId = None
        self._RuleId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuleResponse(AbstractModel):
    """GetRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集id
        :type EventBusId: str
        :param _RuleId: 事件规则id
        :type RuleId: str
        :param _RuleName: 事件规则名称
        :type RuleName: str
        :param _Status: 事件规则状态
        :type Status: str
        :param _Enable: 使能开关
        :type Enable: bool
        :param _Description: 事件规则描述
        :type Description: str
        :param _EventPattern: 事件模式
        :type EventPattern: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _ModTime: 更新时间
        :type ModTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventBusId = None
        self._RuleId = None
        self._RuleName = None
        self._Status = None
        self._Enable = None
        self._Description = None
        self._EventPattern = None
        self._AddTime = None
        self._ModTime = None
        self._RequestId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._EventPattern = params.get("EventPattern")
        self._AddTime = params.get("AddTime")
        self._ModTime = params.get("ModTime")
        self._RequestId = params.get("RequestId")


class GetTransformationRequest(AbstractModel):
    """GetTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _TransformationId: 转换器id
        :type TransformationId: str
        """
        self._EventBusId = None
        self._RuleId = None
        self._TransformationId = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TransformationId = params.get("TransformationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTransformationResponse(AbstractModel):
    """GetTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Transformations: 转换规则列表
        :type Transformations: list of Transformation
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Transformations = None
        self._RequestId = None

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        self._RequestId = params.get("RequestId")


class ListConnectionsRequest(AbstractModel):
    """ListConnections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _OrderBy: 根据哪个字段进行返回结果排序，目前支持如下以下字段：AddTime, ModTime
        :type OrderBy: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC 和 DESC
        :type Order: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._EventBusId = None
        self._OrderBy = None
        self._Limit = None
        self._Order = None
        self._Offset = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConnectionsResponse(AbstractModel):
    """ListConnections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Connections: 连接器信息
        :type Connections: list of Connection
        :param _TotalCount: 连接器总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Connections = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Connections(self):
        return self._Connections

    @Connections.setter
    def Connections(self, Connections):
        self._Connections = Connections

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Connections") is not None:
            self._Connections = []
            for item in params.get("Connections"):
                obj = Connection()
                obj._deserialize(item)
                self._Connections.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListEventBusesRequest(AbstractModel):
    """ListEventBuses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime（创建时间）, ModTime（修改时间）
        :type OrderBy: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC（升序） 和 DESC（降序）
        :type Order: str
        :param _Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 分页偏移量，默认为0。
        :type Offset: int
        """
        self._OrderBy = None
        self._Limit = None
        self._Order = None
        self._Filters = None
        self._Offset = None

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEventBusesResponse(AbstractModel):
    """ListEventBuses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBuses: 事件集信息
        :type EventBuses: list of EventBus
        :param _TotalCount: 事件集总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EventBuses = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def EventBuses(self):
        return self._EventBuses

    @EventBuses.setter
    def EventBuses(self, EventBuses):
        self._EventBuses = EventBuses

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EventBuses") is not None:
            self._EventBuses = []
            for item in params.get("EventBuses"):
                obj = EventBus()
                obj._deserialize(item)
                self._EventBuses.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListRulesRequest(AbstractModel):
    """ListRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime（创建时间）, ModTime（修改时间）
        :type OrderBy: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 分页偏移量，默认为0。
        :type Offset: int
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC（升序） 和 DESC（降序）
        :type Order: str
        """
        self._EventBusId = None
        self._OrderBy = None
        self._Limit = None
        self._Offset = None
        self._Order = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._OrderBy = params.get("OrderBy")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRulesResponse(AbstractModel):
    """ListRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 事件规则信息
        :type Rules: list of Rule
        :param _TotalCount: 事件规则总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListTargetsRequest(AbstractModel):
    """ListTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _OrderBy: 根据哪个字段进行返回结果排序,支持以下字段：AddTime（创建时间）, ModTime（修改时间）
        :type OrderBy: str
        :param _RuleId: 事件规则ID
        :type RuleId: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 分页偏移量，默认为0。
        :type Offset: int
        :param _Order: 以升序还是降序的方式返回结果，可选值 ASC（升序） 和 DESC（降序）
        :type Order: str
        """
        self._EventBusId = None
        self._OrderBy = None
        self._RuleId = None
        self._Limit = None
        self._Offset = None
        self._Order = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._OrderBy = params.get("OrderBy")
        self._RuleId = params.get("RuleId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTargetsResponse(AbstractModel):
    """ListTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 目标总数
        :type TotalCount: int
        :param _Targets: 目标信息
        :type Targets: list of Target
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Targets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """日志查询相关接口filter参数定义

    """

    def __init__(self):
        r"""
        :param _Key: 过滤字段名称
        :type Key: str
        :param _Operator: 运算符，全等 eq，不等 neq，相似 like，排除相似 not like,  小于 lt，小于且等于 lte，大于 gt，大于且等于 gte，在范围内 range，不在范围内 norange
        :type Operator: str
        :param _Value: 过滤值,范围运算需要同时输入两个值，以英文逗号分隔

        :type Value: str
        :param _Type: 该层级filters逻辑关系，取值 "AND" 或 "OR"
        :type Type: str
        :param _Filters: LogFilters数组
        :type Filters: list of LogFilters
        """
        self._Key = None
        self._Operator = None
        self._Value = None
        self._Type = None
        self._Filters = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        self._Type = params.get("Type")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = LogFilters()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogFilters(AbstractModel):
    """日志存储过滤条件

    """

    def __init__(self):
        r"""
        :param _Key: 过滤字段名称
        :type Key: str
        :param _Operator: 运算符, 全等 eq，不等 neq，相似 like，排除相似 not like,  小于 lt，小于且等于 lte，大于 gt，大于且等于 gte，在范围内 range，不在范围内 norange
        :type Operator: str
        :param _Value: 过滤值，范围运算需要同时输入两个值，以英文逗号分隔

        :type Value: str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputStructParam(AbstractModel):
    """Transform输出参数

    """

    def __init__(self):
        r"""
        :param _Key: 对应输出json中的key
        :type Key: str
        :param _Value: 可以填json-path也可以支持常量或者内置关键字date类型
        :type Value: str
        :param _ValueType: value的数据类型, 可选值: STRING, NUMBER,BOOLEAN,NULL,SYS_VARIABLE,JSONPATH
        :type ValueType: str
        """
        self._Key = None
        self._Value = None
        self._ValueType = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishEventRequest(AbstractModel):
    """PublishEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventList: 事件列表
        :type EventList: list of Event
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        """
        self._EventList = None
        self._EventBusId = None

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = Event()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishEventResponse(AbstractModel):
    """PublishEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PutEventsRequest(AbstractModel):
    """PutEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventList: 事件列表
        :type EventList: list of Event
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        """
        self._EventList = None
        self._EventBusId = None

    @property
    def EventList(self):
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = Event()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._EventBusId = params.get("EventBusId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutEventsResponse(AbstractModel):
    """PutEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RetryPolicy(AbstractModel):
    """用来描述一个ckafka投递目标的重试策略

    """

    def __init__(self):
        r"""
        :param _RetryInterval: 重试间隔 单位:秒
        :type RetryInterval: int
        :param _MaxRetryAttempts: 最大重试次数
        :type MaxRetryAttempts: int
        """
        self._RetryInterval = None
        self._MaxRetryAttempts = None

    @property
    def RetryInterval(self):
        return self._RetryInterval

    @RetryInterval.setter
    def RetryInterval(self, RetryInterval):
        self._RetryInterval = RetryInterval

    @property
    def MaxRetryAttempts(self):
        return self._MaxRetryAttempts

    @MaxRetryAttempts.setter
    def MaxRetryAttempts(self, MaxRetryAttempts):
        self._MaxRetryAttempts = MaxRetryAttempts


    def _deserialize(self, params):
        self._RetryInterval = params.get("RetryInterval")
        self._MaxRetryAttempts = params.get("MaxRetryAttempts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Rule(AbstractModel):
    """规则信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态
        :type Status: str
        :param _ModTime: 修改时间
        :type ModTime: str
        :param _Enable: 使能开关
        :type Enable: bool
        :param _Description: 描述
        :type Description: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AddTime: 创建时间
        :type AddTime: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Targets: Target 简要信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of TargetBrief
        :param _DeadLetterConfig: rule设置的dlq规则. 可能为null
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadLetterConfig: :class:`tencentcloud.eb.v20210416.models.DeadLetterConfig`
        """
        self._Status = None
        self._ModTime = None
        self._Enable = None
        self._Description = None
        self._RuleId = None
        self._AddTime = None
        self._EventBusId = None
        self._RuleName = None
        self._Targets = None
        self._DeadLetterConfig = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ModTime(self):
        return self._ModTime

    @ModTime.setter
    def ModTime(self, ModTime):
        self._ModTime = ModTime

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AddTime(self):
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DeadLetterConfig(self):
        return self._DeadLetterConfig

    @DeadLetterConfig.setter
    def DeadLetterConfig(self, DeadLetterConfig):
        self._DeadLetterConfig = DeadLetterConfig


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ModTime = params.get("ModTime")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._RuleId = params.get("RuleId")
        self._AddTime = params.get("AddTime")
        self._EventBusId = params.get("EventBusId")
        self._RuleName = params.get("RuleName")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetBrief()
                obj._deserialize(item)
                self._Targets.append(obj)
        if params.get("DeadLetterConfig") is not None:
            self._DeadLetterConfig = DeadLetterConfig()
            self._DeadLetterConfig._deserialize(params.get("DeadLetterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SCFParams(AbstractModel):
    """云函数参数

    """

    def __init__(self):
        r"""
        :param _BatchTimeout: 批量投递最长等待时间
        :type BatchTimeout: int
        :param _BatchEventCount: 批量投递最大事件条数
        :type BatchEventCount: int
        :param _EnableBatchDelivery: 开启批量投递使能
        :type EnableBatchDelivery: bool
        """
        self._BatchTimeout = None
        self._BatchEventCount = None
        self._EnableBatchDelivery = None

    @property
    def BatchTimeout(self):
        return self._BatchTimeout

    @BatchTimeout.setter
    def BatchTimeout(self, BatchTimeout):
        self._BatchTimeout = BatchTimeout

    @property
    def BatchEventCount(self):
        return self._BatchEventCount

    @BatchEventCount.setter
    def BatchEventCount(self, BatchEventCount):
        self._BatchEventCount = BatchEventCount

    @property
    def EnableBatchDelivery(self):
        return self._EnableBatchDelivery

    @EnableBatchDelivery.setter
    def EnableBatchDelivery(self, EnableBatchDelivery):
        self._EnableBatchDelivery = EnableBatchDelivery


    def _deserialize(self, params):
        self._BatchTimeout = params.get("BatchTimeout")
        self._BatchEventCount = params.get("BatchEventCount")
        self._EnableBatchDelivery = params.get("EnableBatchDelivery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogRequest(AbstractModel):
    """SearchLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间unix 毫秒时间戳
        :type StartTime: int
        :param _EndTime: 结束时间unix 毫秒时间戳
        :type EndTime: int
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Page: 页码
        :type Page: int
        :param _Limit: 每页数据大小
        :type Limit: int
        :param _Filter: 筛选条件
        :type Filter: list of LogFilter
        :param _OrderFields: 排序数组
        :type OrderFields: list of str
        :param _OrderBy: 排序方式，asc 从旧到新，desc 从新到旧
        :type OrderBy: str
        """
        self._StartTime = None
        self._EndTime = None
        self._EventBusId = None
        self._Page = None
        self._Limit = None
        self._Filter = None
        self._OrderFields = None
        self._OrderBy = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def OrderFields(self):
        return self._OrderFields

    @OrderFields.setter
    def OrderFields(self, OrderFields):
        self._OrderFields = OrderFields

    @property
    def OrderBy(self):
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._EventBusId = params.get("EventBusId")
        self._Page = params.get("Page")
        self._Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = LogFilter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._OrderFields = params.get("OrderFields")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchLogResponse(AbstractModel):
    """SearchLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 日志总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Limit: 每页日志条数
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _Page: 页码
注意：此字段可能返回 null，表示取不到有效值。
        :type Page: int
        :param _Results: 日志检索结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of SearchLogResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Limit = None
        self._Page = None
        self._Results = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Page(self):
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Limit = params.get("Limit")
        self._Page = params.get("Page")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = SearchLogResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class SearchLogResult(AbstractModel):
    """日志检索详情

    """

    def __init__(self):
        r"""
        :param _Timestamp: 单条日志上报时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param _Message: 日志内容详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _Source: 事件来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Type: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _RuleIds: 事件匹配规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleIds: str
        :param _Subject: 实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Subject: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: 事件状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Timestamp = None
        self._Message = None
        self._Source = None
        self._Type = None
        self._RuleIds = None
        self._Subject = None
        self._Region = None
        self._Status = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RuleIds(self):
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def Subject(self):
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._Message = params.get("Message")
        self._Source = params.get("Source")
        self._Type = params.get("Type")
        self._RuleIds = params.get("RuleIds")
        self._Subject = params.get("Subject")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """Target信息

    """

    def __init__(self):
        r"""
        :param _Type: 目标类型
        :type Type: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _TargetId: 目标ID
        :type TargetId: str
        :param _TargetDescription: 目标描述
        :type TargetDescription: :class:`tencentcloud.eb.v20210416.models.TargetDescription`
        :param _RuleId: 事件规则ID
        :type RuleId: str
        :param _EnableBatchDelivery: 开启批量投递使能
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableBatchDelivery: bool
        :param _BatchTimeout: 批量投递最长等待时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchTimeout: int
        :param _BatchEventCount: 批量投递最大事件条数
注意：此字段可能返回 null，表示取不到有效值。
        :type BatchEventCount: int
        """
        self._Type = None
        self._EventBusId = None
        self._TargetId = None
        self._TargetDescription = None
        self._RuleId = None
        self._EnableBatchDelivery = None
        self._BatchTimeout = None
        self._BatchEventCount = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetDescription(self):
        return self._TargetDescription

    @TargetDescription.setter
    def TargetDescription(self, TargetDescription):
        self._TargetDescription = TargetDescription

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EnableBatchDelivery(self):
        return self._EnableBatchDelivery

    @EnableBatchDelivery.setter
    def EnableBatchDelivery(self, EnableBatchDelivery):
        self._EnableBatchDelivery = EnableBatchDelivery

    @property
    def BatchTimeout(self):
        return self._BatchTimeout

    @BatchTimeout.setter
    def BatchTimeout(self, BatchTimeout):
        self._BatchTimeout = BatchTimeout

    @property
    def BatchEventCount(self):
        return self._BatchEventCount

    @BatchEventCount.setter
    def BatchEventCount(self, BatchEventCount):
        self._BatchEventCount = BatchEventCount


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._EventBusId = params.get("EventBusId")
        self._TargetId = params.get("TargetId")
        if params.get("TargetDescription") is not None:
            self._TargetDescription = TargetDescription()
            self._TargetDescription._deserialize(params.get("TargetDescription"))
        self._RuleId = params.get("RuleId")
        self._EnableBatchDelivery = params.get("EnableBatchDelivery")
        self._BatchTimeout = params.get("BatchTimeout")
        self._BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetBrief(AbstractModel):
    """目标简要信息

    """

    def __init__(self):
        r"""
        :param _TargetId: 目标ID
        :type TargetId: str
        :param _Type: 目标类型
        :type Type: str
        """
        self._TargetId = None
        self._Type = None

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetDescription(AbstractModel):
    """TargetDescription描述

    """

    def __init__(self):
        r"""
        :param _ResourceDescription: QCS资源六段式，更多参考 [资源六段式](https://cloud.tencent.com/document/product/598/10606)
        :type ResourceDescription: str
        :param _SCFParams: 云函数参数
        :type SCFParams: :class:`tencentcloud.eb.v20210416.models.SCFParams`
        :param _CkafkaTargetParams: Ckafka参数
        :type CkafkaTargetParams: :class:`tencentcloud.eb.v20210416.models.CkafkaTargetParams`
        :param _ESTargetParams: ElasticSearch参数
        :type ESTargetParams: :class:`tencentcloud.eb.v20210416.models.ESTargetParams`
        """
        self._ResourceDescription = None
        self._SCFParams = None
        self._CkafkaTargetParams = None
        self._ESTargetParams = None

    @property
    def ResourceDescription(self):
        return self._ResourceDescription

    @ResourceDescription.setter
    def ResourceDescription(self, ResourceDescription):
        self._ResourceDescription = ResourceDescription

    @property
    def SCFParams(self):
        return self._SCFParams

    @SCFParams.setter
    def SCFParams(self, SCFParams):
        self._SCFParams = SCFParams

    @property
    def CkafkaTargetParams(self):
        return self._CkafkaTargetParams

    @CkafkaTargetParams.setter
    def CkafkaTargetParams(self, CkafkaTargetParams):
        self._CkafkaTargetParams = CkafkaTargetParams

    @property
    def ESTargetParams(self):
        return self._ESTargetParams

    @ESTargetParams.setter
    def ESTargetParams(self, ESTargetParams):
        self._ESTargetParams = ESTargetParams


    def _deserialize(self, params):
        self._ResourceDescription = params.get("ResourceDescription")
        if params.get("SCFParams") is not None:
            self._SCFParams = SCFParams()
            self._SCFParams._deserialize(params.get("SCFParams"))
        if params.get("CkafkaTargetParams") is not None:
            self._CkafkaTargetParams = CkafkaTargetParams()
            self._CkafkaTargetParams._deserialize(params.get("CkafkaTargetParams"))
        if params.get("ESTargetParams") is not None:
            self._ESTargetParams = ESTargetParams()
            self._ESTargetParams._deserialize(params.get("ESTargetParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextParams(AbstractModel):
    """描述如何切分数据

    """

    def __init__(self):
        r"""
        :param _Separator: 逗号、| 、制表符、空格、换行符、%、#，限制长度为 1。
注意：此字段可能返回 null，表示取不到有效值。
        :type Separator: str
        :param _Regex: 填写正则表达式：长度128
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        """
        self._Separator = None
        self._Regex = None

    @property
    def Separator(self):
        return self._Separator

    @Separator.setter
    def Separator(self, Separator):
        self._Separator = Separator

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex


    def _deserialize(self, params):
        self._Separator = params.get("Separator")
        self._Regex = params.get("Regex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transform(AbstractModel):
    """描述如何数据转换

    """

    def __init__(self):
        r"""
        :param _OutputStructs: 描述如何数据转换
        :type OutputStructs: list of OutputStructParam
        """
        self._OutputStructs = None

    @property
    def OutputStructs(self):
        return self._OutputStructs

    @OutputStructs.setter
    def OutputStructs(self, OutputStructs):
        self._OutputStructs = OutputStructs


    def _deserialize(self, params):
        if params.get("OutputStructs") is not None:
            self._OutputStructs = []
            for item in params.get("OutputStructs"):
                obj = OutputStructParam()
                obj._deserialize(item)
                self._OutputStructs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Transformation(AbstractModel):
    """一个转换器

    """

    def __init__(self):
        r"""
        :param _Extraction: 描述如何提取数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Extraction: :class:`tencentcloud.eb.v20210416.models.Extraction`
        :param _EtlFilter: 描述如何过滤数据
注意：此字段可能返回 null，表示取不到有效值。
        :type EtlFilter: :class:`tencentcloud.eb.v20210416.models.EtlFilter`
        :param _Transform: 描述如何数据转换
注意：此字段可能返回 null，表示取不到有效值。
        :type Transform: :class:`tencentcloud.eb.v20210416.models.Transform`
        """
        self._Extraction = None
        self._EtlFilter = None
        self._Transform = None

    @property
    def Extraction(self):
        return self._Extraction

    @Extraction.setter
    def Extraction(self, Extraction):
        self._Extraction = Extraction

    @property
    def EtlFilter(self):
        return self._EtlFilter

    @EtlFilter.setter
    def EtlFilter(self, EtlFilter):
        self._EtlFilter = EtlFilter

    @property
    def Transform(self):
        return self._Transform

    @Transform.setter
    def Transform(self, Transform):
        self._Transform = Transform


    def _deserialize(self, params):
        if params.get("Extraction") is not None:
            self._Extraction = Extraction()
            self._Extraction._deserialize(params.get("Extraction"))
        if params.get("EtlFilter") is not None:
            self._EtlFilter = EtlFilter()
            self._EtlFilter._deserialize(params.get("EtlFilter"))
        if params.get("Transform") is not None:
            self._Transform = Transform()
            self._Transform._deserialize(params.get("Transform"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionRequest(AbstractModel):
    """UpdateConnection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConnectionId: 连接器ID
        :type ConnectionId: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Enable: 使能开关
        :type Enable: bool
        :param _Description: 描述
        :type Description: str
        :param _ConnectionName: 连接器名称
        :type ConnectionName: str
        """
        self._ConnectionId = None
        self._EventBusId = None
        self._Enable = None
        self._Description = None
        self._ConnectionName = None

    @property
    def ConnectionId(self):
        return self._ConnectionId

    @ConnectionId.setter
    def ConnectionId(self, ConnectionId):
        self._ConnectionId = ConnectionId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConnectionName(self):
        return self._ConnectionName

    @ConnectionName.setter
    def ConnectionName(self, ConnectionName):
        self._ConnectionName = ConnectionName


    def _deserialize(self, params):
        self._ConnectionId = params.get("ConnectionId")
        self._EventBusId = params.get("EventBusId")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._ConnectionName = params.get("ConnectionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConnectionResponse(AbstractModel):
    """UpdateConnection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateEventBusRequest(AbstractModel):
    """UpdateEventBus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Description: 事件集描述，不限字符类型，200字符描述以内
        :type Description: str
        :param _EventBusName: 事件集名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type EventBusName: str
        :param _SaveDays: EB日志存储时长
        :type SaveDays: int
        :param _LogTopicId: EB日志主题ID
        :type LogTopicId: str
        :param _EnableStore: 是否开启存储
        :type EnableStore: bool
        """
        self._EventBusId = None
        self._Description = None
        self._EventBusName = None
        self._SaveDays = None
        self._LogTopicId = None
        self._EnableStore = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EventBusName(self):
        return self._EventBusName

    @EventBusName.setter
    def EventBusName(self, EventBusName):
        self._EventBusName = EventBusName

    @property
    def SaveDays(self):
        return self._SaveDays

    @SaveDays.setter
    def SaveDays(self, SaveDays):
        self._SaveDays = SaveDays

    @property
    def LogTopicId(self):
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId

    @property
    def EnableStore(self):
        return self._EnableStore

    @EnableStore.setter
    def EnableStore(self, EnableStore):
        self._EnableStore = EnableStore


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._Description = params.get("Description")
        self._EventBusName = params.get("EventBusName")
        self._SaveDays = params.get("SaveDays")
        self._LogTopicId = params.get("LogTopicId")
        self._EnableStore = params.get("EnableStore")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEventBusResponse(AbstractModel):
    """UpdateEventBus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateRuleRequest(AbstractModel):
    """UpdateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 事件规则ID
        :type RuleId: str
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _Enable: 使能开关。
        :type Enable: bool
        :param _Description: 规则描述，不限字符类型，200字符描述以内。
        :type Description: str
        :param _EventPattern: 参考：[事件模式](https://cloud.tencent.com/document/product/1359/56084)
        :type EventPattern: str
        :param _RuleName: 事件规则名称，只能包含字母、数字、下划线、连字符，以字母开头，以数字或字母结尾，2~60个字符
        :type RuleName: str
        """
        self._RuleId = None
        self._EventBusId = None
        self._Enable = None
        self._Description = None
        self._EventPattern = None
        self._RuleName = None

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def Enable(self):
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EventPattern(self):
        return self._EventPattern

    @EventPattern.setter
    def EventPattern(self, EventPattern):
        self._EventPattern = EventPattern

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._EventBusId = params.get("EventBusId")
        self._Enable = params.get("Enable")
        self._Description = params.get("Description")
        self._EventPattern = params.get("EventPattern")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRuleResponse(AbstractModel):
    """UpdateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateTargetRequest(AbstractModel):
    """UpdateTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleId: 事件规则ID
        :type RuleId: str
        :param _TargetId: 事件目标ID
        :type TargetId: str
        :param _EnableBatchDelivery: 开启批量投递使能
        :type EnableBatchDelivery: bool
        :param _BatchTimeout: 批量投递最长等待时间
        :type BatchTimeout: int
        :param _BatchEventCount: 批量投递最大事件条数
        :type BatchEventCount: int
        """
        self._EventBusId = None
        self._RuleId = None
        self._TargetId = None
        self._EnableBatchDelivery = None
        self._BatchTimeout = None
        self._BatchEventCount = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TargetId(self):
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def EnableBatchDelivery(self):
        return self._EnableBatchDelivery

    @EnableBatchDelivery.setter
    def EnableBatchDelivery(self, EnableBatchDelivery):
        self._EnableBatchDelivery = EnableBatchDelivery

    @property
    def BatchTimeout(self):
        return self._BatchTimeout

    @BatchTimeout.setter
    def BatchTimeout(self, BatchTimeout):
        self._BatchTimeout = BatchTimeout

    @property
    def BatchEventCount(self):
        return self._BatchEventCount

    @BatchEventCount.setter
    def BatchEventCount(self, BatchEventCount):
        self._BatchEventCount = BatchEventCount


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TargetId = params.get("TargetId")
        self._EnableBatchDelivery = params.get("EnableBatchDelivery")
        self._BatchTimeout = params.get("BatchTimeout")
        self._BatchEventCount = params.get("BatchEventCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTargetResponse(AbstractModel):
    """UpdateTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateTransformationRequest(AbstractModel):
    """UpdateTransformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EventBusId: 事件集ID
        :type EventBusId: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _TransformationId: 转换器id
        :type TransformationId: str
        :param _Transformations: 一个转换规则列表，当前仅限定一个
        :type Transformations: list of Transformation
        """
        self._EventBusId = None
        self._RuleId = None
        self._TransformationId = None
        self._Transformations = None

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def RuleId(self):
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TransformationId(self):
        return self._TransformationId

    @TransformationId.setter
    def TransformationId(self, TransformationId):
        self._TransformationId = TransformationId

    @property
    def Transformations(self):
        return self._Transformations

    @Transformations.setter
    def Transformations(self, Transformations):
        self._Transformations = Transformations


    def _deserialize(self, params):
        self._EventBusId = params.get("EventBusId")
        self._RuleId = params.get("RuleId")
        self._TransformationId = params.get("TransformationId")
        if params.get("Transformations") is not None:
            self._Transformations = []
            for item in params.get("Transformations"):
                obj = Transformation()
                obj._deserialize(item)
                self._Transformations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateTransformationResponse(AbstractModel):
    """UpdateTransformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")