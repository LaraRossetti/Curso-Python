fatorial = lambda n: 1 if n == 0 else n * fatorial(n-1)
print(fatorial(int(input('Digite um número: '))))