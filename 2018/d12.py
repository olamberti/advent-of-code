input = open('d12.txt').read().splitlines()

plants, rules, first = input[0].split(': ')[1], {}, 0
for line in input[2:]:
    patt, res = line.split(' => ')
    rules[patt] = res

def next_gen(plants, first):
    plants = '....' + plants + '....'
    new_plants = ''
    for i in range(len(plants) - 5):
        new_plants = new_plants + rules[plants[i: i + 5]]
    iS, iE = new_plants.find('#'), new_plants.rfind('#')
    return new_plants[iS: iE + 1], first + iS - 2

def calc_sum(plants, first):
    res  = 0
    for i, ch in enumerate(plants):
        if ch == '#': res += i + first
    return res

num, N = calc_sum(plants, first), 50_000_000_000
stable, diff, counter = False, None, 0
for r in range(1, N + 1):
    plants, first = next_gen(plants, first)
    new_num = calc_sum(plants, first)
    counter = counter + 1 if new_num - num == diff else 0
    num, diff = new_num, new_num - num
    # Part 1
    if r == 20: print(num)
    # Part 2
    if counter == 10:
        rem = N - r
        print(num + rem * diff)
        break