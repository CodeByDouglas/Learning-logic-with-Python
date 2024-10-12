from math import sqrt

equação=str(input('Isira uma equação de segundo grau: '))
stop=na=nb=nc=0
a=b=c=''

if equação[0]=='-':
   stop=-1
for v in equação:
    if v =='+'or v=='-':
     stop+=1
    
    if stop==0:
       if v=='x':
          na+=1
       if na==0:
          a+=v        
    
    elif stop==1:
       if v=='x':
          nb+=1
       if nb==0:
          b+=v
            
    elif stop==2:
       if v=='=':
          nc+=1
       if nc==0:
          c+=v
       
aint=int(a)
bint=int(b)
cint=int(c)

delta= (bint**2)-(4*aint*cint)

if delta>0:
    
    if delta.is_integer():
        resultA= (-bint+sqrt(delta))/(2*aint)
        resultB= (-bint-sqrt(delta))/(2*aint)
        print(f'X1={resultA}')
        print(f'X2={resultB}')

    else:   
     print('''Não e possível tirar raiz exata de delta!''')

else:   
     print('''Não e possível tirar raiz  de delta pois e uma número negativo!''')