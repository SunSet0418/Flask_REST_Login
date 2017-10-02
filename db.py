from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj

#MongoDB Connect
client = MongoClient()

#REST_flask DATABASE Connect
db = client.REST_flask

#users TABLE Connect
users = db.users

print('DB Connect')