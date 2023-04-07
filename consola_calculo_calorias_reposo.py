# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:54:14 2023

@author: Milena
"""

import calculadora_indices as calc

    
def calcular_calorias_en_reposo():
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = int(input(" Por favor escriba su altura en centimetros: "))
    edad = int(input(" Por favor escriba su edad en años: "))
    valor_genero = float(input("Por favor escriba: Si su genero es femenino: -161 \n \
                  Si su genero es masculino: 5 \n"));
    
    resultado = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    resultado = round(resultado,2)
    print("\n La cantidad de calorías que usted quema en reposo es de: ", resultado, "cal") 
    return resultado
       

def iniciar_aplicacion()->None:
    print(" Calculemos las calorías que quema estando en reposo \n")
    calcular_calorias_en_reposo()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()