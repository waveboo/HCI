from inters.xunfei import xunfei
from constant import InterpretErrorCode


def map_inter(q):
    try:
        r = xunfei('ner', 'json', q)
        c = filter(lambda w: (w['pos'] == 'n') or (w['pos'] == 'ns') or (w['pos'] == 'j') or (w['pos'] == 'ni') or (w['pos'] == 'nl') or (w['pos'] == 'nz'), r[0][0])
        return InterpretErrorCode.Success, {'location': c[0]['cont']}
    except IndexError:
        return InterpretErrorCode.FailToInterpret, 'fail'

