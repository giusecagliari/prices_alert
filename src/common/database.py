__author__ = 'Giusecagliari'

import pymongo



class Database(object):
   # URI = "mongodb://heroku_hlj2schj:heroku10@ds161653.mlab.com:61653/heroku_hlj2schj"
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
   #heroku_hlj2schj
   #heroku10

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack'] #fullstack

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)