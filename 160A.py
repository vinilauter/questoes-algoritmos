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

n_moedas = int(next(ponteiro))

moedas = []

for i in range(n_moedas):
    moedas.append(int(next(ponteiro)))

merge_sort(moedas)

total = sum(moedas)

minha_soma = 0

i = 0

while minha_soma <= total // 2:
    i += 1

    minha_soma += moedas[-i]

print(i)