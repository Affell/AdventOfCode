print("Starting Day 1 solver")
try:
    with open("input.txt", 'r') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

right, left = [], []
for l in data:
    le, ri = l.split('   ')
    left.append(int(le.strip()))
    right.append(int(ri.strip()))
    
right = sorted(right)
left = sorted(left)


print("\n------------------------------\nComputing first part")
count = 0
for i in range(len(left)):
    count += abs(left[i] - right[i])
print(f"Answer : {count}\n------------------------------\n")

print("\n------------------------------\nComputing second part")
count2 = 0
for n in left:
    count2 += n * right.count(n)
print(f"Answer : {count2}\n------------------------------")