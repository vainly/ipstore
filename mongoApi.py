# -*- coding: utf-8 -*-

from pymongo import MongoClient
import json


ip = "123.57.29.130"
port = 27017


class MgClient(object):

    def get_coll(self, coll_name, db_name):
        """

        :rtype : object
        """
        return self.connect[coll_name][db_name]

    @property
    def connect(self):
        """

        :return:
        """
        return MongoClient(ip, port)


def test():
    client = MongoClient(ip, 27017)
    db = client["test"]
    cursor = db.restaurants.find({"name": "Vella"})
    for document in cursor:
        print document


def test2():
    coll = MgClient().get_coll('test', "restaurants")
    cursor = coll.find({})
    for document in cursor:
        print document


if __name__ == "__main__":
    test()