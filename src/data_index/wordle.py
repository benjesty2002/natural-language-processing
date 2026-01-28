from src.dictionary_management.Dataset import Dataset, SourceType
from src.dictionary_management.wordle import update_wordle_anagrams, update_wordle_unique_letters, sort_wordle, wordle_valid_freq

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

# processed
WORDLE_VALID_ALL = Dataset(
    file_path="data/processed/wordle_valid.txt",
    update_method=sort_wordle
)
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
