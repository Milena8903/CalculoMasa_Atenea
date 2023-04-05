# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:31:14 2023

@author: Milena
"""

import analizar as mod

def ejecutar_analizar_anio()->None:
    anio = int(input(" Ingrese el año que desea analizar: "))
    resultado = mod.analizar_anio(anio)
    print(resultado)

def iniciar_aplicacion()->None:
    print(" Bienvenido al analizador de años ")
    ejecutar_analizar_anio()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()