km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))

preco = (km * 0.15) + (dias * 60)

print('O total a pagar é R${:.2f}.'.format(preco))