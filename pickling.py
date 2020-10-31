# Serialization is a process to store values to a file to be able to be stored later

# Python's method of serialization is called pickling,
#  which is insecure so make sure to pickle trust worthy data.

# When an object is 'Pickled', it is written to a file and a format that contains the object's data
# together with sufficient information to allow the object to be recreated when loaded back in.

import pickle  # 1st. import "pickle", a python library/module 

# imelda is quite complex, containing a tuple of tuples
imelda = ("More Mayhem",
          "Imelda May",
          "2011",
        ((1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

#   COMMENT OUT CODE AFTER CREATING FILE !!
# Now, let's pickle or save the object 'imelda' effectively

with open("imelda.pickle", "wb") as pickle_file: # Here we are writing a file called imelda.pickle.
    pickle.dump(imelda, pickle_file)  # We can store the complex imelda object with a signle dumb call.
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file,protocol=0) # protocol=0 is a user friendly way to format data
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)  # if protocol not specified it auto defaults to protocol = 3

# REMEMBER: READ BACK OBJECTS IN THE SAME ORDER THEY ARE WRITTEN
with open("imelda.pickle", "rb") as imelda_pickled: # Here we are loading the value we wrote, back in.
    imelda2 = pickle.load(imelda_pickled)  # & grabing the values
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled) # this relates to 2998302 above in the wb statement.

print(imelda2)

album, artist, year, track_list = imelda2 # now we are setting the value types and printing them

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print('=' * 40)

for i in even_list: # printing each line of even_list
    print(i) 

print('=' * 40)

for i in even_list: # printing each line of odd_list
    print(i)

print('=' * 40)

print(x)

print('=' * 40)

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.") # For Mac, this removes the file so be careful