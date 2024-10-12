n=int(input('Qual valor você quer saber a tabúada ?\n')) 

for c in range(1, 11):
    print('{}X{}={}'.format(n,c,n*c))