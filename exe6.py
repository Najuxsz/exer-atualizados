#Utilizando a estrutura de repetição for, faça um programa que receba 10 números
#quais deles estão no intervalo [10,20] 
#quais deles estão fora do intervalo.

numeros = []
numeros_intervalo = 0

for i in range(10):
    numero = int(input("Olá, digite um número aqui! "))
    numeros.append(i)
    if numero <= 10 or numero <= 20:
        print(f"Esse número ({numero}) está no intervalo [10,20]")
    else:
        print("Esse número não está no intervalo")

#ok