# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:08:29 2023

@author: Milena
"""

import calculadora_indices as calc

    
def calcular_calorias_en_actividad():
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = int(input(" Por favor escriba su altura en centimetros: "))
    edad = int(input(" Por favor escriba su edad en años: "))
    valor_genero = float(input("Por favor escriba: Si su genero es femenino: -161 \n \
                  Si su genero es masculino: 5 \n"));
    valor_actividad = float(input("Por favor escriba su actividad fisica \
                                  de acuerdo con la siguiente tabla: \n \
                  1.2: poco o ningún ejercicio \n \
                  1.375: ejercicio ligero (1 a 3 días a la semana) \n \
                  1.55: ejercicio moderado (3 a 5 días a la semana) \n \
                  1.725: deportista (6 -7 días a la semana) \n \
                  1.9: atleta (entrenamientos mañana y tarde) \n"));
    
    resultado = calc.calcular_calorias_en_actividad(peso, altura, edad, \
                                                    valor_genero, valor_actividad)
    resultado = round(resultado,2)
    print("\n La cantidad de calorías que usted quema, al realizar algún \n \
          tipo de actividad física semanalmente es de: ", \
                                                          resultado, "cal") 
    return resultado
       

def iniciar_aplicacion()->None:
    print(" Calculemos las calorías que quema realizando una actividad física \n")
    calcular_calorias_en_actividad()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()