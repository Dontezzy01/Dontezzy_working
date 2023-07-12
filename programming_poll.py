while True:

    reason = input("Why do you like programming: ")
    if reason == "q":
        break

    print(f"Reason i love programming is that {reason}.")
    with open("Guest.txt","a") as file_object:
        file_object.write("\n" + reason + "." + "\n")