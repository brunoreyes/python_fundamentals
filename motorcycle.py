import shelve

with shelve.open("bike") as bike: # creating a file named bike and giving it all the items below
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "red"
    # bike["engine_size"] = 250

    del bike['engine_size']

    for key in bike:
        print(key)

    print('=' * 40)

    # print(bike["engine_size"])
    print(bike["colour"])