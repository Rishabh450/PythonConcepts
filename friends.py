friends = input("enter")
lister = friends.split(' ')
people = open('people.txt', 'r+')
people_lines = people.readlines()
people_lines = [name.strip() for name in people_lines]
people_set = set(people_lines)
# print(people_set)

friends_set = set(lister)
# print(friends_set)
friends_nearby = friends_set.intersection(people_set)
print(friends_nearby)
people.close()

nearby_file = open('nearby_friends.txt', 'w')
for friends in friends_nearby:
    nearby_file.write(friends+'\n')
