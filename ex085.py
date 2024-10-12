listanumerica=[[],[]]
for c in range(7):
    numero=int(input('Insira um número:'))
    if numero%2==0:
       listanumerica[0].append(numero)
    else:
        listanumerica[1].append(numero)  
print(sorted(listanumerica[0]),
      sorted(listanumerica[1])) 
