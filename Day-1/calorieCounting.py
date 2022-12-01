elves = []
f = open("input.txt", "r")
tempCals = 0
for line in f:
    if line == "\n":
        elves.append(tempCals)
        tempCals = 0
    else:
        tempCals += int(line)
print(max(elves))