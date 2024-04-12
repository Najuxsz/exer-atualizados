#9. Faça um algoritmo que leia 10 números inteiros, armazene-os em uma lista e imprima em ordem crescente.

lista_numeros = []
contador = 0 

while contador < 10:
    numero = int(input(f"Olá, insira o {contador + 1}º número!"))
    contador +=1
    lista_numeros.append(numero)

print("Os números digitados foram:", sorted(lista_numeros))

#ok
