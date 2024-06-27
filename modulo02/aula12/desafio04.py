import datetime
anoNascimento = int(input('Ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento


if anoNascimento < 1904 or anoNascimento > anoAtual:
    print('Data inválida, tente novamente.')
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNascimento, idade, anoAtual))
    if idade < 18:
        print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(anoAtual + (18 - idade)))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} ano(s).'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))
    else:
        print('Agora em {}, você deve se alistar imediatamente!!'.format(anoAtual))
