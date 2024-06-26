nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Sua média é {:.1f}.'.format(media))
if media >= 6.0:
    print('Está boa, parabéns!')
else: 
    print('Está ruim, estude mais!')
