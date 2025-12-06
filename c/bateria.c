#include <stdio.h>

int main() {
    float vBat;

    printf("Voltaje registrado en la batería: ");
    scanf("%f", &vBat);

    if (vBat < 11.0) {
        printf("Estado: Nivel bajo.\n");
    } 
    else if (vBat > 12.6) {
        printf("Estado: Posible sobrecarga.\n");
    } 
    else {
        printf("Estado: Funcionamiento adecuado.\n");
    }

    return 0;
}
