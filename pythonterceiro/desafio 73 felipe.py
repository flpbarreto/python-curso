times = ('CAM', 'FLA', 'FOR', 'PAL', 'COR', 'BGT', 'CAP',
         'INT', 'FLU', 'ACG', 'AME', 'CUI', 'CEA', 'SAO', 'JUV', 'SPT', 'SAN', 'BAH', 'GRE', 'CHA')
print(f'''--- 5 PRIMEIROS ---
\033[1;33m1º {times[0]}\033[m
\033[1;37m2º {times[1]}\033[m
\033[1;35m3º {times[2]}\033[m
4º {times[3]}
5º {times[4]}\n''')
print(f'''--- ULTIMOS COLOCADOS ---
17º {times[-4]}
18º {times[-3]}
19º {times[-2]}
20º {times[-1]}\n''')
print('--- ORDEM ALFABÉTICA ---')
alfabetica = sorted(times)
for c in range (0, 20, 1):
    print(alfabetica[c], end = '\n')
cha = times.index('CHA') + 1
print(f'''\nA Chapecoense está em {cha}º lugar''')

