matrix=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c]=(int(input(f'Insira o valor da fileira ({l}, {c}): ')))
for l in range(0,3):
    for c in range(0,3):
            print(f'[{matrix[l][c]}]',end='')
    print()