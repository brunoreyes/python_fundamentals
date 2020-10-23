albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
         ("Bad Company", "Bad Company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011 ),
         ("Ride the Lightning", "Metallica", 1984),
         ]

print(len(albums))  # 15

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
        .format(name, artist, year))

        # .format(album[0], album[1], album[2]))

for album in albums:
    name, artist, year = album
    print("Album:{}, Artist: {}, Year: {}"
        .format(name, artist, year))

#homogeneous means the same
#heterogeneous means different

#If you want to append or add new items, use a list because tuples can't be added to b/c uniterable
#If data is different/heterogenous like artist, tracklist, and release year, it's better to use tuples