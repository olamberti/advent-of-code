import math

# Input parsing
reactions = {}
for line in open('14.txt').readlines():
    ingr, prod = line.strip().split(' => ')
    ingr, prod = ingr.split(', '), prod.split(' ')
    reactions[prod[1]] = [int(prod[0])]
    for elem in ingr:
        elem = elem.split(' ')
        reactions[prod[1]].append([elem[1], int(elem[0])])

# Create function to make new elements
def create(elem):
    new, req = reactions[elem][0], []
    for ingr in reactions[elem][1:]:
        req.append(ingr)
    return new, req

# Calculate ore required for given ammount of fuel
def make_fuel(fuel):
    have, need = {}, {}
    need['FUEL'] = fuel
    ore = 0

    while need:
        product = list(need)[0]
        vol = need[product]

        if product == 'ORE':
            ore += vol
            del need[product]
            continue

        if product in have:
            vol_have = have[product]
            if vol_have > vol:
                have[product] -= vol
                del need[product]
                continue
            del have[product]
            vol -= vol_have
            
        if vol > 0:
            new, ings = create(product)
            times = math.ceil(vol / new)
            vol -= new * times
            for e, n in ings:
                if e in need: need[e] += n * times
                else: need[e] = n * times

        if vol < 0:
            if product in have: have[product] += -vol
            else: have[product] = -vol

        del need[product]
    return ore

# P1
ore = make_fuel(1)
print(ore)

# P2
cargo = 1_000_000_000_000
min_fuel = cargo // ore
max_fuel = 2 * min_fuel

while max_fuel - min_fuel > 1:
    new_fuel = (min_fuel + max_fuel) // 2
    ore = make_fuel(new_fuel)
    if ore > cargo:  max_fuel = new_fuel
    else: min_fuel = new_fuel
print(min_fuel)