from src.dictionary_management.Dataset import Dataset, SourceType
from src.dictionary_management.frequencies import combine_with_frequencies
from src.dictionary_management.wordle import update_wordle_anagrams, update_wordle_unique_letters

# raw
WORDLE_VALID_GUESSES = Dataset(
    source=SourceType.KAGGLE, 
    url="bcruise/wordle-valid-words", 
    file_path="data/raw/valid_guesses.csv"
)
WORDLE_VALID_SOLUTIONS = Dataset(
    source=SourceType.KAGGLE, 
    url="bcruise/wordle-valid-words", 
    file_path="data/raw/valid_solutions.csv"
)

def sort_wordle():
    guesses = WORDLE_VALID_GUESSES.load()[1:]
    solutions = WORDLE_VALID_SOLUTIONS.load()[1:]
    with open(WORDLE_VALID_ALL.file_path, "w+") as f:
        f.write("\n".join(sorted(guesses + solutions)))

# processed
WORDLE_VALID_ALL = Dataset(
    file_path="data/processed/wordle_valid.txt",
    update_method=sort_wordle
)

def wordle_valid_freq():
    combine_with_frequencies([WORDLE_VALID_ALL], WORDLE_VALID_FREQ)

WORDLE_VALID_FREQ = Dataset(
    file_path="data/processed/wordle_valid_freq.csv",
    update_method=wordle_valid_freq
)
WORDLE_VALID_FREQ_ANAGRAM_UNIQUE = Dataset(
    file_path="data/processed/wordle_valid_freq_anagram_unique.csv",
    update_method=update_wordle_anagrams
)
WORDLE_VALID_FREQ_ANAGRAM_DUPLICATE = Dataset(
    file_path="data/processed/wordle_valid_freq_anagram_duplicate.csv",
    update_method=update_wordle_anagrams
)
WORDLE_UNIQUE_LETTERS = Dataset(
    file_path="data/processed/wordle_unique_letters.csv",
    update_method=update_wordle_unique_letters
)
