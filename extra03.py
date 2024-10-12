listaresult=['KM','HM','DAM','M','DM','CM','MM']
medida=converçao=''

numero=float(input('Insira um número:\n'))

while medida not in listaresult:
    medida=str(input('''
Qual a medida do seu número?
[kM]-Kilometros
[HM]-Hectómetro                 
[DAM]-Decametro
[M]-Metros
[DM]-Decimetro
[CM]-Centimetro
[MM]-Milimetros

''')).upper().strip()

while converçao not in listaresult:    
    converçao=str(input('''
Para qual medida deseja converter?
[kM]-Kilometros
[HM]-Hectómetro                 
[DAM]-Decametro
[M]-Metros
[DM]-Decimetro
[CM]-Centimetro
[MM]-Milimetros

''')).upper().strip()

print(f'''{numero}{medida}=''',end='')

if listaresult.index(medida)<listaresult.index(converçao):
    for c in range(listaresult.index(medida),listaresult.index(converçao)):
        numero*=10

elif listaresult.index(medida)>listaresult.index(converçao):
        for c in range(listaresult.index(medida),listaresult.index(converçao)):
         numero/=10

print(f'{numero}{converçao}')