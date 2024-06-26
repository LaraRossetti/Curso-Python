import math
catetoOposto = float(input('Qual o comprimento do cateto oposto? '))
catetoAdjacente = float(input('Qual o comprimento do cateto adjacente? '))

#hipotenusa = math.sqrt(catetoOposto**2 + catetoAdjacente**2)
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)


print('A hipotenusa do triângulo com o cateto oposto {} e o cateto adjacente {} é {:.2f}.'.format(catetoOposto, catetoAdjacente, hipotenusa))
