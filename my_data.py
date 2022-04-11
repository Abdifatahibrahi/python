csv_data = open("csv_data.txt", "r")

data = [line.strip() for line in csv_data.readlines()]
csv_data.close()


wanted_data = data[1:]

for line in wanted_data:
    name,age,uni,degree = line.split(",")
    print(f"{name} who is {age} years is doing {degree} in {uni} university")