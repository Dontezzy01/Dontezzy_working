#import json
#Favorite_num = [12,14,17,23,24,2,98, 90]

#filename = "Favorite_num.json"

#with open(filename,"w") as file:
    #json.dump(Favorite_num,file)
#Note: The json.load file is practileFile.py file.

import json

Favorite_num = [12,14,17,23,24,2,98, 90]
try:
    filename = "Favorit_num.json"
    with open(filename,"r") as file:
        Favorite_num= json.load(file)
        print("Your Favorite number " + str(Favorite_num) +" is here")
except FileNotFoundError:
    for i in range(7):
        Filename = int(input("Enter your number: "))

        with open(filename, "w") as file:
            json.dump(Filename,file)
            print("Yoo... Your favorite number are " + str(Favorite_num))
####ERROR............

