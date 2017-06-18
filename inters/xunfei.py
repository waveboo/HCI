# encoding=utf-8
import requests
import json

API_KEY = 'I1U423G3d6g6i4H4c7k0niJAlzdGEr7xUrSeGo8V'

URL_BASE = "http://ltpapi.voicecloud.cn/analysis/"


def xunfei(pattern, form, text):

    params = dict(api_key=API_KEY, text=text, pattern=pattern, format=form)

    r = requests.get(URL_BASE, params=params)
    return r.json()


# if __name__ == '__main__':
#     fin = open('/home/wavelee/info.txt')
#     a = fin.readline()
#     # print a
#     fout = open('/home/wavelee/newa.txt', 'w')
#     l = []
#     while a:
#         print a
#         l.append(a)
#         a = fin.readline()
#     l = list(set(l))
#     for i in l:
#         fout.write(i)
#     fin.close()
#     fout.close()
#     while a:
#         print a
#         c = a.split(',')
#         if len(c) != 0 and len(c) != 1:
#             l = list(c[1])
#             for i in range(0, len(l)):
#                 if l[i] == '\'':
#                     l[i] = '\"'
#             c[1] = ''.join(l)
#             d = json.loads(c[1])
#             r = xunfei('ner', 'json', d['location']);
#             if len(r[0][0]) == 1 and len(c[2]) > 4:
#                 if (r[0][0][0]['pos'] == 'n') or (r[0][0][0]['pos'] == 'ns') or (r[0][0][0]['pos'] == 'j') or (r[0][0][0]['pos'] == 'ni')or (r[0][0][0]['pos'] == 'nl')or (r[0][0][0]['pos'] == 'nz'):
#                 #if (r[0][0][0]['pos'] == 'n') or (r[0][0][0]['pos'] == 'nh') or (r[0][0][0]['pos'] == 'j') or (r[0][0][0]['pos'] == 'r'):
#                     a = list(a)
#                     a[(len(a)-1)] = ''
#                     a = ''.join(a)
#                     a = 'QA(' + a + '),\n'
#                     fout.write(a)
#         a = fin.readline()
        #xunfei('ner', 'json', a);
        # b = ''.join(a)
        # fout.write(b)
    # fin.close()
    # fout.close()
    #xunfei('ner', 'json','首都博物馆');



