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
meals = []
for meal in menu:
    if "spam" not in meal:
        # print(meal)
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
# an if clause or filter added to the comprehension
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

# More readible than the fussy_meals below
fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not
        ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)



fussy_meals = [meal for meal in menu if
                ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

# CONDITIONAL COMPREHENSIONS

#  [meal              for meal in menu        if "spam" not in meal]
# expression               iteration                   filter(s)

# This conditional list comprehension now specifies a filter, extending the incomplete def above line 17

# A comprehension has an expression, in this example, the value of a meal.
# After the comprehension comes the iteration which is followed by one or more filters.
# [expression   iteration   filter(s)]