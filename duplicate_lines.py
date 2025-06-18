outputFile = open("UpdatedFile.txt", "w")
inputFile = open("Repeated.txt", "r")
lines_seen_sofar = set()
print("Eliminating duplicate lines...")

for line in inputFile:
    if line not in lines_seen_sofar:
        outputFile.write(line)
        lines_seen_sofar.add(line)

inputFile.close()
outputFile.close()