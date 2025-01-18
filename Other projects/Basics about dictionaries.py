copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'
del copper['age']

for i, j in copper.items():
    print(i, j)