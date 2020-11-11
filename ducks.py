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

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)
    donald.fly()

    percy = Penguin() # Our penguin is passing the duck test
    test_duck(percy)

# when a bird looks like a duck, acts like a duck, and quacks like a duck, I call that bird a duck
# duck-typed means dynamic dispatching and duck typing, as fas as Python is concerned, percy is a duck

# inheritance results in a 'is a' relationship.
# the enemy is a monster, vampire, or troll

# composition and aggregation has a 'has a' relationship
# the player has a sword