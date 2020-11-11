import random

class Enemy: # Superclass, that can be inheritated from.

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name  # indication we shouldn't be changing these attrubutes manually
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points in damage and have {} life points left".format(damage, self._hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self._alive = False


    def __str__(self):
        return "name: {0._name}, Lives: {0._lives}, Hit Points: {0._hit_points}".format(self)


class Troll(Enemy):  # Troll is a subclass that inherits/extends from the Enemy Class.
    # pass  # pass does not do anything but it doesn't get ignored by the compiler
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23) # super(Troll, self) is the same as super()
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        # Passing name of class "Troll" and current instance "self" into the base class
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
    def grunt(self):
        print("Me {0._name} will stomp you".format(self))
        
class Vampire(Enemy):

    def __init__(self, name): #here is a subclass calling to the superclass
        super().__init__(name=name, lives=3, hit_points=12)

    def charisma(self):
        print("Come hang out with me {0._name}, and party all night".format(self))

    def dodges(self):
        
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False


    def take_damage(self, damage):
        # pass
        if not self.dodges():
            super().take_damage(damage=damage)

        # When searching for python info, make sure to search within the version of python you are using.


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name)
        self._hit_points = 140

    def take_damage(self, damage):
        # pass
        super().take_damage(damage // 4)