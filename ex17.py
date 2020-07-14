from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying data from {from_file} to {to_file}')

in_file_data = open(from_file).read()

print(f'Input file is {len(in_file_data)} bytes')

print(f'Does the output file exists? {exists(to_file)}')
print('Hit Return if you wish to continue, else hit Ctrl-C')


out_file_data = open(to_file, 'w').write(in_file_data)

print('Copying done')