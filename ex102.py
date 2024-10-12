def calcult_fatorial(num,show=False):
    fatorial=1
    for x in range(num, 0, -1):
        fatorial*=x
        if show==True:
            if x>1:
                print(f'{x}*',end='')
            else:
                print(f'{x}=',end='')
    print(f'{fatorial}')        
            
a = calcult_fatorial(5,False)