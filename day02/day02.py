print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
_list = []

for line in inFile:
    temp = line.replace("\n","")
    temp = temp.split("x")
    temp = sorted(map(int, temp))
    _list.append(temp)

print(_list)

print("\n========== Part 1 ==========")
paper = 0
for dim in _list:
    sides = sorted([2*dim[0]*dim[1],2*dim[1]*dim[2],2*dim[2]*dim[0]])
    paper += sides[0] + sides[1] + sides[2] + sides[0]/2

print(paper)

print("\n========== Part 2 ==========")
ribbon = 0
for dim in _list:
    ribbon += 2*dim[0] + 2*dim[1] + dim[0] * dim[1] * dim[2]

print(ribbon)