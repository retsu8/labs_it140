# Get user input
data = input()
data = [int(i) for i in data.split(" ")]

# Printing the avg of the data
print(int(sum(data) / len(data)), end=" ")

# Printing the data max
print(max(data))
