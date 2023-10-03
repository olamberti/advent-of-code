import heapq as hq

# Init
player, boss, effects = [50, 500], [0, 0], [0, 0, 0] # [HP, mana], [HP, damage], [shield, poison, recharge]
for line in open('22.txt').readlines():
    line = line.strip().split(' ')
    if line[0] == 'Hit': boss[0] = int(line[-1])
    elif line[0] == 'Damage:': boss[1] = int(line[-1])
startstate, spellcosts = (0, *player, *boss, *effects), {0: 53, 1: 73, 2: 113, 3: 173, 4: 229}

def next_state(gamestate, sID, hard = False):
    # Read gamestate
    manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT = gamestate

    # Player (0) and boss (1) turn:
    for t in range(2):

        # Hard mode
        if t == 0 and hard:
            pHP -= 1
            if pHP == 0: return -1, None
        
        # Effects:
        if shT > 0: pArm = 7; shT -= 1
        else: pArm = 0
        if poT > 0: bHP -= 3; poT -= 1
        if reT > 0: pMana += 101; reT -= 1
        if bHP <= 0: return 1, manaspent

        # Player's turn - spell choice:
        if t == 0:
            if pMana >= spellcosts[sID]:
                pMana -= spellcosts[sID]
                manaspent += spellcosts[sID]
                if sID == 0:
                    bHP -= 4
                elif sID == 1:
                    bHP -= 2; pHP += 2
                elif sID == 2:
                    if shT == 0: shT += 6
                    else: return -1, None
                elif sID == 3:
                    if poT == 0: poT += 6
                    else: return -1, None
                elif sID == 4:
                    if reT == 0: reT += 5
                    else: return -1, None
            else: return -1, None
            if bHP <= 0: return 1, manaspent

        # Boss's turn, attack:
        elif t == 1:
            pHP -= max(bDMG - pArm, 1)
            if pHP <= 0: return -1, None
    
    # End of turns
    return 0, (manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT)

def min_mana(startstate, hard):
    stack, done = [startstate], False
    hq.heapify(stack)
    while not done:
        state = hq.heappop(stack)
        for sID in range(5):
            res, nstate = next_state(state, sID, hard)
            if res == -1: continue
            elif res == 1:
                min_mana = nstate
                done = True
                break
            elif res == 0:
                hq.heappush(stack, nstate)
    return min_mana

# P1
print(min_mana(startstate, False))

# P2
print(min_mana(startstate, True))