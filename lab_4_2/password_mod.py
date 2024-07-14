word = input()
password = ""

# Build dic for password replace
update_dic = {"i": "!", "a": "@", "m": "M", "B": "8", "o": "."}
for x in word:
    # Check if item in dic
    if x in update_dic.keys():
        # Replace item
        password += update_dic[x]
    else:
        # Use what was entered
        password += x

# Append this at the end as requested
password += "q*s"
print(password)
