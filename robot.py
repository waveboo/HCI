# encoding=utf-8
"""
机器人类
"""
from nlp import Nlp
from qa_base import Base
import sys
import requests
from constant import ComprehendErrorCode, BaseErrorCode, InterpretErrorCode, CheckSlotsErrorCode
from response import com_error, no_answer, success_answer, morethanone, inter_error, lossslots


reload(sys)
sys.setdefaultencoding('UTF-8')


class Robot(object):

    def __init__(self):
        self.nlp = Nlp()
        self.knowledge = Base()
        self.responses = {
            ComprehendErrorCode.UnSolvedType: com_error.response,
            BaseErrorCode.NoAnswer: no_answer.response,
            BaseErrorCode.Success: success_answer.response,
            BaseErrorCode.MoreThanOne: morethanone.response,
            InterpretErrorCode.FailToInterpret: inter_error.response,
            CheckSlotsErrorCode.LossInSlots: lossslots.response
        }

    def listen(self, q):
        code, com = self.nlp.comprehend(q)
        if code is not ComprehendErrorCode.Success:
            return self.responses[code](com, q=q)
        code, answer = self.knowledge.query(com['type'], com['slots'])
        return self.responses[code](com, answer, q=q)


if __name__ == '__main__':
    robot = Robot()
    question = '郭伟华是什么人'
    print '{answer}'.format(answer=robot.listen(question))






