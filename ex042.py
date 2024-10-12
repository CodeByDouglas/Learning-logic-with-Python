r1=float(input('Insira primeira reta :\n'))
r2=float(input('\nInsira a segunda reta :\n'))
r3=float(input('\nInsira a tercwira reta : \n'))

if(r1+r2>r3)and(r1+r3>r2)and(r2+r3>r1):
    print('É possível criar um triângulo com essas retas\n')
    if (r1==r2)and(r1==r3):
        print('Esse e um triângulo Equilátero')
    elif((r1==r2)or(r1==r3))or(r2==r3):
        print('Esse e um triângulo isóseles')
    else:
        print('Esse triângulo e um Escaleno')
else:
    print('Não e possível criar um triângulo com essas retas ')