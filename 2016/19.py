n = int(open('19.txt').read())

class Chain():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# P1
elves = [x for x in range(1, n+1)]