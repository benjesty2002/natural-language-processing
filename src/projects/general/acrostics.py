from src.data_index.raw import NARROW_WORD_LIST
from src.data_index.opted import OPTED_VALID
import json


input_words = [["access", "inside", "go", "open"], ["room", "enter"], ["unlock", "step"]]

workings = list()
for i in range(len(input_words)):
    workings.append({
        "target_length": len(input_words[i]),
        "input_words": input_words[i],
        "input_letters": [set(word) for word in input_words[i]],
        "valid_targets": list()
    })

for word in OPTED_VALID.load():
    for i in range(workings):
        if len(word) == workings[i]["target_length"]:
            word_valid = True
            for l_num in range(len(word)):
                if word[l_num] not in workings[i]["input_letters"][l_num]:
                    word_valid = False
                    break
            if word_valid:
                workings[i]["valid_targets"].append(word)

print(json.dumps(workings, indent=4))