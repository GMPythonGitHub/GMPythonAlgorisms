# gm_Example_Stone_Paper_Scissors_b: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** Stone Paper Scissors ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import random
hands = {0:'Stone', 1:'Paper', 2:'Scissors'}  # 'dict' for hands

strg = input('\tYour hand ?: {0: Stone, 1: Paper, 2: Scissors}')
hand_your = int(strg)
print(f"Your hand:  {hand_your}: {hands[hand_your]}")
hand_comp = random.randint(0,2)
print(f"Comp's hand:  {hand_comp}: {hands[hand_comp]}")

if hand_your - hand_comp == 0:
    print('\tDraw !!')
elif (1 + hand_your - hand_comp) % 3 - 1 > 00:
    print('\tYou Win !!')
elif (1 + hand_your - hand_comp) % 3 - 1 < 0:
    print('\tYou Lose !!')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Stone Paper Scissors ***
# -----------------------------------------------------------------------------
	Your hand ?: {0: Stone, 1: Paper, 2: Scissors}>? 0
Your hand:  0: Stone
Comp's hand:  1: Paper
	You Lose !!
'''