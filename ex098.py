from time import sleep

def contador(inc, fin, pss):
    if pss<0: pss=abs(pss)
    elif pss==0: pss+=1
    
    print(f'''
{20*'--'}
Contagem de {inc} até {fin} de {pss} em {pss}
{20*'--'}''')
    if inc<fin:
         
        for x in range(inc, fin+1, pss):
            print(x,'',end='',flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        
        for x in range(inc, fin-1, -pss):
            print(x,'',end='',flush=True)
            sleep(0.5)         
        print('FIM!')



contador(inc=1, fin=10, pss=1)
contador(inc=10, fin=0, pss=2)

print('Agora e sua vez escolha!')
i=int(input('INICIO: '))
f=int(input('FINAL: '))
p=int(input('INTERVALO: '))

contador(i, f , p)