import json
from pymongo import MongoClient
def insertMeaning(meaningDict):
    print("In insertMeaning method")
    try:
        conn = MongoClient("mongodb://localhost:27017/")
        print("Connected Successfully...")
    except:
        print("Connection Failed")


    meaning = {}
    # print(meaningDict)
    for k,v in meaningDict.items():
        meaning[k] = v
    print(meaning['meaning']['adverb'][0])
    print("Type of meaning :: ", type(meaning))

