# a common source of error: converting a dictionary, that is initialized using a literal, into a shelve.

import shelve

books = shelve.open("book")

# converted dictionary
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]},
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]} # make sure to look out for additional commas


# a dictionary of books:
# {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
#                     "beans_on_toast": ["beans", "bread"],
#                     "scrambled eggs": ["eggs", "butter", "milk"],
#                     "soup": ["tin of soup"],
#                     "pasta": ["pasta", "cheese"]},
#         "maintenance": {"stuck": ["oil"],
#                         "loose": ["gaffer tape"]}}


print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])
print(books["maintenance"]["loose"])

books.close()