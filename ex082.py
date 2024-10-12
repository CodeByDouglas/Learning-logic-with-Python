listaprimaria=[]
listaimpar=[]
listapar=[]
while True:
    entradadenumero=int(input('Insira um número:'))
    listaprimaria.append(entradadenumero)
    verific=str(input('Deseja continuar?\n[S]-sim [N]-não')).upper().strip()[0]
    if  verific=='N': break
for c in range(0,len(listaprimaria)):
    if c%2==0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'''
Primeira lista = {sorted(listaprimaria)}
Lista par = {sorted(listapar)}
Lista impar = {sorted(listaimpar)}''')        
