import re

# P1
inp = open('12.txt').read()
print(sum([int(s) for s in re.findall('-?\d+', inp)]))

# P2
inp = 'inp = ' + inp
exec(inp) # lucky that the input format matches Python's

def nsum(elem):
    res = 0
    if type(elem) == int: return elem
    elif type(elem) == str: return 0
    elif type(elem) == list:
        for e in elem: res += nsum(e)
    elif type(elem) == dict:
        if 'red' in elem.values(): return 0
        else:
            for e in elem.values(): res += nsum(e)
    return res

print(nsum(inp))