from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://amanocha:dukemap@ds049476.mlab.com:49476/heroku_x7nr699f')
    db = client.heroku_rfsb5xrr
    return db