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


class DeregisterMigrationTaskRequest(AbstractModel):
    """DeregisterMigrationTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeregisterMigrationTaskResponse(AbstractModel):
    """DeregisterMigrationTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeMigrationTaskRequest(AbstractModel):
    """DescribeMigrationTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，例如msp-jitoh33n\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMigrationTaskResponse(AbstractModel):
    """DescribeMigrationTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskStatus: 迁移详情列表\n        :type TaskStatus: list of TaskStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskStatus") is not None:
            self.TaskStatus = []
            for item in params.get("TaskStatus"):
                obj = TaskStatus()
                obj._deserialize(item)
                self.TaskStatus.append(obj)
        self.RequestId = params.get("RequestId")


class DstInfo(AbstractModel):
    """迁移目的信息

    """

    def __init__(self):
        """
        :param Region: 迁移目的地域\n        :type Region: str\n        :param Ip: 迁移目的Ip\n        :type Ip: str\n        :param Port: 迁移目的端口\n        :type Port: str\n        :param InstanceId: 迁移目的实例Id\n        :type InstanceId: str\n        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectRequest(AbstractModel):
    """ListMigrationProject请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 记录起始数，默认值为0\n        :type Offset: int\n        :param Limit: 返回条数，默认值为500\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationProjectResponse(AbstractModel):
    """ListMigrationProject返回参数结构体

    """

    def __init__(self):
        """
        :param Projects: 项目列表\n        :type Projects: list of Project\n        :param TotalCount: 项目总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Projects = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListMigrationTaskRequest(AbstractModel):
    """ListMigrationTask请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 记录起始数，默认值为0\n        :type Offset: int\n        :param Limit: 记录条数，默认值为10\n        :type Limit: int\n        :param ProjectId: 项目ID，默认值为空\n        :type ProjectId: int\n        """
        self.Offset = None
        self.Limit = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListMigrationTaskResponse(AbstractModel):
    """ListMigrationTask返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总条数\n        :type TotalCount: int\n        :param Tasks: 迁移任务列表\n        :type Tasks: list of Task\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskBelongToProjectRequest(AbstractModel):
    """ModifyMigrationTaskBelongToProject请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，例如msp-jitoh33n\n        :type TaskId: str\n        :param ProjectId: 项目ID，例如10005\n        :type ProjectId: int\n        """
        self.TaskId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskBelongToProjectResponse(AbstractModel):
    """ModifyMigrationTaskBelongToProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMigrationTaskStatusRequest(AbstractModel):
    """ModifyMigrationTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态，取值为unstart，migrating，finish，fail之一，分别代表该迁移任务状态为迁移未开始，迁移中，迁移完成，迁移失败\n        :type Status: str\n        :param TaskId: 任务ID，例如msp-jitoh33n\n        :type TaskId: str\n        """
        self.Status = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMigrationTaskStatusResponse(AbstractModel):
    """ModifyMigrationTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Project(AbstractModel):
    """列表类型

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID\n        :type ProjectId: int\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        """
        self.ProjectId = None
        self.ProjectName = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskRequest(AbstractModel):
    """RegisterMigrationTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskType: 任务类型，取值database（数据库迁移）、file（文件迁移）、host（主机迁移）\n        :type TaskType: str\n        :param TaskName: 任务名称\n        :type TaskName: str\n        :param ServiceSupplier: 服务提供商名称\n        :type ServiceSupplier: str\n        :param CreateTime: 迁移任务创建时间\n        :type CreateTime: str\n        :param UpdateTime: 迁移任务更新时间\n        :type UpdateTime: str\n        :param MigrateClass: 迁移类别，如数据库迁移中mysql:mysql代表从mysql迁移到mysql，文件迁移中oss:cos代表从阿里云oss迁移到腾讯云cos\n        :type MigrateClass: str\n        :param SrcInfo: 迁移任务源信息\n        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`\n        :param DstInfo: 迁移任务目的信息\n        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`\n        :param SrcAccessType: 源实例接入类型，数据库迁移时填写值为：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)\n        :type SrcAccessType: str\n        :param SrcDatabaseType: 源实例数据库类型，数据库迁移时填写，取值为mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb 之一\n        :type SrcDatabaseType: str\n        :param DstAccessType: 目标实例接入类型，数据库迁移时填写值为：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)\n        :type DstAccessType: str\n        :param DstDatabaseType: 目标实例数据库类型,数据库迁移时填写，取值为mysql,redis,percona,mongodb,postgresql,sqlserver,mariadb 之一\n        :type DstDatabaseType: str\n        """
        self.TaskType = None
        self.TaskName = None
        self.ServiceSupplier = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MigrateClass = None
        self.SrcInfo = None
        self.DstInfo = None
        self.SrcAccessType = None
        self.SrcDatabaseType = None
        self.DstAccessType = None
        self.DstDatabaseType = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.TaskName = params.get("TaskName")
        self.ServiceSupplier = params.get("ServiceSupplier")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MigrateClass = params.get("MigrateClass")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        self.SrcAccessType = params.get("SrcAccessType")
        self.SrcDatabaseType = params.get("SrcDatabaseType")
        self.DstAccessType = params.get("DstAccessType")
        self.DstDatabaseType = params.get("DstDatabaseType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterMigrationTaskResponse(AbstractModel):
    """RegisterMigrationTask返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SrcInfo(AbstractModel):
    """迁移源信息

    """

    def __init__(self):
        """
        :param Region: 迁移源地域\n        :type Region: str\n        :param Ip: 迁移源Ip\n        :type Ip: str\n        :param Port: 迁移源端口\n        :type Port: str\n        :param InstanceId: 迁移源实例Id\n        :type InstanceId: str\n        """
        self.Region = None
        self.Ip = None
        self.Port = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Task(AbstractModel):
    """迁移任务类别

    """

    def __init__(self):
        """
        :param TaskId: 任务Id\n        :type TaskId: str\n        :param TaskName: 任务名称\n        :type TaskName: str\n        :param MigrationType: 迁移类型\n        :type MigrationType: str\n        :param Status: 迁移状态\n        :type Status: str\n        :param ProjectId: 项目Id\n        :type ProjectId: int\n        :param ProjectName: 项目名称\n        :type ProjectName: str\n        :param SrcInfo: 迁移源信息\n        :type SrcInfo: :class:`tencentcloud.msp.v20180319.models.SrcInfo`\n        :param MigrationTimeLine: 迁移时间信息\n        :type MigrationTimeLine: :class:`tencentcloud.msp.v20180319.models.TimeObj`\n        :param Updated: 状态更新时间\n        :type Updated: str\n        :param DstInfo: 迁移目的信息\n        :type DstInfo: :class:`tencentcloud.msp.v20180319.models.DstInfo`\n        """
        self.TaskId = None
        self.TaskName = None
        self.MigrationType = None
        self.Status = None
        self.ProjectId = None
        self.ProjectName = None
        self.SrcInfo = None
        self.MigrationTimeLine = None
        self.Updated = None
        self.DstInfo = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.MigrationType = params.get("MigrationType")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        if params.get("SrcInfo") is not None:
            self.SrcInfo = SrcInfo()
            self.SrcInfo._deserialize(params.get("SrcInfo"))
        if params.get("MigrationTimeLine") is not None:
            self.MigrationTimeLine = TimeObj()
            self.MigrationTimeLine._deserialize(params.get("MigrationTimeLine"))
        self.Updated = params.get("Updated")
        if params.get("DstInfo") is not None:
            self.DstInfo = DstInfo()
            self.DstInfo._deserialize(params.get("DstInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    """迁移详情列表

    """

    def __init__(self):
        """
        :param Status: 迁移状态\n        :type Status: str\n        :param Progress: 迁移进度\n        :type Progress: str\n        :param UpdateTime: 迁移日期\n        :type UpdateTime: str\n        """
        self.Status = None
        self.Progress = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeObj(AbstractModel):
    """时间对象

    """

    def __init__(self):
        """
        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        """
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        