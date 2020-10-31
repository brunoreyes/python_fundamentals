# AFTER WRITING AND READING THE BINARY FILE, MAKE SURE TO COMMENT OUT THE CODE !!

# with open("binary", "bw") as bin_file: # bw - writing a binary file.
# # Processing binary data is done for many use cases such as processing an img file.
#     for i in range(17): # We want the numbers from 0 - 16 be processed.
#         bin_file.write(bytes([i]))  # We are convert to bytes & create a list to write the binary file.

# When trying to read the file, it'll show up a differently than expected and can't be traditionally read.
# with open("binary", "br") as binFile: # br - reading a binary file.
#     for b in binFile: 
#         print(b)



# variables  &   their HEX equivalents
a = 65534        # FF FE
b = 65535        # FF FF
c = 65536        # 00 01 00 00
x = 2998302      # 00 2D C0 1E

with open("binary2", "bw") as bin_file: #writing another binary file, this time 
    bin_file.write(a.to_bytes(2, 'big'))  # converts 'a' to a byte, making length = 2 & byteOrder = big
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))    # the max length for 2 bytes is 2^16 - 1 = 65,535
    bin_file.write(x.to_bytes(4, 'little')) # anything above 65,535 (65536 & 2998302) is 4 bytes
                                            # or greater than # 65,535 but less than 4^16.
                                            # 4 bytes instead of 3 b/c it's preferable to write in even #'s
                                            # when it comes to binary.

#byteOrder "little" shows the least significant byte 1st while "big" shows the most significant byte 1st.

# Reading the binary file, and assiging the previous values to new values and printing them.
with open("binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), 'big') # e relates to a
    print(e) # Output: 65534
    f = int.from_bytes(bin_file.read(2), 'big') # f relates to b
    print(f) # Output: 65535
    g = int.from_bytes(bin_file.read(4), 'big') # g relates to c
    print(g) # Output: 65536
    h = int.from_bytes(bin_file.read(4), 'big') # h relates to x 'big'
    print(h) # Output: 2998302
    i = int.from_bytes(bin_file.read(4), 'big') # i relates to x 'small'
    print(i) # Output: 515910912
                                            
