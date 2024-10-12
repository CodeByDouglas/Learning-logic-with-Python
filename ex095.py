entrada={}
golspt=[] 
jogadores=[]


while True:
    
    entrada['nome']=str(input('Nome do jogador: '))
    entrada['quantpartidas']=int(input('Quantas partidas ele jogou: '))
    
    for x in range(0,entrada['quantpartidas']):

        golspt.append(int(input((f'Quantos gols ele fez na {x+1}° partida: '))))
    
    entrada['golsporpartida']=golspt[:]
    entrada['totaldegols']=sum(golspt)

    jogadores.append(entrada.copy())
    entrada.clear()
    golspt.clear()
    totGOLS=0
    
    verific=''
    while verific!='N' and verific!='S':
        verific=str(input('Deseja inserir outro jogador? [S/N]  ')).upper().strip()[0]
    if verific=='N': break    



print(f'''
COD {'':>{10}}{'NOME'}{'':>{10}}{'GOLS'}{'':>{10}}{'TOTAL'}
{30*'--'}''')
for x in range(0,len(jogadores)):
    print(f'''
{x} {'':>{10}}{jogadores[x]["nome"]}{'':>{10}}{jogadores[x]["golsporpartida"]}{'':>{10}}{jogadores[x]["totaldegols"]}
{30*'--'}''')

while True:
    verific=int(input('Deseja mostrar os dados de qual jogador? '))
    if verific==999:
        break
    
    elif verific>len(jogadores):
        print('Esse código e inválido, insira em código válido!')
    
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[verific]['nome']}:')
        
        for x in range(0,len(jogadores[verific]['golsporpartida'])):
            print(f'No {x+1}° jogo fez {jogadores[verific]['golsporpartida'][x]}')
