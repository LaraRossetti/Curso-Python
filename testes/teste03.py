def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

numero = input('Digite um número: ')
numero = int(numero)

print('O fatorial de ' + str(numero) + ' é ' + str(fatorial(numero)))