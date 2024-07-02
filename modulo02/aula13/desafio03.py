quantidade = 0
soma = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        quantidade += 1
print('Ao todo, são {} valores ímpares e divisíveis por 3 entre 1 e 500, e o somatório desses valores é {}.'.format(quantidade, soma))