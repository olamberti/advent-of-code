data = [int(x) for x in open('d08.txt').read().split()]

class Node():
    def __init__(self, n_child, n_meta, parent):
        self.nCh = n_child
        self.nM = n_meta
        self.parent = parent
        self.children = None

# P1:
tree = Node(data[0], data[1], None)

i = 2
while i < len(data):
    pass


# P2:
# TODO code part 2