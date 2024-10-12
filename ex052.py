n=int(input('Insira um número:\n'))

if n<=1:
    print('Esse número não e prímo!')
else:
 p=str('é primo')
 
 for c in range(2, int(n**0.5)+1):
    if n%c==0:
        p=str('não é prímo')
 
 print('O número digitado {} '.format(p))        
    
    