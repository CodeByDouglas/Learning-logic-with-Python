mediaalunos={}
mediaalunos['Nome']=str(input('Nome:'))
mediaalunos['Média']=float(input('Média:'))

if mediaalunos['Média']>=7:
    mediaalunos['Situação']='aprovado'
else:
    mediaalunos['Situação']='reprovado'    
print(f'''
Nomes: {mediaalunos['Nome']}
Médias: {mediaalunos['Média']} 
Situação: {mediaalunos['Situação']}
''')
