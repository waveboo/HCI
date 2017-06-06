# encoding=utf-8


class BaseErrorCode(object):

    # 返回成功
    Success = 0

    # 数据库中不存在相应答案
    NoAnswer = 1

    # 数据库中有多条符合的结果
    MoreThanOne = 2


class ComprehendErrorCode(object):

    # 理解成功
    Success = 0

    # 不能理解该类型
    UnSolvedType = 1


class InterpretErrorCode(object):

    # 解释成功

    Success = 0

    # 不能解释

    FailToInterpret = 3


class CheckSlotsErrorCode(object):

    # 槽的数目正确
    Success = 0

    # 缺失槽
    LossInSlots = 4
