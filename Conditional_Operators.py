age = int(input("How old are you? "))

if age >= 16 and age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-"* 80)

#when comparing conditions using and, python will stop once it finds something false
# when or, python will run until it finds something true
if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# Less than <
# Less than or equal to  <=
# Greater than >
# Greater than or equal to >=
# Equal to ==
# Not equal to !=

