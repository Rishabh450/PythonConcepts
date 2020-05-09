file = open('cities.csv', 'r')
lines = file.readlines()
lines = [line.strip() for line in lines]

x = ""

for line in lines:
    cont = line.split(',')
    json = '{\n' + f'"name":"{str(cont[1])}",\n "longitude":"{str(cont[2])}",\n"latitude":"{str(cont[3])}",\n "state":"{str(cont[4])}"'+'\n}\n'
    if line == lines[-1]:
        x=x+json
    else:
        x=x+json+','


file.close()

myjson = open('jsson.json', 'w')
x = '\n['+x+']\n'
myjson.write(x)
