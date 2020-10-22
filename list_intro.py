computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]  #a simple list

for part in computer_parts:
    print(part)

print(computer_parts[2])  #prints out keyboard

print(computer_parts[0:3])  #slicing only prints out an array including computer to mouse

print(computer_parts[-1])  #here slicing prints out mouse mat

computer_parts[3:]=["trackball"]
# strings are immutable, meaning they cannot be changed
# lists on the other hand are mutable and they can be changed

