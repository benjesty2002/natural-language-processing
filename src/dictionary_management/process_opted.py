from index import OPTED_RAW


def split_punctuation() -> None:
    previous_word = ""
    with open("data/processed/OPTED-valid-words.txt", "w+") as opted_valid,\
        open("data/processed/OPTED-hyphenated-words.txt", "w+") as opted_hyphenated,\
        open("data/processed/OPTED-punctuated-words.txt", "w+") as opted_punctuated: 
        for line in OPTED_RAW.load():
            word = line.split(",")[0]
            if word == previous_word or word == "":
                continue
            previous_word = word
            if word.isalpha():
                opted_valid.write(f"{word.lower()}\n")
            elif word.replace("-", "").isalpha():
                opted_hyphenated.write(f"{word.lower()}\n")
            else:
                opted_punctuated.write(f"{word.lower()}\n")


def secondary_processing() -> None:
