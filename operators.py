a = 12
b = 3

#mathematical expressions
print(a + b)
print(a - b) 
print(a / b)  #4 simple division produces a float #4.0, we cant use it 
print(a // b)  #4 integer division rounds the answer to the nearest number
print(a % b) #0 is the remainder after division

print()
for i in range(1, 4):
    #recall 1,2,3 and not the last #4
    print(i)

# for "i in range(1, a / b)"" this wouldn't work bc of simple division would produce a float # not an integer
for i in range(1, a // b):
    print(i)

#you sell buns for $2.40 each. A customer has $15 and wants as many as he can buy. Have to sell full bun.
bun_price = 2.40
money = 15
print(money // bun_price)  #4.0  , using integer division we are given a rounded number, whereas real division wouldn't

#PEMDAS
#15/3 - 48
print(a + b / 3 - 4 * 12)  #expect -35 or 5 - 48,
print(((a+b)/3 - 4)* 12) #expecr 15/3 = 5-4 =1 * 12 = 12