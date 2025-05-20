class Darwin:

    @staticmethod
    def factorial(numero):
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

    @staticmethod
    def absoluto(numero):
        return numero if numero >= 0 else -numero

    @staticmethod
    def redondear(numero):
        entero = int(numero)
        return entero if numero - entero < 0.5 else entero + 1

    @staticmethod
    def convertir_entero(numero):
        return int(numero)

    @staticmethod
    def convertir_flotante(numero):
        return float(numero)

    @staticmethod
    def raiz_cuadrada(numero):
        if numero < 0:
            raise Exception("No se puede calcular raíz cuadrada de un número negativo")
        # Método de aproximación de Newton
        aproximacion = numero
        for _ in range(10):
            aproximacion = 0.5 * (aproximacion + numero / aproximacion)
        return aproximacion

    @staticmethod
    def raiz(numero, indice):
        if numero < 0 and indice % 2 == 0:
            raise Exception("No se puede calcular raíz par de un número negativo")
        # Método de aproximación
        aproximacion = numero
        for _ in range(10):
            aproximacion = ((indice - 1) * aproximacion + numero / (aproximacion ** (indice - 1))) / indice
        return aproximacion

    @classmethod
    def seno(cls, x):
        resultado = 0
        x2 = (x*3.141592653589793238462643383279502884197169399375105820974944)/  180
        for i in range(10):
            signo = (-1) ** i
            resultado += signo * (x2 ** (2 * i + 1)) / cls.factorial(2 * i + 1)
        
        return resultado

    @classmethod
    def coseno(cls, x):
        resultado = 0
        x2 = (x*3.141592653589793238462643383279502884197169399375105820974944)/180
        for i in range(10):
            signo = (-1) ** i
            resultado += signo * (x2 ** (2 * i)) / cls.factorial(2 * i)
        
        return resultado

    @classmethod
    def tangente(cls, x):
        coseno_valor = cls.coseno(x)
        if coseno_valor == 0:
            raise Exception("Tangente indefinida en este valor")
        return cls.seno(x) / coseno_valor
    @staticmethod
    def regresion(x, y):
        n = len(x)
        if n != len(y):
            print("Error: Las listas deben tener la misma longitud")
            return

        sum_xy = sum(a * b for a, b in zip(x, y))
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x2 = sum(i ** 2 for i in x)

        b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        a = (sum_y / n) - b * (sum_x / n)
        
        print(f"La ecuacion de la regresion lineal es : y=({round(a,2)})+({round(b,2)})x")
