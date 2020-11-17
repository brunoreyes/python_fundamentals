from named_tuples_data import people, basic_plants_list, plants_list, plants_dict

#  people = []

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")


if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")


if any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

# using generator ()
if any(plant.plant_type == "Cactus" for plant in plants_dict.values()):
    print("This pack contains grass")
else:
    print("No grasses in this pack")


# dictionary, not in order, using key
if any(plants_dict[key].plant_type == "Cactus" for key in plants_dict):
    print("This pack contains grass")
else:
    print("No grasses in this pack")