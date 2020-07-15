# passing argument as list
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1} and arg2: {arg2}')

# passing arguments individually
def print_two_again(arg1, arg2):
    print(f'arg1 is equal to = {arg1} and arg2 is equal to = {arg2}')

# pass no argument
def print_none():
    print('No arguments passed to me')

print_two('john', 'doe')
print_two_again('jack', 'rayn')
print_none()