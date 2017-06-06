# encoding=UTF-8

import requests


wordmodel_server_url = 'http://localhost:8888/'


def get_vec(sentence):
    """
    得到一个句子的向量
    """
    params = dict(sentence=sentence)
    r = requests.post(wordmodel_server_url, params)
    return r.json()['vec']

if __name__ == '__main__':
	get_vec('我要你')


