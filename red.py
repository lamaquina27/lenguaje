import random
import numpy as np
from sklearn.datasets import fetch_openml

# Cargar MNIST
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
x = mnist.data[:500] / 255.0  # Primeras 500 imágenes normalizadas
y = mnist.target[:500].astype(int)

# Función para convertir las etiquetas a one-hot
def a_one_hot(etiquetas, num_clases=10):
    resultado = []
    for etiqueta in etiquetas:
        vector = [0] * num_clases
        vector[int(etiqueta)] = 1
        resultado.append(vector)
    return resultado

y_one_hot = a_one_hot(y)

# Función para reducir una imagen 28x28 a 16x16
def reducir_28a16(imagen):
    imagen_28x28 = imagen.reshape(28, 28)
    imagen_16x16 = np.zeros((16, 16))
    for i in range(16):
        for j in range(16):
            x_start = int(i * 28 / 16)
            x_end = int((i + 1) * 28 / 16)
            y_start = int(j * 28 / 16)
            y_end = int((j + 1) * 28 / 16)
            bloque = imagen_28x28[x_start:x_end, y_start:y_end]
            imagen_16x16[i, j] = np.mean(bloque)
    return imagen_16x16.flatten()

# Reducir todas las imágenes
x_reducido = np.array([reducir_28a16(img) for img in x])

class RedNeuronal:
    def __init__(self, entradas, salidas, ocultas=64, tasa=0.78):
        self.x = entradas         # Lista de listas (cada imagen)
        self.y = salidas          # Lista one-hot
        self.tasa = tasa          # Tasa de aprendizaje

        # Inicializar pesos (entrada → oculta) aleatoriamente
        self.pesos1 = [[random.uniform(-1, 1) for _ in range(256)] for _ in range(ocultas)]  # 256 entradas por cada neurona oculta
        self.umbral1 = [random.uniform(-1, 1) for _ in range(ocultas)]

        # Pesos (oculta → salida)
        self.pesos2 = [[random.uniform(-1, 1) for _ in range(ocultas)] for _ in range(10)]  # 10 salidas (clases)
        self.umbral2 = [random.uniform(-1, 1) for _ in range(10)]  # umbral de la neurona de salida
    #funcion sigmoide para las capas ocultas
    def sigmoide(self, x):
        return 1 / (1 + np.exp(-x))
    #funcion sigmoide derivada para las capas ocultas

    def derivada_sigmoide(self, x):
        return x * (1 - x)

    def entrenar(self, epocas=60):
        #iteracion por epocas 
        for epoca in range(epocas):
            error_total = 0
            #iteracion por cada entrada
            for idx, entrada in enumerate(self.x):
                objetivo = self.y[idx]
                salida_oculta = []
                # Calcular el valor de los nodos en la capa oculta
                for j in range(len(self.pesos1)):
                    suma = sum(entrada[i] * self.pesos1[j][i] for i in range(256)) + self.umbral1[j]  # 256 entradas
                    salida_oculta.append(self.sigmoide(suma))
                

                # Calcular el valor de los nodos en la capa de salida
                salida_final = []
                for k in range(10):
                    suma_salida = sum(salida_oculta[i] * self.pesos2[k][i] for i in range(len(salida_oculta))) + self.umbral2[k]
                    salida_final.append(self.sigmoide(suma_salida))
                #calcula el error de la salida para la retroalimentacion
                delta_salida = [0] * 10
                for k in range(10):
                    error = objetivo[k] - salida_final[k]
                    delta_salida[k] = error * self.derivada_sigmoide(salida_final[k])
                    error_total += error ** 2
                # Calcular el error de la capa oculta
                delta_oculta = [0] * len(salida_oculta)
                for j in range(len(salida_oculta)):
                    error_oculto = sum([delta_salida[k] * self.pesos2[k][j] for k in range(10)])
                    delta_oculta[j] = error_oculto * self.derivada_sigmoide(salida_oculta[j])
                #REEMPLAZA LOS PESOS DE LA CAPA DE SALIDA Y LOS UMBRALES DE LA CAPA DE SALIDA
                for k in range(10):
                    for j in range(len(salida_oculta)):
                        self.pesos2[k][j] += self.tasa * delta_salida[k] * salida_oculta[j]
                    self.umbral2[k] += self.tasa * delta_salida[k]
                #REEMPLAZA LOS PESOS DE LA CAPA OCULTA Y LOS UMBRALES DE LA CAPA OCULTA
                for i in range(len(self.pesos1)):
                    for j in range(256):  # Cambié de 784 a 256
                        self.pesos1[i][j] += self.tasa * delta_oculta[i] * entrada[j]
                    self.umbral1[i] += self.tasa * delta_oculta[i]
            
            if epoca % 10 == 0:
                print(f"Época {epoca}, Error total: {error_total:.4f}")
    #FUNCION PARA PREDECIR UNA IMAGEN
    def predecir(self, entrada):
        # Calcular el valor de los nodos en la capa oculta
        salida_oculta = []
        for i in range(len(self.pesos1)):
            suma = sum(entrada[j] * self.pesos1[i][j] for j in range(256)) + self.umbral1[i]  # 256 entradas
            salida_oculta.append(self.sigmoide(suma))
        # Calcular el valor de los nodos en la capa de salida
        salida_final = []
        for i in range(10):
            suma_final = sum(salida_oculta[j] * self.pesos2[i][j] for j in range(len(salida_oculta))) + self.umbral2[i]
            salida_final.append(self.sigmoide(suma_final))
        #almacena el valor mas grande del onehot de Y y lo retorna como prediccion
        prediccion = salida_final.index(max(salida_final))
        print(f"Predicción: {prediccion} (salidas: {['%.2f' % s for s in salida_final]})")
        return prediccion

# Convertir etiquetas a one-hot dentro de la clase
red = RedNeuronal(x_reducido, y_one_hot)
red.entrenar()

# Hacer predicción con una imagen de prueba
imagen_prueba = x_reducido[278]  # Puedes cambiar el índice para elegir otra imagen
red.predecir(imagen_prueba)
