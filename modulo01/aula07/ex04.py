n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
exponencial = n1 ** n2

print('Divisão inteira é {} e a potência é {}.'.format(divisaoInteira, exponencial), end= ' ') #para os dois prints serem na mesma linha
print('A soma vale {}, o produto vale {} e a divisão vale {:.3f}.'.format(soma, multiplicacao, divisao)) #colocar apenas 3 casas decimais
