# Declaração das listas usadas.
geral=[]
notas=[]
# Estrutura para receber e salvar os dados(Nome, Notas e Média) na lista geral. 
while True:
    nome=str(input('Nome:'))
    
    notas.append(float(input('Nota 1:')))
    notas.append(float(input('Nota 2:')))
    # Utilizando os elementos da lista notas para calcular a média do aluno.
    media=(notas[0]+notas[1])/2
    # Salvando as informações na lista geral a varíavel nome a lista com as duas 
    # notas e por fim a vaíavel média.
    geral.append([nome,notas[:],media])
    # Resetando a lista de  notas para que não interfira no próximo processo. 
    notas.clear()
    # verificação para saber se o user quer incerir mais alunos.
    verific=str(input('Deseja inserir mais alunos?  [S/N]  ')).upper().strip()[0]
    if verific=='N': break
# Exibindo a tabela de indice nome e média do aluno(Salva na lista geral).  
print(f'''
{'No.':<4} {'NOME':<10}     {'MÉDIA':>8}
{30*'--'}''')
for c in range(0,len(geral)):
    print(f'''{c:<4} {geral[c][0]:<10}     {geral[c][2]:>8}
{30*'--'}''')
# Exibindo a nota individual de cada aluno conforme e solicitado pelo user.
while True:
    
    verificNotas=int(input('''
Digite o Número do aluno que 
deseja ver a nota, 999 encerrara o sistema!
No.:'''))
    
    if verificNotas==999:break
    else:
        print(f'''
As notas de {geral[verificNotas][0]} são {geral[verificNotas][1]}
{30*'--'}''')