with open("Codingal.txt", "w") as file:
    file.write("Hi! I'm Penguin. I'm a 1-year-old.")
file.close()

with open("Codingal.txt", "r") as file:
    data = file.readlines()
    print("The words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()