maiorPeso = 0
menorPeso = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso lido foi de {}Kg.'.format(maiorPeso))
print('O menor peso lido foi de {}Kg.'.format(menorPeso))