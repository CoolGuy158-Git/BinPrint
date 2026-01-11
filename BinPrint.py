import os
import textwrap
user_file = input("Enter the file name: ")
try:
    with open(user_file, "rb") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
    exit()
binary = ' '.join(format(byte, '08b') for byte in data)
binary_wrapped = '\n'.join(textwrap.wrap(binary, 64))
temp_file = "binary_dump.txt"
with open(temp_file, "w") as f:
    f.write(binary_wrapped)
try:
    os.startfile(temp_file, "print")
    print("Printing started.")
except Exception as e:
    print(f"Printing failed: {e}")
