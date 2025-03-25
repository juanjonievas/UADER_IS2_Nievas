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
    rango = input("Ingrese un numero o un rango EJ: 4-8")
else:
    rango = sys.argv[1]  # Si el rango fue pasado como argumento

# Procesar el rango ingresado
try:
    # Si el rango comienza con '-', se asume un rango hasta el número
    if rango.startswith('-'):
        hasta = abs(int(rango[1:]))  # Convertir el número después del '-' en positivo
        desde = 1  # El rango comienza desde 1
    elif rango.endswith('-'):
        desde = int(rango[:-1])  # El rango empieza en el número indicado
        hasta = 60  # El rango termina en 60
    else:
        desde, hasta = map(int, rango.split('-'))

    # Verificar que el rango sea válido
    if desde > hasta:
        print("Error: El valor inicial debe ser menor o igual al valor final.")
    else:
        for num in range(desde, hasta + 1):
            print(f"Factorial de {num} es {factorial(num)}")

except ValueError:
    print("Ingrese un numero o un rango EJ: 4-8.")



