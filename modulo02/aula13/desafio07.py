numero = int(input('Digite um número: '))
contagem = 0

for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        contagem += 1
    else:
        print('\033[31m{}\033[m'.format(c), end=' ')

print('\nO número {} é divisível {} vezes.'.format(numero, contagem))
if contagem == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
