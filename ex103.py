def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez um total de {gols} gols no campeonato! ')

n=str(input('Insira o n do jogador: '))
g=str(input('Insira a quantidade de gols: '))

if g.isnumeric():
    g=int(g)
else:
    g=0

if n=='':
    ficha(gols=g)
else:
    ficha(n,g)
