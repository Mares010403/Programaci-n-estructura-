#include <stdio.h>

int main() {
float temperatura;

printf("Ingrese la temperatura en °C: ");
scanf("%f", &temperatura);

if (temperatura < 20) {
    printf("El ventilador está APAGADO.\n");
} else if (temperatura >= 20 && temperatura <= 30) {
    printf("El ventilador está en BAJA VELOCIDAD.\n");
} else {
    printf("El ventilador está en ALTA VELOCIDAD.\n");
}

return 0;


}