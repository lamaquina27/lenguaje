# --- Utilidades básicas sin librerías ---
def raiz_cuadrada(n, epsilon=1e-10):
    """Calcula raíz cuadrada usando el método de Newton-Raphson."""
    if n == 0:
        return 0
    x = n
    while True:
        y = 0.5 * (x + n / x)
        if abs(x - y) < epsilon:    
            return y
        x = y

def generar_aleatorio(seed):
    """Generador lineal congruencial simple."""
    a = 1664525
    c = 1013904223
    m = 2**32
    while True:
        seed = (a * seed + c) % m
        yield seed / m

def seleccionar_muestra_aleatoria(lista, k, seed=42):
    """Selecciona k elementos aleatorios sin repetición."""
    generador = generar_aleatorio(seed)
    indices = set()
    while len(indices) < k:
        indices.add(int(next(generador) * len(lista)))
    return [lista[i] for i in indices]

# --- Algoritmo de K-Medoids ---
class Agrupamiento:
    @staticmethod
    def distancia_euclidiana(p1, p2):
        return raiz_cuadrada(sum((x - y) ** 2 for x, y in zip(p1, p2)))

    @classmethod
    def _inicializar_centroides(cls, datos, k, seed=42):
        """Selecciona k puntos aleatorios distintos de los datos."""
        return seleccionar_muestra_aleatoria(datos, k, seed)

    @classmethod
    def _asignar_clusters(cls, datos, centroides):
        """Asigna cada punto al centroide más cercano."""
        clusters = [[] for _ in range(len(centroides))]
        for punto in datos:
            distancias = [cls.distancia_euclidiana(punto, centro) for centro in centroides]
            idx = cls._indice_minimo(distancias)
            clusters[idx].append(punto)
        return clusters

    @classmethod
    def _calcular_medoide(cls, cluster):
        """Encuentra el punto en el cluster con la menor distancia total a los demás."""
        if not cluster:
            return None
            
        distancias_totales = []
        for punto in cluster:
            distancia_total = sum(cls.distancia_euclidiana(punto, otro) for otro in cluster)
            distancias_totales.append(distancia_total)
        
        idx_medoide = cls._indice_minimo(distancias_totales)
        return cluster[idx_medoide]

    @classmethod
    def _actualizar_centroides(cls, clusters):
        """Actualiza los centroides como los medoides de cada cluster."""
        nuevos = []
        for cluster in clusters:
            nuevos.append(cls._calcular_medoide(cluster))
        return nuevos

    @staticmethod
    def _indice_minimo(lista):
        """Encuentra el índice del valor mínimo en una lista."""
        minimo = lista[0]
        idx = 0
        for i in range(1, len(lista)):
            if lista[i] < minimo:
                minimo = lista[i]
                idx = i
        return idx

    @classmethod
    def ajustar(cls, datos, k, max_iter=100, seed=42):
        """Ejecuta el algoritmo de agrupamiento."""
        centroides = cls._inicializar_centroides(datos, k, seed)
        
        for _ in range(max_iter):
            clusters = cls._asignar_clusters(datos, centroides)
            nuevos_centroides = cls._actualizar_centroides(clusters)
            
            # Verificar convergencia (si los centroides no cambian)
            if nuevos_centroides == centroides:
                break
                
            centroides = nuevos_centroides
        
        return clusters, centroides

    @classmethod
    def predecir(cls, punto, centroides):
        """Predice a qué cluster pertenece un nuevo punto."""
        distancias = [cls.distancia_euclidiana(punto, c) for c in centroides]
        return cls._indice_minimo(distancias)


# --- Función de prueba ---
    @staticmethod
    def ejecutar_agrupamiento(datos, k):
        clusters, centroides = Agrupamiento.ajustar(datos, k)
        print("\n--- Resultados ---")
        for i in range(len(clusters)):
            print(f"Cluster {i + 1} (Centroide: {centroides[i]}):")
            for punto in clusters[i]:
                print(f"  {punto}")
        print(f"\nCentroides finales: {centroides}")
