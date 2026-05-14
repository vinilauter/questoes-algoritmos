//
// Created by vinni on 13/04/2026.
//
// Lógica: recebe n e m tamanhos dos arrays -> calloc e recebe array 1 -> calloc e recebe array 2 -> ordenar array 1 ->
// varrer array 2 e ver quanto elementos são maiores ou iguais a array 2
//

#include <stdio.h>
#include <stdlib.h>

int compara_numeros(const void *a, const void *b) {
    int valor_a = *(const int*)a;
    int valor_b = *(const int*)b;

    return valor_a - valor_b;
}

int busca_binaria_indice (int arr[], int n, int alvo) {
    int esquerda = 0;
    int direita = n - 1;
    int melhor_resposta = n;

    while (esquerda <= direita) {
        int meio = esquerda + (direita - esquerda)/2;

        if (arr[meio] > alvo) {
            melhor_resposta = meio;
            direita = meio - 1;
        } else {
            esquerda = meio + 1;
        }
    }

    return melhor_resposta;
}

int main() {

    int tam_arr1 = 0;
    int tam_arr2 = 0;

    scanf("%d", &tam_arr1);

    int *arr1 = (int*) calloc(tam_arr1, sizeof(int));

    scanf("%d", &tam_arr2);

    int *arr2 = (int*) calloc(tam_arr2, sizeof(int));

    for (int i = 0; i < tam_arr1; i++) {
        scanf ("%d", &arr1[i]);
    }

    for (int i = 0; i < tam_arr2; i++) {
        scanf ("%d", &arr2[i]);
    }

    qsort(arr1, tam_arr1, sizeof(int), compara_numeros);

    for (int i = 0; i < tam_arr2; i++) {
        int n_iguais_ou_menores = busca_binaria_indice(arr1, tam_arr1, arr2[i]);
        printf("%d ", n_iguais_ou_menores);
    }

    return 0;
}