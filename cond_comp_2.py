menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         # print(meal)
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
# # an if clause or filter added to the comprehension
# meals = [meal for meal in menu if "spam" not in meal]
# print(meals)

# for meal in menu:
#     print(meal, "contains chicken" if "chicken" in meal
#         else "contains bacon" if "bacon" in meal else "contains egg")

# print()

# printing a set of all items within all meals, w/o duplicates
items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()

# for meal in menu:
#     for item in items:
#         if item in meal:
#             print("{} contains {}".format(meal, item))
#             break




# CONDITIONAL EXPRESSION must contain an else statement, where an if must be follwed by an else
x = 12
expression = "Twelve" if x == 12 else "unknown"
print(expression)

x = 15
expression2 = "Twelve" if x == 12 else "unknown"
print(expression2) # prints "unknown" as expected bc x isn't truthy to = twelve

# The filter has been removed here (if "spam" not in meal), but the expression is more complex
meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
#       |                   EXPRESSION                      |     ITERATION     |
print(meals)


for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)


