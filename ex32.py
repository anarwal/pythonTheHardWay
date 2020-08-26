#using for loops

the_count = [1,2,3,4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# create a list
elements = []

for i in range(0,6):
    print(f"Adding {i} to list")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")