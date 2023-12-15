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
hand_comp1 = random.randint(0,2)
hand_comp2 = random.randint(0,2)
print(f"Comp1's hand:  {hand_comp1}: {hands[hand_comp1]}")
print(f"Comp2's hand:  {hand_comp2}: {hands[hand_comp2]}")

hand_yc1 = (1 + hand_your - hand_comp1) % 3 - 1
hand_yc2 = (1 + hand_your - hand_comp2) % 3 - 1
if hand_yc1 + hand_yc2 == 0: print('\tDraw !!')
elif hand_yc1 + hand_yc2 > 0: print('\tYou Win !!')
elif hand_yc1 + hand_yc2 < 0: print('\tYou Lose !!')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Stone Paper Scissors ***
# -----------------------------------------------------------------------------
	Your hand ?: {0: Stone, 1: Paper, 2: Scissors}>? 2
Your hand:  2: Scissors
Comp1's hand:  0: Stone
Comp2's hand:  0: Stone
	You Lose !!
'''