straights, curves_1, curves_2, intersections = set(), set(), set(), set()
carts, n_carts = [], 0

class Cart:
    def __init__(self, pos, face, id):
        self.id = id
        self.pos = pos
        self.face = [1, -1, 1j, -1j]['><v^'.find(face)]
        self.turns = 0
        self.options = [-1j, 1, 1j]
        self.crashed = False
        
    def __eq__(self, other):
        return self.id == other.id
    
    def move(self):
        if self.pos in straights:
            self.pos = self.pos + self.face
        elif self.pos in curves_1:
            if self.face.real == 0: turn = 1j
            elif self.face.imag == 0: turn = -1j
            self.pos = self.pos + self.face * turn
            self.face = self.face * turn
        elif self.pos in curves_2:
            if self.face.real == 0: turn = -1j
            elif self.face.imag == 0: turn = 1j
            self.pos = self.pos + self.face * turn
            self.face = self.face * turn
        elif self.pos in intersections:
            turn = self.options[self.turns % 3]
            self.pos = self.pos + self.face * turn
            self.face = self.face * turn
            self.turns += 1

for y, line in enumerate(open('d13.txt').read().splitlines()):
    for x, c in enumerate(line):
        if c in '-|': straights.add(x + y*1j)
        elif c == '/': curves_1.add(x + y*1j)
        elif c == '\\': curves_2.add(x + y*1j)
        elif c == '+': intersections.add(x + y*1j)
        elif c in '^v<>':
            straights.add(x + y*1j)
            carts.append(Cart(x + y*1j, c, n_carts))
            n_carts += 1

p1 = True
while n_carts > 1:
    carts = sorted(carts, key = lambda x: (x.pos.imag, x.pos.real))
    for cart in carts:
        if cart.crashed or n_carts == 1: continue
        cart.move()
        for other_cart in carts:
            if cart == other_cart: continue
            if cart.pos == other_cart.pos:
                cart.crashed, other_cart.crashed = True, True
                n_carts -= 2
                if p1:
                    print(int(cart.pos.real), int(cart.pos.imag), sep=',')
                    p1 = False
                break
    for cart in carts:
        if cart.crashed: carts.remove(cart)

print(int((carts[0].pos.real)), int((carts[0].pos.imag)),sep=',')