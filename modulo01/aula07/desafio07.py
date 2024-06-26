altura = float(input('Digite o valor da altura: '))
largura = float(input('Digite o valor da largura: '))

area = altura * largura

print('Será necessário {:.2f}L de tinta para pintar a parede de {:.2f} m².'.format(area/2, area))