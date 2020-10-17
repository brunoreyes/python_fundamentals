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
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
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