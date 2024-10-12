from random import randint
pontopositivo=pontonegativo=0
listapersonalizada=[]
listapython=['variáveis e tipos de dados', 'x = 10', 'y = 3.14', 'name = "Alice"', 'is_active = True',
'operadores aritméticos', 'a + b', 'a - b', 'a * b', 'a / b', 'a // b', 'a ** b',
'operadores de comparação', 'a == b', 'a != b', 'a > b', 'a < b', 'a >= b', 'a <= b',
'operadores lógicos', 'a and b', 'a or b', 'not a',
'operadores de atribuição', 'a = 10', 'a += 1', 'a -= 1', 'a *= 2', 'a /= 2', 'a //= 2', 'a %= 2', 'a **= 2',
'estruturas de controle', 'if', 'elif', 'else',
'loops', 'while', 'for', 'for i in range(5)', 'for fruit in fruits',
'funções', 'def', 'return',
'listas', 'fruits = ["apple", "banana", "cherry"]', 'fruits[0]', 'fruits.append("date")', 'fruits.remove("banana")', 'len(fruits)',
'tuplas', 'point = (10, 20)', 'point[0]',
'dicionários', 'person = {"name": "Alice", "age": 25}', 'person["name"]', 'person["age"] = 26', 'person.keys()', 'person.values()',
'conjuntos', 'fruits = {"apple", "banana", "cherry"}', 'fruits.add("date")', 'fruits.remove("banana")',
'compreensões', '[x**2 for x in range(10)]', '{x**2 for x in range(10)}',
'classes e objetos', 'class', '__init__', 'self', 'def greet(self)', 'p = Person("Alice", 25)', 'p.greet()',
'módulos', 'import math', 'math.sqrt(16)', 'from math import pi', 'pi',
'tratamento de exceções', 'try', 'except', 'finally',
'entrada e saída', 'input', 'print', 'with open("file.txt", "r") as file', 'content = file.read()', 'with open("file.txt", "w") as file', 'file.write("Hello, World!")'
]

print('Olá vamos começar o treino de digitação de sitax')

modo=str(input('''
Você quer seguir com as configurações padrão
ou deseja personalizar as palavras?
[A]-padrão [B]-personalizar\n''')).upper().strip()[0]

while modo!='A' and modo!='B':
    modo=str(input('''
Desculpe não consegui entender sua resposta 
escolha uma das opções:                                       
[A]-padrão [B]-personalizar\n''')).upper().strip()[0]

if modo=='B':
 print('Insira as palavras que você quer treinar, quando quiser parar de inserir palavras digite "STOP"\n')
 while True:
    palavra=str(input()).strip().upper()
    if palavra=='STOP': break
    else:
        listapersonalizada.append(palavra)

print('''Vamos começar...
-Para cada palavra digitada corrertamente você ganha um ponto positivo.
-Para cada palavra digitada errada você ganha um ponto negativo.
-Digite "STOP" para encerrar o progama''')

while True:
  if modo=='B':
   
        indicelista=randint(0,len(listapersonalizada))
        
        print(listapersonalizada[indicelista])
        palavradigitada=str(input()).upper().strip()   
        
        if palavradigitada=='STOP':
            break
        
        if  palavradigitada==listapersonalizada[indicelista].upper().strip():
            pontopositivo+=1
        else:
            pontonegativo+=1 
       
  else:
            indicelista=randint(0,len(listapython))
        
            print(listapython[indicelista])
            palavradigitada=str(input()).upper().strip()   
        
            if palavradigitada=='STOP':
                break
        
            if  palavradigitada==listapython[indicelista].upper().strip():
              pontopositivo+=1
            else:
              pontonegativo+=1
print(f''''
Treino finalizado!
Você acertou {pontopositivo} palavras. 
Você errou {pontonegativo} palavras.''')