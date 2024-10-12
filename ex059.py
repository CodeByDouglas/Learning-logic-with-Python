from time import sleep
menu=0

while menu!=5:
 
 if menu==0 or menu==4:
   n1=float(input('Digite p primeiro valor:\n'))
   n2=float(input('Digite o segundo valor:\n'))
 sleep(2)
 menu=int(input(('\nOlá qual das opções você deseja:\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do progama\n')))
 
 if menu==1:
    print('A soma dos números enviados é : {}'.format(n1+n2))
 elif menu==2:
    print('A multiplicação dos números enviados da : {}'.format(n1*n2))
 elif menu==3:
    if n1>n2:
       print('O maior número é {}'.format(n1))
    elif n2>n1:
        print('O maior número é {}'.format(n2))
    else:
        print('Ambos os números são iguais')

