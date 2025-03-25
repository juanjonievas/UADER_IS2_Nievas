#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verificar si se ha pasado un argumento
if len(sys.argv) == 1:  # Si no se ha pasado ningún argumento
    # Solicitar el rango al usuario
    rango = input("Por favor ingrese un rango entre '1-15': ")
else:
    rango = sys.argv[1]  # Si el rango fue pasado como argumento

# Procesar el rango ingresado
try:
    desde, hasta = map(int, rango.split('-'))

    # Limitar el valor de hasta a 15
    if hasta > 15:
        print("El valor máximo permitido es 15. Ajustando el rango.")
        hasta = 15

    # Verificar que el rango sea válido
    if desde > hasta:
        print("Error: El valor inicial debe ser menor o igual al valor final.")
    else:
        for num in range(desde, hasta + 1):
            print(f"Factorial de {num} es {factorial(num)}")

except ValueError:
    print("Error: El formato del rango es incorrecto. Debe ser 'desde-hasta' con números válidos.")



