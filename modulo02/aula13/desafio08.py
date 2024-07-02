frase = str(input('Digite uma frase: '))
frase = frase.upper().split()
junto = ''.join(frase)
tamanho = len(junto)
contrario = ''

for c in range(tamanho, 0, -1):
    contrario += junto[c-1]
print('O inverso de {} é {}'.format(junto, contrario))
if junto == contrario:
    print('A frase digitada \033[32mé um palíndromo\033[m.')
else:
    print('A frase digitada \033[31mnão é palíndromo\033[m.')

