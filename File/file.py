
# f = open('D:\my personal drive\OneDrive\Desktop\CODE\DSA\Python\Python\File\example.txt', 'r')
# print(f.read())
# f.close()

## another way

# with open('example.txt', 'w') as file:
#     file.write('Hello, this is a test!\n')
#     file.write('Writing to a file in Python is easy.\n')
#     file.close()

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
#     file.close()

# with open('example.txt', 'a') as file:
#     file.write('Appending additional content.\n')
#     file.close()


# with open('example.txt', 'r') as file:
#     content = file.read()
#     file.close()
#     print(content)


with open('binary_data.bin', 'wb') as file:
    data = bytearray([0x48, 0x65, 0x6C, 0x6C, 0x6F]) 
    file.write(data)

with open('binary_data.bin', 'rb') as file:
    binary_data = file.read()
    print(binary_data)
    hex_data = ' '.join(format(byte, '02X') for byte in binary_data)
    print("Hexadecimal representation:", hex_data)
