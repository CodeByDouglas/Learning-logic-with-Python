elementos=int(input('Quantos elementos deseja ver?\n'))
c=0
e1=0
e2=1
print('{}--{}'.format(e1,e2),end='')
while c<=elementos:
    e3=e1+e2
    c+=1
    print('--{}'.format(e3),end='') #end serve para não pular linha 
    e1=e2
    e2=e3
    
    