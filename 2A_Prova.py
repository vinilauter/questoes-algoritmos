import sys

def busca_binaria(arr, alvo):
    esquerda = 0
    direita = len(arr) - 1

    while esquerda <= direita:
        meio = esquerda + (direita - esquerda) // 2  

        if arr[meio] == alvo:
            return meio + 1
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

buffer = sys.stdin.read().split()

ponteiro = iter(buffer)

n_cadastrados = int(next(ponteiro))
cadastrados = []

for i in range(n_cadastrados):
    cadastrados.append(int(next(ponteiro)))

n_consultas = int(next(ponteiro))

for i in range(n_consultas):
    alvo = int(next(ponteiro))
    resultado = busca_binaria(cadastrados, alvo)
    print(resultado)