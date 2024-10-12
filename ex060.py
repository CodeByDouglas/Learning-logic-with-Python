from math import factorial

n=int(input('Insira um número:\n'))
lista=[str(i) for i in range(n,0,-1)]

expreçao='X'.join(lista) + '=' + str(factorial(n))
print(expreçao)
