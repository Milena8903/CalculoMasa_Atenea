# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 09:55:47 2023

@author: Milena
"""

def calcular_imc(peso:float, altura:float)->float:
    imc = peso/(altura**2)
    return imc

def calcular_porcentaje_grasa(peso:float, altura:float, edad:int, valor_genero:float)->float:
    imc = float(calcular_imc(peso,altura))
    gc = ((1.2 * imc) + (0.23 * edad)) - 5.4 - valor_genero
    return gc

def calcular_calorias_en_reposo(peso:float, altura:int, edad:int, valor_genero:float)->float:
    tmb = ((10 * peso) + (6.25 * altura)) - (5 * edad) + valor_genero
    return tmb

def calcular_calorias_en_actividad(peso:float, altura:int, edad:int, valor_genero:float,\
                                   valor_actividad)->float:
    tmb = float(calcular_calorias_en_reposo(peso, altura, edad, valor_genero))
    tmb_actividad_fisica = tmb * valor_actividad
    return tmb_actividad_fisica

def consumo_calorias_recomendado_para_adelgazar(peso:float, altura:int, edad:int, \
                                                valor_genero:float)->str:
    tmb = float(calcular_calorias_en_reposo(peso, altura, edad, valor_genero))
    rango_superior = round(tmb - (tmb * (15/100)), 2)
    rango_inferior = round(tmb - (tmb * (20/100)), 1)
    
    respuesta = "Para adelgazar es recomendado que consumas entre: " + str(rango_inferior) \
                  + " y " + str(rango_superior) + " calorías al día. Siendo "\
                  + str(rango_inferior) + " el rango inferior y " \
                  + str(rango_superior) +  " el rango superior."
    
    print(respuesta)
    return respuesta

