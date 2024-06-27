nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {} e {}, a média do aluno é {:.2f}.'.format(nota1, nota2, media))
if media < 5.0:
    print('O aluno está \033[31mREPROVADO\033[m.')
elif media < 6.9:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m.')
elif media <= 10.0:
    print('O aluno está \033[32mAPROVADO\033[m.')
else:
    print('Média inválida, tente novamente.')