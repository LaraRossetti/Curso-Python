nome = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nome.split()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(''.join(nomeDividido))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomeDividido[0], len(nomeDividido[0])))



