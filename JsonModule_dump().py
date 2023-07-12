import json
username = input("Enter your fullname: ")

filename = "username.json"
with open(filename,"w") as file:
    json.dump(username,file)


