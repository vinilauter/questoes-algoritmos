//
// Created by vinni on 09/04/2026.
//

#include <stdio.h>

int main(void){

    int n_matrix = 0;

    scanf("%d", &n_matrix);

    int matrix[n_matrix][n_matrix];

    for (int i = 0; i<n_matrix; i++){

        matrix[i][0] = 1;
    }

    for (int j = 0; j<n_matrix; j++){

        matrix[0][j] = 1;
    }

    for (int i = 1; i < n_matrix; i++) {
        for (int j = 1; j < n_matrix; j++) {
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
        }
    }

    printf("%d\n", matrix[n_matrix-1][n_matrix-1]);

    return 0;

}