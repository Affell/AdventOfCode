print("Starting Day 24 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

locks = []
keys = []
for j in range(0, len(data), 8):
    key_part = data[j] == '.....'
    heights = []
    for y in range(5):
        for x in range(7):
            if data[j+x][y] == ('#' if key_part else '.'):
                heights.append(6-x if key_part else x-1)
                break
    if key_part:
        keys.append(tuple(heights))
    else:
        locks.append(tuple(heights))
        
def overlap(a, b):
    for i in range(len(a)):
        if a[i] + b[i] > 5:
            return True
    return False
  
  
def fit(locks, keys):
    count = 0
    for l in locks:
        for i in range(len(keys)):
            if overlap(l, keys[i]):
                continue
            count += 1
    return count

print("\n------------------------------\nComputing answer")
count = fit(locks, keys)
print(f"Answer : {count}\n------------------------------\n")
