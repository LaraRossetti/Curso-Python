print('===== LOJAS ROSSETTI =====')
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra de R${} vai custar R${:.2f} no final, com 10% de desconto.'.format(preco, preco*0.90))
elif opcao == 2: 
    print('Sua compra de R${} vai custar R${:.2f} no final, com 5% de desconto.'.format(preco, preco*0.95))
elif opcao == 3: 
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(parcelas, (preco/parcelas)))
    print('Sua compra de R${} vai custar R${} no final'.format(preco, preco))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f}, com juros.'.format(parcelas, (preco*1.20)/parcelas))
    print('Sua compra de R${} vai custar R${:.2f} no final.'.format(preco, preco*1.20))
else:
    print('Opção inválida, tente novamente.')
