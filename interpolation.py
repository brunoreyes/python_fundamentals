age = 24
print("My age is %d years" % age)  #here %d will be replaced by a %value that comes after the string

major = "years"
minor = "months"
print("My age is %d %s, %d %s" %(age, major, 6, minor))  # %d will produce an integer output & %s will produce a string output
#Output: My age is 24 years, 6 months
print("PI is approxiamately %f" % (22 / 7))  #%f is the floating point result
#Output: PI is approxiamately 3.142857

print("PI is approxiamately %60.50f" % (22 / 7))
#Output: PI is approxiamately 3.14285714285714279370154144999105483293533325195312
# %e is used for scinetific notification
# %o is used for octodecimal notification
# %x is used for hexidecimal notification