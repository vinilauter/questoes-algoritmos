//
// Created by vinni on 10/04/2026.
//
// Lógica: pegar n_pilhas -> pegar via calloc o número em cada pilha -> pegar número minhocas suculentas
// -> pegar onde estão as suculentas -> fazer busca binária para cada minhoca suculenta -> imprimir a pilha respectiva
//
#include <stdio.h>
#include <stdlib.h>

int busca_binaria (int arr[], int n, int alvo) {
    int esquerda = 0;
    int direita = n - 1;
    int melhor_resposta = -1;

    while (esquerda <= direita) {
        int meio = esquerda + (direita - esquerda)/2;

        if (arr[meio] >= alvo) {
            melhor_resposta = meio;
            direita = meio - 1;
        } else {
            esquerda = meio + 1;
        }
    }

    return melhor_resposta;
}

int main() {
    int n_pilhas = 0;
    int n_suculentas = 0;

    scanf("%d", &n_pilhas);

    int *pilha = (int*) calloc(n_pilhas, sizeof(int));

    for (int i = 0; i < n_pilhas; i++) {
        scanf("%d", &pilha[i]);
        if (i>0) {
            pilha[i]+=pilha[i-1];
        }
    }

    scanf ("%d", &n_suculentas);

    int *loc_suculentas = (int*) calloc(n_suculentas, sizeof(int));

    for (int i = 0; i < n_suculentas; i++) {
        scanf("%d", &loc_suculentas[i]);
    }

    for (int i = 0; i < n_suculentas; i++) {
        int suculenta = busca_binaria(pilha, n_pilhas, loc_suculentas[i]);
        printf("%d\n", suculenta+1);
    }

    return 0;
}
