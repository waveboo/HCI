# encoding=utf-8
from constant import BaseErrorCode, CheckSlotsErrorCode
"""
 QA 数据库
"""
from db import DB
from config import project_config as cfg


class Base(object):

    def __init__(self):
        self.db = DB()

    def save(self, qa):
        return self.db.save(qa.type_, qa.slots, qa.answer)

    def delete(self, qa):
        return self.db.delete(qa.type, qa.slots, qa.answer)

    def update(self, qa):
        return self.db.update(qa.type, qa.slots, qa.answer)

    def query(self, type_, slots):
        code, slots_lost = check_slots(type_, slots)
        if code is not CheckSlotsErrorCode.Success:
            return CheckSlotsErrorCode.LossInSlots, slots_lost
        r = self.db.query(type_, slots)
        if len(r) == 0:
            return BaseErrorCode.NoAnswer, None
        if len(r) > 1:
            return BaseErrorCode.MoreThanOne, r
        return BaseErrorCode.Success, r[0]


def check_slots(type_, slots):
    need_slots = cfg['types'][type_]['slots']
    if len(need_slots) == len(slots):
        return CheckSlotsErrorCode.Success, 'success'
    missing_type = [slot for slot in need_slots if slot not in need_slots]
    return CheckSlotsErrorCode.LossInSlots, missing_type


class QA(object):
    """
        slots: []
    """
    def __init__(self, type_, slots, answer):
        self.type_ = type_
        self.slots = slots
        self.answer = answer

# if __name__ == '__main__':
#     qas = [
#
#     ]
#     for qa in qas:
#        Base().save(qa)


