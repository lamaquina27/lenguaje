from sklearn.datasets import fetch_openml

import time
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
    def carga_datos_x(rango1=0, rango2=500,ds='mnist_784'):
        
        mnist = fetch_openml(f'{ds}', version=1, as_frame=False)
        return mnist.data[rango1:rango2] / 255.0

    @staticmethod
    def carga_datos_y(rango1=0, rango2=500,ds='mnist_784'):
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
        """
        Reduce una matriz de imágenes 28x28 (planas) a 16x16 (planas),
        promediando bloques por imagen.

        :param matriz_imagenes: lista de listas, cada una con 784 elementos
        :return: lista de listas, cada una con 256 elementos
        """
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
        return 1 / (1 + (Red.euler ** -x))

    @staticmethod
    def derivada_sigmoide(x):
        return x * (1 - x)

    @classmethod
    def inicializar(cls, entradas, salidas, ocultas=64, tasa=0.78):
        red = {
            "x": entradas,
            "y": salidas,
            "tasa": tasa,
            "pesos1": [[cls.my_uniform(-1, 1) for _ in range(len(entradas[0]))] for _ in range(ocultas)],
            "umbral1": [cls.my_uniform(-1, 1) for _ in range(ocultas)],
            "pesos2": [[cls.my_uniform(-1, 1) for _ in range(ocultas)] for _ in range(len(salidas[0]))],
            "umbral2": [cls.my_uniform(-1, 1) for _ in range(len(salidas[0]))]
        }
        return red

    @classmethod
    def entrenar(cls, red, epocas=60):
        for epoca in range(epocas):
            error_total = 0
            for idx, entrada in enumerate(red["x"]):
                objetivo = red["y"][idx]

                salida_oculta = [cls.sigmoide(sum(entrada[i] * red["pesos1"][j][i] for i in range(len(entrada))) + red["umbral1"][j]) for j in range(len(red["pesos1"]))]
                salida_final = [cls.sigmoide(sum(salida_oculta[i] * red["pesos2"][k][i] for i in range(len(salida_oculta))) + red["umbral2"][k]) for k in range(len(red["y"][0]))]

                delta_salida = [(objetivo[k] - salida_final[k]) * cls.derivada_sigmoide(salida_final[k]) for k in range(len(red["y"][0]))]
                error_total += sum((objetivo[k] - salida_final[k]) ** 2 for k in range(len(red["y"][0])))

                delta_oculta = [sum(delta_salida[k] * red["pesos2"][k][j] for k in range(len(red["y"][0]))) * cls.derivada_sigmoide(salida_oculta[j]) for j in range(len(salida_oculta))]

                for k in range(len(red["y"][0])):
                    for j in range(len(salida_oculta)):

                        red["pesos2"][k][j] += red["tasa"] * delta_salida[k] * salida_oculta[j]
                    red["umbral2"][k] += red["tasa"] * delta_salida[k]

                for i in range(len(red["pesos1"])):
                    for j in range(len(entrada)):
                        red["pesos1"][i][j] += red["tasa"] * delta_oculta[i] * entrada[j]
                    red["umbral1"][i] += red["tasa"] * delta_oculta[i]

            if epoca % 10 == 0:
                print(f"Época {epoca}, Error total: {error_total:.4f}")

    @classmethod
    def predecir(cls, red, entrada):
        predicciones = []

        for imagen in entrada:
            if len(imagen) != len(red["x"][0]):
                raise ValueError(f"Entrada debe tener {len(red['x'][0])} elementos por imagen.")

            salida_oculta = [
                cls.sigmoide(
                    sum(imagen[j] * red["pesos1"][i][j] for j in range(len(imagen))) + red["umbral1"][i]
                )
                for i in range(len(red["pesos1"]))
            ]

            salida_final = [
                cls.sigmoide(
                    sum(salida_oculta[j] * red["pesos2"][i][j] for j in range(len(salida_oculta))) + red["umbral2"][i]
                )
                for i in range(len(red["y"][0]))
            ]

            prediccion = salida_final.index(max(salida_final))
            print(f"Predicción: {prediccion} (salidas: {['%.2f' % s for s in salida_final]})")
            predicciones.append(prediccion)

        return predicciones
