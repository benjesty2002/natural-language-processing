# TODO convert this method into new form

def combine_with_frequencies(input_files: list[str], output_file: str, freq_file: str = "unigram_freq.csv"):
    print(f"filtering frequency dataset with [{', '.join(input_files)}]")
    
    # read in all valid words
    all_valid = set()
    for file_name in input_files:
        with open(f"english_dictionaries/{file_name}", "r") as f:
            all_valid = all_valid.union(set(f.read().split("\n")))
    all_valid.remove("")
    
    with open(f"english_dictionaries/{freq_file}", "r") as freq_source,\
         open(f"english_dictionaries/{output_file}", "w+") as freq_filtered:
        for line in freq_source:
            word = line.split(",")[0].lower()
            if word in all_valid:
                all_valid.remove(word)
                freq_filtered.write(line)
        # add valid words which did not appear in the frequency file
        for word in sorted(list(all_valid)):
            freq_filtered.write(f"{word},0\n")