print("Starting Day 11 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

rocks = list(map(int, data[0].split(" ")))
cache = {}

def blink(rocks, nb_blinks):
    grouped = {}

    for r in rocks:
        if r not in grouped:
            grouped[r] = 0
        grouped[r] += 1

    for _ in range(nb_blinks):
        next = {}
        for n, count in grouped.items():
            if n == 0:
                if 1 not in next:
                    next[1] = count
                else:
                    next[1] += count
            elif len(str(n)) % 2 == 0:
                str_nb = str(n)
                left = int(str_nb[:len(str_nb)//2])
                right = int(str_nb[len(str_nb)//2:])
                if left not in next:
                    next[left] = count
                else:
                    next[left] += count
                if right not in next:
                    next[right] = count
                else:
                    next[right] += count
            else:
                if n*2024 not in next:
                    next[n*2024] = count
                else:
                    next[n*2024] += count
        grouped = {k: v for k, v in next.items()}

    return grouped

print("\n------------------------------\nComputing first part")
r = blink(rocks, 25)
count = sum(r.values())
print(f"Answer : {count}\n------------------------------\n")

print("\n------------------------------\nComputing second part")
r = blink(rocks, 75)
count = sum(r.values())
print(f"Answer : {count}\n------------------------------")