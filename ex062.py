inicial=float(input('Qual o inicio da seua PA?\n'))
razao=float(input('Qual a razão da sua PA?\n'))
contaador=0
limt=10
while contaador<=limt:
    contaador+=1
    print(inicial)
    inicial+=razao
    if contaador==limt:
     quant=float(input('Mais quantos termos você deseja ver ?'))
     limt+=quant
     if quant==0:
        contaador+=1
    
    