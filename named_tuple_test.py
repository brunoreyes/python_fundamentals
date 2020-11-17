from named_tuples_data import basic_plants_list, plants_list

print(plants_list[0])

# named tuples cannot start with an underscore

for plant in basic_plants_list:
    print(plant[0])


for plant in plants_list:
    print(plant.name, plant[1])

print()

# named tuples can change the name of one or more fields within a tuple
# tuples are immutable but can use _replace to change a name

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')
print(example)
