p1, p2 = 0, 0
for line in open('04.txt').read().splitlines():
    words, ans, phrase = set(), set(), line.split()
    for w in phrase:
        words.add(w)
        ans.add(''.join(sorted(w)))
    if len(words) == len(phrase): p1 += 1
    if len(ans) == len(phrase): p2 += 1
print(p1)
print(p2)