from src.dictionary_management import index


def sort_wordle():
    guesses = index.WORDLE_VALID_GUESSES.load()[1:]
    solutions = index.WORDLE_VALID_SOLUTIONS.load()[1:]
    with open("english_dictionaries/wordle_valid.txt", "w+") as f:
        f.write("\n".join(sorted(guesses + solutions)))



# remove anagrams
def sort_word_by_letters(word):
    return "".join(sorted(list(word)))


# remove words with duplicated letters
def has_duplicate_letter(word):
    ordered = sorted(list(word))
    for i in range(len(ordered) - 1):
        if ordered[i] == ordered[i + 1]:
            return True
    return False


def update_wordle_anagrams():
    letter_combinations_used = set()
    used_lines = dict()
    with open(index.WORDLE_VALID_FREQ_ANAGRAM_UNIQUE.file_path, "w+") as f_out, \
        open(index.WORDLE_VALID_FREQ_ANAGRAM_DUPLICATE.file_path, "w+") as f_fail:
        for line in index.WORDLE_VALID_FREQ.load():
            word = line.split(",")[0].lower()
            hash = sort_word_by_letters(word)
            if hash in letter_combinations_used:
                f_fail.write(f"{line[:-1]},{used_lines[hash]}")
            else:
                letter_combinations_used.add(hash)
                used_lines[hash] = line
                f_out.write(line)


def update_wordle_unique_letters():
    with open("english_dictionaries/wordle_unique_letters.csv", "w+") as f_dest:
        for line in index.WORDLE_VALID_FREQ_ANAGRAM_UNIQUE.load():
            if not has_duplicate_letter(line[:5]):
                f_dest.write(line)