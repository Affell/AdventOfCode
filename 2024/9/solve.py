print("Starting Day 9 solver")
try:
    with open('input.txt') as f:
        line = f.read().splitlines()[0]
except:
    print("Your input file must be named input.txt and placed in this directory")

def translateDiskMap(line):
    fs = []
    index = 0
    for i in range(len(line)):
        if i%2==0:
            fs += [index] * int(line[i])
            index += 1
        else:
            fs += ['.'] * int(line[i])
    return fs

def defrag(fs):
    defragged = fs[:]
    firstFree = fs.index('.')
    for i in range(len(fs)):
        if firstFree > len(fs)-i-1:
            break
        e = fs[len(fs)-i-1]
        if e != '.':
            defragged[firstFree] = e
            defragged[len(fs)-i-1] = '.'
            found = False
            for j in range(firstFree+1, len(fs)):
                if defragged[j] == '.':
                    firstFree = j
                    found = True
                    break
            if not found:
                break
    return defragged

def checksum(fs):
    sum = 0
    for i in range(1, len(fs)):
        if fs[i] != '.':
            sum += fs[i] * i
    return sum

print("\n------------------------------\nComputing first part")
fs = translateDiskMap(line)
defragged = defrag(fs)
result = checksum(defragged)
print(f"Answer : {result}\n------------------------------\n")

def defrag_block(fs):
    defragged = fs[:]
    def get_next_free(start):
        first = -1
        count = 0
        for i in range(start, len(defragged)):
            if defragged[i] == '.':
                if first == -1:
                    first = i
                count += 1
            elif first != -1:
                break
        return (first, count)
    firstFree = get_next_free(0)
    size = 1
    for i in range(len(fs)):
        if firstFree[0] > len(fs)-i-1 or firstFree[0] == -1:
            break
        e = fs[len(fs)-i-1]
        if i<len(fs)-1 and fs[len(fs)-i-2] == e:
            size += 1
            continue
        if e != '.':
            tmpFree = firstFree
            while tmpFree[1] < size and tmpFree[0] != -1:
                tmpFree = get_next_free(tmpFree[0]+1)
                if tmpFree[0] > len(fs)-i-1:
                    tmpFree = (-1, 0)
            if tmpFree[0] == -1:
                size = 1
                continue
            for j in range(size):
                defragged[tmpFree[0]+j] = e
                defragged[len(fs)-i-1+j] = '.'
            size = 1
            if tmpFree[0] == firstFree[0]:
                firstFree = get_next_free(tmpFree[0]+size)
        else:
            size = 1
    return defragged

print("\n------------------------------\nComputing second part")
defragged = defrag_block(fs)
result = checksum(defragged)
print(f"Answer : {result}\n------------------------------")