cores = {
    'limpa' : '\033[m',
    'cinza' : '\033[30m',
    'vermelho' : '\033[31m',
    'verde' : '\033[32m',
    'amarelo' : '\033[33m',
    'roxo' : '\033[34m',
    'rosa' : '\033[35m',
    'azul' : '\033[36m',
    'branco' : '\033[37m'
}

print('{}30 - cinza{}'.format(cores['cinza'],cores['limpa']))
print('{}31 - vermelho{}'.format(cores['vermelho'],cores['limpa']))
print('{}32 - verde{}'.format(cores['verde'],cores['limpa']))
print('{}33 - amarelo{}'.format(cores['amarelo'],cores['limpa']))
print('{}34 - roxo{}'.format(cores['roxo'],cores['limpa']))
print('{}35 - rosa{}'.format(cores['rosa'],cores['limpa']))
print('{}36 - azul{}'.format(cores['azul'],cores['limpa']))
print('{}37 - branco{}'.format(cores['branco'],cores['limpa']))