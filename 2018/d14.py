input = open('d14.txt').read()

N, pattern, scores = int(input), bytearray(map(int,input)), bytearray([3, 7])
i, e1, e2 = 0, 0, 1
while True:
    if (i % 1_000_000) == 0 and pattern in scores: break
    for ch in [int(x) for x in str(scores[e1] + scores[e2])]:
        scores.append(ch)
    e1 = (e1 + scores[e1] + 1) % len(scores)
    e2 = (e2 + scores[e2] + 1) % len(scores)
    i += 1

print(''.join([str(x) for x in scores[N:N+10]]))
print(scores.index(pattern))