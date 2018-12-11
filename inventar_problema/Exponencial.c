#include <stdio.h>
#include <stdlib.h>

int exponencial (int base, int expoente){
    if (expoente == 0){
        return 1;
    }
    if (expoente % 2 == 0){
        return exponencial(base, expoente/2) * exponencial(base, expoente/2);
    } else{
        return exponencial(base, (expoente-1)/2) * exponencial(base, (expoente-1)/2) * base;
    }
}


int teste (int base, int expoente){
    if (expoente == 0){
        return 1;
    }
    if (expoente % 2 == 0){
        return exponencial(base, expoente/2) * exponencial(base, expoente/2);
    } else{
        return exponencial(base, expoente/2) * exponencial(base, expoente/2) * base;
    }
}



void main(){
    int base, expoente, potencia;
    printf ("Digite a base: ");
    scanf ("%d", &base);
    printf ("Digite o expoente: ");
    scanf ("%d", &expoente);
    potencia = exponencial (base, expoente);
    printf ("%d^%d = %d\n", base, expoente, potencia);
    printf ("%d^%d = %d\n", base,expoente, teste(base, expoente));
}
