# gm_Stone_Paper_Scissors_multi: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Stone Paper Scissors: multiple computer hands ***')
# ---------------------------------------------------------
import random

# --- main routine ---
strg = '-1'  # inputting number of comps
while not strg.isdigit() or int(strg) <= 0:
    strg = input("\tnumber of Comp's hands: {0 < } ? ")
numcomp = int(strg)
hand_comps = [-1 for i in range(numcomp)]

hands = {0: 'Stone', 1: 'Paper', 2: 'Scissors'}  # 'dict' for hands
round = 1  # counter of round
while True:
    print(f'=== Round {round} ===')

    strg = '-1'  # inputting your hand
    while not strg.isdigit() or int(strg) < 0 or int(strg) > 2:
        strg = input('\tYour hand: {0: Stone, 1: Paper, 2: Scissors} ? ')
    hand_your = int(strg)
    print(f"Your hand:  {hand_your}: {hands[hand_your]}")

    hand_comps = [  # generating hand of comps
        random.randint(0, 2) if hand_comp is not None else None
        for hand_comp in hand_comps ]
    for i, hand_comp in enumerate(hand_comps):
        if hand_comp is None:
            print(f'Comp{i}:  ', None)
        else:
            print(f'Comp{i}:  ', f'{hand_comp}: {hands[hand_comp]}')
            hand_comps[i] = (1 + hand_your - hand_comp) %3 - 1

    if 1 in hand_comps:  # judging the winner
        if -1 in hand_comps:
            print('\tDraw !!')
        else:
            print('\tYou Win !!')
            if 0 in hand_comps:
                hand_comps = [
                    None if hand_comp == 1 else hand_comp
                    for hand_comp in hand_comps ]
            else:
                break
    else:
        if -1 in hand_comps:
            print('\tYou Lose !!')
            break
        else:
            print('\tDraw !!')
    round += 1

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Stone Paper Scissors: multiple computer hands ***
	number of Comp's hands: {0 < } ? 2
=== Round 1 ===
	Your hand: {0: Stone, 1: Paper, 2: Scissors} ? 1
Your hand:  1: Paper
Comp0:   1: Paper
Comp1:   1: Paper
	Draw !!
=== Round 2 ===
	Your hand: {0: Stone, 1: Paper, 2: Scissors} ? 2
Your hand:  2: Scissors
Comp0:   0: Stone
Comp1:   0: Stone
	You Lose !!
'''