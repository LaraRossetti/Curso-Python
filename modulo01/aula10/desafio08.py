print('-=-'*10)
print('Analisador de triângulos')
print('-=-'*10)
segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))
if segmento1 < segmento2+segmento3 and segmento2 < segmento1+segmento3 and segmento3 < segmento1+segmento2:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')