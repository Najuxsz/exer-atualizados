#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido

print("Olá! Qual tabuada você quer saber hoje?\n")

while True:
    numero = int(input("Por favor insira um número de 1 a 10 para saber a tabuada: "))
    if numero < 1 or numero > 10:
        print("Número inválido. Por favor, insira um número de 1 a 10.")
        continue
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#ok