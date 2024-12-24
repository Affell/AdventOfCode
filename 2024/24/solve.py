print("Starting Day 24 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def xor_gate(a, b):
    return a ^ b

def get_gate(gate):
    if gate == 'AND':
        return and_gate
    elif gate == 'OR':
        return or_gate
    elif gate == 'XOR':
        return xor_gate
    
vals = {}
circuits = []
result_of = {}
for i in range(len(data)):
    if data[i] == '':
        break
    vals[data[i][:3]] = int(data[i][5:])

for j in range(i+1, len(data)):
    if data[j] == '':
        continue
    arg1 = data[j].split(' ')[0]
    gate = get_gate(data[j].split(' ')[1])
    arg2 = data[j].split(' ')[2]
    output = data[j].split(' ')[4]
    result_of[output] = len(circuits)
    arg1, arg2 = tuple(sorted([arg1, arg2]))
    if arg1 not in vals:
        vals[arg1] = None
    if arg2 not in vals:
        vals[arg2] = None
    if output not in vals:
        vals[output] = None
    circuits.append((gate, arg1, arg2, output))

def apply_gates(circuits, vals):
    queue = circuits.copy()
    while queue:
        gate, arg1, arg2, output = queue.pop(0)
        if vals[arg1] is not None and vals[arg2] is not None:
            vals[output] = gate(vals[arg1], vals[arg2])
        else:
            queue.append((gate, arg1, arg2, output))

print("\n------------------------------\nComputing first part")
test_vals = vals.copy()
apply_gates(circuits, test_vals)
res = int(''.join([str(test_vals[k]) for k in sorted([key for key in test_vals if key.startswith('z')], reverse=True)]), 2)
print(f"Answer : {res}\n------------------------------\n")

def swap_circuits(circuits, result_of, a, b):
    aIndex = result_of[a]
    bIndex = result_of[b]
    newA = tuple(list(circuits[aIndex][:-1]) + [b])
    newB = tuple(list(circuits[bIndex][:-1]) + [a])
    circuits[aIndex] = newA
    circuits[bIndex] = newB

from graphviz import Digraph

def visualize_circuit(circuits):
    dot = Digraph()
    
    for gate, arg1, arg2, output in circuits:
        dot.node(arg1, arg1, shape='circle')
        dot.node(arg2, arg2, shape='circle')
        dot.node(output, output, shape='circle')
        gate_label = gate.__name__[:-5]
        gate_node = f"{arg1}_{gate_label}_{arg2}"
        dot.node(gate_node, gate_label, shape='box')
        dot.edge(arg1, gate_node)
        dot.edge(arg2, gate_node)
        dot.edge(gate_node, output)
    
    return dot

print("\n------------------------------\nComputing second part")
swapped_circuits = circuits.copy()

#######################
# ADD YOUR SWAPS HERE
# to_swap = [('dbp', 'fdv'), ('z15', 'ckj'), ('z23', 'kdf'), ('z39', 'rpp')]
to_swap = []
#######################

for a, b in to_swap:
    swap_circuits(swapped_circuits, result_of, a, b)

in_len = max([int(k[1:]) for k in vals if k.startswith('x')])+1

test = True
# Test all carries
for i in range(in_len):
    test_vals = {k: 0 if v is not None else None for k, v in vals.items()}
    test_vals[f'x{str(i).zfill(2)}'] = 1
    test_vals[f'y{str(i).zfill(2)}'] = 1
    apply_gates(swapped_circuits, test_vals)
    if test_vals[f'z{str(i).zfill(2)}'] == 1 or test_vals[f'z{str(i+1).zfill(2)}'] == 0:
        print(f"Carry test failed at z{str(i+1).zfill(2)}, a swap is needed")
        test = False
        break

if test:
    import random
    # Test 500 additions
    for i in range(500):
        x = random.randint(0, 1<<in_len-1)
        y = random.randint(0, 1<<in_len-1)
        test_vals = vals.copy()
        for j in range(in_len):
            test_vals[f'x{str(j).zfill(2)}'] = (x >> j) & 1
            test_vals[f'y{str(j).zfill(2)}'] = (y >> j) & 1
        apply_gates(swapped_circuits, test_vals)
        res = int(''.join([str(test_vals[k]) for k in sorted([key for key in test_vals if key.startswith('z')], reverse=True)]), 2)
        if res != x + y:
            print(f'Failed at {x} + {y} = {res} ({i})')
            test = False
            break

if test:
    swapped_values = []
    for a, b in to_swap:
        swapped_values.append(a)
        swapped_values.append(b)
    swapped_values.sort()
    print(f"All tests passed, answer : {','.join(swapped_values)}\n------------------------------")
else:
    print('Tests failed, opening graph visualizer to find the correct swap and add it to the to_swap list')
    dot = visualize_circuit(circuits)
    dot.render('circuit', format='png', view=True)
    exit()

