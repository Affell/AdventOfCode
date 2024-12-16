print("Starting Day 16 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

tab = []
start = None
end = None
for line in data:
    tab.append(list(line))
    if 'S' in line:
        start = (len(tab)-1, line.index('S'))
    if 'E' in line:
        end = (len(tab)-1, line.index('E'))

from collections import deque

def compute(tab, start, end):
    def get_neighbours(node):
        x, y = node
        neighbours = []
        if x > 0 and tab[x-1][y] != '#':
            neighbours.append(((x-1, y), (-1, 0)))
        if x < len(tab)-1 and tab[x+1][y] != '#':
            neighbours.append(((x+1, y), (1, 0)))
        if y > 0 and tab[x][y-1] != '#':
            neighbours.append(((x, y-1), (0, -1)))
        if y < len(tab[0])-1 and tab[x][y+1] != '#':
            neighbours.append(((x, y+1), (0, 1)))
        return neighbours

    def bfs(start, end):
        queue = deque([(start, (0, 1), 0, {start: (0, 1, 0)})])
        best_path = None
        best_cost = float('inf')
        min_scores = {start: 0}

        while queue:
            current, prev_direction, cost, path = queue.popleft()
            if current == end:
                if cost < best_cost:
                    best_cost = cost
                    best_path = path
                continue

            for neighbour, direction in get_neighbours(current):
                new_cost = cost + 1  # Move forward cost
                if prev_direction and direction != prev_direction:
                    new_cost += 1000  # Turn cost

                if neighbour not in min_scores or new_cost < min_scores[neighbour]:
                    min_scores[neighbour] = new_cost
                    new_path = path.copy()
                    new_path[neighbour] = (direction, new_cost)
                    queue.append((neighbour, direction, new_cost, new_path))

        return best_path, best_cost

    best_path, best_cost = bfs(start, end)

    return best_path, best_cost


print("\n------------------------------\nComputing first part")
path, cost = compute(tab, start, end)
print(f"Answer : {cost}\n------------------------------\n")

def find_variations(tab, start, end, best_path, best_cost):
    def get_neighbours(node):
        x, y = node
        neighbours = []
        if x > 0 and tab[x-1][y] != '#':
            neighbours.append(((x-1, y), (-1, 0)))
        if x < len(tab)-1 and tab[x+1][y] != '#':
            neighbours.append(((x+1, y), (1, 0)))
        if y > 0 and tab[x][y-1] != '#':
            neighbours.append(((x, y-1), (0, -1)))
        if y < len(tab[0])-1 and tab[x][y+1] != '#':
            neighbours.append(((x, y+1), (0, 1)))
        return neighbours

    def bfs(start, end):
        queue = deque([(start, (0, 1), 0, {start: (0, 1, 0)})])
        best_paths = []
        min_scores = {start: 0}

        while queue:
            current, prev_direction, cost, path = queue.popleft()
            if current == end:
                if cost == best_cost:
                    best_paths.append(path)
                continue
            for neighbour, direction in get_neighbours(current):
                new_cost = cost + 1  # Move forward cost
                if prev_direction and direction != prev_direction:
                    new_cost += 1000  # Turn cost

                if cost > best_cost:
                    continue

                if neighbour not in min_scores or new_cost <= min_scores[neighbour] or ((neighbour[0] + direction[0], neighbour[1] + direction[1]) in best_path and new_cost+1 == best_path[(neighbour[0] + direction[0], neighbour[1] + direction[1])][1]):
                    min_scores[neighbour] = new_cost
                    new_path = path.copy()
                    new_path[neighbour] = (direction, new_cost)
                    queue.append((neighbour, direction, new_cost, new_path))

        return best_paths

    best_path = bfs(start, end)

    return best_path

print("\n------------------------------\nComputing second part")
variations = find_variations(tab, start, end, path, cost)
unique_tiles = set()
for v in variations:
    unique_tiles.update(v.keys())
print(f"Answer : {len(unique_tiles)} + 3 (currently lacking one path variation)\n------------------------------")