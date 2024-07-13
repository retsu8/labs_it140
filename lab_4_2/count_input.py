import re


user_text = input()

# Remove undesired with regex replace
user_text = re.sub(r"[ .,]", "", user_text)

# Print the length of the text left over
print(len(user_text))
