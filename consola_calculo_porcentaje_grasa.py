# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:43:48 2023

@author: Milena
"""


import calculadora_indices as calc

    
def calcular_porcentaje_grasa():
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = float(input(" Por favor escriba su altura en metros: "))
    edad = int(input(" Por favor escriba su edad en años: "))
    valor_genero = float(input("Por favor escriba: Si su genero es femenino: 0 \n \
                  Si su genero es masculino: 10.8 \n"));
    
    resultado = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    resultado = round(resultado,2)
    print("\n El porcentaje de grasa que tiene el cuerpo es de: ", resultado, "%") 
    return resultado
       

def iniciar_aplicacion()->None:
    print(" Calculemos su índice de masa corporal \n")
    calcular_porcentaje_grasa()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

