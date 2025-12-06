#include <stdio.h>

int main() {
    float tempC, tempF;

    printf("Introduce la temperatura en grados Celsius: ");
    scanf("%f", &tempC);

    tempF = (tempC * 1.8) + 32;

    printf("Temperatura en Fahrenheit: %.2f\n", tempF);

    return 0;
}