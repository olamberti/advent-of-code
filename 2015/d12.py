import re

# P1
inp = open('d12.txt').read()
print(sum([int(s) for s in re.findall('-?\d+', inp)]))

# P2
inp = 'inp = ' + inp
exec(inp) # lucky that the input format matches Python's

def nsum(elem):
    if type(elem) == int: return elem
    elif type(elem) == str: return 0
    elif type(elem) == list: return sum([nsum(e) for e in elem])
    elif type(elem) == dict:
        if 'red' in elem.values(): return 0
        else: return sum([nsum(e) for e in elem.values()])
    return None

print(nsum(inp))