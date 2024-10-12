n= soma= c=0
while n!=999:
    soma+=n
    c+=1
    n=float(input('Insira um número:'))

print('A soma dos {} números digitados é {}'.format(c-1,soma))

#print('insira quantos números inteiros desejar')
#n=0
#soma=0
#expresao=[]
#while n != 999:
 #   n=int(input())
 #   if n!=999:
 #    soma+=n
 #     expresao.append(str(n))
#exibir=str('+'.join(expresao) + '=' +  str(soma))
#print(exibir)