print("Starting Day 5 solver")
try:
    with open('input.txt') as f:
        lines = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

rules = {}
updates = []
rule = True
for line in lines:
    if line == "":
        rule = False
        continue
    if rule:
        a, b = line.split("|")
        a, b = int(a), int(b)
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a].append(b)
    else:
        updates.append(list(map(int, line.split(","))))


def is_ordered(update: list[int]):
    """
    Check if an update is ordered according to the rules
    """
    for i in range(len(update)): # for each element in the update
        n = update[i]
        if n in rules:
            # n has at least one element that should be after it
            for o in rules[n]: # loop through the elements that should be after n
                try:
                    j = update.index(o) # check the index of the first element
                    if j < i: # if the first element is before n, the update is not ordered
                        return False
                except ValueError:
                    continue
    return True

print("\n------------------------------\nComputing first part")
count = 0
# Count the middle element of each update that is ordered
for update in updates:
    if is_ordered(update):
        count += update[len(update)//2] # middle element
print(f"Answer : {count}\n------------------------------\n")

def fix_order(update: list[int], iteration=0):
    """
    Fix the order of an update that is not ordered
    This is recursive and will stop after 100 iterations for safety
    """
    if iteration > 100: # my code is perfect, this should never happen :)
        print(f"too many iterations: {update}")
        return update
    for i in range(len(update)): # for each element in the update
        n = update[i]
        if n in rules:
            # n has at least one element that should be after it
            for o in rules[n]: # loop through the elements that should be after n
                try:
                    j = update.index(o)
                    if j < i: # if the first element is before n, swap them
                        update[i], update[j] = update[j], update[i]
                except ValueError:
                    continue
    return update if is_ordered(update) else fix_order(update, iteration+1) # if the update is ordered, return it, else try again (i'm lazy)

print("\n------------------------------\nComputing second part")
# Apply the fix_order function to each unordered update and count the middle element
count = 0
for update in updates:
    if not is_ordered(update): # if the update is not ordered
        fixed = fix_order(update.copy())
        count += fixed[len(fixed)//2] # middle element

print(f"Answer : {count}\n------------------------------")