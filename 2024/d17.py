from collections import deque as dq

top, bottom = open('d17.txt').read().split('\n\n')
a, b, c = (int(l.split()[-1]) for l in top.splitlines())
prog = [int(x) for x in bottom[8:].split(',')]

# Part 1
def run(a, b, c, prog):
    output, i = [], 0
    while i < len(prog):
        combo = {0:0, 1:1, 2:2, 3:3, 4:a, 5:b, 6:c}
        opcode, op = prog[i], prog[i + 1]
        match opcode:
            case 0: a = a // 2**combo[op]
            case 1: b = b ^ op
            case 2: b = combo[op] % 8
            case 3: i = op - 2 if a else i
            case 4: b = b ^ c
            case 5: output.append(combo[op] % 8)
            case 6: b = a // 2**combo[op]
            case 7: c = a // 2**combo[op]
        i += 2
    return output

print(','.join([str(x) for x in run(a, b, c, prog)]))

# Part 2 - Input specific reverse engineering
# Manual analysis of the 'run' function above with the
# program input reduces the function to the following:
"""
def F1(a, b, c):
    output = []
    while a != 0:
        b = a % 8 ^ 3
        c = a // 2**b
        output.append(b ^ 5 ^ c % 8)
        a = a // 8
    return output

assert(F1(a, b, c) == run(a, b, c, prog))
"""
# C and B are only used to calculate the output, so we can
# ignore them and simplify the function even more:
"""
def F2(a):
    output = []
    while a != 0:
        output.append(a % 8 ^ 3 ^ 5 ^ (a // 2**(a % 8 ^ 3)) % 8)
        a = a // 8
    return output

assert(F2(a) == run(a, b, c, prog))
"""

# From the above function we can see that the output is
# calculated by a series of XOR and modulo operations resulting
# in a 3 bit number (0-7).
# Then the input is divided by 8, which is equivalent 
# to right shifting the input by 3 bits.

# This means that the output is calculated in reverse order and
# the input is right shifted by 3 bits for each iteration. We can
# use this information to find the input that results the given output:

stack = dq((0,))
while stack:
    x = stack.popleft()
    for a in (x*8 + i for i in range(8)):
        res = run(a, 0, 0, prog)
        if res == prog:
            print(a)
            break
        elif res == prog[-len(res):]:
            stack.append(a)
    else: continue
    break

# Note: alternatively we can also change the modulo 8
# operation to a bitwise AND with 7, and change the division
# by 2**x to right shifts by x bits and reduce the function
# even further:
"""
def F3(a):
    output = []
    while a != 0:
        output.append(a & 7 ^ 3 ^ 5 ^ a >> (a & 7 ^ 3) & 7)
        a >>= 3
    return output

assert(F3(a) == run(a, b, c, prog))
"""
# Since most bitwise operations are not reversible, we can't
# directly reverse the function to find the input and we have
# to use the iterative method above to find the solution.