burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

# nested list comprehension version
for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)
print() # output: ('spicy bean', 'spam')

# for loop version
# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]: 
    print(nested_meals)  # output: [('beef', 'cheese'), ('chicken', 'cheese'), ('spicy bean', 'cheese')]
    

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]: 
    print(nested_meals)
    
# Create a nested comprehension to produce the times tables for values 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

times = [(i, i * j) for i in range(1, 11) for j in range(1, 11)] 
print(times)


for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)