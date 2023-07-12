filename = "Guest.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        #print(content)
except FileNotFoundError:
    print("The file " + filename + " does not exist!")
else:
    words = content.split()
    words_count = words.count("Programming")
    Msg = "The file" + filename + "consist of " + str(words_count) + "'Programming"
    print(Msg)