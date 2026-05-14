tam_arr, queries = map(int, input().split())

array = [int(x) for x in input().split()]

contador = 0

for i in range(tam_arr):
    if array[i] == 1:
        contador += 1

for i in range(queries):
    tipo, valor = map(int, input().split())
    if tipo == 1:
        indice = valor - 1
        if array[indice] == 1:
            array[indice] = 0
            if contador != 0:
                contador -= 1
        else:
            array[indice] = 1
            contador += 1
    elif tipo == 2:
        if valor > contador:
            print(0)
        else:
            print(1)