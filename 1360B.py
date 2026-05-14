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

n_cases = int(input())
for i in range(n_cases):
    n_atletas = int(input())
    forcas = [int(x) for x in input().split()]

    forcas_ordenadas = merge_sort(forcas)

    menor_diferenca = float('inf')

    for i in range(1, n_atletas):
        dif_atual = forcas[i] - forcas[i-1]
        if dif_atual < menor_diferenca:
            menor_diferenca = dif_atual
        i += 1
    
    print(menor_diferenca)
