maiordeidade=contmasculino=mulhermenosde20=0

while True:
    sexo=str(input('Qual o seu sexo?\n')).upper().strip()[0]
    while sexo!='M'and sexo!='F':
       sexo=str(input('Sexo ínvalido, insira novamente!\n')).upper().strip()[0]
    
    idade=int(input('Qual a sua idade?\n'))
    
    if idade>18:
       maiordeidade+=1
    if sexo=='M':
       contmasculino+=1
    if sexo=='F'and idade<20:   
     mulhermenosde20+=1
    
    verific=str(input('Deseja prosseguir?\n[S]|[N]\n')).upper().strip()[0]
    while verific!='S'and verific!='N':
     verific=str(input('Resposta invalida, insira novamente\n[S]|[N]\n' )).upper().strip()[0]

    if verific=='N':
        break 
print(f'''Neste grupo posuem:
      {maiordeidade} Pessoas maiores de idade!
      {contmasculino} Homens!
      {mulhermenosde20} Mulheres com menos de 20 anos de idade!''')
       