listadevalores=[]
pares=soma=maior=0
for p in range(0,3):
    for c in range(0,3):
        print(f'Insira o valor da fileira ({p}, {c})',end='')
        listadevalores.append(int(input()))
for c in listadevalores:
    if c%2==0:
        pares+=c
if listadevalores[3]>listadevalores[4] and listadevalores[3]>listadevalores[5]:
    maior=listadevalores[3]
elif listadevalores[4]>listadevalores[3]and listadevalores[4]>listadevalores[5]:
    maior=listadevalores[4]
else:
    maior=listadevalores[5]

soma=listadevalores[2]+listadevalores[5]+listadevalores[8]        


print(f'''
[{listadevalores[0]}][{listadevalores[1]}][{listadevalores[2]}]
[{listadevalores[3]}][{listadevalores[4]}][{listadevalores[5]}]
[{listadevalores[6]}][{listadevalores[7]}][{listadevalores[8]}]
''')
print(f'''
Soma dos pares ={pares}
Soma da terceira coluna={soma}
Maior da segunda linha={maior} 
''')        