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


# 1. Carrega todo o fluxo de dados para a memória de uma vez
buffer = sys.stdin.read().split()

ponteiro = iter(buffer)

# 2. Leitura da quantidade de pilhas
n_pilhas = int(next(ponteiro))
pilha = []

# 3. Construção do Prefix Sum (Somas Acumuladas) In-Place
for i in range(n_pilhas):
    valor_atual = int(next(ponteiro))
    if i > 0:
        # Soma o valor atual com o topo anterior da pilha
        pilha.append(pilha[-1] + valor_atual)
    else:
        pilha.append(valor_atual)

# 4. Leitura da quantidade de minhocas suculentas (consultas)
n_suculentas = int(next(ponteiro))

# 5. Processamento das consultas em tempo real (O(M log N))
for _ in range(n_suculentas):
    minhoca_alvo = int(next(ponteiro))
        
    # A busca binária retorna o índice (base 0), somamos 1 para a resposta (base 1)
    indice_pilha = busca_binaria(pilha, minhoca_alvo)
    print(indice_pilha + 1)
