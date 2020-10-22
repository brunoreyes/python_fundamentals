pangram = "The quick brown fox jumps over the lazy dog"
#pangram is a phrase that contains all letters of the alphabet, to check lets sort
letters = sorted(pangram)
print(letters)
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'T', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'f', 'g', 'h',
# 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'o', 'o', 'o', 'p', 'q', 'r', 'r', 's', 't', 'u', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
#sort can sort numbers, letters, and literals
sorted_numbers = sorted(numbers)
print(sorted_numbers)
#don't do this, sorted = sorted(numbers)
missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)  #here we see s is missing, making this not a pangram

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
#to sort without having to worry about capitilization use  key=str.casefold

names = [
    'eric','John', 'terry', 'micheal', 'Terry'
]
names.sort(key=str.casefold)
print(names)  #['eric', 'John', 'micheal', 'terry', 'Terry']

empyty_list = []
more_numbers = numbers[:] #here we slice
digits = sorted("439228394")
print(digits)  # ['1','2','3','4','5','6','7','8','9']
print(numbers is more_numbers) #False not fully true
print(numbers == more_numbers)  #True truthy


