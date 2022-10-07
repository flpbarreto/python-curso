r1 = float(input('digite o cumprimento da r1: '))
r2 = float(input('digite o cumprimento da r2: '))
r3 = float(input('digite o cumprimento da r3: '))
if r3 > r2 and r3 > r1:
    if (r2 + r1) > r3:
        print('\no trinagulo existe')
    else:
        print('\no trinagulo não existe')
if r2 > r3 and r2 > r1:
    if (r3 + r1) > r2:
        print('\no trinagulo existe')
    else:
        print('\no trinagulo não existe')
if r1 > r3 and r1 > r2:
    if (r3 + r2) > r1:
        print('\no trinagulo existe')
    else:
        print('\no trinagulo não existe')
print('\n----FIM----')