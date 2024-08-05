# Get the replacement words, then build replacement dictionary.
replace_pairs = input().split(" ")
replace_pairs = {
    i[0].strip(): i[1].strip() for i in zip(replace_pairs[0::2], replace_pairs[1::2])
}

# Get the sentence to modify
sentence = input().strip()

# Modify the sentence input
for key, value in replace_pairs.items():
    sentence = sentence.replace(key, value)

# Print the new sentence.
print(sentence)