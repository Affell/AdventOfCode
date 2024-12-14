print("Starting Day 13 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

size = (101,103)
robots = []
for line in data:
    pos = list(map(int, line.split(' ')[0][2:].split(',')))
    velocity = list(map(int, line.split(' ')[1][2:].split(',')))
    robots.append([pos, velocity])
    

def simulate(robots, seconds):
    for i in range(len(robots)):
        robots[i] =(((robots[i][0][0] + robots[i][1][0] * seconds)%size[0], (robots[i][0][1] + robots[i][1][1] * seconds)%size[1]), robots[i][1])
    return robots

def get_quadrant_occupation(robots):
    quadrants = [0 for _ in range(4)]
    middle = (size[0]//2, size[1]//2)
    for robot in robots:
      if robot[0][0] == middle[0] or robot[0][1] == middle[1]:
        continue
      x = int(robot[0][0] > middle[0])
      y = int(robot[0][1] > middle[1])
      quadrants[x + 2*y] += 1
    return quadrants


print("\n------------------------------\nComputing first part")
new_robots = simulate(robots[:], 100)
occ = get_quadrant_occupation(new_robots)
count = 1
for n in occ:
  count *= n
print(f"Answer : {count}\n------------------------------\n")

def get_christmas_tree():
    new_robots = robots[:]
    for i in range(1, 10000):
        new_robots = simulate(new_robots, 1)
        positions =  [robot[0] for robot in new_robots]
        groups = {}
        for p in positions:
            x, y = p[0] // 5, p[1] // 5
            if (x,y) not in groups:
                groups[(x,y)] = [p]
            else:
                groups[(x,y)].append(p)
        
        for group in groups:
            if len(groups[group]) > 15:
                return i

print("\n------------------------------\nComputing second part")
index = get_christmas_tree()
print(f"Answer : {index}\n------------------------------")