from collections import defaultdict
import json
from src.data_index.opted import OPTED_RAW, OPTED_VALID
from src.data_index.raw import FREQUENCIES


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


def identify_suffixes() -> None:
    opted_original_set = set(OPTED_VALID.load())
    words = [
        {
            "word": line.split(",")[0],
            "freq": int(line.split(",")[1]),
            "opted": line.split(",")[0] in opted_original_set,
            "extend_from": None
        }
        for line in sorted(FREQUENCIES.load()[1:-1])
    ]
    
    allowed_suffixes = {"s", "es", "ed"}

    additions = defaultdict(list)
    suffixes = defaultdict(list)
    pointer = 0
    while pointer < len(words):
        # find next opted original word
        while pointer < len(words) and not words[pointer]["opted"]:
            pointer += 1
        if pointer >= len(words):
            break
        source = words[pointer]
        secondary_pointer = pointer + 1
        while secondary_pointer < len(words) and words[secondary_pointer]["word"].startswith(source["word"]):
            secondary = words[secondary_pointer]
            freq_ratio = source["freq"] / secondary["freq"]
            suffix = secondary["word"][len(source["word"]):]
            if freq_ratio > 5 or secondary["extend_from"] is not None or secondary["opted"] or \
                (len(secondary["word"])-len(source["word"])) > 4 or suffix not in allowed_suffixes:
                secondary_pointer += 1
                continue
            words[secondary_pointer]["extend_from"] = source["word"]
            # additions[source["word"]].append(words[secondary_pointer]["word"] + " " + str(freq_ratio))
            suffixes[suffix].append(freq_ratio)
            print(source["word"], words[secondary_pointer]["word"])
            secondary_pointer += 1
        pointer += 1

    with open("english_dictionaries/OPTED-suffix-additions.txt", "w+") as f:
        f.write("\n".join([word["word"] for word in words if word["extend_from"] is not None]))

    filtered_suffixes = [
        {
            "suffix": suffix,
            "count": len(ratio_list),
            "avg": sum(ratio_list) / len(ratio_list)
        }
        for suffix, ratio_list in suffixes.items()
        if len(ratio_list) > 100
    ]

    sorted_suffixes = sorted(filtered_suffixes, key=lambda d: d["count"], reverse=True)
    with open("english_dictionaries/OPTED-suffixes.json", "w+") as f:
        json.dump(sorted_suffixes, f, indent=4)