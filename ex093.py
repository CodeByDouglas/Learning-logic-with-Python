aproveitamento={}
golsporpt=[]
totgols=0
aproveitamento['nome']=str(input('Nome do jogador: '))
aproveitamento['quantpartidas']=int(input('Quantas partidas ele jogou: '))

for c in range(0,aproveitamento['quantpartidas']):
    print(f'Quantos gols ele marcou na partida {c+1}: ',end='')
    golsporpt.append(int(input()))    

aproveitamento['golspotpt']=golsporpt.copy()
totgols=sum(aproveitamento['golspotpt'])

print(f'O jogador {aproveitamento["nome"]} jogou {aproveitamento["quantpartidas"]} partidas.')
for p, g in enumerate(aproveitamento['golspotpt']):
    print(f'=> Na {p+1}° partida , fez {g} gols.')
print(f'Foi um total de {totgols} gols.') 