import pymongo
import datetime

db = pymongo.MongoClient('mongodb://localhost:27017')
db = db['bot_spot']
db = db['logs']


def log(message: str, level: str = 'info'):
    db.insert_one({
        'message': message,
        'level': level,
        "date": datetime.date.today().replace()
    })
