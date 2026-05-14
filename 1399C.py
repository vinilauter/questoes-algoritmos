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

cases = int(input())

for i in range(cases):
    competidores = int(input())
    pesos = [int(x) for x in input().split()]

    merge_sort(pesos)
    
    max_pares = 0

    for S in range(2, competidores * 2 + 1):
        esq = 0
        dir = competidores - 1
        pares_atuais = 0

        while esq < dir:
            soma_atual = pesos[esq] + pesos[dir]

            if soma_atual == S:
                pares_atuais += 1
                esq += 1
                dir -= 1
            elif soma_atual < S:
                esq += 1
            else:
                dir -= 1
                
        if pares_atuais > max_pares:
            max_pares = pares_atuais

    print(max_pares)