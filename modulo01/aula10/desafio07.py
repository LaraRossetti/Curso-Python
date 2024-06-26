salario = float(input('Qual é o salário do funcionário? '))
if salario <= 1250:
    salarioFinal = salario*1.15
else:
    salarioFinal = salario*1.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salarioFinal)) 