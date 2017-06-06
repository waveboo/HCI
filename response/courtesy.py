import os
import yaml
import sys
from random import randint
from config import courtesy_config as cfg

reload(sys)
sys.setdefaultencoding('UTF-8')

filename = os.path.join(os.path.dirname(__file__), 'courtesy.yml')


courtesy_dict = {
    'ce': cfg['ce'],
    'na': cfg['na'],
    'sa.map': cfg['sa']['map'],
    'sa.reason': cfg['sa']['reason'],
    'sa.information': cfg['sa']['information'],
    'ie': cfg['ie'],
    'ls': cfg['ls'],
    'mto': cfg['mto']
}


def courtesy_reply(type_, answer=""):
    candidates = courtesy_dict['.'.join(type_)]
    nums = len(candidates)
    random_index = randint(0, nums-1)
    return candidates[random_index].format(answer=answer)




