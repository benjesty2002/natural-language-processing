import os
from typing import NotRequired, TypedDict
import kaggle
import zipfile
import urllib.request


class DatasetSource(TypedDict):
    name: str
    source: str
    url: str
    filename: str
    description: NotRequired[str]


KAGGLE_DATASETS: list[DatasetSource] = [
    DatasetSource(
        name="Frequency dataset", 
        source="Kaggle", 
        url="rtatman/english-word-frequency", 
        filename="unigram_freq.csv"
    ),
    DatasetSource(
        name="OPTED dataset", 
        source="Kaggle", 
        url="dfydata/the-online-plain-text-english-dictionary-opted", 
        filename="OPTED-Dictionary.csv"
    ),
    DatasetSource(
        name="Wordle valid guesses", 
        source="Kaggle", 
        url="bcruise/wordle-valid-words", 
        filename="valid_guesses.csv"
    ),
    DatasetSource(
        name="Wordle valid solutions", 
        source="Kaggle", 
        url="bcruise/wordle-valid-words", 
        filename="valid_solutions.csv"
    ),
    DatasetSource(
        name="Narrow word list", 
        source="PublicURL", 
        url="http://www.gwicks.net/textlists/engmix.zip", 
        filename="eng-words-narrow.zip"
    ),
]


def unzip_file(expected_file_name: str) -> None:
    found_file_name = [f for f in os.listdir("data/raw") if f"{expected_file_name}" in f]
    if not found_file_name:
        raise RuntimeError(f"{expected_file_name} not found")
    found_file_name = found_file_name[0]

    if found_file_name.endswith(".zip"):
        os.rename(f"data/raw/{found_file_name}", f"data/raw/zipped/{found_file_name}")
        with zipfile.ZipFile(f"data/raw/zipped/{found_file_name}", 'r') as zip_ref:
            zip_ref.extractall("data/raw/unzipped")
    else:
        os.rename(f"data/raw/{found_file_name}", f"data/raw/unzipped/{found_file_name}")


def download_kaggle_dictionary(dataset, file_name):
    kaggle.api.dataset_download_file(
        dataset=dataset, 
        file_name=file_name,
        path="data/raw",
    )
    unzip_file(file_name)
    

def download_public_url(url: str, file_name: str) -> None:
    urllib.request.urlretrieve(url, f"data/raw/{file_name}")
    unzip_file(file_name)


def retrieve_dataset(dataset_definition: DatasetSource) -> None:
    print(f"Retrieving {dataset_definition['name']}")
    match dataset_definition["source"]:
        case "Kaggle":
            download_kaggle_dictionary(dataset_definition["url"], dataset_definition["filename"])
        case "PublicURL":
            download_public_url(dataset_definition["url"], dataset_definition["filename"])
        case _:
            raise RuntimeError(f"Unknown source: {dataset_definition['source']}")


if __name__ == "__main__":
    for ds in KAGGLE_DATASETS:
        retrieve_dataset(ds)
