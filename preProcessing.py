import re
from fetchMeaning import fetchWordMeaning
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def passingWord(filtered_words):
    for word in filtered_words:
        fetchWordMeaning(word)

def getWordsList():
    file = open("D:/Jyoti-backup/python-project_folders/dictionaryApp/input.txt", "r")
    content = file.read()
    without_stopWords = []
    filtered_words = []
    tokenized_words = word_tokenize(content)

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
    passingWord(filtered_words)





