#reading a file

from sys import argv

# inputs
script, filename = argv

# create file object
text = open(filename)

print(f"You want to read to read {filename}")
print(text.read())
# close file after reading it
text.close()

# read the file again by taking user input
print("What's the new filename")
filename_new = input(">")

# create new file object
text_new = open(filename_new)
print(text_new.read())
text_new.close()