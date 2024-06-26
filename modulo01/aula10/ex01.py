import emoji
nome = str(input('Qual é o seu nome? '))

if nome == 'Lara':
    print('Que lindo nome você tem, {}!'.format(nome), end='')
else:
    print('Bom dia, {}.'.format(nome), end='')
print(emoji.emojize(':thumbs_up:'))