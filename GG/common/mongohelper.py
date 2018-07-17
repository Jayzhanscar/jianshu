from pymongo import MongoClient


def get_db():
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.bysj
    return db