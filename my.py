# list comprehension
from Tools.demo.beer import n

numbers = list(range(10))
print(numbers)

doubled_numbers = [n * 2 for n in numbers if n % 2 == 0]
print(f'doubled numbers = {doubled_numbers}')
names = ['rishabh', 'shraddha', 'Moni', 'Riya']
names = [name.capitalize() for name in names]
last_seen = [10, 20, 27]
dic = dict(zip(names, last_seen))
print(dic)
# temp function
(lambda x, y: x + y)(10, 5)
# first class function:
#function that takes another function as a parameter