soma= c= n= 0
while True:
    n=int(input('incira um número:\n'))
    if n==999:
        break
    soma+=n
    c+=1
print(f'Foram digitados {c} e a soma entre eles é {soma}')
