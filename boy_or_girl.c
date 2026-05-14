#include <stdio.h>

int main(void) {
    char username[101];
    int registro[256] = {0};
    int contador = 0;

    scanf("%s", username);

    for (int i = 0; username[i] != '\0'; i++) {
        char atual = username[i];
        if (registro[atual] == 0 ) {
            registro[atual] = 1;
            contador++;
        }
    }

    if (contador % 2 !=0) {
        printf("IGNORE HIM!");
    }
    else {
        printf("CHAT WITH HER!");
    }
}