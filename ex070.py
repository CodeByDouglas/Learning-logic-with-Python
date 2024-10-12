gastototal=produtomaisdemil=menorpreço=0
menorproduto=[]

while True:
    produto=str(input('Insira o nome do produto:'))
    preço=float(input('Qual o valor do produto:'))
    
    gastototal+=preço
    
    if preço>1000:
        produtomaisdemil+=1
   
    if menorpreço==0:
        menorpreço=preço
    if preço<menorpreço:
        menorpreço=preço
        menorproduto.clear()
        menorproduto.append(produto)
    elif preço==menorpreço:
        menorproduto.append(produto)
     

    verificaçao=str(input('Deseja inserir mais produtos a esta compra?\n[S]|[N]\n')).upper().strip()[0]
    while verificaçao!='S' and verificaçao!='N':
        verificaçao=str(input('Resposta invalida, insira uma nova resposta:\n[S]|[N]\n ')).upper().strip()[0]
    if verificaçao=='N':
        break    
print('''DADOS DA COMPRA 
      Produtos com valor acima de R$1000 - {}
      Produto mais barato - {}
      Total gasto = {}'''.format(produtomaisdemil,menorproduto,gastototal))