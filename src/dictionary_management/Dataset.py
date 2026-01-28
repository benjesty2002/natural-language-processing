import json
import os

import urllib.request
import kaggle
from enum import StrEnum
from functools import partial
from typing import Callable, Optional, Tuple, Union
import zipfile


class SourceType(StrEnum):
    KAGGLE = "Kaggle"
    PUBLIC_URL = "Public_URL"


def unzip_files() -> None:
    zip_files = [f for f in os.listdir("data/raw") if f.endswith(".zip")]
    for zf in zip_files:
        with zipfile.ZipFile(f"data/raw/{zf}", "r") as zip_ref:
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


class Dataset:
    def __init__(
        self,
        file_path: str,
        source: Optional[SourceType] = None,
        url: Optional[str] = None,
        update_method: Optional[Callable] = None,
        description: Optional[str] = None,
    ) -> None:
        self.file_path, self.directory, self.file_name, self.file_type = (
            self.__expand_file_path(file_path)
        )
        self.source = source
        self.url = url
        self.update = (
            update_method if update_method else self.__generate_update_method()
        )
        self.description = description
        self.__raw_data: Union[str, None] = None
        self.__data: Union[list, dict, None] = None

    def __expand_file_path(self, file_path: str) -> Tuple[str, str, str, str]:
        *dir_path, file_name = file_path.split("/")
        directory = "/".join(dir_path)
        *_, file_type = file_name.split(".")
        return file_path, directory, file_name, file_type

    def __generate_update_method(self) -> Callable:
        if not self.url or not self.file_name:
            raise RuntimeError(
                "url and filename must be specified if no update method is provided"
            )
        match self.source:
            case SourceType.KAGGLE:
                return partial(download_kaggle_dictionary, self.url, self.file_name)
            case SourceType.PUBLIC_URL:
                return partial(download_public_url, self.url, self.file_name)
            case _:
                raise RuntimeError(f"Unknown source: {self.source}")

    def load(self) -> Union[list, dict]:
        if not self.__data:
            raw_content = self.load_raw()
            match self.file_type:
                case "json":
                    self.__data = json.loads(raw_content)
                case "csv":
                    self.__data = raw_content.split("\n")
                case _:
                    self.__data = raw_content.split("\n")
        if not self.__data:
            raise RuntimeError("Failed to load data")
        return self.__data

    def load_raw(self) -> str:
        if not self.__raw_data:
            if not os.path.isfile(self.file_path):
                self.update()
            with open(self.file_path, "rb") as f:
                self.__raw_data = f.read().decode(encoding="utf-8", errors="replace")
        return self.__raw_data
