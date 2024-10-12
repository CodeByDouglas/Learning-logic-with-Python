n=int(input('Insira um número entre 1 e 1000:\n'))
chute=int(0)
maximo=100000
minimo=0
while n!=chute:
 chute=int((minimo+maximo)/2)
 if chute!=n:
  if n>chute:
   minimo=chute
  elif n<chute:
    maximo=chute
    
print('Seu número é : {}'.format(chute))