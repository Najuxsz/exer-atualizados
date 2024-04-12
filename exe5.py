#5 Ler 10 números e imprimir quantos são pares e quantos são ímpares.

contador = 0
qntd_par = 0
qntd_impar = 0

while contador < 10:
    numero = int(input(f"Olá, insira o {contador + 1}º número!"))
    contador +=1
    if numero%2 == 0:
        print(f"{numero} é par!!")
        qntd_par +=1
    else:
        print(f"({numero}) não é par.")
        qntd_impar +=1
        if numero < 0:  #parte opicional, não sabia se deixava o programa rodar com ou sem numero negativo
            print("Número invalido. Encerrando!")
        break
        

print(f"A quantidade de numeros pares digitados foram: {qntd_par}")
print(f"A quantidade de numeros pares digitados foram: {qntd_impar}")


#ok