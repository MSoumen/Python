t=int(input())
while t>0:
    ids=input()
    if ids=='B' or ids=='b':
        print('BattleShip')
    elif ids=='C' or ids=='c':
        print('Cruiser')
    elif ids=='D' or ids=='d':
        print('Destroyer')
    elif ids=='F' or ids=='f':
        print('Frigate')
    t-=1
