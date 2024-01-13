# gm_rc_Hanoi_Tower.py: coded by Kinya MIURA 230414
# ---------------------------------------------------------
print('*** Recursive call: Hanoi Tower ***')

# =========================================================
## --- defining function --- ##
def hanoi(nn, gtt, stt, tmp):
    if nn <= 0:
        return
    hanoi(nn - 1, gtt, tmp, stt)
    stt.append(gtt.pop())
    print_hanoi()
    hanoi(nn - 1, tmp, stt, gtt)
def print_hanoi():
    global ii
    print(f'ii: {ii:2d}: gtt; {gtt}, stt; {stt}, tmp; {tmp}')
    ii += 1

## --- main routine --- ##
nn, ii = 4, 0; print(f'{nn = }')
gtt, stt, tmp = list(range(nn)), [], []
print_hanoi()
hanoi(nn, gtt, stt, tmp)

# =============================================================
# terminal log / terminal log / terminal log /
'''
*** Recursive call: Hanoi Tower ***
nn = 4
ii:  0: gtt; [0, 1, 2, 3], stt; [], tmp; []
ii:  1: gtt; [0, 1, 2], stt; [], tmp; [3]
ii:  2: gtt; [0, 1], stt; [2], tmp; [3]
ii:  3: gtt; [0, 1], stt; [2, 3], tmp; []
ii:  4: gtt; [0], stt; [2, 3], tmp; [1]
ii:  5: gtt; [0, 3], stt; [2], tmp; [1]
ii:  6: gtt; [0, 3], stt; [], tmp; [1, 2]
ii:  7: gtt; [0], stt; [], tmp; [1, 2, 3]
ii:  8: gtt; [], stt; [0], tmp; [1, 2, 3]
ii:  9: gtt; [], stt; [0, 3], tmp; [1, 2]
ii: 10: gtt; [2], stt; [0, 3], tmp; [1]
ii: 11: gtt; [2, 3], stt; [0], tmp; [1]
ii: 12: gtt; [2, 3], stt; [0, 1], tmp; []
ii: 13: gtt; [2], stt; [0, 1], tmp; [3]
ii: 14: gtt; [], stt; [0, 1, 2], tmp; [3]
ii: 15: gtt; [], stt; [0, 1, 2, 3], tmp; []
'''