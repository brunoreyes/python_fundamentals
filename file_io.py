# here we are opening a file
# jabber = open("sample_python_text_file_in_folder.txt", 'r')

# # how to open files outside of project folder
# # jabber = open("/Users/brunoreyes/Desktop/sample_python_text_file.txt",'r') # r sets it to read-only mode
# # in windows we probably would do "C:\\documents and settings\\my documents\\sample.txt"

# # here we are iterating through each line of text and printing it off
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#     # print(line)

# # here we are closing the file
# jabber.close()



# using "with" we don't have to close the file with .close(), it does so automatically
# "with" closes files even if there's an error reading file.
# "open", by itself (without "with") doesn't close if there's an error reading the file

# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline() # .readline() reads each line of a file and returns a string for each line
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')
#

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines() #.readlines() reads the entire file and returns each line as a string
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
    #.read() reads the entire file and if it's a text file,
    #it returns a string of the optional text file

for line in lines[::-1]:
    print(line, end='')

        