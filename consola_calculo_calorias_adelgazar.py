# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:39:09 2023

@author: Milena
"""

import calculadora_indices as calc

    
def consumo_calorias_recomendado_para_adelgazar():
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = int(input(" Por favor escriba su altura en centimetros: "))
    edad = int(input(" Por favor escriba su edad en años: "))
    valor_genero = float(input("Por favor escriba: Si su genero es femenino: -161 \n \
                  Si su genero es masculino: 5 \n"));
    
    resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, \
                                                                 valor_genero)
        
    return resultado
       

def iniciar_aplicacion()->None:
    print(" Calculemos el consumo recomendado de calorias \n")
    consumo_calorias_recomendado_para_adelgazar()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()