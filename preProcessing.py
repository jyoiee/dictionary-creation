import re
import requests as req
from pymongo import MongoClient

import json
from fetchMeaning import fetchWordMeaning
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def passingWord(filtered_words):
    try:
        conn = MongoClient("mongodb://localhost:27017/")
    except:
        print("Connection Failed")

    db = conn.english_dictionary
    collection = db.dictionary
    ids_list = []
    for mongodb_ids in collection.find():
        ids_list.append(mongodb_ids["_id"])
    ids_set= set(ids_list)
    print("total words in ids_set list :: ", len(ids_set))
    final_set = filtered_words.difference(ids_set)
    print("total words in final_set list :: ", len(final_set))
    for word in final_set:
        fetchWordMeaning(word)

def getWordsList():
    # to read words from url
    url = "http://www.fullbooks.com/Entire-PG-Edition-of-The-Works-of-William33.html"
    try:
        resp = req.get(url)
    except Exception as e:
        print(e)

    # to read words from text file
    # file = open("D:/Jyoti-backup/python-project_folders/dictionaryApp/txtInput.txt", "r")
    # content = file.read()
    without_stopWords = []
    filtered_words = []
    tokenized_words = word_tokenize(resp.text)

    stop_words = set(stopwords.words('english'))
    # to add extra stop words by own
    stop_words.add('.')
    stop_words.add(',')
    stop_words.add('?')
    stop_words.add('!')
    stop_words.add("'")
    stop_words.add("''")
    stop_words.add("'s")
    stop_words.add("'t")
    stop_words.add('"')
    stop_words.add(':')
    stop_words.add(';')
    stop_words.add('-')
    stop_words.add('--')
    stop_words.add('*')
    stop_words.add('_')
    stop_words.add('`')
    stop_words.add('``')
    stop_words.add('(')
    stop_words.add(')')
    stop_words.add('{')
    stop_words.add('}')
    stop_words.add('[')
    stop_words.add(']')
    stop_words.add('<')
    stop_words.add('>')

    # to remove the stop words
    for w in tokenized_words:
        if w.lower() not in stop_words:
            without_stopWords.append(w.lower())

    # to remove the words which matches the regular expressions
    p = re.compile("\d+")
    for word in without_stopWords:
        m = p.match(word)
        if not m:
            filtered_words.append(word)
    print("total words in filtered_words list :: ", len(filtered_words))
    removed_duplicate = set(filtered_words)

    print("total words in removed_duplicate list :: ", len(removed_duplicate))
    passingWord(removed_duplicate)





