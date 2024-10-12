valores=[]
for c in range (5):
 valores.append(int(input('insira um número:\n')))
dados=[max(valores),min(valores)]
indiceMAX=[indice for indice,numero in enumerate(valores) if numero==dados[0]]
indiceMIN=[indice2 for indice2,numero2 in enumerate(valores) if numero2==dados[1]]

print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {dados[0]} e esta na posição {indiceMAX}')
print(f'O menor valor digitado foi {dados[1]} e esta na posição {indiceMIN}')
