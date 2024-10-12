print('Pense em  qualquer número entre 1 e 1 Bilhão\nque eu vou acertar em no maxímo 30 palpites!')
chute=0
acerto=0
c=0
minimo=0
maximo=1000000000
while acerto==0:
    c+=1
    chute=int((minimo+maximo)/2)
    print('Palpite-0{}|{} seu número é ?'.format(c, chute))
    mn=str(input('[A]-Maior\n[B]-Menor\n[C]-É este\n')).strip().upper()
    
    if mn=='A':
        minimo=chute
    elif mn=='B':
        maximo=chute
    elif mn=='C':
       acerto=1
print('Seu número é : {}'.format(chute))

#Utilização de pesquisa binária 
 
    
