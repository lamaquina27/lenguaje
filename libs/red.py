from sklearn.datasets import fetch_openml
import time
import numpy as np

class Red:
    seed = int(time.time() * 1000) % (2**31)
    euler = 2.71828

    @staticmethod
    def pseudo_random():
        Red.seed = (1103515245 * Red.seed + 12345) % (2**31)
        return Red.seed / (2**31)

    @staticmethod
    def my_uniform(a, b):
        return a + (b - a) * Red.pseudo_random()

    @staticmethod
    def carga_datos_x(rango1=0, rango2=500, ds='mnist_784'):
        mnist = fetch_openml(f'{ds}', version=1, as_frame=False)
        return mnist.data[rango1:rango2] / 255.0

    @staticmethod
    def carga_datos_y(rango1=0, rango2=500, ds='mnist_784'):
        mnist = fetch_openml(ds, version=1, as_frame=False)
        return mnist.target[rango1:rango2].astype(int)

    @staticmethod
    def a_one_hot(etiquetas, num_clases=10):
        resultado = []
        for etiqueta in etiquetas:
            vector = [0] * num_clases
            vector[int(etiqueta)] = 1
            resultado.append(vector)
        return resultado

    @staticmethod
    def reducir_imagenes_28a16(matriz_imagenes):
        resultado = []
        for imagen in matriz_imagenes:
            if len(imagen) != 28 * 28:
                raise ValueError("Cada imagen debe tener 784 elementos (28x28)")

            reducida = []
            for i in range(16):
                for j in range(16):
                    x_start = int(i * 28 / 16)
                    x_end = int((i + 1) * 28 / 16)
                    y_start = int(j * 28 / 16)
                    y_end = int((j + 1) * 28 / 16)

                    bloque = []
                    for x in range(x_start, x_end):
                        for y in range(y_start, y_end):
                            bloque.append(imagen[x * 28 + y])

                    promedio = sum(bloque) / len(bloque)
                    reducida.append(promedio)

            resultado.append(reducida)
        return resultado

    @staticmethod
    def sigmoide(x):
        return 1 / (1 + (Red.euler ** (-x)))

    @staticmethod
    def derivada_sigmoide(x):
        return x * (1 - x)

    @staticmethod
    def softmax(x):
        exp_x = [Red.euler ** (xi - max(x)) for xi in x]  # Restamos max(x) para estabilidad numérica
        sum_exp_x = sum(exp_x)
        return [xi / sum_exp_x for xi in exp_x]

    @staticmethod
    def cross_entropy(predicciones, objetivos):
        epsilon = 1e-12  # Para evitar log(0)
        return -sum(objetivo * np.log(max(prediccion, epsilon)) for prediccion, objetivo in zip(predicciones, objetivos))

    @classmethod
    def inicializar(cls, entradas, salidas, ocultas=64, tasa=0.95):
        red = {
            "x": entradas,
            "y": salidas,
            "tasa": tasa,
            "batch_size": 1,  # Tamaño del mini-batch
            "pesos1": [[cls.my_uniform(-1, 1) for _ in range(len(entradas[0]))] for _ in range(ocultas)],
            "umbral1": [cls.my_uniform(-1, 1) for _ in range(ocultas)],
            "pesos2": [[cls.my_uniform(-1, 1) for _ in range(ocultas)] for _ in range(len(salidas[0]))],
            "umbral2": [cls.my_uniform(-1, 1) for _ in range(len(salidas[0]))]
        }
        return red

    @classmethod
    def forward_pass(cls, red, entrada):
        # Capa oculta
        salida_oculta = []
        for j in range(len(red["pesos1"])):
            suma = sum(entrada[i] * red["pesos1"][j][i] for i in range(len(entrada)))
            suma += red["umbral1"][j]
            
            salida_oculta.append(cls.sigmoide(suma))
        
        # Capa de salida (antes del softmax)
        salida_final = []
        for k in range(len(red["y"][0])):
            suma = sum(salida_oculta[i] * red["pesos2"][k][i] for i in range(len(salida_oculta)))
            suma += red["umbral2"][k]
            salida_final.append(suma)
        # Aplicar softmax
        salida_final_softmax = cls.softmax(salida_final)
        return salida_oculta, salida_final, salida_final_softmax
    @classmethod
    def entrenar(cls, red, epocas=60):

        num_muestras = len(red["x"])
        batch_size = red["batch_size"]
        print(red['pesos1'])
        print(red['umbral1'])
                
        for epoca in range(epocas):
            error_total = 0
            indices = list(range(num_muestras))
            np.random.shuffle(indices)  # Mezclar los datos para cada época
            
            for inicio in range(0, num_muestras, batch_size):
                fin = min(inicio + batch_size, num_muestras)
                batch_indices = indices[inicio:fin]
                
                # Acumuladores para los gradientes
                grad_pesos1 = [[0 for _ in range(len(red["x"][0]))] for _ in range(len(red["pesos1"]))]
                grad_umbral1 = [0 for _ in range(len(red["pesos1"]))]
                grad_pesos2 = [[0 for _ in range(len(red["pesos1"]))] for _ in range(len(red["y"][0]))]
                grad_umbral2 = [0 for _ in range(len(red["y"][0]))]
                
                batch_error = 0
                
                
                for idx in batch_indices:
                    entrada = red["x"][idx]
                    objetivo = red["y"][idx]
                    # Forward pass
                    salida_oculta, salida_final, salida_final_softmax = cls.forward_pass(red, entrada)
                    
                    # Calcular error (cross-entropy)
                    batch_error += cls.cross_entropy(salida_final_softmax, objetivo)
                    
                    # Backward pass
                    # Capa de salida (softmax + cross-entropy)
                    delta_salida = [salida_final_softmax[k] - objetivo[k] for k in range(len(objetivo))]
                    
                    # Capa oculta
                    delta_oculta = [
                        sum(delta_salida[k] * red["pesos2"][k][j] for k in range(len(red["y"][0]))) * 
                        cls.derivada_sigmoide(salida_oculta[j])
                        for j in range(len(salida_oculta))
                    ]
                    
                    # Acumular gradientes
                    for k in range(len(red["y"][0])):
                        for j in range(len(salida_oculta)):
                            grad_pesos2[k][j] += delta_salida[k] * salida_oculta[j]
                        grad_umbral2[k] += delta_salida[k]
                    
                    for j in range(len(red["pesos1"])):
                        for i in range(len(entrada)):
                            grad_pesos1[j][i] += delta_oculta[j] * entrada[i]
                        grad_umbral1[j] += delta_oculta[j]
                
                # Promediar gradientes y actualizar pesos
                batch_len = len(batch_indices)
                for k in range(len(red["y"][0])):
                    for j in range(len(red["pesos1"])):
                        red["pesos2"][k][j] -= red["tasa"] * grad_pesos2[k][j] / batch_len
                    red["umbral2"][k] -= red["tasa"] * grad_umbral2[k] / batch_len

                for j in range(len(red["pesos1"])):
                    for i in range(len(red["x"][0])):
                        red["pesos1"][j][i] -= red["tasa"] * grad_pesos1[j][i] / batch_len
                    red["umbral1"][j] -= red["tasa"] * grad_umbral1[j] / batch_len
                
                error_total += batch_error / batch_len
            
            if epoca % 1 == 0:
                print(f"Época {epoca}, Error promedio: {error_total / (num_muestras / batch_size):.4f}")

    @classmethod
    def predecir(cls, red, entrada):
        predicciones = []
        for imagen in entrada:
            if len(imagen) != len(red["x"][0]):
                raise ValueError(f"Entrada debe tener {len(red['x'][0])} elementos por imagen.")

            _, _, salida_final = cls.forward_pass(red, imagen)
            
            prediccion = salida_final.index(max(salida_final))
            print(f"Predicción: {imagen} salidas: {['%.4f' % s for s in salida_final]})")
            predicciones.append(prediccion)
        return predicciones