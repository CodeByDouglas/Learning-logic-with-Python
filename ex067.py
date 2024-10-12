while True:
    n=int(input('Incira um número:\n'))
    if n<0:
     break
    for c in range(1,11):
        print(f'{c}x{n}={c*n}')
        