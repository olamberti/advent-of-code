import re

# Read input
chem, rchem = {}, {}
for line in open('19.txt').readlines():
    if ' => ' in line:
        a, b = line.strip().split(' => ')
        if a not in chem: chem[a] = []
        chem[a].append(b)
        rchem[b] = a
    elif line:
        medicine = line.strip()

# Functions
def find_index(pattern, string):
    return [(m.start(0), m.end(0)) for m in re.finditer(pattern, string)]

def replacements(mol, reactions):
    results = set()
    for start, products in reactions.items():
        for elem in products:
            for i1, i2 in find_index(start, mol):
                new_mol = mol[:i1] + elem + mol[i2:]
                if new_mol not in results: results.add(new_mol)
    return results

# P1
print(len(replacements(medicine, chem)))

# P2
chemlist, steps = sorted(list(rchem.keys()), key = len, reverse = True), 0
while medicine != 'e':
    for chem in chemlist:
        while chem in medicine:
            i1, i2 = find_index(chem, medicine)[-1]
            medicine = medicine[:i1] + rchem[chem] + medicine[i2:]
            steps += 1
print(steps)