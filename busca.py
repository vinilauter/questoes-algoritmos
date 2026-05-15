import sys

def busca_binaria(arr, alvo):
    esquerda = 0
    direita = len(arr) - 1
    melhor_resposta = -1

    while esquerda <= direita:
        meio = esquerda + (direita - esquerda) // 2  

        if arr[meio] >= alvo:
            melhor_resposta = meio
            direita = meio - 1
        else:
            esquerda = meio + 1

    return melhor_resposta