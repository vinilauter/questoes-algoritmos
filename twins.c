//
// Created by vinni on 10/04/
//
// Lógica: Entrada -> Alocar -> Somar Tudo -> Ordenar -> Iterar Somando -> Printar -> Free
//

#include <stdio.h>
#include <stdlib.h>

int comparar_num(const void *a, const void *b) {
    int valor_a = *(const int *)a;
    int valor_b = *(const int*)b;

    return valor_b - valor_a; // b antes, pois vai ser decrescente
}

int main() {

    int n_moedas;
    int soma_total = 0;
    int valor_pego = 0;
    int indice_saco = 0;

    scanf("%d", &n_moedas);

    int *moedas = calloc(n_moedas, sizeof(int));

    for (int i = 0; i<n_moedas; i++) {
        scanf("%d", &moedas[i]);
        soma_total += moedas[i];
    }

    qsort(moedas, n_moedas, sizeof(int), comparar_num);

    while (valor_pego <= soma_total/2) {
        valor_pego += moedas[indice_saco];
        indice_saco++;
    }

    printf("%d", indice_saco);

    free(moedas);

    return 0;

}