class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio # ratio of wings 2:3 still can fly but it hard, 1:1 can fly perfectly

    def fly(self):
        if self.ratio > 1:
            print("Wee, this is fun")
        elif self.ration == 1:
            print("This is hard work, but i'm flying")
        else:
            print("I think I will just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water is lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate # adding a reference to the aviate method

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")

    def aviate(self):
        print("I won the lottery and bought a learjet")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

class Mallard(Duck):
    pass

class Flock(object):
    def __init__(self):
        self.flock = []
    
    def add_duck(self, duck: Duck) -> None:  # type of perameter is duck, and we return None
        fly_method = getattr(duck, 'fly', None)  # getattr(,,) checks obj's dictionary to see
            # if it contains the attribute specified, in this case 'fly'.
        if callable(fly_method):  # functions and methods are callable but plain attributes aren't
                    # however in this case we are calling it within a function called 'fly_method'.

        # if isinstance(duck, Duck): # here, isinstance is checking if the duck is part of class Duck
            self.flock.append(duck)  # focus on behavior, not type of object
        else:
            raise TypeError("Cannot add duck, are you sure it's not a"+ str(type(duck).__name__))
    
    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                # raise AttributeError("Testing exception handler in migrate") # testing exceptions # TODO: remove before release
            except AttributeError as e: # here a reference to the exception is stored in a variable
                # pass  # when raising an error, please do so outside of a for loop to prevent termination
                print("One Duck Down")
                problem = e
                # raise    # don't raise error within for loop`
        if problem:
            raise problem # specify the exception you want to raise outside and at the end of the for loop

if __name__ == '__main__':
    donald = Duck()
    # test_duck(donald)
    donald.fly()

    percy = Penguin() # Our penguin is passing the duck test
    # test_duck(percy)






# when a bird looks like a duck, acts like a duck, and quacks like a duck, I call that bird a duck
# duck-typed means dynamic dispatching and duck typing, as fas as Python is concerned, percy is a duck

# inheritance results in a 'is a' relationship.
# the enemy is a monster, vampire, or troll

# composition and aggregation has a 'has a' relationship
# the player has a sword