import sys

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]
    
        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1
        
        if i < len(esquerda):
            arr[k:] = esquerda[i:]
        if j < len(direita):
            arr[k:] = direita[j:]
    
    return arr

buffer = sys.stdin.read().split()

ponteiro = iter(buffer)

qnt_pedras = int(next(ponteiro))

custos = []

for i in range(qnt_pedras):
    custos.append(int(next(ponteiro)))

soma_original = [0]

for custo in custos:
    soma_atual = soma_original[-1] + custo
    soma_original.append(soma_atual)

custos_ordenados = merge_sort(custos[:])

soma_ordenada = [0]

for custo in custos_ordenados:
    soma_atual = soma_ordenada[-1] + custo
    soma_ordenada.append(soma_atual)

qnt_requests = int(next(ponteiro))

for i in range(qnt_requests):
    tipo = int(next(ponteiro))
    inicio = int(next(ponteiro))
    fim = int(next(ponteiro))

    if tipo == 1:
        resultado = soma_original[fim] - soma_original[inicio - 1]
    if tipo == 2:
        resultado = soma_ordenada[fim] - soma_ordenada[inicio - 1]
    
    print(resultado)