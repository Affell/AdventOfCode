print("Starting Day 17 solver")
try:
    with open('input.txt') as f:
        data = f.read().splitlines()
except:
    print("Your input file must be named input.txt and placed in this directory")

reg = [0, 0, 0]
for i in range(3):
    reg[i] = int(data[i].split(": ")[-1])

prog = [int(x) for x in data[-1].split(": ")[-1].split(",")]

def get_combo_value(reg, operand):
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6 :
        return reg[operand - 4]
    else:
        return None
    
def adv(pc, reg, operand):
    val = get_combo_value(reg, operand)
    if val is None:
        return -1
    
    reg[0] = reg[0] >> val
    return pc+2

def bxl(pc, reg, operand):
    reg[1] = reg[1] ^ operand
    return pc+2

def bst(pc, reg, operand):
    val = get_combo_value(reg, operand)
    if val is None:
        return -1
    
    reg[1] = val % 8
    return pc+2

def jnz(pc, reg, operand):
    if reg[0] == 0:
        return pc+2

    return operand

def bxc(pc, reg, _):
    reg[1] = reg[1] ^ reg[2]
    return pc+2

def out(pc, reg, operand):
    val = get_combo_value(reg, operand)
    if val is None:
        return -1
    
    return pc+2, val%8

def bdv(pc, reg, operand):
    val = get_combo_value(reg, operand)
    if val is None:
        return -1
    
    reg[1] = reg[0] >> val
    return pc+2

def cdv(pc, reg, operand):
    val = get_combo_value(reg, operand)
    if val is None:
        return -1
    
    reg[2] = reg[0] >> val
    return pc+2

operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def execute_program(program, init_reg):
    reg = [e for e in init_reg]
    pc = 0
    stdout = []
    while pc < len(program)-1:

        op = program[pc]
        operand = program[pc+1]
        res = operations[op](pc, reg, operand)
        if type(res) != int and len(res) == 2:
            pc, val = res
            stdout.append(val)
        else:
            pc = res

        if pc < 0 or pc % 2 == 1:
            print(f"Exec error: invalid pointer pc={pc} following op={op} operand={operand} res={res}")
            break

    return stdout

print("\n------------------------------\nComputing first part")
output = execute_program(prog, reg)
res = ','.join([str(x) for x in output])
print(f"Answer : {res}\n------------------------------\n")

def find_reg_value():
    As = [0]
    for i in range(len(prog)//2):
        valid = []
        for A in As:
            for j in range(1<<6):
                test = A<<6 | j
                new_reg = [test] + reg[1:]
                output = execute_program(prog, new_reg)
                if output == prog[len(prog)-2*(i+1):]:
                    valid.append(test)
        if len(valid) == 0:
            return None
        As = valid
    return As[0] if len(As) >= 1 else None

print("\n------------------------------\nComputing second part")
reg_value = find_reg_value()
print(f"Answer : {reg_value}\n------------------------------")