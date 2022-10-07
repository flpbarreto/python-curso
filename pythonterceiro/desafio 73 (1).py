ordem = ('CAM','FLA', 'PAL', 'FOR','COR', 'BGT',
         'FLU', 'AME','ACG', 'SAN', 'CEA', 'INT',
         'SAO', 'CAP', 'CUI', 'JUV', 'GRE', 'BAH',
         'SPT', 'CHA')
print('COLOCAÇÃO:\n')
for c in range(0, 20):
    print(ordem[c])
print(end='\n')
print('QUATRO ÚLTIMOS COLOCADOS:\n')
for c in range(16, 20):
    print(ordem[c])
print(end='\n')
alfabetica = sorted(ordem)
print('ORDEM ALFABÉTICA:\n')
for c in range(0, 20):
    print(alfabetica[c])
print(end='\n')
cha = ordem.index('CHA')
print(f'A Chapecoense está em {cha + 1}° lugar.')