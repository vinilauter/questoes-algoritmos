//
// Created by vinni on 13/04/2026.
//
// Lógica: Recebe k unidade de centímetros que precisa crescer -> recebe o crescimento de cada mês -> ordena o crescimento
// -> soma até dar o k -> imprime a quantidade de mêses pra regar
//

#include <stdio.h>
#include <stdlib.h>

int compara_numeros(const void *a, const void *b) {
    int valor_a = *(const int *)a;
    int valor_b = *(const int *)b;

    return valor_b - valor_a;

}

int main() {

    int meta_crescimento = 0;

    scanf("%d", &meta_crescimento);

    int meses[12];

    for (int i=0; i<12; i++) {
        scanf("%d", &meses[i]);
    }

    qsort(meses, 12, sizeof(int), compara_numeros);

    int total_acumulado = 0;
    int contador_meses = 0;

    while (meta_crescimento > total_acumulado && contador_meses < 12) {
        total_acumulado+=meses[contador_meses];
        contador_meses++;
    }

    if (total_acumulado >= meta_crescimento) {
        printf("%d\n", contador_meses);
    } else {
        printf("-1\n");
    }

    return 0;

}