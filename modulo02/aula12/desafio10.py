import random, time
print('Suas opções: ')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
computador = random.randint(0, 2)
if computador == 0:
        computador = 'pedra'
elif computador == 1:
    computador = 'papel'
else:
    computador = 'tesoura'

if jogador > 2 or jogador < 0:
    print('Opção inválida, tente novamente.')
else:
    if jogador == 0:
        jogador = 'pedra'
    elif jogador == 1:
        jogador = 'papel'
    else:
        jogador = 'tesoura'

    print('JO')
    time.sleep(0.7)
    print('KEN')
    time.sleep(0.7)
    print('PO!!')
    time.sleep(0.7)
    print('-=-'*9)

    print('Computador jogou {}.'.format(computador))
    print('Jogador jogou {}.'.format(jogador))
    print('-=-'*9)

    if computador == 'pedra' and jogador == 'pedra' or computador == 'papel' and jogador == 'papel' or computador == 'tesoura' and jogador == 'tesoura':
         print('EMPATE!')
    elif computador == 'papel' and jogador == 'pedra' or computador == 'tesoura' and jogador == 'papel' or computador == 'pedra' and jogador == 'tesoura':
         print('COMPUTADOR GANHOU!')
    else:
         print('JOGADOR GANHOU!')
