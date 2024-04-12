#7. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

num_par = []
soma_pares = 0

for i in range(0,101):
    if i %2==0:
        num_par.append(i)
        soma_pares = num_par+i
        print(f"A soma dos 50 primeiros números pares são: {soma_pares}")

        

#Calcule a soma dos 105 primeiros numeros pares
#esse segundo foi feito com o professor 

cont_pares = 0
soma_pares = 0
num = 0
while cont_pares < 105:
    
    if num %2==0:
        cont_pares+=1
        soma_pares = soma_pares + num
        print(f"o número {num} é par")
    num+=1

print("A soma dos pares são", soma_pares)

#ok