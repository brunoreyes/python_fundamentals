for i in range(1, 13): #1 to 12
    for j in range(1, 13):
        print("{0} time {1} is {2}".format(j, i, i * j))  #i time j is (i * j)
        #print("-----------------") this would give us a line after every product
    print("-----------------")  #here  after each print of 12 products each time will be seperated by line
    