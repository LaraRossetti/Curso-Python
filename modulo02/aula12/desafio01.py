valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))
print('-=-'*30)
prestacao = valorCasa/(financiamento*12)

if prestacao > salario*0.30:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}. \n\033[31mEMPRÉSTIMO NEGADO!\033[m'.format(valorCasa, financiamento, prestacao))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}. \n\033[32mEMPRÉSTIMO pode ser CONCEDIDO!\033[m'.format(valorCasa, financiamento, prestacao))
print('-=-'*30)