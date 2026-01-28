from src.dictionary_management.Dataset import Dataset, SourceType


FREQUENCIES = Dataset(
    source=SourceType.KAGGLE, 
    url="rtatman/english-word-frequency", 
    file_path="data/raw/unigram_freq.csv"
)

NARROW_WORD_LIST = Dataset(
    source=SourceType.PUBLIC_URL, 
    url="http://www.gwicks.net/textlists/engmix.zip", 
    file_path="data/raw/engmix.txt"
)
