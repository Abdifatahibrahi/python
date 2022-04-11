friends = input("Enter your three friends: ").split(",")

people = open("people.txt", "r")
read_people = [line.strip() for line in people.readlines()]
people.close()

friends_set = set(friends)
read_people_set = set(read_people)

friend_in_people = friends_set.intersection(read_people_set)

our_friends = open("friends.txt", "w")
for friend in friend_in_people:
    our_friends.write(f"{friend}\n")

our_friends.close()

