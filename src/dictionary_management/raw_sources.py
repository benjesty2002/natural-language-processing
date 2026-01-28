import os
from typing import NotRequired, TypedDict
import kaggle
import zipfile
import urllib.request


def unzip_files() -> None:
    zip_files = [f for f in os.listdir("data/raw") if f.endswith(".zip")]
    for zf in zip_files:
        with zipfile.ZipFile(f"data/raw/{zf}", 'r') as zip_ref:
            zip_ref.extractall("data/raw")
        os.remove(f"data/raw/{zf}")


def download_kaggle_dictionary(dataset: str, file_name: str):
    kaggle.api.dataset_download_file(
        dataset=dataset, 
        file_name=file_name,
        path="data/raw",
    )
    unzip_files()
    

def download_public_url(url: str, file_name: str) -> None:
    if url.endswith(".zip"):
        file_name = "temp.zip"
    urllib.request.urlretrieve(url, f"data/raw/{file_name}")
    unzip_files()
