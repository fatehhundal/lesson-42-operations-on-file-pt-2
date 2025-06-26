with open("Assignment_File.txt", "w") as file:
    print("Rewriting the document...")
    file.write("This is the document about Codingal.")
file.close()

with open("Codingal.txt", "r") as file:
    data = file.readlines()
    print("The words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()

import os
print("Checking if my_file.txt exists...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("This file doesn't exist")

my_file = open("my_file.txt", "w")
print("Creating my_file.txt")
my_file.write("Hi! I'm Penguin. I'm a 1-year-old.")
my_file.close()

print("Removing sample_doc.txt")
os.remove("sample_doc.txt")