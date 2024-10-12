from random import randint
from time import sleep
listadepalpites=[]
gerandojogo=[]

Qpalapites=int(input('Quantos palpites você deseja gerar:'))

for c in range(0,Qpalapites):
    while True:
        naleatorio=randint(0,60)
        
        if naleatorio not in gerandojogo:
         gerandojogo.append(naleatorio)

        if len(gerandojogo)==6:
         listadepalpites.append(gerandojogo[:])
         gerandojogo.clear()
         break
    
    print(f'Jogo {c+1}:{sorted(listadepalpites[c])}')
    sleep(2)