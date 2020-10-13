#Write a program to print out all the numbers from 0 to 20 that aren;t divisible by 3 or 5
for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)