#include <stdio.h>

int main() {
    int n1, n2, n3;

    printf("Operacion: x + y - z\n");

    printf("Introduce el valor de x: ");
    scanf("%d", &n1);

    printf("Introduce el valor de y: ");
    scanf("%d", &n2);

    printf("Introduce el valor de z: ");
    scanf("%d", &n3);

    int resultado = n1 + n2 - n3;

    printf("El resultado obtenido es: %d\n", resultado);

    return 0;
}
