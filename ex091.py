from random import randint
ordenador=[]
results={}
cont=0
results['jogador1']=randint(1,6)
results['jogador2']=randint(1,6)
results['jogador3']=randint(1,6)
results['jogador4']=randint(1,6)

print(results)

for j, n in results.items():
    ordenador.append([n,j])
ordenador=sorted(ordenador,reverse=True)  
# ordenador= sorted(results.itens(), key=itemgetter(1), reverse=True) tem que dar inport / from operator inport itemgetter
results.clear()

for x in ordenador:
    results[x[1]]=x[0]
    
for j, n in results.items():
    cont+=1
    print(f'{cont}° lugar: {j} com {n}')