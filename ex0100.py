from random import randint

def sorteador(lista):
    for i in range(0, 5):
        lista.append(randint(0, 10))
    print(lista) 
    

def spar(*numbrs):
    newlist=[]
    for X in numbrs:
       if X%2==0:
           newlist.append(X)
    print(newlist)

numeros=[]

sorteador(numeros)
spar(*numeros)


