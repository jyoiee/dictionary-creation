from collections import defaultdict

from nltk.stem.snowball import SnowballStemmer

STEMMER = SnowballStemmer("english")
def generate_stem_map(wordlist):
    print("wordList :: ", wordlist)
    stem_map = defaultdict(list)
    for word in wordlist:
        stem = STEMMER.stem(word)
        print("$$$ ::",stem)
        # we don’t have to store words that stem to themselves:
        if stem == word:
            continue
        else:
            stem_map[stem].append(word)
    print("stem_map :: ", stem_map['possibl'])
    return stem_map

# STEM_MAP = generate_stem_map(["possiblities","changing","changed","possibility","bicycling"])

def explode_search_term(search_term):
    STEM_MAP = generate_stem_map(["possiblities","changing","changed","possibility","bicycling","comprehensively","obiviously","necessary"])
    stem = STEMMER.stem(search_term)
    exploded_terms = STEM_MAP.get(stem, [])
    # we include the original search term in the list of
    # exploded terms, because we didn't save words that
    # stem to themselves in the stem map:
    exploded_terms.append(search_term)
    return exploded_terms
exploded_terms = explode_search_term("obivious")
print("$$$$$$ :: ", exploded_terms)