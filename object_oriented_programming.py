class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):  # the presence of the parameter is called self, so keep it as self
        self.on = True # self is a reference to the instance of a class
        

# when a function is a part of a class in Python, it is considered as a method
kenwood = Kettle("Kenwood", 8.99) # An instance of the class Kettle called kenwood
print(kenwood.make) # name, make, and price are accessed using dot notation
print(kenwood.price) # kenwood would also be called a data attribute

kenwood.price = 12.75 # Changing the price or attribute of the instantiated object, kenwood
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))
# you can call out an instance like kenwood or kettle to grab their make and price
# if it's a Kenwood kettle, then kenwood would be considered an instance of the kettle class,
# or an object of type Kettle.
# each instance like kenwood or hamilton have their own value calle

# using a kettle or self-igniting cigarette
# ( both have extensive functionality embedded into each)

a = 12
b = 4
print("a:{} + b:{} = {}".format(a,b,a + b))
print(a + b)
print(a.__add__(b))  # everything in python is an object, even classes and functions(methods)

'''
Class: template for creating objects, of which, all under the same class, will have the same traits.
Objects: an instance of a class.
Instantiate: creating an instance of a class. 
Method: a function defined within a class. 
Attribute: a variable bond to an instace of a class.
'''

# Each way has the exact same effect, turning on the self.on for each instantiated object
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 1.5 # It is possible to add additional attributes to individual objects of a class 
print(kenwood.power)
# If we did print(hamilton.power) we would get an error
print(Kettle.power_source)  # similar to static fields, placing a variable within a class
print(kenwood.power_source) # can be attributed to all Instantiate objects
print(hamilton.power_source)
print(kenwood.__dict__) 
print(Kettle.__dict__)  # here we can see a dictionary, of what attributes are connects to which objects

print("switch power source to atomic")
Kettle.power_source = "atomic"
print(hamilton.power_source) 