nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Sua média é {:.1f}.'.format(media))
print('Parabéns!' if media >= 6.0 else 'Estude mais!')