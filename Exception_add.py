while True:
    try:
        first_num = input("Enter first number: ")
        second_num = input("Enter second number: ")
        if first_num and second_num == "q":
            break
        Addition = int(first_num) + int(second_num)
        print("The result:",Addition)
    except TypeError:
        Msg = "Sorry, you dont enter number, please! Enter number"
        print(Msg)
    except ValueError:
        print(" Invalid literals")

filename = "programming.txt"
try:
    with open(filename) as file_obj:
        result = file_obj.read()
        #print(result)
except FileNotFoundError:
    print( "The file " + filename + " does not exist" )
else:
    words = result.split()
    num_count = len(words)
    msg = "The file "+ filename + " is about " + str(num_count) + "words."
    print(msg)
