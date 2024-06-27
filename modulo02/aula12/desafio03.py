numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

if numero1 > numero2:
    print('{} é \033[32mMAIOR\033[m do que {}.'.format(numero1, numero2))
elif numero1 < numero2:
    print('{} é \033[32mMENOR\033[m do que {}.'.format(numero1, numero2))
else:
    print('Os dois valores são \033[32mIGUAIS\033[m.')