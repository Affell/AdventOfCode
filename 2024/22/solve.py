print("Starting Day 22 solver")

try:
  with open('input.txt') as f:
    data = f.read().splitlines()
except:
  print("Your input file must be named input.txt and placed in this directory")
  exit()

import sys
sys.setrecursionlimit(10**6)

numbers = [int(x) for x in data]
def evolve(n, cycles):
    if cycles == 0:
        return n
    new = ((n<<6) ^ n) & (1<<24)-1
    new = ((new>>5) ^ new) & (1<<24)-1
    new = ((new<<11) ^ new) & (1<<24)-1
    return evolve(new, cycles-1)
  
def low_evolve(n, cycles, prices):
    if cycles == 0:
        return
    new = ((n<<6) ^ n) & (1<<24)-1
    new = ((new>>5) ^ new) & (1<<24)-1
    new = ((new<<11) ^ new) & (1<<24)-1
    prices.append(new%10)
    low_evolve(new, cycles-1, prices)

print("\n------------------------------\nComputing first part")
ans1 = sum([evolve(n, 2000) for n in numbers])
print(f"Answer : {ans1}\n------------------------------\n")

print("\n------------------------------\nComputing second part")
prices = []
for n in numbers:
    p = [n%10]
    low_evolve(n, 2000, p)
    prices.append(p)
    
sequences = {}
for p in prices:
    change = [0] + [p[i] - p[i-1] for i in range(1, 4)]
    cache = []
    for i in range(len(p)):
        change.pop(0)
        change.append(p[i]-p[i-1])
        cur = tuple(change)
        if cur in cache:
            continue
        cache.append(cur)
        if cur in sequences:
            sequences[cur] += p[i]
        else:
            sequences[cur] = p[i]
        
ans2 = max(sequences.values())
print(f"Answer : {ans2}\n------------------------------\n")