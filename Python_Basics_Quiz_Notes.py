# you can't do quotes within double quotes in Python like so: ""What's the weather like", says Will.""

# meal2 = "spam\neggs\nbeans" is the same as this
# meal4 = """spam
# eggs
# beans"""

print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")
#Expected output: Terry  John  Graham  Michael  Eric  Terry

first_name = "John"
last_name = "Cleese"
age = 78
 
#print(first_name + last_name + age)
#This will produce an error bc #'s can;t be concatenated with strings in Python

a = 45
b = 15
c = 3
 
print(a - b / c)
# since it is using PEMDAS and regular devision, it will produce a floating #: 40.0

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)
# Trick question, recall case sensitivity, the answer is 50.0

#What will this program print?

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

#Output is MTWTFSS bc M _ _ _ _ T _ _ _ _ W ...


#Given the string

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"



#we want to slice the string to extract just the digits.

#Which of these slices will NOT do what we want?
print(data[1:5])
#Correct. This slice will start at position 1, which is the : after 1, up to (but not including) the 2. The result will be :A,


#The variable flower has been given a value with the code below:
flower = "blue violet" 
#Which of the following statements will print True
print('blue' in flower)


# add flowers to flower array and shrubs to shrub array
#If flower and colour are defined as:
flower = "rose"
colour = "red"
#Which of these lines will correctly print: The rose is red
print("The {0} is {1}".format(flower, colour))

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for item in data:
    if 'Flower' in item:
        flowers.append(item)
    elif 'Shrub' in item:
        shrubs.append(item) 