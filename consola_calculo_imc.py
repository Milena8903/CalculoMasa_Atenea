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

# Realizar las funciones
#def imc(peso, altura):
#    return peso/(altura**2)

# Realizar operacion
#imc = peso/(altura**2)

# Llamo a la función
#print("Su indice de masa es: " );
#print(imc);


def imc(peso:float, altura:float)-> str:
    imc = peso/(altura**2)
    
    respuesta = " El indice de masa corporal es " + str(imc)  
                  
                 
#Se retorna el string
    return respuesta


