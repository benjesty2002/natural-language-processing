from src.dictionary_management.Dataset import Dataset, SourceType
from src.dictionary_management.opted import split_punctuation, identify_suffixes


OPTED_RAW = Dataset(
    source=SourceType.KAGGLE, 
    url="dfydata/the-online-plain-text-english-dictionary-opted", 
    file_path="data/raw/OPTED-Dictionary.csv"
)
OPTED_VALID = Dataset(
    file_path="data/processed/OPTED-valid-words.txt",
    update_method=split_punctuation
)
OPTED_HYPHENATED = Dataset(
    file_path="data/processed/OPTED-hyphenated-words.txt",
    update_method=split_punctuation
)
OPTED_PUNCTUATED = Dataset(
    file_path="data/processed/OPTED-punctuated-words.txt",
    update_method=split_punctuation
)
OPTED_SUFFIX_ADDITIONS = Dataset(
    file_path="data/processed/OPTED-suffix-additions.txt",
    update_method=identify_suffixes
)
OPTED_SUFFIXES = Dataset(
    file_path="data/processed/OPTED-suffixes.json",
    update_method=identify_suffixes
)
