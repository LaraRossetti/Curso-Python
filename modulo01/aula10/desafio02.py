velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido de 80 km/h. \nSua multa é de R${:.1f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')