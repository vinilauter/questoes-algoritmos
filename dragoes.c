#include <stdio.h>
#include <stdlib.h> // Biblioteca necessária para ter acesso à função qsort()

int forca_dragao[1000];
int bonus_vitoria[1000];


int compare_indices(const void *a, const void *b) {
    int indice_A = *(const int *)a;
    int indice_B = *(const int *)b;

    int forca_A = forca_dragao[indice_A];
    int forca_B = forca_dragao[indice_B];

    if (forca_A < forca_B) return -1;
    if (forca_A > forca_B) return 1;
    return 0; // Empate
}

int main(void) {
    int forca_kirito;
    int numero_dragoes;

    scanf("%d %d", &forca_kirito, &numero_dragoes);

    for (int i = 0; i < numero_dragoes; i++) {
        scanf("%d %d", &forca_dragao[i], &bonus_vitoria[i]);
    }

    int ordem[1000];
    for (int i = 0; i < numero_dragoes; i++) {
        ordem[i] = i;
    }

    qsort(ordem, numero_dragoes, sizeof(int), compare_indices);


    for (int i = 0; i < numero_dragoes; i++) {
        int dragao_atual = ordem[i];


        if (forca_kirito > forca_dragao[dragao_atual]) {
            forca_kirito += bonus_vitoria[dragao_atual];
        } else {
            printf("NO\n");
            return 0;
        }
    }

    printf("YES\n");
    return 0;
}