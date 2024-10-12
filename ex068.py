from random import randint
cont=0
while True:
    numero=int(input('Insira uma número:'))
    maquina=randint(1,11)
    pi=''
    while pi not in 'PI': 
     pi=str(input("[P]-Par\n   ou\n[I]-Ímpar\n")).upper().strip()[0]
    verific=''
    if (numero+maquina)%2==0:
        if pi=='P':
         verific='Venceu'
         cont+=1
    else:
        if pi=='I':
           verific='Venceu'
           cont+=1    
    print(f'''
Você escolheu o número {numero} e a maquina escolheu o número {maquina}
Que resulta em {numero+maquina} = {'PAR'if (numero+maquina)%2==0 else 'ÍMPAR'}''')
    print('-=-'*30)
    print('''
Você Venceu,Parabéns!!
Vamos continuar... '''
          if verific=='Venceu' else f'''
Você perdeu!!
E conseguiu {cont} vítorias consecutivas ''')
    if verific=='':
       break
    






















#from random import randint #import de biblioteca 
#cont=0
#while True:
#   n=int(input('Qual valor deseja jogar:'))
#    pi=str(input('[P]/[I]')).upper().strip()[0]

#    ncomp=randint(1,10)
    
#    if n+ncomp%2==0:
#     result='PAR'
#     if pi=='P':
#      vf='Você Ganhou Parabéns!'
#      cont+=1
#      print(f'Você jogou {n} e o computador jogou {ncomp}\nTotal de {n+ncomp} deu {result}\n{vf}!\nVamos jogar novemnete..')
#     else:
#        vf='você Perdeu'
#        break
#    else: 
#     result='IMPAR' 
#     if pi=='I': 
#      vf='Você Ganhou Parabéns'
#      cont+=1
#      print(f'Você jogou {n} e o computador jogou {ncomp}\nTotal de {n+ncomp} deu {result}\n{vf}!\nVamos jogar novemnete..')
#     else:
#        vf='você Perdeu'
#        break
    
#print(f'Você jogou {n} e o computador jogou {ncomp}\nTotal de {n+ncomp} deu {result}\n{vf}!\nVocê ganhou {cont} vezes consecutivas')
  

