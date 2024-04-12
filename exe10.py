#10. Dada a lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete mais vezes.

lista = [2,3,2,5,4,3,7,2,9,4,1,4]

num_repetido = 0
freq_num = 0 

for num in lista:
    if lista.count(num) > freq_num:
        freq_num = lista.count(num)
        num_repetido = num
        print(f"O numero mais repetido foi o número {num_repetido}, ele repetiu {freq_num} vezes")


#ok