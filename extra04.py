listadetexto=[]
frequencia=[]
for c in range(5):
 listadetexto.append(str(input()))
for c in listadetexto:
 if c not in frequencia:
  frequencia.append(c)
  print(c,'=',listadetexto.count(c))
