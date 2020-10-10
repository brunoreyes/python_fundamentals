parrot = "Norwegian Blue"
print(parrot)
#Slicing
print(parrot[0:6])  #Norweg starts index 0 upto but not including 6
print(parrot[3:5])  #we starts index 3, it includes it upto but not including 5, so just w, index 3, and e, index 4
print(parrot[:9])  #Norwegian starts at index 0 and goes upto but nut including index 9
print(parrot[10:])  #Blue, starts at index 10 and goes til the end
print(parrot[6:])  #ian Blue
print(parrot[:6])  #Norweg
print(parrot[:6] + parrot[6:])  #Norwegian Blue
print(parrot[:])  #Norwegian Blue, "[:]" produces a copy of the original
print(parrot[-4:-2])  #Bl
print(parrot[-4:12])  #Bl starts from the negative index, ends on the positive index
letter = "abcdefghijklmnopqrstuvwxyz "
print(letter[7] + letter[4:5] + letter[-3] + letter[26:] + letter[18:21])  #hey stu
print(parrot[0:6:2]) #Nw starts at index 0, goes upto but not including index 6, and goes by 2, 
number = "9,233,345,678"
print(number[1::4])  #,,,
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

#print(parrot[3])  #expect w bc index 0,1,2,3
#continue printing out we win on seperate lines
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[0])

#print we win using negative index
#the last value in a string is -1, not 0, and the first is -14
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print(parrot[3 - 14])
# print(parrot[4 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[0 - 14])

