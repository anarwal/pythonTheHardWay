cars = {
    'sedans': ['accord', 'city'],
    'trucks': ['f150', 'f250'],
    'suvs': ['evoque', 'velar', 'sports'],
    'hatchbacks': ['alto', 'wagonr', 'swift']
}

manufacturer = {'sedans': 'honda', 'trucks': 'ford', 'suvs': 'range rover'}

manufacturer['hatchbacks'] = 'maruti'

#print some manufacturers
print('-'*20)
print('hatchbacks are manufactured by', manufacturer['hatchbacks'])
print('sedans are manufactured by', manufacturer['sedans'])

#print cars by manufacturer
print('-'*20)
print('Types of sedans: ', cars['sedans'])
print('Types of suvs: ', cars['suvs'])

#print all car types
print('-'*20)
for cars, models in list(cars.items()):
    print(f"{models} are {cars}")

print('-'*20)
try:
    car = cars.get('luxury')
except:
    print("Sorry no luxury type car")