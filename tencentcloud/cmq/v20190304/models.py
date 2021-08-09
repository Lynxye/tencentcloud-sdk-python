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


class ClearQueueRequest(AbstractModel):
    """ClearQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearQueueResponse(AbstractModel):
    """ClearQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearSubscriptionFilterTagsRequest(AbstractModel):
    """ClearSubscriptionFilterTags请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearSubscriptionFilterTagsResponse(AbstractModel):
    """ClearSubscriptionFilterTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateQueueRequest(AbstractModel):
    """CreateQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。\n        :type PollingWaitSeconds: int\n        :param VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。\n        :type MsgRetentionSeconds: int\n        :param RewindSeconds: 队列是否开启回溯消息能力，该参数取值范围0-msgRetentionSeconds,即最大的回溯时间为消息在队列中的保留周期，0表示不开启。\n        :type RewindSeconds: int\n        :param Transaction: 1 表示事务队列，0 表示普通队列\n        :type Transaction: int\n        :param FirstQueryInterval: 第一次回查间隔\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: 最大回查次数\n        :type MaxQueryCount: int\n        :param DeadLetterQueueName: 死信队列名称\n        :type DeadLetterQueueName: str\n        :param Policy: 死信策略。0为消息被多次消费未删除，1为Time-To-Live过期\n        :type Policy: int\n        :param MaxReceiveCount: 最大接收次数 1-1000\n        :type MaxReceiveCount: int\n        :param MaxTimeToLive: policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds\n        :type MaxTimeToLive: int\n        :param Trace: 是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为true表示开启，为false表示不开启\n        :type Trace: bool\n        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.Transaction = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.Policy = None
        self.MaxReceiveCount = None
        self.MaxTimeToLive = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.Transaction = params.get("Transaction")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Policy = params.get("Policy")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQueueResponse(AbstractModel):
    """CreateQueue返回参数结构体

    """

    def __init__(self):
        """
        :param QueueId: 创建成功的queueId\n        :type QueueId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.QueueId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        :param Protocol: 订阅的协议，目前支持两种协议：http、queue。使用http协议，用户需自己搭建接受消息的web server。使用queue，消息会自动推送到CMQ queue，用户可以并发地拉取消息。\n        :type Protocol: str\n        :param Endpoint: 接收通知的Endpoint，根据协议Protocol区分：对于http，Endpoint必须以“`http://`”开头，host可以是域名或IP；对于Queue，则填QueueName。 请注意，目前推送服务不能推送到私有网络中，因此Endpoint填写为私有网络域名或地址将接收不到推送的消息，目前支持推送到公网和基础网络。\n        :type Endpoint: str\n        :param NotifyStrategy: 向Endpoint推送消息出现错误时，CMQ推送服务器的重试策略。取值有：1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s...由于Topic消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是EXPONENTIAL_DECAY_RETRY。\n        :type NotifyStrategy: str\n        :param FilterTag: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。\n        :type FilterTag: list of str\n        :param BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。\n        :type BindingKey: list of str\n        :param NotifyContentFormat: 推送内容的格式。取值：1）JSON；2）SIMPLIFIED，即raw格式。如果Protocol是queue，则取值必须为SIMPLIFIED。如果Protocol是http，两个值均可以，默认值是JSON。\n        :type NotifyContentFormat: str\n        """
        self.TopicName = None
        self.SubscriptionName = None
        self.Protocol = None
        self.Endpoint = None
        self.NotifyStrategy = None
        self.FilterTag = None
        self.BindingKey = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.Protocol = params.get("Protocol")
        self.Endpoint = params.get("Endpoint")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.FilterTag = params.get("FilterTag")
        self.BindingKey = params.get("BindingKey")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param SubscriptionId: SubscriptionId\n        :type SubscriptionId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubscriptionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscriptionId = params.get("SubscriptionId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。\n        :type MaxMsgSize: int\n        :param FilterType: 用于指定主题的消息匹配策略。1：表示标签匹配策略；2：表示路由匹配策略，默认值为标签匹配策略。\n        :type FilterType: int\n        :param MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。\n        :type MsgRetentionSeconds: int\n        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。\n        :type Trace: bool\n        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.FilterType = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.FilterType = params.get("FilterType")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: TopicName\n        :type TopicId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeadLetterPolicy(AbstractModel):
    """DeadLetterPolicy

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: 死信队列名字。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterQueueName: str\n        :param DeadLetterQueue: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterQueue: str\n        :param Policy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Policy: int\n        :param MaxTimeToLive: 最大未消费过期时间。Policy为1时必选。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxTimeToLive: int\n        :param MaxReceiveCount: 最大接收次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxReceiveCount: int\n        """
        self.DeadLetterQueueName = None
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.DeadLetterQueue = params.get("DeadLetterQueue")
        self.Policy = params.get("Policy")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeadLetterSource(AbstractModel):
    """DeadLetterSource

    """

    def __init__(self):
        """
        :param QueueId: 消息队列ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueueId: str\n        :param QueueName: 消息队列名字。
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueueName: str\n        """
        self.QueueId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubscribeRequest(AbstractModel):
    """DeleteSubscribe请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscribeResponse(AbstractModel):
    """DeleteSubscribe返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type TopicName: str\n        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeDeadLetterSourceQueues请求参数结构体

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: 死信队列名称\n        :type DeadLetterQueueName: str\n        :param Limit: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。\n        :type Limit: int\n        :param Offset: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Offset: int\n        :param Filters: 过滤死信队列源队列名称，目前仅支持SourceQueueName过滤\n        :type Filters: list of Filter\n        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeDeadLetterSourceQueues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足本次条件的队列个数\n        :type TotalCount: int\n        :param QueueSet: 死信队列源队列\n        :type QueueSet: list of DeadLetterSource\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0\n        :type Offset: int\n        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Limit: int\n        :param Filters: 筛选参数，目前支持QueueName筛选，且仅支持一个关键字\n        :type Filters: list of Filter\n        :param TagKey: 标签搜索\n        :type TagKey: str\n        :param QueueName: 精确匹配QueueName\n        :type QueueName: str\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.QueueName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总队列数。\n        :type TotalCount: int\n        :param QueueSet: 队列详情列表。\n        :type QueueSet: list of QueueSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueSet()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionDetailRequest(AbstractModel):
    """DescribeSubscriptionDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param Offset: 分页时本页获取主题列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0\n        :type Offset: int\n        :param Limit: 分页时本页获取主题的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Limit: int\n        :param Filters: 筛选参数，目前只支持SubscriptionName，且仅支持一个关键字。\n        :type Filters: list of Filter\n        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionDetailResponse(AbstractModel):
    """DescribeSubscriptionDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param SubscriptionSet: Subscription属性集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionSet: list of Subscription\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SubscriptionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self.SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = Subscription()
                obj._deserialize(item)
                self.SubscriptionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0。\n        :type Offset: int\n        :param Limit: 分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。\n        :type Limit: int\n        :param Filters: 目前只支持过滤TopicName ， 且只能填一个过滤值。\n        :type Filters: list of Filter\n        :param TagKey: 标签匹配。\n        :type TagKey: str\n        :param TopicName: 精确匹配TopicName。\n        :type TopicName: str\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 主题列表总数。\n        :type TotalCount: int\n        :param TopicSet: 主题详情列表。\n        :type TopicSet: list of TopicSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TopicSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicSet") is not None:
            self.TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self.TopicSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """过滤参数

    """

    def __init__(self):
        """
        :param Name: 过滤参数的名字\n        :type Name: str\n        :param Values: 数值\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeRequest(AbstractModel):
    """ModifyQueueAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。\n        :type PollingWaitSeconds: int\n        :param VisibilityTimeout: 消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: 消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: 消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。\n        :type MsgRetentionSeconds: int\n        :param RewindSeconds: 消息最长回溯时间，取值范围0-msgRetentionSeconds，消息的最大回溯之间为消息在队列中的保存周期，0表示不开启消息回溯。\n        :type RewindSeconds: int\n        :param FirstQueryInterval: 第一次查询时间\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: 最大查询次数\n        :type MaxQueryCount: int\n        :param DeadLetterQueueName: 死信队列名称\n        :type DeadLetterQueueName: str\n        :param MaxTimeToLive: MaxTimeToLivepolicy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间MsgRetentionSeconds\n        :type MaxTimeToLive: int\n        :param MaxReceiveCount: 最大接收次数\n        :type MaxReceiveCount: int\n        :param Policy: 死信队列策略\n        :type Policy: int\n        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。\n        :type Trace: bool\n        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None
        self.Policy = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.Policy = params.get("Policy")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeResponse(AbstractModel):
    """ModifyQueueAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscriptionAttributeRequest(AbstractModel):
    """ModifySubscriptionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线（-）。\n        :type TopicName: str\n        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type SubscriptionName: str\n        :param NotifyStrategy: 向 Endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值如下：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息。
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始1s，后面是2s，4s，8s···由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。\n        :type NotifyStrategy: str\n        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 Protocol 是 queue，则取值必须为 SIMPLIFIED。如果 Protocol 是 HTTP，两个值均可以，默认值是 JSON。\n        :type NotifyContentFormat: str\n        :param FilterTags: 消息正文。消息标签（用于消息过滤)。标签数量不能超过5个，每个标签不超过16个字符。与(Batch)PublishMessage的MsgTag参数配合使用，规则：1）如果FilterTag没有设置，则无论MsgTag是否有设置，订阅接收所有发布到Topic的消息；2）如果FilterTag数组有值，则只有数组中至少有一个值在MsgTag数组中也存在时（即FilterTag和MsgTag有交集），订阅才接收该发布到Topic的消息；3）如果FilterTag数组有值，但MsgTag没设置，则不接收任何发布到Topic的消息，可以认为是2）的一种特例，此时FilterTag和MsgTag没有交集。规则整体的设计思想是以订阅者的意愿为主。\n        :type FilterTags: list of str\n        :param BindingKey: BindingKey数量不超过5个， 每个BindingKey长度不超过64字节，该字段表示订阅接收消息的过滤策略，每个BindingKey最多含有15个“.”， 即最多16个词组。\n        :type BindingKey: list of str\n        """
        self.TopicName = None
        self.SubscriptionName = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None
        self.FilterTags = None
        self.BindingKey = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        self.FilterTags = params.get("FilterTags")
        self.BindingKey = params.get("BindingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscriptionAttributeResponse(AbstractModel):
    """ModifySubscriptionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributeRequest(AbstractModel):
    """ModifyTopicAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 主题名字，在单个地域同一帐号下唯一。主题名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type TopicName: str\n        :param MaxMsgSize: 消息最大长度。取值范围1024 - 65536 Byte（即1 - 64K），默认值65536。\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: 消息保存时间。取值范围60 - 86400 s（即1分钟 - 1天），默认值86400。\n        :type MsgRetentionSeconds: int\n        :param Trace: 是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。\n        :type Trace: bool\n        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributeResponse(AbstractModel):
    """ModifyTopicAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QueueSet(AbstractModel):
    """批量queue属性信息

    """

    def __init__(self):
        """
        :param QueueId: 消息队列ID。\n        :type QueueId: str\n        :param QueueName: 消息队列名字。\n        :type QueueName: str\n        :param Qps: 每秒钟生产消息条数的限制，消费消息的大小是该值的1.1倍。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Qps: int\n        :param Bps: 带宽限制。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bps: int\n        :param MaxDelaySeconds: 飞行消息最大保留时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxDelaySeconds: int\n        :param MaxMsgHeapNum: 最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: 消息接收长轮询等待时间。取值范围0 - 30秒，默认值0。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PollingWaitSeconds: int\n        :param MsgRetentionSeconds: 消息保留周期。取值范围60-1296000秒（1min-15天），默认值345600秒（4 天）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRetentionSeconds: int\n        :param VisibilityTimeout: 消息可见性超时。取值范围1 - 43200秒（即12小时内），默认值30。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: 消息最大长度。取值范围1024 - 1048576 Byte（即1K - 1024K），默认值65536。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxMsgSize: int\n        :param RewindSeconds: 回溯队列的消息回溯时间最大值，取值范围0 - 43200秒，0表示不开启消息回溯。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RewindSeconds: int\n        :param CreateTime: 队列的创建时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param LastModifyTime: 最后一次修改队列属性的时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTime: int\n        :param ActiveMsgNum: 在队列中处于 Active 状态（不处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ActiveMsgNum: int\n        :param InactiveMsgNum: 在队列中处于 Inactive 状态（正处于被消费状态）的消息总数，为近似值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InactiveMsgNum: int\n        :param DelayMsgNum: 延迟消息数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DelayMsgNum: int\n        :param RewindMsgNum: 已调用 DelMsg 接口删除，但还在回溯保留时间内的消息数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RewindMsgNum: int\n        :param MinMsgTime: 消息最小未消费时间，单位为秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinMsgTime: int\n        :param Transaction: 事务消息队列。true表示是事务消息，false表示不是事务消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Transaction: bool\n        :param DeadLetterSource: 死信队列。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterSource: list of DeadLetterSource\n        :param DeadLetterPolicy: 死信队列策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`\n        :param TransactionPolicy: 事务消息策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`\n        :param CreateUin: 创建者Uin。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: int\n        :param Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Trace: bool\n        """
        self.QueueId = None
        self.QueueName = None
        self.Qps = None
        self.Bps = None
        self.MaxDelaySeconds = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.MsgRetentionSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.RewindSeconds = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.ActiveMsgNum = None
        self.InactiveMsgNum = None
        self.DelayMsgNum = None
        self.RewindMsgNum = None
        self.MinMsgTime = None
        self.Transaction = None
        self.DeadLetterSource = None
        self.DeadLetterPolicy = None
        self.TransactionPolicy = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        self.Qps = params.get("Qps")
        self.Bps = params.get("Bps")
        self.MaxDelaySeconds = params.get("MaxDelaySeconds")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.RewindSeconds = params.get("RewindSeconds")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.ActiveMsgNum = params.get("ActiveMsgNum")
        self.InactiveMsgNum = params.get("InactiveMsgNum")
        self.DelayMsgNum = params.get("DelayMsgNum")
        self.RewindMsgNum = params.get("RewindMsgNum")
        self.MinMsgTime = params.get("MinMsgTime")
        self.Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self.DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self.DeadLetterPolicy = DeadLetterPolicy()
            self.DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self.TransactionPolicy = TransactionPolicy()
            self.TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueRequest(AbstractModel):
    """RewindQueue请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。\n        :type QueueName: str\n        :param StartConsumeTime: 设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。\n        :type StartConsumeTime: int\n        """
        self.QueueName = None
        self.StartConsumeTime = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.StartConsumeTime = params.get("StartConsumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueResponse(AbstractModel):
    """RewindQueue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """订阅返回参数

    """

    def __init__(self):
        """
        :param SubscriptionName: 订阅名字，在单个地域同一帐号的同一主题下唯一。订阅名称是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionName: str\n        :param SubscriptionId: 订阅 ID。订阅 ID 在拉取监控数据时会用到。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubscriptionId: str\n        :param TopicOwner: 订阅拥有者的 APPID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicOwner: int\n        :param MsgCount: 该订阅待投递的消息数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgCount: int\n        :param LastModifyTime: 最后一次修改订阅属性的时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTime: int\n        :param CreateTime: 订阅的创建时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param BindingKey: 表示订阅接收消息的过滤策略。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindingKey: list of str\n        :param Endpoint: 接收通知的 endpoint，根据协议 protocol 区分：对于 HTTP，endpoint 必须以http://开头，host 可以是域名或 IP；对于 queue，则填 queueName。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Endpoint: str\n        :param FilterTags: 描述用户创建订阅时选择的过滤策略：
filterType = 1表示用户使用 filterTag 标签过滤
filterType = 2表示用户使用 bindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterTags: list of str\n        :param Protocol: 订阅的协议，目前支持两种协议：HTTP、queue。使用 HTTP 协议，用户需自己搭建接受消息的 Web Server。使用 queue，消息会自动推送到 CMQ queue，用户可以并发地拉取消息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param NotifyStrategy: 向 endpoint 推送消息出现错误时，CMQ 推送服务器的重试策略。取值有：
（1）BACKOFF_RETRY，退避重试。每隔一定时间重试一次，重试够一定次数后，就把该消息丢弃，继续推送下一条消息；
（2）EXPONENTIAL_DECAY_RETRY，指数衰退重试。每次重试的间隔是指数递增的，例如开始 1s，后面是 2s，4s，8s...由于 Topic 消息的周期是一天，所以最多重试一天就把消息丢弃。默认值是 EXPONENTIAL_DECAY_RETRY。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotifyStrategy: str\n        :param NotifyContentFormat: 推送内容的格式。取值：（1）JSON；（2）SIMPLIFIED，即 raw 格式。如果 protocol 是 queue，则取值必须为 SIMPLIFIED。如果 protocol 是 HTTP，两个值均可以，默认值是 JSON。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotifyContentFormat: str\n        """
        self.SubscriptionName = None
        self.SubscriptionId = None
        self.TopicOwner = None
        self.MsgCount = None
        self.LastModifyTime = None
        self.CreateTime = None
        self.BindingKey = None
        self.Endpoint = None
        self.FilterTags = None
        self.Protocol = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.SubscriptionName = params.get("SubscriptionName")
        self.SubscriptionId = params.get("SubscriptionId")
        self.TopicOwner = params.get("TopicOwner")
        self.MsgCount = params.get("MsgCount")
        self.LastModifyTime = params.get("LastModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.BindingKey = params.get("BindingKey")
        self.Endpoint = params.get("Endpoint")
        self.FilterTags = params.get("FilterTags")
        self.Protocol = params.get("Protocol")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        """
        :param TagKey: 标签Key
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagKey: str\n        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSet(AbstractModel):
    """topic返回信息展示字段

    """

    def __init__(self):
        """
        :param TopicId: 主题的 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicId: str\n        :param TopicName: 主题名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicName: str\n        :param MsgRetentionSeconds: 消息在主题中最长存活时间，从发送到该主题开始经过此参数指定的时间后，不论消息是否被成功推送给用户都将被删除，单位为秒。固定为一天（86400秒），该属性不能修改。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgRetentionSeconds: int\n        :param MaxMsgSize: 消息最大长度。取值范围1024 - 1048576Byte（即1 - 1024K），默认值为65536。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxMsgSize: int\n        :param Qps: 每秒钟发布消息的条数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Qps: int\n        :param FilterType: 描述用户创建订阅时选择的过滤策略：
FilterType = 1表示用户使用 FilterTag 标签过滤;
FilterType = 2表示用户使用 BindingKey 过滤。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterType: int\n        :param CreateTime: 主题的创建时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: int\n        :param LastModifyTime: 最后一次修改主题属性的时间。返回 Unix 时间戳，精确到秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastModifyTime: int\n        :param MsgCount: 当前该主题中消息数目（消息堆积数）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MsgCount: int\n        :param CreateUin: 创建者 Uin，CAM 鉴权 resource 由该字段组合而成。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateUin: int\n        :param Tags: 关联的标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param Trace: 消息轨迹。true表示开启，false表示不开启。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Trace: bool\n        """
        self.TopicId = None
        self.TopicName = None
        self.MsgRetentionSeconds = None
        self.MaxMsgSize = None
        self.Qps = None
        self.FilterType = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.MsgCount = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.Qps = params.get("Qps")
        self.FilterType = params.get("FilterType")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.MsgCount = params.get("MsgCount")
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionPolicy(AbstractModel):
    """TransactionPolicy

    """

    def __init__(self):
        """
        :param FirstQueryInterval: 第一次回查时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: 最大查询次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxQueryCount: int\n        """
        self.FirstQueryInterval = None
        self.MaxQueryCount = None


    def _deserialize(self, params):
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterRequest(AbstractModel):
    """UnbindDeadLetter请求参数结构体

    """

    def __init__(self):
        """
        :param QueueName: 死信策略源队列名称，调用本接口会清空该队列的死信队列策略。\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterResponse(AbstractModel):
    """UnbindDeadLetter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")