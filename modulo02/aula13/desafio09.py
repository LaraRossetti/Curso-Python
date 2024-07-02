from datetime import date
anoAtual = date.today().year
maiorDeIdade = 0
menorDeIdade = 0

for c in range(1, 8):
    anoNascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if anoNascimento <= anoAtual and (anoAtual - anoNascimento) < 130:
        if (anoAtual - anoNascimento) >= 18:
            maiorDeIdade += 1
        else:
            menorDeIdade += 1
print('\nAo todo tivemos {} pessoas maiores de idade.'.format(maiorDeIdade))
print('E também tivemos {} pessoas menores de idade.\n'.format(menorDeIdade))