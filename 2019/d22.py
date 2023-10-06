def get_card(a0, m, n):
    return (a0 + m * n) % N

def eea(a1, a2): # Extended Euclidean algorithm
    q = [[a1, 1, 0], [a2, 0, 1]]
    while q[-1][0] != 0:
        d = q[-2][0] // q[-1][0]
        r = q[-2][0] - d * q[-1][0]
        a = q[-2][1] - d * q[-1][1]
        b = q[-2][2] - d * q[-1][2]
        q.append([r, a, b])
    return q[-2][2] % a1

def mod_exp(base, exp, mod): # modular exponentiation
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1: res = (res * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return res

def cut(deck, n):
    a0 = deck[0] + deck[1] * n
    m = deck[1]
    return (a0, m)

def rev(deck):
    a0 = deck[0] - deck[1]
    m = -deck[1]
    return (a0, m)

def inc(deck, n):
    a0 = deck[0]
    m = deck[1] * eea(N, n)
    return(a0, m)

def shuffle(deck, inst):
    for line in inst:
        line = line.strip().split()
        if line[0] == 'cut': deck = cut(deck, int(line[-1]))
        elif line[2] == 'increment': deck = inc(deck, int(line[-1]))
        else: deck = rev(deck)
    return deck


# P1
inst = open('d22.txt').readlines()
N, deck = 10_007, (0, 1)

a0, m = shuffle(deck, inst)
deck = [get_card(a0, m, i) for i in range(N)]
print(deck.index(2019))

# P2
N = 119_315_717_514_047
S = 101_741_582_076_661
deck = (0, 1)

k1, k2 = shuffle(deck, inst)
a0 = (k1 * (1 - mod_exp(k2, S, N)) * eea(N, 1 - k2)) % N
m = mod_exp(k2, S, N)
print(get_card(a0, m, 2020))