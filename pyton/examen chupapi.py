#include <stdio.h>

int main() {
    int n1, n2, n3, n4, n5, n6, n7;  
    float prima = 10000;

    printf("Ingrese tu edad: ");
    scanf("%d", &n1);

    if (n1 > 21) {
       
        printf("Tipo de vehiculo (1 = Deportivo, 0 = Otro): ");
        scanf("%d", &n2);

        if (n2 > 3) {  
            printf("Años sin accidentes: ");
            scanf("%d", &n4);

            if (n4 > 2) {
                prima = prima - (prima * 0.15); 
                printf("Tu monto es: %.2f\n", prima);
            } else {
                printf("Tu monto es: %.2f\n", prima);
            }
        } else {
            printf("Años sin accidentes: ");
            scanf("%d", &n5);

            if (n5 > 2) {
                prima = prima - (prima * 0.15); 
                printf("Tu monto es: %.2f\n", prima);
            } else {
                printf("Tu monto es: %.2f\n", prima);
            }
        }

    } else {
       
        printf("Tipo de vehiculo (1 = Deportivo, 0 = Otro): ");
        scanf("%d", &n3);

        if (n3 > 3) {
            printf("Años sin accidentes: ");
            scanf("%d", &n7);

            if (n7 > 2) {
                prima = prima - (prima * 0.15);
                printf("Tu monto es: %.2f\n", prima);
            } else {
                prima = prima + (prima * 0.20);
                printf("Tu monto es: %.2f\n", prima);
            }
        } else {
            printf("Años sin accidentes: ");
            scanf("%d", &n6);

            if (n6 > 2) {
                prima = prima - (prima * 0.15); 
                printf("Tu monto es: %.2f\n", prima);
            } else {
                prima = prima + (prima * 0.20); 
                printf("Tu monto es: %.2f\n", prima);
            }
        }
    }

    return 0;
}