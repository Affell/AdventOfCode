print("Starting Day 12 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

tab = []
for line in data:
    tab.append(list(line))

def bfs(x, y, target, elements, walls, visited):
    if (x, y) in visited:
        return tab[x][y] == target
    visited.append((x, y))
    if x < 0 or x >= len(tab) or y < 0 or y >= len(tab[0]) or tab[x][y] != target:
        return False
    elements.append((x, y))
    if not bfs(x-1, y, target, elements, walls, visited): # up
        walls[0].append((x, y))
    if not bfs(x+1, y, target, elements, walls, visited): # down
        walls[1].append((x, y))
    if not bfs(x, y-1, target, elements, walls, visited): # left
        walls[2].append((x, y))
    if not bfs(x, y+1, target, elements, walls, visited): # right
        walls[3].append((x, y))
    return True


print("\n------------------------------\nComputing first part")
groups = []
edges = []
visited = []
for i in range(len(tab)):
    for j in range(len(tab[0])):
        if (i, j) not in visited:
            elements = []
            walls = [[], [], [], []]
            bfs(i, j, tab[i][j], elements, walls, [])
            edge = []
            for element in elements:
                if element[0] == 0 or (element[0]-1, element[1]) not in elements:
                    edge.append(element)
                if element[0] == len(tab)-1 or (element[0]+1, element[1]) not in elements:
                    edge.append(element)
                if element[1] == 0 or (element[0], element[1]-1) not in elements:
                    edge.append(element)
                if element[1] == len(tab[0])-1 or (element[0], element[1]+1) not in elements:
                    edge.append(element)
            groups.append((elements, walls))
            edges.append(edge)
            visited.extend(elements)

price = 0
for i in range(len(edges)):
    price += len(edges[i]) * len(groups[i][0])
print(f"Answer : {price}\n------------------------------\n")

def side_bfs(x, y, group, elements, visited):
    if (x, y) in visited:
        return
    visited.append((x, y))
    if x < 0 or x >= len(tab) or y < 0 or y >= len(tab[0]) or (x, y) not in group:
        return
    elements.append((x, y))
    side_bfs(x-1, y, group, elements, visited)
    side_bfs(x+1, y, group, elements, visited)
    side_bfs(x, y-1, group, elements, visited)
    side_bfs(x, y+1, group, elements, visited)

print("\n------------------------------\nComputing second part")
sides = []
for elem, walls in groups:
    group_sides = []
    for dir in walls:
        visited = []
        for wall in dir:
            if wall in visited:
                continue
            side = []
            side_bfs(wall[0], wall[1], dir, side, [])
            group_sides.append(side)
            visited.extend(side)
    sides.append(len(group_sides))

price = 0
for i in range(len(groups)):
    price += sides[i] * len(groups[i][0])
print(f"Answer : {price}\n------------------------------")