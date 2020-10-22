available_parts = ["computer","monitor","keyboard","mouse","mouse pad","hdmi cable", "dvd drive"] #iterable list
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = '-'
computer_parts = []  #creating an empty list

while current_choice != '0':
    if current_choice in valid_choices:
      
        index = int(current_choice) - 1
        # To check if the part is already in their list we do the following below
        # To remove an item from a list use s.remove(x), removing the first item from s where s[i] = x
        # removing the value that has a matching index, if no matching value you get a ValueError
        chosen_part = available_parts[index]
        # if an item like a monitor is already within the list, when entering the # for monitor again, remove monitor.
        # so pressing 2 adds or appends the monitor, pressing 2 again removes it
        if chosen_part in computer_parts:
            # Since here we checked if chosen_parts was in the list we won't get an error when removing.
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
        # if current_choice == "1":
        #     computer_parts.append("computer")
        # elif current_choice == "2":
        #     computer_parts.append("monitor")
        # elif current_choice == "3":
        #     computer_parts.append("keyboard")
        # elif current_choice == "4":
        #     computer_parts.append("mouse")
        # elif current_choice == "5":
        #     computer_parts.append("mouse mat")
        # elif current_choice == "6":
        #     computer_parts.append("hdmi cable")
    else:
       print("Please add options from the list below:")
       for number, part in enumerate(available_parts):
           print("{0}: {1}".format(number + 1, part))  #adding 1 to index
           #the enumerate function returns each item with it's index position
#enumerate returns pairs of value, with index position, an the item
# which is more efficient than print("{0}: {1}".format(availabe_parts.index(part) + 1, part))
    current_choice = input()

print(computer_parts)


 # print("Please add options from the list below:")
        # print("1: computer")
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5: mouse mat")
        # print("6: hdmi cable")
        # print("0: to finish")