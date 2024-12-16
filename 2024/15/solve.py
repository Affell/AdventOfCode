print("Starting Day 15 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")


def get_move(char):
    match char:
      case '^':
        return (-1, 0)
      case 'v':
        return (1, 0)
      case '<':
        return (0, -1)
      case '>':
        return (0, 1)
    
tab = []
moves = []
start = (0, 0)
i = 0
while data[i] != '':
    tmp = []
    for j in range(len(data[i])):
        tmp.append(data[i][j])
        if data[i][j] == '@':
            start = (i, j)
    tab.append(tmp)
    i+=1
for j in range(i, len(data)):
    for k in range(len(data[j])):
        moves.append(get_move(data[j][k]))
    

def in_bounds(t, x, y):
    return 0 <= x < len(t) and 0 <= y < len(t[0])

def move(t, pos, dir):
    x, y = pos
    while in_bounds(t, *pos) and t[pos[0]][pos[1]] != '#':
        if t[pos[0]][pos[1]] == '.':
            while pos != (x, y):
                t[pos[0]][pos[1]] = t[pos[0] - dir[0]][pos[1] - dir[1]]
                pos = (pos[0] - dir[0], pos[1] - dir[1])
            t[x][y] = '.'
            return (x + dir[0], y + dir[1])
        pos = (pos[0] + dir[0], pos[1] + dir[1])
    return (x, y)

def get_gps_sum(t):
    return sum([100 * i + j for i in range(len(t)) for j in range(len(t[i])) if t[i][j] == 'O'or t[i][j] == '['])


print("\n------------------------------\nComputing first part")
tab_copy = [[e for e in x] for x in tab]
for m in moves:
    start = move(tab_copy, start, m)
count = get_gps_sum(tab_copy)
print(f"Answer : {count}\n------------------------------\n")

def extend_map(t):
    new_tab = []
    start = (0, 0)
    for line in t:
        tmp = []
        for e in line:
            match e:
                case '#':
                    tmp.extend(['#', '#'])
                case 'O':
                    tmp.extend(['[', ']'])
                case '.':
                    tmp.extend(['.', '.'])
                case '@':
                    start = (len(new_tab), len(tmp))
                    tmp.extend(['@', '.'])
        new_tab.append(tmp)
    return new_tab, start

def move2(t, pos, dir):    
    q = [(pos[0], pos[1], pos[0], pos[1])]
    moving = []
    while q:
        x, y, sx, sy = q.pop(0)
        nx, ny = (x + dir[0], y + dir[1])
        if not in_bounds(t, x, y) or not in_bounds(t, nx, ny) or t[nx][ny] == '#':
            return pos
        
        if t[nx][ny] == '.':
            moving.append((nx, ny, sx, sy))
        else:
            if (nx, ny, nx, ny) in q:
                q.remove((nx, ny, nx, ny))
            q.append((nx, ny, sx, sy))
        
        if t[nx][ny] == ']':
            f = False
            for m in q:
                if m[0] == nx and m[1] == ny-1:
                    f = True
                    break
            if f:
                continue
            q.append((nx, ny-1, nx, ny-1))
        elif t[nx][ny] == '[':
            f = False
            for m in q:
                if m[0] == nx and m[1] == ny+1:
                    f = True
                    break
            if f:
                continue
            q.append((nx, ny+1, nx, ny+1))
            
    for m in moving:
        cur = (m[0], m[1])
        while cur != (m[2], m[3]):
            t[cur[0]][cur[1]] = t[cur[0] - dir[0]][cur[1] - dir[1]]
            cur = (cur[0] - dir[0], cur[1] - dir[1])
        t[m[2]][m[3]] = '.'
        
    return (pos[0]+dir[0], pos[1]+dir[1])

print("\n------------------------------\nComputing second part")
tab2, start2 = extend_map(tab)
for m in moves:
    if m[0] == 0:
      start2 = move(tab2, start2, m)
    else:
      start2 = move2(tab2, start2, m)
count = get_gps_sum(tab2)
print(f"Answer : {count}\n------------------------------")