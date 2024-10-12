peso=float(input('Qual o seu peso ?\n'))
altura=float(input('Qual a sua altura ?\n'))
imc= peso/altura**2

if imc<18.5:
    print('Abaixo do peso!')
elif imc>=18.6 and imc<25:
    print('Saudável!')
elif imc>=25 and imc<30:
    print('peso em excesso!')
elif imc>=30 and imc<36:
    print('obesidade grau I!')
elif imc>=35 and imc>40:
    print('obesidade grau II!')
else: 
    print('obesidade grau III!')
    