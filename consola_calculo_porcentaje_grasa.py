# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:43:48 2023

@author: Milena
"""

# Realizo la importación del archivo
#import consola_calculo_imc as mod

# Declaración de las variables
#edad = float(input("Por favor escriba su edad en años: "));
#genero = input("Por favor escriba su genero (masculino o femenino): ");
#peso = float(input("Por favor escriba su peso en Kg: "));
#altura = float(input("Por favor escriba su altura en mtrs: "));


#if genero == "masculino":
#    valor_genero = 10.8
#elif genero == "femenino":
#        valor_genero = 0
#else:
#     print("Escriba masculino o femenino");


#imc = peso/(altura**2)

#GC = 1.2 * imc + 0.23 * edad - 5.4 - valor_genero

# Llamo a la función
#print("Su porcentaje de grasa corporal es: " );
#print(GC);


import consola_calculo_imc as mod

def ejecutar_imc()->None:
    peso = float(input(" Por favor escriba su peso en Kg: "))
    altura = float(input(" Por favor escriba su altura en mtrs: "))
    resultado = mod.imc(peso, altura)
    print(resultado)

imc = ejecutar_imc()

def genero()->float:
    genero =str(input("Por favor escriba su genero (masculino o femenino): "));
    
    if genero == "masculino":
        valor_genero = 10.8
    elif genero == "femenino":
            valor_genero = 0
    else:
         print("Escriba masculino o femenino");
 
    return valor_genero
       
resultado_genero = genero()


def calculo_porcentaje(imc, resultado_genero):
    edad = int(input("Por favor escriba su edad en años: "));       
        
    GC = 1.2 * imc + 0.23 * edad - 5.4 - resultado_genero
    
    respuesta = " El porcentaje de grasa corporal es " + str(float(GC))

    return respuesta

def iniciar_aplicacion()->None:
    print(" Calculemos su índice de masa corporal ")
   
    calculo_porcentaje(imc, resultado_genero)

#PROGRAMA PRINCIPAL
iniciar_aplicacion()

 #ejecutar_imc()


#def ejecutar_porcentaje_grasa_corporal()->None:
#    edad = int(input(" por favor escriba su edad (años): "))
#    resultado = mod.porcentaje_grasa_corporal(edad)
#    print(resultado)
    

#def iniciar_aplicacion()->None:
#    print(" Bienvenido al ejecutador de porcentaje de grasa corporal ")
#    ejecutar_porcentaje_grasa_corporal()
    


#iniciar_aplicacion()