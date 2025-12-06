#include <stdio.h>

int main() {
    int edad Actual;
    int año Hoy;
    int año Nac;

    printf("¿Cuántos años tienes actualmente? ");
    scanf("%d", &edad Actual);

    printf("¿En qué año estamos? ");
    scanf("%d", &año Hoy);

    año Nac = año Hoy - edad Actual;

    printf("Tu año de nacimiento es: %d\n", año Nac);

    return 0;
}

