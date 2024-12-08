print("Starting Day 8 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

tab = [['' for _ in range(len(data[0]))] for _ in range(len(data))]
locations = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        c = data[i][j]
        tab[i][j] = c
        if c != '.':
            if c not in locations:
                locations[c] = [(i,j)]
            else:
                locations[c].append((i,j))

def get_antinodes(tab, locations):
    antinodes = []
    for k in locations:
        if len(locations[k]) == 1:
            continue
        for i in range(len(locations[k])):
            for j in range(i+1, len(locations[k])):
                p1 = locations[k][i]
                p2 = locations[k][j]
                diff = (p2[0]-p1[0], p2[1]-p1[1])
                firstAntinode = (p1[0]-diff[0], p1[1]-diff[1])
                secondAntinode = (p2[0]+diff[0], p2[1]+diff[1])
                if firstAntinode[0] >= 0 and firstAntinode[0] < len(tab) and firstAntinode[1] >= 0 and firstAntinode[1] < len(tab[0]) and firstAntinode not in antinodes:
                    antinodes.append(firstAntinode)
                if secondAntinode[0] >= 0 and secondAntinode[0] < len(tab) and secondAntinode[1] >= 0 and secondAntinode[1] < len(tab[0]) and secondAntinode not in antinodes:
                    antinodes.append(secondAntinode)
    return antinodes
    

print("\n------------------------------\nComputing first part")
antinodes = get_antinodes(tab, locations)
print(f"Answer : {len(antinodes)}\n------------------------------\n")

def get_antinodes_harmonics(tab, locations):
    antinodes = []
    for k in locations:
        if len(locations[k]) == 1:
            continue
        for i in range(len(locations[k])):
            for j in range(i+1, len(locations[k])):
                p1 = locations[k][i]
                p2 = locations[k][j]
                if p1 not in antinodes:
                    antinodes.append(p1)
                if p2 not in antinodes:
                    antinodes.append(p2)
                diff = (p2[0]-p1[0], p2[1]-p1[1])
                firstAntinode = (p1[0]-diff[0], p1[1]-diff[1])
                while firstAntinode[0] >= 0 and firstAntinode[0] < len(tab) and firstAntinode[1] >= 0 and firstAntinode[1] < len(tab[0]):
                    if firstAntinode not in antinodes:
                        antinodes.append(firstAntinode)
                    firstAntinode = (firstAntinode[0]-diff[0], firstAntinode[1]-diff[1])
                secondAntinode = (p2[0]+diff[0], p2[1]+diff[1])
                while secondAntinode[0] >= 0 and secondAntinode[0] < len(tab) and secondAntinode[1] >= 0 and secondAntinode[1] < len(tab[0]):
                    if secondAntinode not in antinodes:
                        antinodes.append(secondAntinode)
                    secondAntinode = (secondAntinode[0]+diff[0], secondAntinode[1]+diff[1])
    return antinodes

print("\n------------------------------\nComputing second part")
harmonic_antinodes = get_antinodes_harmonics(tab, locations)
print(f"Answer : {len(harmonic_antinodes)}\n------------------------------")