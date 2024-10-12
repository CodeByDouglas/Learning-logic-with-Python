print('Olá\n')
vi = float(input('Qual o valor do imóvel que você deseja adquirir?\n'))
s = float(input('\nQuanto você recebe por mês?\n'))
ta = int(input('\nEm quanto tempo você pretende pagar o imóvel ?\n'))

parcela = vi/(ta*12)

if (s*0.3)>parcela:
    print('Compra aprovada, as parcelas do seu imóvel vao ficar {:.2f}'.format(parcela))
else:
    print('Compra negada, as pareclas exedem mais de (30%) da sua renda atual')