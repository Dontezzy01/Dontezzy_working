import json

filename = 'username.json'

with open(filename, "r") as file:
    name = json.load(file)
    print("Hi " + name + "!" + " Welcome back!")