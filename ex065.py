c= menor= maior= soma= 0
continuaçao=''
while continuaçao!='NÃO':
  numero=int(input('insira um número\n'))
  #variavel de verificação
  continuaçao=str(input('Deseja inserir outro número?\n')).upper().strip()
  #medía
  soma+=numero 
  c+=1
  #Maior e menor  
  if menor==0 and maior==0:
    maior=numero
    menor=numero 
  elif numero > maior :
    maior=numero
  elif numero < menor:
    menor = numero  
print('Á média foi de {} o maior número foi {} e o menor {}.'.format(soma/c, maior, menor))
