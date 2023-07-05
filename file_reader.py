with open("pi_digits.txt") as file_object:
    content = file_object.read()
    print(content)
#It is used to remove the extra backline
    #print(content.rstrip())

#or

f = open("pi_digits.txt", "r")
print(f.read())

with open("pi_digits.txt") as file_object:
    for data in file_object:
        print(data.rstrip())

filename = "learning_python.txt"
with open(filename, "r") as file_object:
    result = file_object.read()
    print(result)
print()

with open("learning_python.txt", "r") as file_object:
    for data in file_object:
        print(data,end="")


filename = "programming.txt"
with open(filename, "w") as file_object:
    file_object.write("I love progamming.\n")
    file_object.write("I am determined to be a programmer.\n")