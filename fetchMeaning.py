import requests as req
import json
import insertInDb
def fetchWordMeaning(word):
    print("In fetch meaning Method :: ", word)
    url = "https://googledictionaryapi.eu-gb.mybluemix.net/?define="+word+"&lang=en"
    try:
        resp = req.get(url)
        jsn = json.loads(resp.text)
        insertInDb.insertMeaning(jsn)
    except Exception as e:
        print(e)
        print("Meaning not found")


