a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 3
print(x) # x is bound to one
print(y)  # y is bound to two
print(z)  # z is bound to three

print("Unpacking a tuple")

data = 1, 2, 76  #data represents a tuple
x, y, z = data # the values of data are now bounded to x,y, and z
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]  #This isn't a tuple, it's a list, if something changes the list, code breaks.
# data_list.append(15) This would crash the code, you can't change a list and unpack it.
p, q, r = data_list
print(p)
print(q)
print(r)

#The second advantage of tuples, is that you can always unpack them successfully
# Since a tuple cannot be changed, you always know how many items there are to unpack
# That's why it is refered to "Unpacking a tuple" even though you can unpack any sequence type