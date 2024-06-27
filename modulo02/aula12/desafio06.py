from datetime import date
anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento

if idade > 120 or anoNascimento > date.today().year:
    print('Ano de nascimento inválido, tente novamente.')
else:
    print('O atleta tem {} anos.'.format(idade))
    if idade <= 9:
        print('Classificação: MIRIM')
    elif idade <= 14:
        print('Classificação: INFANTIL')
    elif idade <= 19:
        print('Classificação: JUNIOR')
    elif idade <= 25:
        print('Classificação: SÊNIOR')
    else:
        print('Classificação: MASTER')