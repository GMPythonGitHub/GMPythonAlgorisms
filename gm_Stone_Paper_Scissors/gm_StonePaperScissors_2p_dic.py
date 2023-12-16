# gm_Stone_Paper_Scissors: coded by Kinya MIURA 230415
# ---------------------------------------------------------
print('*** Stone Paper Scissors: two persons ***')
# ---------------------------------------------------------
import random

# --- main routine ---
hands = {0:'Stone', 1:'Paper', 2:'Scissors'}  # 'dict' for hands
strg = '-1'
while not strg.isdigit() or int(strg) < 0 or int(strg) > 2:
    strg = input('\tYour hand: {0: Stone, 1: Paper, 2: Scissors} ? ')
hand_your = int(strg)
print(f"Your hand:  {hand_your}: {hands[hand_your]}")
hand_comp = random.randint(0,2)
print(f"Comp's hand:  {hand_comp}: {hands[hand_comp]}")

if hand_your == hand_comp:
    print('\tDraw !!')
elif (1 + hand_your - hand_comp) % 3 - 1 > 00:
    print('\tYou Win !!')
elif (1 + hand_your - hand_comp) % 3 - 1 < 0:
    print('\tYou Lose !!')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Stone Paper Scissors:  ***
# -----------------------------------------------------------------------------
	Your hand ?: {0: Stone, 1: Paper, 2: Scissors}>? 0
Your hand:  0: Stone
Comp's hand:  1: Paper
	You Lose !!
'''