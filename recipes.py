import shelve

# blt = ["bacon", "lettuce", "tomatoes", "breads"]
# beans_on_toast = ["beans", "toast"]
# scrammled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese","water"]

with shelve.open("recipes", writeback=True) as recipes:  #writeback allows us to cache the object in memory
    # when the shelve is closed, it is saved into the file
    #writebacks can have heavy memory usage

    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrammled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    # recipes["soup"].append("crotons")

    # recipes.sync()    #be careful when using .sync()
    

    for snack in recipes:
        print(snack, recipes[snack])