tupla=(int(input('Insira o primeiro valor:')),
int(input('Insira o seugundo valor:')),
int(input('Insira o terceiro valor:')),
int(input('Insira o quarto valor:')))

valor=3
if valor in tupla: print(f'O primeiro 3 esta na posição {tupla.index(valor+1)}')
else :print('Tres não foi inserido na lista')

print(f'Foram inceridos {tupla.count(9)} números 9 ')

print('Os números pares são:',end='')
for c in tupla:
 print( '',c,end='' if c%2==0 else '')
 



