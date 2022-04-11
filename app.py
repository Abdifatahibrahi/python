my_file = open("data.txt", 'r')

file_content = my_file.read()

my_file.close()

print(file_content)


name = input("What is your name? ")
my_file_write = open("data.txt", 'w')

my_file_write.write(name)




