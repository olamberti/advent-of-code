input = list(map(int, open('d11.txt').read().split()))
stones, cache = {x: input.count(x) for x in input}, {0: (1,)}

def split(n):
    if n in cache:
        return cache[n]
    s = str(n)
    if len(s) % 2:
        ans = (n * 2024,) 
    else:
        ans = (int(s[:len(s)//2]), int(s[len(s)//2:]))
    cache[n] = ans
    return ans

for step in range(2000):
    new_stones = {}
    for x, n in stones.items():
        for y in split(x):
            if y in new_stones:
                new_stones[y] += n
            else:
                new_stones[y] = n
    if step == 25:
        print(sum(stones.values()))
    stones = new_stones
          
print(sum(stones.values()))