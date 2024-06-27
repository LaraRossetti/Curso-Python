numero = int(input('Digite um número inteiro: \033[32m'))
cores = {
    'limpa': '\033[m',
    'roxo' : '\033[34m',
    'rosa' : '\033[35m',
    'amarelo' : '\033[33m'
         }
print('\033[mEscolha uma das bases para conversão: ')
print('{}[1] converter para BINÁRIO{}'.format(cores['roxo'], cores['limpa']))
print('{}[2] converter para OCTAL{}'.format(cores['rosa'], cores['limpa']))
print('{}[3] converter para HEXADECIMAL{}'.format(cores['amarelo'], cores['limpa']))
bases = int(input('Sua opção: \033[32m'))

if bases == 1:
    binario = bin(numero)
    print('\033[32m{}\033[m convertido para {}BINÁRIO{} é igual a {}{}{}.'.format(numero, cores['roxo'], cores['limpa'], cores['roxo'], binario[2:], cores['limpa']))
elif bases == 2:
    octal = oct(numero)
    print('\033[32m{}\033[m convertido para {}OCTAL{} é igual a {}{}{}.'.format(numero, cores['rosa'], cores['limpa'], cores['rosa'], octal[2:], cores['limpa']))
elif bases == 3:
    hexadecimal = hex(numero)
    print('\033[32m{}\033[m convertido para {}HEXADECIMAL{} é igual a {}{}{}.'.format(numero, cores['amarelo'], cores['limpa'], cores['amarelo'], hexadecimal[2:], cores['limpa']))
else:
    print('\033[31mOpção inexistente, tente novamente.\033[m')