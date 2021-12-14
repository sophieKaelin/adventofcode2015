print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
compass = inFile.readline()
print(compass)

def updateCoord(index, c):
    if c == '^':
        index = (index[0], index[1]+1)
    elif c == 'v':
        index = (index[0], index[1]-1)
    elif c == '>':
        index = (index[0]+1, index[1])
    else:
        index = (index[0]-1, index[1])
    return (index)

print("\n========== Part 1 ==========")
pos = (0, 0)
houses = [(0, 0)]
for c in compass:
    pos = updateCoord(pos, c)
    if pos not in houses:
        houses.append(pos)

print(len(houses))

print("\n========== Part 1 ==========")

pos = [(0, 0), (0, 0)] #x1, y1, x2, y2
houses = [(0, 0)]
for c in range(len(compass)):
    pos[c%2] = updateCoord(pos[c%2],compass[c])
    if pos[c%2] not in houses:
        houses.append(pos[c%2])

print(len(houses))