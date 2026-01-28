# TODO swap out direct loading for UNIGRAM_FREQ_OPTED when created
import re
from src.dictionary_management.index import FREQUENCIES


def is_valid(word: str):
    word = word.lower()
    word = re.sub("[^a-z]", "", word)
    word = re.sub("[eiou]", "a", word)
    word = re.sub("[^a]", "b", word)
    for lnum in range(1, len(word)):
        # if word[lnum-1] == word[lnum]:
        #     return False
        if word[lnum-1] == "b" and word[lnum] == "b":
            return False
    return True

max_len = 0
with open("english_dictionaries/unigram_freq_opted.csv", "r") as f:
    for line in f.read().splitlines():
        word = line.split(",")[0]
        if len(word) >= max_len and is_valid(word):
            print(len(word), word)
            max_len = len(word)
