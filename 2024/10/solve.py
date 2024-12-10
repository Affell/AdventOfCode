print("Starting Day 10 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

tab = []
for line in data:
    tab.append(list(map(int, [e for e in line])))

def get_trail_head_score(x, y, visited=None):
    if visited is None:
        visited = []
    visited.append((x, y))
    if tab[x][y] == 9:
        return 1
    else:
        count = 0
        if x > 0  and tab[x-1][y] == tab[x][y]+1 and (x-1, y) not in visited:
            count += get_trail_head_score(x-1, y, visited)
        if x < len(tab)-1 and tab[x+1][y] == tab[x][y]+1 and (x+1, y) not in visited:
            count += get_trail_head_score(x+1, y, visited)
        if y > 0 and tab[x][y-1] == tab[x][y]+1 and (x, y-1) not in visited:
            count += get_trail_head_score(x, y-1, visited)
        if y < len(tab[0])-1 and tab[x][y+1] == tab[x][y]+1 and (x, y+1) not in visited:
           count += get_trail_head_score(x, y+1, visited)
        return count

print("\n------------------------------\nComputing first part")
count = 0
for x in range(len(tab)):
    for y in range(len(tab[0])):
        if tab[x][y] == 0:
            count += get_trail_head_score(x, y)
print(f"Answer : {count}\n------------------------------\n")

def get_trail_head_rating(x, y, visited=None):
    if visited is None:
        visited = []
    if tab[x][y] == 9:
        return 1
    else:
        count = 0
        if x > 0  and tab[x-1][y] == tab[x][y]+1 and (x-1, y) not in visited:
            count += get_trail_head_rating(x-1, y, visited + [(x, y)])
        if x < len(tab)-1 and tab[x+1][y] == tab[x][y]+1 and (x+1, y) not in visited:
            count += get_trail_head_rating(x+1, y, visited + [(x, y)])
        if y > 0 and tab[x][y-1] == tab[x][y]+1 and (x, y-1) not in visited:
            count += get_trail_head_rating(x, y-1, visited + [(x, y)])
        if y < len(tab[0])-1 and tab[x][y+1] == tab[x][y]+1 and (x, y+1) not in visited:
           count += get_trail_head_rating(x, y+1, visited + [(x, y)])
        return count

print("\n------------------------------\nComputing second part")
count = 0
for x in range(len(tab)):
    for y in range(len(tab[0])):
        if tab[x][y] == 0:
            count += get_trail_head_rating(x, y)
print(f"Answer : {count}\n------------------------------")