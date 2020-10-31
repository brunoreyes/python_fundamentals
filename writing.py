cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

# This was ran already, and the file has been written, so we can comment it out now.
# with open("cities.txt", "w") as city_file:
#     #here we are writing a file called cities.txt to the same folder with the content from the cities list
#     for city in cities:
#         print(city, file=city_file)


cities = []

with open("cities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city.strip('\n')) # .strip('\n') removes the new line from the print

print(cities)
for city in cities:
    print(city)
# Printed out result:
# Adelaide
# Alice Springs
# Darwin
# Melbourne
# Sydney


# Instead of this:

# Adelaide

# Alice Springs

# Darwin

# Melbourne

# Sydney


# Here we created a file and commented out the code afterwards.
# imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# with open("imelda3.txt", 'w') as imelda_file: # we created a txt file using the tuple: imelda
#     print(imelda, file=imelda_file)

with open("imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda  #here we are appending each value a name
# appending adds data to the end of the file without messing with any of the data already in the file
print(title)
print(artist)
print(year)
print(tracks)