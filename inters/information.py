# encoding=utf-8
from inters.xunfei import xunfei
from constant import InterpretErrorCode


def info_inter(q):
    try:
        r = xunfei('ner', 'json', q)
        c = filter(lambda w: (w['pos'] == 'n') or (w['pos'] == 'nh')or (w['pos'] == 'j')or (w['pos'] == 'r'), r[0][0])
        return InterpretErrorCode.Success, {'info': c[0]['cont']}
    except IndexError:
        return InterpretErrorCode.FailToInterpret, 'fail'


