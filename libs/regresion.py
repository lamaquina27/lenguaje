import time

class Regresion:
    seed = int(time.time() * 1000) % (2**31)

    # --- Random y Uniforme
    @staticmethod
    def pseudo_random():
        Regresion.seed = (1103515245 * Regresion.seed + 12345) % (2**31)
        return Regresion.seed / (2**31)

    @staticmethod
    def my_uniform(a, b):
        return a + (b - a) * Regresion.pseudo_random()

    # --- Normalización (individual)
    @staticmethod
    def obtener_minimos(x):
        return [min(col) for col in zip(*x)]

    @staticmethod
    def obtener_maximos(x):
        return [max(col) for col in zip(*x)]

    @staticmethod
    def normalizar_x(x, minimos, maximos):
        return [[(v[j] - minimos[j]) / (maximos[j] - minimos[j]) for j in range(len(v))] for v in x]

    @staticmethod
    def obtener_minimo_y(y):
        return min(y)

    @staticmethod
    def obtener_maximo_y(y):
        return max(y)

    @staticmethod
    def normalizar_y(y, minimo, maximo):
        return [(v - minimo) / (maximo - minimo) for v in y]

    @staticmethod
    def normalizar_valor(valores, minimos, maximos):
        return [(valores[i] - minimos[i]) / (maximos[i] - minimos[i]) for i in range(len(valores))]

    @staticmethod
    def desnormalizar_valor(valor, minimo, maximo):
        return valor * (maximo - minimo) + minimo

     # --- Generación de datos X ---
    @staticmethod
    def generar_x_ejemplo(n=1000, ds='houses'):
        x_datos = []
        for _ in range(n):
            if ds == 'houses':
                # 1. Tamaño (m2)
                tam = int(20 + Regresion.my_uniform(0, 180))
                # 2. Habitaciones
                hab = int(1 + Regresion.my_uniform(0, 7))
                # 3. Edad (años)
                edad = int(Regresion.my_uniform(0, 40))
                # 4. Baños
                banos = int(1 + Regresion.my_uniform(0, 4))
                # 5. Distancia a centro (km)
                distancia = float(Regresion.my_uniform(0.5, 15.0))
                # 6. Calificación zona (1-10)
                zona = int(1 + Regresion.my_uniform(0, 9))
                x_datos.append([tam, hab, edad, banos, distancia, zona])
                
            elif ds == 'sales':
                # 1. Presupuesto publicidad
                publicidad = float(Regresion.my_uniform(0, 1000))
                # 2. Empleados
                empleados = int(1 + Regresion.my_uniform(0, 9))
                # 3. Días de promoción
                promocion = int(Regresion.my_uniform(1, 30))
                # 4. Precio producto
                precio = float(Regresion.my_uniform(5, 50))
                # 5. Competidores en zona
                competidores = int(Regresion.my_uniform(0, 10))
                # 6. Temporada (1=baja, 2=media, 3=alta)
                temporada = int(1 + Regresion.my_uniform(0, 2))
                x_datos.append([publicidad, empleados, promocion, precio, competidores, temporada])
                
            elif ds == 'grades':
                # 1. Horas estudio
                horas = float(Regresion.my_uniform(0, 30))
                # 2. Asistencia (%)
                asistencia = float(Regresion.my_uniform(0.5, 1.0))
                # 3. Libros leídos
                libros = int(Regresion.my_uniform(0, 20))
                # 4. Participación en clase
                participacion = float(Regresion.my_uniform(0, 10))
                # 5. Tareas entregadas (%)
                tareas = float(Regresion.my_uniform(0.3, 1.0))
                # 6. Dificultad materia (1-5)
                dificultad = int(1 + Regresion.my_uniform(0, 4))
                x_datos.append([horas, asistencia, libros, participacion, tareas, dificultad])
                
            elif ds == 'fuel':
                # 1. Peso vehículo (kg)
                peso = float(800 + Regresion.my_uniform(0, 1700))
                # 2. Cilindraje (litros)
                cilindraje = float(1 + Regresion.my_uniform(0, 4))
                # 3. Tipo combustible (1=regular, 2=premium)
                combustible = int(1 + Regresion.my_uniform(0, 1))
                # 4. Presión llantas (psi)
                llantas = float(28 + Regresion.my_uniform(0, 12))
                # 5. Velocidad promedio (km/h)
                velocidad = float(Regresion.my_uniform(30, 120))
                # 6. Aire acondicionado (0=no, 1=sí)
                aire = int(Regresion.my_uniform(0, 1))
                x_datos.append([peso, cilindraje, combustible, llantas, velocidad, aire])
                
            else:
                raise ValueError(f"Dataset no soportado: {ds}")
                
        return x_datos

    # --- Generación de datos Y ---
    @staticmethod
    def generar_y_ejemplo(x_datos, ds='houses'):
        y_datos = []
        for fila in x_datos:
            if ds == 'houses':
                tam, hab, edad, banos, distancia, zona = fila
                precio = (100 + 2.5*tam + 15*hab - 1.2*edad + 10*banos - 
                          5*distancia + 8*zona + Regresion.my_uniform(-10, 10))
                y_datos.append(round(precio, 2))
                
            elif ds == 'sales':
                pub, emp, prom, prec, comp, temp = fila
                ventas = (50 + 0.8*pub + 30*emp + 2*prom - 1.5*prec - 
                          5*comp + 20*temp + Regresion.my_uniform(-20, 20))
                y_datos.append(round(ventas, 2))
                
            elif ds == 'grades':
                hrs, asi, lib, par, tar, dif = fila
                calificacion = (30 + 2*hrs + 40*asi + 0.5*lib + 2*par + 
                               15*tar - 3*dif + Regresion.my_uniform(-15, 15))
                y_datos.append(round(calificacion, 2))
                
            elif ds == 'fuel':
                pes, cil, com, lla, vel, air = fila
                consumo = (5 + 0.002*pes + 1.5*cil - 0.5*com + 0.1*lla + 
                           0.05*vel + 0.8*air + Regresion.my_uniform(-1, 1))
                y_datos.append(round(consumo, 2))
                
            else:
                raise ValueError(f"Dataset no soportado: {ds}")
                
        return y_datos
    # --- Inicialización
    @staticmethod
    def inicializar_modelo(x, y, tasa=0.0001):
        modelo = {
            "x": x,
            "y": y,
            "tasa": tasa,
            "num_entradas": len(x[0]),
            "pesos": [Regresion.my_uniform(-1, 1) for _ in range(len(x[0]))],
            "umbral": Regresion.my_uniform(-1, 1)
        }
        return modelo

    # --- Entrenamiento
    @staticmethod
    def entrenar(modelo, epocas=100):
        for epoca in range(epocas):
            error_total = 0
            for i in range(len(modelo["x"])):
                entrada = modelo["x"][i]
                objetivo = modelo["y"][i]
                pred = sum(entrada[j] * modelo["pesos"][j] for j in range(modelo["num_entradas"])) + modelo["umbral"]
                error = objetivo - pred
                for j in range(modelo["num_entradas"]):
                    modelo["pesos"][j] += modelo["tasa"] * error * entrada[j]
                modelo["umbral"] += modelo["tasa"] * error
                error_total += error ** 2

            if epoca % 10 == 0:
                print(f"Época {epoca}, Error total: {error_total:.2f}")

    # --- Predicción
    @staticmethod
    def predecir(modelo, entrada):
        pred = sum(entrada[j] * modelo["pesos"][j] for j in range(modelo["num_entradas"])) + modelo["umbral"]
        print(f"Predicción: {pred:.2f}")
        return pred
