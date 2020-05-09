friends_last_seen ={
    'name': 'Rishabh',
    'id': 15
}
print(id(friends_last_seen))

friends_last_seen ={
    'name': 'Rishabh',
    'id': 15
}
print(id(friends_last_seen))
# mutable object, when dictionary is passed in argument the change occus
# in same memory location same object, be careful this can be dangerous
friends_last_seen['name'] = 'Sajal'
print(id(friends_last_seen))
# non mutable object
my_int = 5
print(id(my_int))
# my_int = my_int+1 # my_int.__add__() invoked
my_int += +1
print(id(my_int))
# mutable when += used
primes = [2, 3, 5]
print(id(primes))
primes += [7, 11]
print(id(primes))
# non mutable when + or - used
primes = [2, 3, 5]
print(id(primes))
primes +=[7, 11]
print(id(primes))
primes = [2, 3, 5]
print(id(primes))
prime = [7,11]
primes.append([7, 11])
print(id(primes))
