import pymongo

db = pymongo.MongoClient('mongodb://localhost:27017')
db = db['bot_spot']
db = db['trades']
