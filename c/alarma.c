#include <stdio.h>

int main() {
    float v;

    printf("Voltaje detectado en el sistema: ");
    scanf("%f", &v);

    if (v < 220.0f || v > 240.0f) {
        printf("Advertencia: El voltaje no está dentro del rango permitido.\n");
    } else {
        printf(" El voltaje es adecuado, todo en orden.\n");
    }

    return 0;
}