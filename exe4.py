#Leia várias idades e calcule a média entre as idades (usar uma variável para idade).

soma_idades = 0
idades_digitadas =[]

while True:
    idades = int(input("Olá, digite uma idade aqui! (números negativos encerram o programa!) "))
    if idades < 0:
        break
    else:
        idades_digitadas.append(idades)
    if len(idades_digitadas) > 0:
        soma_idades = idades + soma_idades
        media_idades = soma_idades / len(idades_digitadas)
    

print("As idades digitadas foram", idades_digitadas)
print("A média das idades é:", media_idades)

#ok