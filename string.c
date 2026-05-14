#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    char entrada[101];

    fgets(entrada, 101, stdin);

    entrada[strcspn(entrada, "\n")] = 0;

    for (int i = 0; entrada[i] != '\0'; i++) {
        char atual = tolower(entrada[i]);
        if (atual != 'y' && atual != 'a' && atual != 'e' && atual != 'i' && atual != 'o' && atual != 'u') {
            printf(".%c",atual);
        }
    }
}
