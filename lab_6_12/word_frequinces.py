# Get sentence input for split
sentence = input()

# Split sentence
sentence = sentence.split(" ")

# Build sentence dictionary of terms.
dict_sentence = dict()

# Fill dictionary count
for word in sentence:
    # Check if word is already counted
    if word in dict_sentence:
        dict_sentence[word] += 1
    # If not then make a new word
    else:
        dict_sentence[word] = 1

# Print new dictionary of terms
for word in sentence:
    print(f"{word} {dict_sentence[word]}")
