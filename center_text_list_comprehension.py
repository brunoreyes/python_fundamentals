def center_text(*args, sep=' '):
    # text = ""
    # for arg in args:
    #     text += str(arg) + sep
    text = "-".join([str(arg) for arg in args])  # this is a list comprehension
    # text = "-".join(str(arg) for arg in args) # this is a generator
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin + text)
    

center_text("span and eggs")
center_text("span, span, and eggs")
center_text(12)
center_text("span, span, span, and eggs")

center_text("first","second", 3, 4, "spam")