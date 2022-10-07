n = 0
while n >= 0:
    n = int(input('Digite qual tabuada deseja ver: '))
    if n < 0:
        break
    for c in range (1, 11, 1):
        tab = n * c
        print(f'{n} x {c} = {tab}')
print('---FIM!---')
