import csv
import os

if __name__ == "__main__":
    """Create a dictionary to keep track of csv"""
    word_dict = dict()

    # Grag the file for processing input
    file_input = input()

    # Remove any stale files from last run if they exists. Need only check one as both will always be created.
    if os.path.isfile("output_keys.txt"):
        os.remove("output_keys.txt")
        os.remove("output_titles.txt")

    # Open the csv and get data
    with open(file_input, "r") as c:
        # Create zipped replication file for doubles.
        replace_pairs = [line for line in c]
        for i in zip(replace_pairs[0::2], replace_pairs[1::2]):
            key = int(i[0])
            if key in word_dict.keys():
                word_dict[key] += [i[1].strip()]
            else:
                word_dict[key] = [i[1].strip()]

    # Pretty print out the dictionary
    with open("output_keys.txt", "a+") as w:
        for k in sorted(word_dict.keys()):
            # Doing extra bit here so the upload processor doesnt fail.
            r = ("; ").join(word_dict[k])
            w.write(f"{k}: {r}\n")

    # Pull tvshows and build word dictionary
    tv_shows = []
    for v in word_dict.values():
        tv_shows += v

    # Output the titles file for the information. 
    with open("output_titles.txt", "a+") as w:
        for k in sorted(tv_shows):
            w.write(f"{k}\r\n")
