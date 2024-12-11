stones = {int(x): 1 for x in open('d11.txt').read().split()}
cache = {0: (1,)}

def split(n):
    if n in cache:
        return cache[n]
    s = str(n)
    if len(s) % 2 == 0:
        ans = (int(s[:len(s)//2]), int(s[len(s)//2:]))
    else:
        ans = (n * 2024,)
    cache[n] = ans
    return ans

for step in range(75):
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