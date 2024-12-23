print("Starting Day 23 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

links = {}
for line in data:
    a, b = line.split('-')
    if b not in links:
        links[b] = []
    if a not in links:
        links[a] = []
    links[b].append(a)
    links[a].append(b)

def dfs(start, links, cycle_length=3):
    stack = [(start, [], 0)]
    cycles = []
    while stack:
        node, path, c = stack.pop()
        if node == start and c == cycle_length:
            cycles.append(sorted(path))
        elif node == start and c > 0:
            continue
        elif c == cycle_length:
            continue
        else:
            for n in links[node]:
                stack.append((n, path + [n], c+1))
    return cycles

print("\n------------------------------\nComputing first part")
three_groups = []
for node in links:
    if node[0] != 't':
        continue
    groups = dfs(node, links)
    for group in groups:
        if group not in three_groups:
            three_groups.append(group)
print(f"Answer : {len(three_groups)}\n------------------------------\n")

def bron_kerbosch(R, P, X, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for v in P.copy():
        bron_kerbosch(R.union([v]), P.intersection(links[v]), X.intersection(links[v]), cliques)
        P.remove(v)
        X.add(v)

def find_cliques(links):
    cliques = []
    bron_kerbosch(set(), set(links.keys()), set(), cliques)
    return cliques

print("\n------------------------------\nComputing second part")
cliques = find_cliques(links)
largest_clique = max(cliques, key=len)
password = ','.join([node for node in sorted(largest_clique)])
print(f"Answer : {password}\n------------------------------")