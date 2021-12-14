print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
compass = inFile.readline()
print(compass)

print("\n========== Part 1 ==========")
x, y = 0, 0
houses = [(0, 0)]
for c in compass:
    if c == '^':
        y +=1
    elif c == 'v':
        y -=1
    elif c == '>':
        x +=1
    else:
        x -=1
    if (x, y) not in houses:
        houses.append((x,y))

print(len(houses))

print("\n========== Part 1 ==========")
x1, y1, x2, y2 = 0, 0, 0, 0
houses = [(0, 0)]
for c in range(len(compass)):
    if compass[c] == '^':
        if c%2==0:
            y1 +=1
        else:
            y2 +=1
    elif compass[c] == 'v':
        if c%2==0:
            y1 -=1
        else:
            y2 -=1
    elif compass[c] == '>':
        if c%2==0:
            x1 +=1
        else:
            x2 +=1
    else:
        if c%2==0:
            x1 -=1
        else:
            x2 -=1
    if c%2 == 0 and (x1, y1) not in houses:
        houses.append((x1,y1))
    elif (x2, y2) not in houses:
        houses.append((x2,y2))

print(len(houses))