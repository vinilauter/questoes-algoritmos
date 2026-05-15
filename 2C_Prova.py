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

def busca_linear(arr, alvo):
    for item in arr:
        if item[2] == alvo:
            return item[3]
    return -1

dados = sys.stdin.read().strip().split('\n')

n_bandas = int(dados[0].strip())
bandas = []

for i in range(1, n_bandas + 1):
    partes = dados[i].split(',')
    nome = partes[0].strip()
    tempo = int(partes[1].strip())
    bandas.append([tempo, i, nome, 0])

merge_sort(bandas)

tempo_acumulado = 0
for i in range(n_bandas):
    bandas[i][3] = tempo_acumulado
    tempo_acumulado += bandas[i][0]

linha_q = n_bandas + 1
q_consultas = int(dados[linha_q].strip())

for i in range(linha_q + 1, linha_q + 1 + q_consultas):
    alvo = dados[i].strip()
    resultado = busca_linear(bandas, alvo)
    print(resultado)