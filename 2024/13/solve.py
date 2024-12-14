print("Starting Day 13 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

c = [3, 1]
machines = []
for i in range(0, len(data), 4):
    machine = {}
    machine['A'] = [int(e[2:]) for e in data[i].split(': ')[1].split(', ')]
    machine['B'] = [int(e[2:]) for e in data[i+1].split(': ')[1].split(', ')]
    machine['prize'] = [int(e[2:]) for e in data[i+2].split(': ')[1].split(', ')]
    machines.append(machine)

def get_min_tokens(machine, part2=False):
    A = machine['A']
    B = machine['B']
    P = machine['prize']

    if part2:
        P = [10000000000000 + p for p in P]

    a = (P[0]*B[1] - P[1]*B[0]) / (A[0]*B[1] - A[1]*B[0])
    b = (P[1]*A[0] - P[0]*A[1]) / (A[0]*B[1] - A[1]*B[0])
    if a == int(a) and b == int(b):
        return (int(a), int(b)), int(a)*c[0] + int(b)*c[1]
    return ([0, 0], 0)


print("\n------------------------------\nComputing first part")
count = 0
for machine in machines:
    x, fun = get_min_tokens(machine)
    count += int(fun)
print(f"Answer : {count}\n------------------------------\n")

print("\n------------------------------\nComputing second part")
count = 0
for machine in machines:
    x, fun = get_min_tokens(machine, part2=True)
    count += int(fun)
print(f"Answer : {count}\n------------------------------")