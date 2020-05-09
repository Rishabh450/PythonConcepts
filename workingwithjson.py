import json

file = open('jsson.json', 'r')
# load json file into dictionary
file_contents = json.load(file)
# print(file_contents[0])
file.close()

dic = [
    {
        'name': 'Rishabh',
        'age': 21
    },
    {
        'name': 'Shr',
        'age': 21
    }
]
# to convert a dictionary to string
xn = json.dumps(dic)
print(xn)

filer = open('created.json', 'w')
# to convert dictionary to json file
json.dump(dic, filer)
filer.close()
