# Init:
player, boss, effects = [50, 500], [0, 0], [0, 0, 0] # [HP, mana], [HP, damage], [shield, poison, recharge]
for line in open('22.txt').readlines():
    line = line.strip().split(' ')
    if line[0] == 'Hit': boss[0] = int(line[-1])
    elif line[0] == 'Damage:': boss[1] = int(line[-1])
startstate = (0, *player, *boss, *effects)
spellcosts = {0: 53, 1: 73, 2: 113, 3: 173, 4: 229}

def next_state(gamestate, sID):
    # Read gamestate
    manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT = gamestate
    
    # Player's turn - effects:
    if shT > 0: pArm = 7; shT -= 1
    else: pArm = 0
    if poT > 0: bHP -= 3; poT -= 1
    if reT > 0: pMana += 101; reT -= 1

    # Check boss's HP
    if bHP <= 0: return True, (manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT)
    
    # Player's turn - spell choice:
    if pMana >= spellcosts[sID]:
        pMana -= spellcosts[sID]
        manaspent += spellcosts[sID]
        if sID == 0:
            bHP -= 4
        elif sID == 1:
            bHP -= 2; pHP += 2
        elif sID == 2:
            if shT == 0: shT += 6
            else: return False, None
        elif sID == 3:
            if poT == 0: poT += 6
            else: return False, None
        elif sID == 4:
            if reT == 0: reT += 5
            else: return False, None
    else: return False, None

    # Check boss's HP
    if bHP <= 0: return True, (manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT)

    # Boss's turn, apply effects:
    if shT > 0: pArm = 7; shT -= 1
    else: pArm = 0
    if poT > 0: bHP -= 3; poT -= 1
    if reT > 0: pMana += 101; reT -= 1

    # Check boss's HP
    if bHP <= 0: return True, (manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT)

    # Boss's turn, attack:
    pHP -= max(bDMG - pArm, 1)

    # Check players's HP
    if pHP <= 0: return False, None

    return None, (manaspent, pHP, pMana, bHP, bDMG, shT, poT, reT)

# P1:
# priority queue to find cheapest way to win