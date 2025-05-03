class Darwin:

    @staticmethod
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @classmethod
    def sin(cls, x):
        result = 0
        for i in range(10):  # 10 términos es aceptable para buena precisión
            sign = (-1) ** i
            result += sign * (x ** (2 * i + 1)) / cls.factorial(2 * i + 1)
        return result

    @classmethod
    def cos(cls, x):
        result = 0
        for i in range(10):
            sign = (-1) ** i
            result += sign * (x ** (2 * i)) / cls.factorial(2 * i)
        return result

    @classmethod
    def tan(cls, x):
        cosx = cls.cos(x)
        if cosx == 0:
            raise Exception("Tangente indefinida en este valor")
        return cls.sin(x) / cosx

    @classmethod
    def ejecutar(cls, nombre, valor):
        if hasattr(cls, nombre):
            return getattr(cls, nombre)(valor)
        raise Exception("Función no encontrada")
