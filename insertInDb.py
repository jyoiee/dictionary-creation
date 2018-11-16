import json
from pymongo import MongoClient

a = 0
def insertMeaning(meaningDict):
    print("In insertMeaning method")
    try:
        conn = MongoClient("mongodb://localhost:27017/")
    except:
        print("Connection Failed")

    db = conn.english_dictionary
    collection = db.dictionary
    try:
        meaning = {}
        for k, v in meaningDict.items():
            if k == "word":
                meaning["_id"] = v
            else:
                meaning[k] = v
        collection.insert_one(meaning)
        global a
        a = a + 1
        print(a)
        print("Meaning Inserted successfully for ", meaningDict["word"])
        conn.close()
    except Exception as e:
        print("Exception Message :: ", e)
        conn.close()




