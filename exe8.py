#8. Faça um algoritmo que leia um número positivo e imprima seus divisores.

#tentando com o while
while True:
    numero = float(input("Olá, digite um número positivo!!:  "))
    if numero < 0:
        print("NÚMERO INVÁLIDO, tente novamente")
        continue
    elif numero == 0:
        print("O número zero não possui divisores.")
    else:
        print(f"Os divisores do número {numero} são:")
        divisor = 1
        while divisor <= numero:
            if numero%divisor == 0:
                print(divisor)
            divisor += 1


#achei mais fácil com o while
#ok

