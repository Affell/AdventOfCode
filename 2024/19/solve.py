print("Starting Day 19 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

available = [e for e in data[0].split(', ')]
available.sort(key=lambda x: len(x), reverse=True)
patterns = [e for e in data[2:]]

possible_cache = {}
def is_possible(pattern, elems):
    if pattern in possible_cache:
        return possible_cache[pattern]

    if len(pattern) == 0:
        return True

    for elem in elems:
        if pattern.startswith(elem) and is_possible(pattern[len(elem):], elems):
            possible_cache[pattern] = True
            return True
    
    possible_cache[pattern] = False
    return False


print("\n------------------------------\nComputing first part")
possibles = [p for p in patterns if is_possible(p, available)]
count = len(possibles)
print(f"Answer : {count}\n------------------------------\n")

possible_count_cache = {}
def count_possible(pattern, elems):
    if pattern in possible_count_cache:
        return possible_count_cache[pattern]

    if len(pattern) == 0:
        return True
    count = 0
    for elem in elems:
        if pattern.startswith(elem):
            res = count_possible(pattern[len(elem):], elems)
            possible_count_cache[pattern] = res
            count += res
    
    possible_count_cache[pattern] = count
    return count

print("\n------------------------------\nComputing second part")
count_possibles = [count_possible(p, available) for p in patterns]
count = sum(count_possibles)
print(f"Answer : {count}\n------------------------------")