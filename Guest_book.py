while True:
    name = input("Enter your name (or 'q' is for quit): ")
    if name == "q":
        break

    print(F"Hello, {name}!")
    with open("Guest.txt", "a") as file:
        file.write(name +"\n")