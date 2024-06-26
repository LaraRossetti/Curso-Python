valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
valor3 = int(input('Terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
    maiorValor = valor1
elif valor2 > valor1 and valor2 > valor3:
    maiorValor = valor2
else:
    maiorValor = valor3

if valor1 < valor2 and valor1 < valor3:
    menorValor = valor1
elif valor2 < valor1 and valor2 < valor3:
    menorValor = valor2
else:
    menorValor = valor3
print('O maior valor digitado é {}'.format(maiorValor))
print('O menor valor digitado é {}'.format(menorValor))