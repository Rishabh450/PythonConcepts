my_file = open('data.txt', 'r')
file_content = my_file.read()
my_file.close()
print(file_content)
add = input("enter text to append")
my_file_write = open('data.txt', 'w')
my_file_write.write(add)
my_file_write.close()

