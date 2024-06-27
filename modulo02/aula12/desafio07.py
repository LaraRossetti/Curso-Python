segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 > segmento2+segmento3 or segmento2 > segmento1+segmento3 or segmento3 > segmento1+segmento2:
    print('Não é possível formar um triângulo com esses segmentos.')
else:
    if segmento1 == segmento2 == segmento3:
        print('Triângulo EQUILÁTERO!')
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print('Triângulo ISÓSCELES!')
    else:
        print('Triângulo ESCALENO!')
        