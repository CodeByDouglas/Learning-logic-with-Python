vph=float(input("Inssira o valor da sua hora:"))
hm=float(input("inssira a suas horas trabalhadas:"))
sb= hm*vph
inss= sb*0.08
sdct=sb*0.05
ir=sb*0.11
sl=sb-(inss+sdct+ir)
print("O salario bruto é : {}\n O valor pago ao INSS foi de : {} \n Valor pago ao sindicato:{} \n O sálario liquido foi de {}".format(sb,inss,sdct,sl))
