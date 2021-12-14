print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
sequence = inFile.readline()

print("\n========== Part 1 ==========")

print(sequence.count('(') - sequence.count(')'))

print("\n========== Part 2 ==========")
floor = 0
for c in range(len(sequence)):
    if sequence[c] == ")":
        floor -=1
        if floor < 0:
            print("Basement: " + str(c+1))
            break
    else:
        floor +=1