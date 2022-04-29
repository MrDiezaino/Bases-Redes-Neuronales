# coding=utf-8

import math
import random

class Neurona():
    def __init__(self):
        # Semilla para que se vuelvan a repetir los números aleatorios.
        random.seed(1)
        self.pesos = [random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)]
        # Bias lo usaremos para evitar que la red se estanque
        self.bias = random.uniform(-1,1)

    def __sumatoria(self,neurona_entrada):
        suma = 0
        for i, neurona_entrada in enumerate(neurona_entrada):
            suma += self.pesos[i] * neurona_entrada
        return suma

    def __sigmoide(self,suma):
        return 1 / (1 + math.exp(-suma))

    def respuesta(self, neurona_entrada):
        suma = self.__sumatoria(neurona_entrada)
        neurona_respuesta = self.__sigmoide(suma) + self.bias
        return neurona_respuesta

    # neurona_respuesta = y
    def __gradiente(self, neurona_respuesta):
        return neurona_respuesta * (1-neurona_respuesta)

    def entranamiento(self, ejemplos, epocas):
        for i in range(epocas):
            for ejemplo in ejemplos:
                prediccion = self.respuesta(ejemplo["entradas"])
                error = ejemplo["salida"]-prediccion

                for e in range(len(self.pesos)):
                    neurona_entrada = ejemplo["entradas"][e]
                    ajustar_peso = neurona_entrada * error * self.__gradiente(prediccion)

                    self.pesos[e] += ajustar_peso
                    # Actualizar el bias
                    self.bias += error * self.__gradiente(prediccion)

neurona1 = Neurona()
print("Pesos" + str(neurona1.pesos))

# Valores de entrada
ejemplos = [{"entradas": [0,0,1],"salida":1},
           {"entradas": [1,0,0],"salida":0},
           {"entradas": [0,1,0],"salida":0},
           {"entradas": [1,1,1],"salida":1},
           {"entradas": [0,1,1],"salida":1}]

neurona1.entranamiento(ejemplos, epocas = 5)
print("Nuevos pesos: "+ str(neurona1.pesos))

examen = [1,0,1]
valor_precedido = neurona1.respuesta(examen)
print ("Respuesta: "+ str(valor_precedido))