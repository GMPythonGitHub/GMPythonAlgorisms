# gm_sorting_list.py: coded by Kinya MIURA 231229
# ---------------------------------------------------------
print('*** sorting: list ***')

# =========================================================
## --- creating list of dict --- ##
lstdct = [
    {'Name': 'Alpha', 'Age': 30, 'Score': 200},
    {'Name': 'Bravo', 'Age': 25, 'Score': 300},
    {'Name': 'Charlie', 'Age': 30, 'Score': 500},
    {'Name': 'Delta', 'Age': 35} ]
print(f'{lstdct = } \n')

## --- sorting list of dict --- ##
lstdctname = sorted(lstdct, key=lambda x: x['Name'])
print(f"lstdctname = sorted(lstdct, key=lambda x: x['Name']): {lstdctname = }")
lstdctage = sorted(lstdct, key=lambda x: x['Age'])
print(f"lstdctage = sorted(lstdct, key=lambda x: x['Age']): {lstdctage = } \n")

## --- sorting list of dict with get() --- ##
lstdctname = sorted(lstdct, key=lambda x: x.get('Name'))
print(f"lstdctname = sorted(lstdct, key=lambda x: x.get('Name')): {lstdctname = }")
lstdctage = sorted(lstdct, key=lambda x: x.get('Age'))
print(f"lstdctage = sorted(lstdct, key=lambda x: x.get('Age')): {lstdctage = }")
lstdctscore = sorted(lstdct, key=lambda x: x.get('Score', -float('inf')))
print(f"lstdctscore = sorted(lstdct, key=lambda x: x.get('Score', -float('inf'))): {lstdctscore = } \n")

## --- sorting list of dict with itemgetter() --- ##
from operator import itemgetter
lstdctname = sorted(lstdct, key=itemgetter('Name'))
print(f"lstdctname = sorted(lstdct, key=itemgetter('Name')): {lstdctname = }")
lstdctage = sorted(lstdct, key=itemgetter('Age'))
print(f"lstdctage = sorted(lstdct, key=itemgetter('Age')): {lstdctage = }")
lstdctagename = sorted(lstdct, key=itemgetter('Age', 'Name'))
print(f"lstdctagename = sorted(lstdct, key=itemgetter('Age', 'Name')): {lstdctagename = }")


# =========================================================
# terminal log / terminal log / terminal log /
'''
*** sorting: list ***
lstdct = [
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}] 

lstdctname = sorted(lstdct, key=lambda x: x['Name']): lstdctname = [
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}]
lstdctage = sorted(lstdct, key=lambda x: x['Age']): lstdctage = [
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}] 

lstdctname = sorted(lstdct, key=lambda x: x.get('Name')): lstdctname = [
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}]
lstdctage = sorted(lstdct, key=lambda x: x.get('Age')): lstdctage = [
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}]
lstdctscore = sorted(lstdct, key=lambda x: x.get('Score', -float('inf'))): lstdctscore = [
    {'Name': 'Delta', 'Age': 35}, 
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}] 

lstdctname = sorted(lstdct, key=itemgetter('Name')): lstdctname = [
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}]
lstdctage = sorted(lstdct, key=itemgetter('Age')): lstdctage = [
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}]
lstdctagename = sorted(lstdct, key=itemgetter('Age', 'Name')): lstdctagename = [
    {'Name': 'Bravo', 'Age': 25, 'Score': 300}, 
    {'Name': 'Alpha', 'Age': 30, 'Score': 200}, 
    {'Name': 'Charlie', 'Age': 30, 'Score': 500}, 
    {'Name': 'Delta', 'Age': 35}]
'''
