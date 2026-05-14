//
// Created by vinni on 07/04/2026.
//

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int movimentos = 0;
    for (int i = 0; i<5; i++) {
        for (int j = 0; j<5; j++) {
            int numero;
            scanf("%d", &numero);
            if (numero == 1) {
                movimentos = abs(2 - i) + abs(2 - j);
            }
        }
    }
    printf("%d\n", movimentos);
    return 0;
}
