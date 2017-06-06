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
#         QA('map', {'location': '国机'}, '国机二院又叫中国联合工程公司，总部在中国杭州'),
#         QA('map', {'location': '同济'}, '同济大学位于上海，有四平，嘉定，沪北，沪西，彰武等校区'),
#         QA('map', {'location': '复旦'}, '复旦大学位于上海，有邯郸，枫林，张江，江湾四个校区'),
#         QA('map', {'location': '北大'}, '北京大学位于北京，有燕园，昌平，大兴，医学部等校区'),
#         QA('map', {'location': '斯坦福'}, '斯坦福大学位于美国旧金山，临近世界著名高科技园区硅谷'),
#         QA('map', {'location': '清华大学'}, '清华大学位于北京，在北京只有海淀本部校区'),
#         QA('map', {'location': '上海交大'}, '上海交通大学位于上海，有徐汇，闵行，黄埔，长宁，七宝，浦东六个校区'),
#         QA('map', {'location': '比萨'}, '比萨斜塔位于意大利'),
#         QA('map', {'location': '埃菲尔'}, '埃菲尔铁塔位于法国'),
#         QA('map', {'location': '金门桥'}, '金门桥位于美国'),
#         QA('map', {'location': '泰姬陵'}, '泰姬陵位于印度'),
#         QA('map', {'location': '万里长城'}, '万里长城位于中国'),
#         QA('reason', {'phenomenon': '多喝热水'}, '因为人生名言就是不行就分,喜欢就买,多喝点水,重启试试啊'),
#         QA('reason', {'phenomenon': '无可奉告'}, '因为我今天就要得罪你们一下'),
#         QA('reason', {'phenomenon': '另请高明'}, '因为我也不是谦虚'),
#         QA('reason', {'phenomenon': '天气晴朗'}, '因为本来今天要下雨'),
#         QA('reason', {'phenomenon': '多反思'}, '因为爱反思才会有收获'),
#         QA('reason', {'phenomenon': '地球是圆的'}, '因为球体会达到物体内部引力的平衡'),
#         QA('reason', {'phenomenon': '地球有四季'}, '因为地球的公转使地球面向太阳的一面不断改变'),
#         QA('reason', {'phenomenon': '黑洞'}, '因为根据广义相对论，黑洞是由恒星演变来的，引力大到光也无法逃脱'),
#         QA('reason', {'phenomenon': '我喜欢你'}, '因为我是个人见人爱的小可爱啊'),
#         QA('reason', {'phenomenon': '我这么帅'}, '帅有啥用，有对象了吗'),
#         QA('reason', {'phenomenon': '原谅'}, '因为要坚强'),
#         QA('reason', {'phenomenon': '学习'}, '因为我爱学习，学习使我快乐'),
#         QA('information', {'info': '名字'}, '我叫三叶'),
#         QA('information', {'info': '郭伟华'}, '他是一个爱反思的人'),
#         QA('information', {'info': '徐嘉诰'}, '他是天气制造学家'),
#         QA('information', {'info': '朱物华'}, '他曾担任上海交大的校长，国机二院的院长'),
#         QA('information', {'info': '愣头青'}, '指没有经验的年轻人'),
#         QA('information', {'info': '瓜皮'}, '傻瓜啊你'),
#         QA('information', {'info': '算法'}, '算法是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令'),
#         QA('information', {'info': '圆周率'}, '圆周率是圆的周长与直径的比值'),
#         QA('information', {'info': '基因'}, '基因是具有遗传效应的DNA片段'),
#         QA('information', {'info': '柯基'}, '威尔士柯基犬，好想揉他的肥臀啊'),
#         QA('information', {'info': '恐龙'}, '恐龙是出现在中生代时期的一类爬行动物的统称'),
#         QA('information', {'info': '你'}, '我是一个可爱又聪明的小AI'),
#     ]
#     for qa in qas:
#        Base().save(qa)


