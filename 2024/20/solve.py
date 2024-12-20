print("Starting Day 20 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

start, end = (0, 0), (0, 0)
tab = []
for i, line in enumerate(data):
    tab.append(list(line))
    if 'S' in line:
        start = (i, line.index('S'))
    if 'E' in line:
        end = (i, line.index('E'))

def a_star(tab, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbours(node):
        neighbours = []
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = node[0] + i, node[1] + j
            if 0 <= x < len(tab) and 0 <= y < len(tab[0]) and tab[x][y] != '#':
                neighbours.append((x, y))
        return neighbours

    open_set = {start}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        open_set.remove(current)
        for neighbour in get_neighbours(current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbour, float('inf')):
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour, end)
                if neighbour not in open_set:
                    open_set.add(neighbour)

    return None

original_path = a_star(tab, start, end)

from itertools import combinations

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

dist = []
for i, node in enumerate(original_path):
    dist.append((node, i))

def get_cheats(time_allowed, min_save):
    cheats = 0
    dist = []
    for i, node in enumerate(original_path):
        dist.append((node, i))
    for a, b in combinations(dist, 2):
        nodeA, timeA = a
        nodeB, timeB = b
        d = manhattan(nodeA, nodeB)
        if d <= time_allowed and d <= timeB-timeA-min_save:
            cheats += 1
    return cheats

print("\n------------------------------\nComputing first part")
count = get_cheats(2, 100)
print(f"Answer : {count}\n------------------------------\n")

possible_count_cache = {}
def count_possible(pattern, elems):
    if pattern in possible_count_cache:
        return possible_count_cache[pattern]

    if len(pattern) == 0:
        return True
    count = 0
    for elem in elems:
        if pattern.startswith(elem):
            res = count_possible(pattern[len(elem):], elems)
            possible_count_cache[pattern] = res
            count += res
    
    possible_count_cache[pattern] = count
    return count

print("\n------------------------------\nComputing second part")
count = get_cheats(20, 100)
print(f"Answer : {count}\n------------------------------")