from class_user import user


my_user = user("Quadri", "Dolapo", 22, "University of Ibadan", "Chelsea")
our_user = user("Oyindamola", "Olaitan", 22, "Oke-ogun polytechnic", "realmadrid")
my_user.describe_user()

import json

Favorite_num = [12,14,17,23,24,2,98, 90]
try:
    filename = "Favorite_num.json"
    with open(filename,"w") as file:
        json.dump(Favorite_num, file)
except FileNotFoundError:
    with open(filename, "r") as file:
        Fav_num = json.load(file)
        print("Yoo... Your favorite number are " + str(Favorite_num))
