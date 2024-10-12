salario=float(0)
salario=float(input("Digite o valor do seu sálario:"))
if salario>1 and salario<=2259.20 :
    print("isento")
 

if salario<2259.20 :  print("isento")

if salario>2259.21 and salario<=2828.65 :  print("Você pagara {}".format(salario*0.075))

if salario>=2825.66 and salario<=3751.05 :  print("Você pagara {}".format(salario*0.15))

if salario>=3751.06 and salario<=4664.68 :  print("Você pagara {}".format(salario*0.225))

if salario>4664.68 :  print("Você pagara {}".format(salario*0.275))






