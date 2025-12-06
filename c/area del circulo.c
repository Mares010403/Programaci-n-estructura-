#include <stdio.h>

int main() {
    float piValor, radio, areaCirculo;

    printf("Valor de pi: ");
    scanf("%f", &piValor);

    printf("Ingresa el radio del círculo: ");
    scanf("%f", &radio);

    areaCirculo = piValor * (radio * radio);

    printf("El área del círculo es: %.2f\n", areaCirculo);

    return 0;
}
