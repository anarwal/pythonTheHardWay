from sys import argv

script, filename = argv

print(f'We are going to delete {filename}')
print('If you want to quit, hit CTRL-C(^C)')
print('If you want to continue, hit RETURN')

input("?")

print('Opening the file')

# file should be opened in write mode, thus pass 'w', else it will be opened in read mode by default
target = open(filename, 'w')

# as file is in write mode, you can not read it
# print(target.read())

print('You selected to truncate above file, deleting its contents now!')
target.truncate()

print('Lets add some content to the file')
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target.write(line1+"\n"+line2+"\n"+line3+"\n")
target.close()