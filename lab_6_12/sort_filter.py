# Get user input and split into points
data = input()
data = map(int, data.split(" "))

# Clean string for only nonegitive
data = [i for i in data if i > -1]

# Sort the data
data.sort()

# Map str to data
data = map(str, data)

# Print the info
print(" ".join(data), end=" ")
