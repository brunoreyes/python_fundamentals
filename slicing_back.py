#slicing backwards
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:-1:-1]  # this gives us nothing, because -1 can't be an ending index
backwards = letters[25::-1]  # this gives us everything
backwards = letters[::-1] # this gives us everything as well
print(backwards)

#Challenge

#make qpo
qpo = letters[-10:-13:-1]
print(qpo)

#make edcba
edcba = letters[4::-1]
print(edcba)

#make last 8 characters backwards
last8reversed = letters[:-9:-1] #starts at -1 bc it ends at -9 index
print(last8reversed)

#get first index
firstLetter = letters[:1]
print(firstLetter)

#get last index
lastLetter = letters[-1:]
print(lastLetter)


#produce the last 8 characters, in reverse order

