# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Declaración de las variables
# Realización del casteo
# Solicita datos al usuario

#peso = float(input("Por favor escriba su peso en Kg: "));
#altura = float(input("Por favor escriba su altura en mtrs: "));



# Llamo a la función
#print("Su indice de masa es: " );
#print(imc);


def imc(peso:float, altura:float):
    imc = peso/(altura**2)
    return imc

def porcentaje_grasa_corporal(edad:int, genero):
    gc = 1.2 * float(imc) + 0.23 * edad - 5.4 - genero
    return gc

