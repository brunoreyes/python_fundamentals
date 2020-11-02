# turtle is a children's game to move a turtle that leaves a trail (line), in multiple directions.

import turtle  # enables the python turtle graphic
# import time # enables the python turtle graphic to stay on the screen

#with imports we can choose just like in React, specifically what to import from module as shown below:
# from turtle import forward, right, done

# DON'T import like this, b/c you don't know what you are importing & could conflict with variable names
# from turtle import *

# noinspection PyUnresolvedReferences
# this handles suppression of errors

# forward(150)  # turtle going forward 150 degrees with specified import: from turtle import forward, right, done
turtle.right(250)  # making the turtle turn to the right 250 degrees
turtle.forward(150)  # forward(150) is making the turtle go forward 150 steps
turtle.circle(75) # this command will only work if specified within the import or generally import turtle

# time.sleep(4) # keeping the python turtle graphic up for a time of 4 seconds

turtle.done() #this command enabled us to keep the turtle module up until we close it manually

