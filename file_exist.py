new_file = open("New_File.txt", "x")
new_file.close()

import os
print("Checking if my_file.txt exists...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("This file doesn't exist")


my_file = open("my_file.txt", "w")
my_file.write("Hi! I'm Penguin. I'm a 1-year-old.")
my_file.close()

os.remove("Codingal.txt")

os.rmdir("Folder")