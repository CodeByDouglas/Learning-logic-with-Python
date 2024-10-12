Valor=float(input('Qual o valor do produto?\n'))
fp=str(input('qual o metodo de pagamento?\ndinheiro, cheque ou cartão : ')).strip().upper()
if fp=='CARTÃO':
  cartao=str(input('débito ou crédito?\n')).strip().upper()
  if cartao=='CRÉDITO':
     parcela=int(input('\nQuantas vezes deseja parcelar?\n'))

if (fp == 'DINHEIRO')or(fp=='CHEQUE'):
    desconto=float(Valor*0.1)
    print('Você recebera um desconto de 10% , o produto vai sair por {}R$'.format(Valor-desconto))
elif cartao=='DÉBITO':
    desconto=float(Valor*0.05)
    print('Você recebera um desconto de 5%, o produto vai sair por {}R$'.format(Valor-desconto))
elif (cartao=='CRÉDITO')and(parcela<=2):
    print('O produto vai sair no preço normal , por {}R$'.format(Valor))
else:
    acrecimo=Valor*0.2
    print('Você tera um acrecimo de 20%, sua compra ficara {}R$'.format(Valor+acrecimo))