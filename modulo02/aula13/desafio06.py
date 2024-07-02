print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)
a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for n in range(1, 11):
    an = a1 + (n - 1)*razao
    print('{} →'.format(an), end=' ')
print('ACABOU')