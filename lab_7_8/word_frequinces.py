import csv


def word_count(word_dict, data_row):
    """Fill dictionary count"""
    for word in data_row:
        # Check if word is already counted
        if word in word_dict:
            word_dict[word] += 1
        # If not then make a new word
        else:
            word_dict[word] = 1
    # Return our new updated dictionary for row
    return word_dict


if __name__ == "__main__":
    """Create a dictionary to keep track of csv"""
    word_dict = dict()

    # Open the csv and get data
    with open("input1.csv", "r") as c:
        data = csv.reader(c)
        for row in data:
            # Read csv rows and extract data for counting.
            word_dict = word_count(word_dict, row)

    # Pretty print out the dictionary
    for k, v in word_dict.items():
        print(f"{k} {v}")
