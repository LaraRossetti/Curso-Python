reais = float(input('Digite quantos reais você tem na carteira? R$'))

dolar = reais / 3.27

print('Você consegue comprar US${:.2f} com R${}.'.format(dolar, reais))