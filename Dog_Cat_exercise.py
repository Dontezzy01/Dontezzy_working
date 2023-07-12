filename = "Dogs.txt"
try:
    with open(filename,"r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    # to fail silently use "pass"
    #pass
    print("The file " + filename + " does not exist")


filename = "Cats.txt"
try:
    with open(filename,"r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    # to fail silently use "pass"
    #pass
    print("The file " + filename + " does not exist")