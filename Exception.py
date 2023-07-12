print("Enter two number for the equation")
print("Enter q for quit")
while True:
    try:
        firstnum = input("Enter first number: ")
        if firstnum == "q":
            break

        secondnum = input("Enter second number: ")
        if secondnum == "q":
            break
        result = int(firstnum) / int(secondnum)
        print(result)

    except ZeroDivisionError:
        print("Cannot be divisible by zero")

    except ValueError:
        print("You entered invalid literal")


