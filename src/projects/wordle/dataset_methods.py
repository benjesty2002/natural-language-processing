from src.dictionary_management.index import WORDLE_VALID_GUESSES, WORDLE_VALID_SOLUTIONS


def sort_wordle():
    guesses = WORDLE_VALID_GUESSES.load()[1:]
    solutions = WORDLE_VALID_SOLUTIONS.load()[1:]
    with open("english_dictionaries/wordle_valid.txt", "w+") as f:
        f.write("\n".join(sorted(guesses + solutions)))