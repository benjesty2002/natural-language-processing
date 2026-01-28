import process_opted
from src.dictionary_management.Dataset import Dataset, SourceType
from src.projects.wordle.dataset_methods import sort_wordle


# Raw datasets
FREQUENCIES = Dataset(
    source=SourceType.KAGGLE, 
    url="rtatman/english-word-frequency", 
    file_path="data/raw/unigram_freq.csv"
)
OPTED_RAW = Dataset(
    source=SourceType.KAGGLE, 
    url="dfydata/the-online-plain-text-english-dictionary-opted", 
    file_path="data/raw/OPTED-Dictionary.csv"
)
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
NARROW_WORD_LIST = Dataset(
    source=SourceType.PUBLIC_URL, 
    url="http://www.gwicks.net/textlists/engmix.zip", 
    file_path="data/raw/engmix.txt"
)
RAW_DATASETS: dict[str, Dataset] = {
    "frequencies": FREQUENCIES,
    "opted_raw": OPTED_RAW,
    "wordle_valid_guesses": WORDLE_VALID_GUESSES,
    "wordle_valid_solutions": WORDLE_VALID_SOLUTIONS,
    "narrow_word_list_raw": NARROW_WORD_LIST,
}

# Processed datasets
OPTED_VALID = Dataset(
    file_path="data/processed/OPTED-valid-words.txt",
    update_method=process_opted.split_punctuation()
)
OPTED_HYPHENATED = Dataset(
    file_path="data/processed/OPTED-hyphenated-words.txt",
    update_method=process_opted.split_punctuation()
)
OPTED_PUNCTUATED = Dataset(
    file_path="data/processed/OPTED-punctuated-words.txt",
    update_method=process_opted.split_punctuation()
)
OPTED_SUFFIX_ADDITIONS = Dataset(
    file_path="data/processed/OPTED-suffix-additions.txt",
    update_method=process_opted.identify_suffixes()
)
OPTED_SUFFIXES = Dataset(
    file_path="data/processed/OPTED-suffixes.json",
    update_method=process_opted.identify_suffixes()
)
WORDLE_VALID_ALL = Dataset(
    file_path="data/processed/wordle_valid.txt",
    update_method=sort_wordle()
)


def load_all(only_raw=False):
    for k, v in RAW_DATASETS.items():
        if only_raw:
            v.load_raw()
        else:
            v.load()
