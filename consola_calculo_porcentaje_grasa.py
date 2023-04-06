# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:43:48 2023

@author: Milena
"""


import consola_calculo_imc as mod


def ejecutar_imc():
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = float(input(" Por favor escriba su altura en mtrs: "))
    imc = mod.imc(peso, altura)
    imc = round(imc,2)
    print("su indice de masa corporal es: ")
    print(imc)
    
#imc = ejecutar_imc()

#print(type(ejecutar_imc()))

def ejecutar_porcentaje_grasa_corporal():
    edad = int(input(" Por favor escriba su edad en años: "))
    genero =str(input("Por favor escriba: Si su genero es femenino: 0  \n \
                  Si su genero es masculino: 10.8 \n"));
    resultado = mod.porcentaje_grasa_corporal(edad, genero)
    print(resultado) 
       
#resultado_genero = genero()



def iniciar_aplicacion()->None:
    print(" Calculemos su índice de masa corporal ")
    ejecutar_imc()
    #calculo_porcentaje(imc, resultado_genero)
    ejecutar_porcentaje_grasa_corporal()

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

