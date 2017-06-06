# encoding=UTF-8
"""
    根据定义好的语法和词汇，生成训练集，训练模型，存储到tmp/文件夹下
"""
import yaml
import itertools
from sklearn import tree
import numpy as np
import sys
import pickle
from tool import get_vec
from db import DB
reload(sys)
sys.setdefaultencoding('UTF-8')

with open('config.yml') as ymlfile:
    cfg = yaml.load(ymlfile)

types = cfg['types']


label_map = {
    'map': 0,
    'reason': 1,
    'information': 2
}


def get_word():
    return DB().get_words()

words = get_word()


def get_label(type_):
    return label_map[type_]


def get_train_data():
    train_data = []
    train_label = []
    """
      t: type
      d: detail
    """
    for t, d in types.items():
        states = d['statement']
        slots = d['slots']
        combs = cartesian(slots)
        for state in states:
            for comb in combs:
                sentence = state.format(**comb)
                train_data.append(sentence)
                train_label.append(get_label(t))

    return train_data, train_label


def cartesian(slots):
    materials = [words[slot] for slot in slots]
    products = [x for x in itertools.product(*materials)]
    ts = [zip(slots, product) for product in products]
    return [dict(t) for t in ts]


train_data, train_label = get_train_data()


for record, label in zip(train_data, train_label):
    print record, label


train_data = map(get_vec, train_data)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_label)


for t, l in zip(train_data, train_label):
    t = np.asarray(t).reshape(1, -1)
    print clf.predict(t) == l

# save trained model to file
with open('tmp/model.plk', 'w') as f:
    pickle.dump(clf, f)


if __name__ == '__main__':
    pass


