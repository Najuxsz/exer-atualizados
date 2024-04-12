#Fazer um programa para encontrar todos os números pares entre 1 e 100.

numeros = 0

while numeros < 101:
    if numeros%2 == 0:
        print(f"{numeros} é par!")
    else:
        print(f"Ops, ({numeros}) não é par.")
    numeros += 1


#agora vamos fazer isso com o FOR

for numero in range(1,101):
    if numero%2 == 0:
        print(f"{numero} é par!!")
    else:
        print(f"({numero}) não é par.")
    numero += 1


#ok