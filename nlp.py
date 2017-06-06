# encoding=utf-8
import pickle
from tool import get_vec
import numpy as np
from constant import ComprehendErrorCode,InterpretErrorCode
import sys
from inters.reason import reason_inter
from inters.map import map_inter
from inters.information import info_inter
reload(sys)
sys.setdefaultencoding('UTF-8')


MODEL_FILE = '/home/wavelee/robot/tmp/model.plk'


def load_model(filename):
    with open(filename, 'r') as f:
        model = pickle.load(f)
    return model


type_mapping = {
    0: 'map',
    1: 'reason',
    2: 'information'
}


class Nlp(object):
    def __init__(self):
        self.model = load_model(MODEL_FILE)
        self.interpreters = {
            'map': map_inter,
            'reason': reason_inter,
            'information': info_inter
        }

    def comprehend(self, question):
        print '问题是{question}'.format(question=question)
        print '正在分析....'
        vec = np.asarray(get_vec(question))
        type_ = self.model.predict(vec.reshape(1, -1))[0]
        print type_
        code, slots = self.interpreters[type_mapping[type_]](question)
        if code is InterpretErrorCode.Success:
            analyse_log(type_, slots)
            return ComprehendErrorCode.Success, dict(type=type_mapping[type_], slots=slots)
        else:
            return InterpretErrorCode.FailToInterpret, 'fail'


def analyse_log(t, s):
    if type_mapping[t] == 'map':
        print '问题类型{type}, 槽是{slot}\n'.format(type=type_mapping[t], slot=s['location'])
    if type_mapping[t] == 'reason':
        print '问题类型{type}, 槽是{slot}\n'.format(type=type_mapping[t], slot=s['phenomenon'])
    if type_mapping[t] == 'information':
        print '问题类型{type}, 槽是{slot}\n'.format(type=type_mapping[t], slot=s['info'])

if __name__ == '__main__':
    nlp = Nlp()
    result = nlp.comprehend('你是谁')


