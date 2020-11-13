import ducks

flock = ducks.Flock()

donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
percy = ducks.Penguin()  # shouldn't be able to fly on account of not having the attribute to do so.

# add_ducking ducks to the flock
flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy) # warning bc percy isn't a duck, and add_duck() expects & only takes in ducks
# AttributeError was passed to migrate() , which shouldn't have happened so we changed migrate()
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)


flock.migrate()