#do not name any python file: "range"
for i in range(1, 21):
    print("i is now {}".format(i))
    #this prints out 1,2,3,4..20 but not the last number: 21 just like number[1:5] doesn't print out 5

    #if the range was range(10,15), we would just get #10-14

#Print out all the numbers 0 to 9, each number on a new line
#for i in range(0, 10):
    #print(i)

for i in range(10): #the default start value is now 0 so this will print numbers 0-9
    print("i is now {}".format(i))

for i in range(0,10, 2): 
    print("i is now {}".format(i))  #this will print out 0,2,4,6,8 but not 10

for i in range(10,0, -2): 
    print("i is now {}".format(i))  #this will print out 10,8,6,4,2 so instead of not getting 10, this time we don't get 0

# if age in range(16,66): is the same as 16 <= age <= 65

#Ex: Print out all # from 0 to 100 that are divisible by 7
for i in range (0,101,7):
    print(i)
# or for i in range(101)[::7]:
    #print(i)