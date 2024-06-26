import random, time

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
numero = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
numeroAleatorio = random.randint(0,5)
if numero == numeroAleatorio:
    print('Você ganhou! Tinha pensado no número {}.'.format(numeroAleatorio))
else:
    print('Eu ganhei! Pensei no número {} e não no número {}.'.format(numeroAleatorio, numero))
