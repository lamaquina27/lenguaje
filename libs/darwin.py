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
        if resultado > 0.999:
            resultado = 1
        elif resultado < 0.001:
            resultado = 0
        return resultado

    @classmethod
    def coseno(cls, x):
        resultado = 0
        #x2 = (x*3.141592653589793238462643383279502884197169399375105820974944)/180
        for i in range(10):
            signo = (-1) ** i
            resultado += signo * (x ** (2 * i)) / cls.factorial(2 * i)
        if resultado > 0.999:
            resultado = 1
        elif resultado < 0.001:
            resultado = 0
        return resultado

    @classmethod
    def tangente(cls, x):
        coseno_valor = cls.coseno(x)
        if coseno_valor == 0:
            raise Exception("Tangente indefinida en este valor")
        return cls.seno(x) / coseno_valor
