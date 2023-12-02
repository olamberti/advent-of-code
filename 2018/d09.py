import re

players, N = [int(x) for x in re.findall(r'(\d+)', open('d09.txt').read())]

class Link:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next 
        self.prev = prev

current = Link(0)
current.next = current
current.prev = current

scores = [0] * players
for i in range(1, (100 * N) + 1):
    player = i % players
    if i % 23 != 0:
        current = current.next
        new_link = Link(i, current.next, current)
        current.next = new_link
        new_link.next.prev = new_link
        current= new_link
    else:
        scores[player] += i
        for _ in range(7): current = current.prev
        scores[player] += current.value
        current.prev.next = current.next
        current.next.prev = current.prev
        current = current.next
    if i == N + 1: print(max(scores))

print(max(scores))