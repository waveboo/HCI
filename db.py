# encoding=utf-8
"""
  mongodb
"""

import config
from pymongo import MongoClient

cfg = config.project_config

_client = MongoClient(host=cfg['mongo']['host'], port=cfg['mongo']['port'])
_db = _client[cfg['mongo']['db']]


class DB(object):

    def __init__(self):
        self.db = _db
        self.types = cfg['types']

    def save(self, table, slots, answer):
        query = self.get_query(table, slots, answer)
        result = self.db[table].insert_one(query)
        return result.inserted_id

    def delete(self, table, slots, answer):
        pass

    def update(self, table, slots, answer):
        pass

    def query(self, table, slots):
        query = self.get_query(table, slots, None)
        cursor = self.db[table].find(query)
        return list(cursor)

    def get_query(self, table, slots, answer):
        query = dict()
        for slot in self.types[table]['slots']:
            query[slot] = slots[slot]
        if answer:
            query['answer'] = answer
        return query

    def get_words(self):
        words = {}
        for table in self.types:
            result = list(self.db[table].find({}))
            for slot in self.types[table]['slots']:
                words[slot] = map(lambda x: x[slot], result)
        return words

if __name__ == '__main__':
    print DB().get_words()


