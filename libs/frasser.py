class Frasser:

    # -------------------- LISTAS --------------------
    @staticmethod
    def crear_lista(*elementos):
        return list(elementos)

    @staticmethod
    def longitud(lista):
        return len(lista)

    @staticmethod
    def obtener(lista, indice):
        if indice < 0 or indice >= len(lista):
            raise Exception("Índice fuera de rango.")
        return lista[indice]

    @staticmethod
    def concatenar_listas(a, b):
        return a + b

    @staticmethod
    def invertir_lista(lista):
        return lista[::-1]

    @staticmethod
    def eliminar_elemento(lista, valor):
        return [x for x in lista if x != valor]

    @staticmethod
    def contar(lista, valor):
        contador = 0
        for x in lista:
            if x == valor:
                contador += 1
        return contador

    @staticmethod
    def duplicados(lista):
        vistos = []
        repetidos = []
        for x in lista:
            if x in vistos and x not in repetidos:
                repetidos.append(x)
            else:
                vistos.append(x)
        return repetidos

    @staticmethod
    def sublista(lista, inicio, fin):
        return lista[inicio:fin]

    # -------------------- MATRICES --------------------
    @staticmethod
    def crear_matriz(filas, columnas, valor=0):
        return [[valor for _ in range(columnas)] for _ in range(filas)]

    @staticmethod
    def suma_matrices(a, b):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise Exception("Dimensiones incompatibles para suma.")
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    @staticmethod
    def resta_matrices(a, b):
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise Exception("Dimensiones incompatibles para resta.")
        return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    @staticmethod
    def transpuesta(m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

    @staticmethod
    def producto_matrices(a, b):
        if len(a[0]) != len(b):
            raise Exception("Columnas de A deben coincidir con filas de B.")
        resultado = []
        for i in range(len(a)):
            fila = []
            for j in range(len(b[0])):
                suma = 0
                for k in range(len(b)):
                    suma += a[i][k] * b[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado

    @staticmethod
    def concatenar_matrices(a, b, eje):
        if eje == 0:
            if len(a[0]) != len(b[0]):
                raise Exception("Matrices deben tener igual número de columnas para concatenar por filas.")
            return a + b
        elif eje == 1:
            if len(a) != len(b):
                raise Exception("Matrices deben tener igual número de filas para concatenar por columnas.")
            return [a[i] + b[i] for i in range(len(a))]
        else:
            raise Exception("Eje inválido. Usa 0 para filas o 1 para columnas.")

    @staticmethod
    def matriz_identidad(n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    @staticmethod
    def es_cuadrada(m):
        return all(len(fila) == len(m) for fila in m)

    @staticmethod
    def determinante_2x2(m):
        if len(m) != 2 or len(m[0]) != 2:
            raise Exception("Solo se permite determinante de matrices 2x2.")
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    @staticmethod
    def inversa_2x2(m):
        det = Newton.determinante_2x2(m)
        if det == 0:
            raise Exception("La matriz no tiene inversa (determinante 0).")
        return [[m[1][1]/det, -m[0][1]/det], [-m[1][0]/det, m[0][0]/det]]

    @staticmethod
    def es_simetrica(m):
        if not Newton.es_cuadrada(m):
            return False
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] != m[j][i]:
                    return False
        return True
