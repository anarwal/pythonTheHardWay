print("Practicing functions")
print("\nalong with adding new lines")
print("\nnewlines along with\t\ttabs")

short_story = '''
The lovely world 
with logic so firmly planted 
cannot discern\nthe needs of love
nor comprehend passion from intuition
'''

print("---------")
print(short_story)
print("---------")

ten = 30-5+10-25
print(f'this should be equal to ten: {ten}\n')

def new_formula(ingredient):
    jelly_beans = ingredient*100
    jars = jelly_beans/10
    crates = jars/5
    return jelly_beans, jars, crates

new_formula_ingredient = 10000
beans, jars, crates = new_formula(new_formula_ingredient)

print("given input of: {}".format(new_formula_ingredient))
print(f'Output is {beans} beans\n {jars} jars\n {crates} crates.')
