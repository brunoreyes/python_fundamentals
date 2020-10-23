menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]

#     print(menu)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()  #here we print ever meal sperated from one another
    
# or

for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    #generator allows us to insert commas w/o trailing commas
    
    print(items) 