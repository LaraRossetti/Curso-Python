import emoji
nome = str(input('Qual é o seu nome? '))

if nome == 'Lara':
    print('Uau! Que nome lindo!',end='')
elif nome == 'João' or 'Paulo' or 'Ana':
    print('Seu nome é bem comum no Brasil.',end='')
else:
    print('Tenha um bom dia!')
print(emoji.emojize(':thumbs_up:'))