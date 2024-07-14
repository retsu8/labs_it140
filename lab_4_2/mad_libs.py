# Simple mad lips
mad_libs = "Eating {} {} a day keeps the doctor away."

# State noun here for loop
noun = ""
while True:
    # Get user noun
    noun, number = input().split(" ")
    # Print the mad libs
    if noun == "quit":
        break
    print(mad_libs.format(number, noun))
