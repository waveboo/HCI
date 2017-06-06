# encoding=utf-8
from inters.xunfei import xunfei
from constant import InterpretErrorCode


def reason_inter(q):
    try:
        r = xunfei('ner', 'json', q)
        c = r[0][0]
        if c[0]['pos'] == 'r':
            del c[0]
        if c[0]['pos'] == 'v':
            del c[0]
        slot = ''
        slot = map(lambda x: slot + x['cont'], c)
        return InterpretErrorCode.Success, {'phenomenon': "".join(slot)}
    except IndexError:
        return InterpretErrorCode.FailToInterpret, 'fail'


