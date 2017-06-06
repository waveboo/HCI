# encoding=utf-8
import requests

API_KEY = 'I1U423G3d6g6i4H4c7k0niJAlzdGEr7xUrSeGo8V'

URL_BASE = "http://ltpapi.voicecloud.cn/analysis/"


def xunfei(pattern, form, text):

    params = dict(api_key=API_KEY, text=text, pattern=pattern, format=form)

    r = requests.get(URL_BASE, params=params)
    return r.json()


