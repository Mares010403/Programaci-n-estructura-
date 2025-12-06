#include <stdio.h>

int main() {
    float I, V;

    // Solicitud de datos al usuario
    printf("Introduce el valor de la corriente (A): ");
    scanf("%f", &I);

    printf("Introduce el valor del voltaje (V): ");
    scanf("%f", &V);

    // Evaluación de condiciones del sistema
    if (I > 3.0 && V < 1.0) {
        printf("Advertencia: posible cortocircuito detectado.\n");
    } else {
        printf("Estado: todo dentro de los parámetros normales.\n");
    }

    return 0;
}