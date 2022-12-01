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

# part two

topThreeTotal = 0

for _ in range(3):
    topThreeTotal += max(elves)
    elves.pop(elves.index(max(elves)))


print(topThreeTotal)

