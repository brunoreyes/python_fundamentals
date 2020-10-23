welcome = "Welcome to my Nightmare", "Alice Cooper", 1975 #this is a tuple
bad = "Bad Company", "Bad Company", 1974 #this is a tuple
budgie = "Nightflight", "Budgie", 1981 #this is a tuple
imelda = "More Mayhem", "Emilda May", 2011  #this is a tuple
metallica = "Ride the Lightning", "Metallica", 1984 #this is a tuple

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artist, year = metallica
print(title) #More unpacking, more developer friendly data
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])  #Here the code is calculating the area of a coffee table but that's not clear

name, length, width, height, price = table #here we are naming each index within our tuple
print(length * width)  #Making it easier to use our variables
# It is crucial to remember to unpack tuples, and also list if the size doens't change

# metallica2 = list(metallica)
# print(metallica2)

# metallica2[0] = "Master of Puppets"
# print(metallica2) #creating a new list can help mutate.

# Don't try to change an item within a tuple, you'll get an error
# CAN'T DO THIS: metallica[0] = "Thunder" b/c it's within a tuple!!!

# Two reasons to choose a tuple over a list
# 1. Tuples are immutable, so they protect the integrity of your data
