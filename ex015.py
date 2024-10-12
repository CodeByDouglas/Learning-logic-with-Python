from math import trunc
c1=float(input('qual o valor do cateto:'))
c2=float(input('qual o valor do segundo cateto:'))
hip=(c1**2+c2**2)** (1/5)
print('A hipotesa desse triangulo é {}'.format(trunc(hip)))