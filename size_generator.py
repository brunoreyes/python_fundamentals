import sys


def my_range(n: int):  # we cannot iterate over an int
    print("my_range starts")
    start = 0
    while start < n:
        print("mu_range is returning {}".format(start))
        yield start
        start += 1

# _ = input("line 12")
big_range = my_range(5)  # you should not assign a variable to a generator
big_range = my_range(5)

# _ = input("line 15")
# print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

# _ = input("line 22")

for value in big_range:
    # _ = input("line 25 - inside the for loop")
    big_list.append(value) # 1st value added to the list is 1

print("big_list is {} bytes".format(sys.getsizeof(big_list)))  # while big_list takes up 9016 bytes
print(big_range) 
print(big_list)

print("leeping again... or not")
for i in big_range:
# for i in my_range(5):
    print("i is {}".format(i))