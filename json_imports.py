import json

file = open("friends_json.txt", "r")

file_contents = json.load(file)

print(file_contents['friends'][0])


cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"}
]

file1 = open("cars.txt", "w")

contents = json.dump(cars, file1)

print(contents)