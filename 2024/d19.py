from functools import cache

top, bottom = open('d19.txt').read().split('\n\n')
patterns, designs = {x for x in top.split(', ')}, bottom.splitlines()

@cache
def count(design):
    if design == '': return 1
    new_designs = [design[len(p):] for p in patterns if design.startswith(p)]
    return sum(count(d) for d in new_designs)

result = [count(d) for d in designs]
print(sum(bool(x) for x in result))
print(sum(result))