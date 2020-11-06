import os


def list_directories(s): # having (s) and (d) is mainly done when dealing with functions within functions

    def dir_list(d):
        # nonlocal looks for variables within inclosed functions but if not found, it'll check another inclosed function as well.
        nonlocal tab_stop # making the variable accessible within the closing scope, hence within list_directories
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)
                

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


list_directories('.')

# listing = os.walk('.') #os.walk is a recursive function
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)