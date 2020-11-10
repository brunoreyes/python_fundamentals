from getters_and_setters import Player  # Generally not the best practice, but we are placing each class
# in there individual file, just to show what getters and setters do (same functions as JS)

tim = Player("Tim")
print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim.lives)  # Unlike Java and C++, Python gives direct access to data attributes
# getters and setters are not typically used within Classes for Python
# print(tim._get_name())
# tim.set_lives(300)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim._lives = 9
print(tim)

# although setters aren't needed, they are useful when you want to include validation on the
# values your data attributes can be set to

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level -= 2
print(tim)

tim.score = 500
print(tim)