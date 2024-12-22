from collections import defaultdict

def next_num(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x

p1, bananas = 0, defaultdict(int)
for n in open('d22.txt').readlines():
    x = int(n)
    prices = [x % 10]
    for _ in range(2000):
        x = next_num(x)
        prices.append(x % 10)
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    seen = set()
    for i in range(2000 - 3):
        seq = tuple(changes[i : i + 4])
        if seq in seen: continue
        seen.add(seq)
        bananas[seq] += prices[i + 4]
    p1 += x
print(p1)
print(max(bananas.values()))