print("Starting Day 6 solver")
try:
    with open('input.txt') as f:
        lines = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

# Computing starting position and direction
tab = []
init_pos = None
for i in range(len(lines)):
    line = lines[i]
    tmp = []
    for j in range(len(line)):
        c = line[j]
        tmp.append(c)
        match c:
            case '^':
                init_pos = (i, j, -1, 0)
            case 'v':
                init_direction = (i, j, 1, 0)
            case '<':
                init_direction = (i, j, 0, -1)
            case '>':
                init_direction = (i, j, 0, 1)
    tab.append(tmp)
if init_pos is None:
    raise ValueError('No initial direction found')

def turnRight(dx, dy):
    """
    Apply a 90° right turn to the direction vector (dx, dy)
    """
    match (dx, dy):
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)
        case (-1, 0):
            return (0, 1)
        
def computeVisits(x, y, dx, dy):
    """
    Register all visited positions in the grid by simply moving forward and turning right obstacles are encountered
    """
    visits = set()
    visits.add((x, y))
    while True:
        x += dx
        y += dy
        if x < 0 or x >= len(tab) or y < 0 or y >= len(tab[0]): # we moved out of the grid
            break
        if tab[x][y] == '#': # we moved on a obstacle, step back and turn right
            x, y = x - dx, y - dy
            dx, dy = turnRight(dx, dy)
            continue
        visits.add((x, y))
    return visits

print("\n------------------------------\nComputing first part")
positions = computeVisits(*init_pos)
print(f"Answer : {len(positions)}\n------------------------------\n")

def count_loop_possibilities(startX, startY, startDx, startDy, visited_pos):
    """
    A loop is a when the robot make the same turn twice
    """
    loops = []
    for pos in visited_pos: # for each visited position, we will simulate an obstacle and check if the robot loops
        tab[pos[0]][pos[1]] = '#'
        turns = [] # record all turns made by the robot
        x, y, dx, dy = startX, startY, startDx, startDy
        while True:
            x += dx
            y += dy
            if x < 0 or x >= len(tab) or y < 0 or y >= len(tab[0]): # we moved out of the grid, no loop
                break
            if tab[x][y] == '#':
                x, y = x - dx, y - dy
                if (x, y, dx, dy) in turns: # we already made this turn, we are looping
                    loops.append(pos) # register the position where the loop is detected
                    break
                turns.append((x, y, dx, dy))
                dx, dy = turnRight(dx, dy)
                continue
        tab[pos[0]][pos[1]] = '.'
    return loops

print("\n------------------------------\nComputing second part")
loops = count_loop_possibilities(*init_pos, positions)
print(f"Answer : {len(loops)}\n------------------------------")