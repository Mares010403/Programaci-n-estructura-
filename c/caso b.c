#include <stdio.h>

int main() {
    int n1, n2, n3, n5;
    float n4;

    printf("Evaluar expresion: a + (b * c) - (d / e)\n");

    printf("Ingresa el valor de a: ");
    scanf("%d", &n1);

    printf("Ingresa el valor de b: ");
    scanf("%d", &n2);

    printf("Ingresa el valor de c: ");
    scanf("%d", &n3);

    printf("Ingresa el valor de d: ");
    scanf("%f", &n4);

    printf("Ingresa el valor de e: ");
    scanf("%d", &n5);

    float resultado = n1 + (n2 * n3) - (n4 / n5);

    printf("Resultado final = %.2f\n", resultado);

    return 0;
}