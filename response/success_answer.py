# encoding=utf-8
from courtesy import courtesy_reply


def response(com, answer, **kwargs):
    return courtesy_reply(('sa', com['type']), answer=answer['answer'])
