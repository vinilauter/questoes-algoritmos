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

n_lojas = int(input())

buffer = sys.stdin.read().split()

ponteiro = iter(buffer)

gasto_a = 0
gasto_b = 0
gasto_c = 0
gasto_d = 0

for i in range(n_lojas):
    n_compras = int(next(ponteiro))

    itens = []

    for i in range(n_compras):

        itens.append(int(next(ponteiro)))

    merge_sort(itens)

    n_itens = len(itens)

    gasto_a += itens[-1]
    gasto_b += itens[n_itens//2]
    gasto_c += itens[n_itens//2]
    gasto_d += itens[0]

print(f"{gasto_a} {gasto_b} {gasto_c} {gasto_d}")