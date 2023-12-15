# gm_Example_Stone_Paper_Scissors_a: coded by Kinya MIURA 230415
# -----------------------------------------------------------------------------
print('\n*** Stone Paper Scissors ***')
print('# -----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
import random

strg = input('\tType your hand : {S: Stone, P: Paper, C: Scissors}')
if strg in ('S', 's'):
    hand_your = 'Stone'
elif strg in ('P', 'p'):
    hand_your = 'Paper'
else:
    hand_your = 'Scissors'
print(f"Your hand:  {hand_your}")
hand_comp = random.choice(['Stone', 'Paper', 'Scissors'])
print(f"Comp's hand:  {hand_comp}")

if hand_your == hand_comp:
    print('\tDraw !!')
elif (  hand_your == 'Stone' and hand_comp == 'Scissors' or
        hand_your == 'Paper' and hand_comp == 'Stone' or
        hand_your == 'Scissors' and hand_comp == 'Paper'):
    print('\tYou Win !!')
elif (
        hand_your == 'Stone' and hand_comp == 'Paper' or
        hand_your == 'Paper' and hand_comp == 'Scissors' or
        hand_your == 'Scissors' and hand_comp == 'Stone'):
    print('\tYou Lose !!')

# =============================================================================
# terminal log / terminal log / terminal log /
'''
*** Stone Paper Scissors ***
# -----------------------------------------------------------------------------
	Type your hand : {S: Stone, P: Paper, C: Scissors}>? p
Your hand:  Paper
Comp's hand:  Paper
	Draw !!
'''