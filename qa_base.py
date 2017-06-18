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

if __name__ == '__main__':
     qas = [
        QA('information', {'info': '郭子仪'}, '郭子仪（697——781），祖籍山西汾阳，华州郑县（今陕西华县）人。'),
        QA('information', {'info': '明妃曲'}, '《明妃曲二首》是宋代文学家王安石的组诗作品，被称为是咏王昭君最好的诗。'),
        QA('information', {'info': '李宏毅'}, '李宏毅，1998年6月26日出生于辽阳市，《变形计》第九季城市主人公。'),
        QA('information', {'info': '苏辙'},
           '苏辙（1039年3月18日—1112年10月25日），字子由，一字同叔，晚号颍滨遗老，汉族，眉州眉山（今属四川）人，北宋文学家、诗人、宰相，唐宋八大家之一。'),
        QA('information', {'info': '西天目山'}, '西天目山是国家级森林和野生动物类型的自然保护区，位于杭州临安31公里处，是大自然赐予天然尤物。'),
        QA('information', {'info': '鼓子词'}, '鼓子词是中国宋代的说唱伎艺。')
     ]
     for qa in qas:
        Base().save(qa)


