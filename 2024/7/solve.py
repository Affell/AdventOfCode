print("Starting Day 7 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

calibrations = {}
for line in data:
    calibrations[int(line.split(":")[0])] = list(map(int, line.split(":")[1].strip().split(" ")))

def plus_operator(x, y):
    return x + y
  
def multiply_operator(x, y):
    return x * y

def is_possible(target, numbers, operators):
    if len(numbers) == 0:
        return target == 0
    if len(numbers) == 1:
        return numbers[0] == target
      
    for op in operators:
        res = op(numbers[0], numbers[1])
        tmp = [res] + numbers[2:]
        if is_possible(target, tmp, operators):
            return True
    return False

print("\n------------------------------\nComputing first part")
count = sum([k for k, v in calibrations.items() if is_possible(k, v, [plus_operator, multiply_operator])])
print(f"Answer : {count}\n------------------------------\n")


def concat_operator(x, y):
    return int(str(x) + str(y))

print("\n------------------------------\nComputing second part")
copunt = sum([k for k, v in calibrations.items() if is_possible(k, v, [plus_operator, multiply_operator, concat_operator])])
print(f"Answer : {count}\n------------------------------")