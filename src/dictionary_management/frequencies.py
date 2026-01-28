from typing import Optional
from data_index.raw import FREQUENCIES
from Dataset import Dataset


def combine_with_frequencies(input_files: list[Dataset], output_file: Dataset, freq_file: Optional[Dataset] = None):
    if freq_file is None:
        freq_file = FREQUENCIES
    print(f"filtering frequency dataset with [{', '.join([d.file_name for d in input_files])}]")
    
    # read in all valid words
    all_valid = set()
    for dataset in input_files:
        all_valid = all_valid.union(set(dataset.load()))
    all_valid.remove("")
    
    with open(output_file.file_path, "w+") as freq_filtered:
        for line in freq_file.load():
            word = line.split(",")[0].lower()
            if word in all_valid:
                all_valid.remove(word)
                freq_filtered.write(line)
        # add valid words which did not appear in the frequency file
        for word in sorted(list(all_valid)):
            freq_filtered.write(f"{word},0\n")