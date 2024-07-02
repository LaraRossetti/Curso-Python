idadeTotal = 0
mulheresMenoresDeVinte = 0
homemMaisVelho = {
    'nome' : '',
    'idade' : 0
}
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: ')) 
    sexo = str(input('Sexo [M/F]: ')).strip()
    idadeTotal += idade
    if sexo.upper() == 'M' and c == 1:
        homemMaisVelho['nome'] = nome
        homemMaisVelho['idade'] = idade
    if sexo.upper() == 'M' and idade > homemMaisVelho['idade']:
        homemMaisVelho['idade'] = idade
        homemMaisVelho['nome'] = nome
    elif sexo.upper() == 'F':
        if idade < 20:
            mulheresMenoresDeVinte += 1

media = idadeTotal/4
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(homemMaisVelho['idade'], homemMaisVelho['nome']))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheresMenoresDeVinte))
