from sys import argv

script, file_name = argv

def print_file(f):
    print(f.read())

def rewind(f):
    f.seek(0)

current_file = open(file_name)

print("Print complete file\n")
print_file(current_file)

print('Rewind like a tape')
rewind(current_file)

