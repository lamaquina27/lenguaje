class Entrada:

    @staticmethod
    def texto(mensaje=""):
        return input(mensaje)

    @staticmethod
    def entero(mensaje=""):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Error: Se esperaba un número entero.")

    @staticmethod
    def decimal(mensaje=""):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Error: Se esperaba un número decimal.")