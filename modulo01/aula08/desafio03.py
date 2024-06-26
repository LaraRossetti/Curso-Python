from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
angulo = radians(angulo)

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(angulo)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(angulo)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan(angulo)))