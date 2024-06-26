import math
numero = float(input('Digite um número: '))

porcaoInteira = math.trunc(numero)
print('O número {} tem a parte inteira {}.'.format(numero, porcaoInteira))

print('O número é {} e sua parte inteira é {}.'.format(numero, int(numero)))  #outro jeito de fazer