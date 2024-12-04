print("Starting Day 4 solver")
try:
    with open("input.txt", 'r') as f:
        data = f.read()
except:
    print("Your input file must be named input.txt and placed in this directory")

translate = {
    'X': 0,
    'M': 1,
    'A': 2,
    'S': 3,
}

# Compute the input as a 2D int matrix
tab = []
for line in data.splitlines():
    tab.append([translate[x] for x in line])


def get_words(x, y, dirx=0, diry=0, target=1):
    """
    Returns the list of the found words starting at x,y.
    """
    # Check matrix boundaries
    if x < 0 or x >= len(tab) or y < 0 or y >= len(tab[0]):
        return False
    # target == 4 when we have completed the word
    if target == 4 and tab[x][y] == 3:
        return True
    # If our position match the previous targetted int, we continue to search 
    elif tab[x][y] == target-1:
        # No searching direction has been set, we launch a BFS
        if dirx == 0 and diry == 0:
            words = []
            if get_words(x-1, y, -1, 0, target+1):
                words.append((x-1, y, -1, 0))
            if get_words(x+1, y, 1, 0, target+1):
                words.append((x+1, y, 1, 0))
            if get_words(x, y-1, 0, -1, target+1):
                words.append((x, y-1, 0, -1))
            if get_words(x, y+1, 0, 1, target+1):
                words.append((x, y+1, 0, 1))
            if get_words(x-1, y-1, -1, -1, target+1):
                words.append((x-1, y-1, -1, -1))
            if get_words(x-1, y+1, -1, 1, target+1):
                words.append((x-1, y+1, -1, 1))
            if get_words(x+1, y-1, 1, -1, target+1):
                words.append((x+1, y-1, 1, -1))
            if get_words(x+1, y+1, 1, 1, target+1):
                words.append((x+1, y+1, 1, 1))
            return words
        # A direction is set, we search only in this direction
        else:
            return get_words(x+dirx, y+diry, dirx, diry, target+1)
    return False

print("\n------------------------------\nComputing first part")
count = 0
# BFS on every X to find all XMAS words
for i in range(len(tab)):
    for j in range(len(tab[0])):
        if tab[i][j] == 0:
            count += len(get_words(i, j))
print(f"Answer : {count}\n------------------------------\n")

print("\n------------------------------\nComputing second part")
# Pending A in MAS words without two crossing MAS are stored here as key=(xA,yA) and value=[(xDir,yDir)]
words = {}
crossed_words = []
# BFS on every M to find all MAS
for i in range(len(tab)):
    for j in range(len(tab[0])):
        if tab[i][j] == 1:
            found = get_words(i, j, target=2)
            # Every words direction vector found is computed with other A overlapping words direcyion vectors as a scalar product. 
            for w in found:
                x, y, dirx, diry = w
                if dirx == 0 or diry == 0: # Can't be a cross
                    continue
                if (x, y) not in words: # Put this position in pending state
                    words[(x, y)] = [(dirx, diry)]
                else:
                    for dx, dy in words[(x, y)]:
                        if dx*dirx + dy*diry == 0: # Scalar product == 0 means it's a cross
                            crossed_words.append((x, y, dirx, diry, dx, dy))
                            words[(x, y)] = [e for e in words[(x, y)] if e != (dx, dy)] # Remove from pending state
                            break

print(f"Answer : {len(crossed_words)}\n------------------------------")