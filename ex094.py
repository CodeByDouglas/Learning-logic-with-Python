pessoa={}
bddpessoas=[]
mulheres=[]
idadeacimadamedia=[]
totidade=0

while True:
    pessoa['nome']=str(input('Insira o nome da pessoa: '))
    pessoa['sexo']=str(input('Insira o sexo da pessoa: ')).upper().strip()[0]
    pessoa['idade']=int(input('Insira a idade da pessoa: '))
    totidade+=pessoa['idade']
    bddpessoas.append(pessoa.copy())
    pessoa.clear()
    
    verific=''
    while verific!='S' and verific!='N':
        verific=str(input('Deseja inserir outra pessoa? [S/N] ')).upper().strip()[0]
    if verific=='N':break

med=totidade/len(bddpessoas)

for x in bddpessoas:
    if x['sexo']=='F':
        mulheres.append(x['nome'])
    
    if x['idade']>med:
        idadeacimadamedia.append(x['nome'])

print(f'''
Quantidade de pessoas: {len(bddpessoas)}
Média do grupo: {med}
Lista de mulheres: {mulheres}
Pesssoas com idade acima da média: {idadeacimadamedia}''')



