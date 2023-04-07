# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import calculadora_indices as calc

def calcular_imc():
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = float(input(" Por favor escriba su altura en mtrs: "))
    imc = calc.calcular_imc(peso, altura)
    imc = round(imc,2)
    print("\n Su indice de masa corporal es: " , imc)
    return imc

def iniciar_aplicacion()->None:
    print(" Calculemos su índice de masa corporal \n")
    calcular_imc()

 
#PROGRAMA PRINCIPAL
iniciar_aplicacion()
