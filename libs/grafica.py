class Grafica:

    @staticmethod
    def crear_canvas(ancho, alto):
        return [[' ' for _ in range(ancho)] for _ in range(alto)]

    

    @staticmethod
    def dibujar_linea(canvas, x0, y0, x1, y1, barra):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            if canvas[y0][x0] == ' ':
                canvas[y0][x0] = barra
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    @staticmethod
    def escalar(x_val, y_val, max_x, min_y, max_y, ancho, alto):
        col = int(x_val / max_x * (ancho - 10)) + 8
        rango_y = max_y - min_y
        row = alto - 1 - int((y_val - min_y) / rango_y * (alto - 1))
        return col, row

    @staticmethod
    def grafica_lineal(x, y, ancho=80, alto=20, color='white'):
        colores = {
            'red': '\033[91m*\033[0m',
            'white': '\033[97m*\033[0m',
            'green': '\033[92m*\033[0m',
            'blue': '\033[94m*\033[0m',
            'yellow': '\033[93m*\033[0m'
        }
        
        if len(x) != len(y):
            raise ValueError("x e y deben tener la misma longitud")
        x = list(map(float, x))
        y = list(map(float, y))
        max_x = max(x)
        min_x = min(x)
        max_y = max(y)
        min_y = min(y)

        # Escalado
        x_scaled = [int((xi - min_x) / (max_x - min_x) * (ancho - 10)) for xi in x]
        y_scaled = [int((yi - min_y) / (max_y - min_y) * (alto - 1)) for yi in y]

        # Crear la cuadrícula con espacios vacíos
        canvas = [[' ' for _ in range(ancho)] for _ in range(alto)]

        # Carácter coloreado para pintar
        bloque_color = colores.get(color, colores['white'])

        # Trazar líneas entre puntos usando '.'
        for i in range(1, len(x_scaled)):
            x0, y0 = x_scaled[i-1], y_scaled[i-1]
            x1, y1 = x_scaled[i], y_scaled[i]
            dx = abs(x1 - x0)
            dy = -abs(y1 - y0)
            sx = 1 if x0 < x1 else -1
            sy = 1 if y0 < y1 else -1
            err = dx + dy
            while True:
                if 0 <= alto - 1 - y0 < alto and 0 <= x0 < ancho:
                    # Para las líneas puedes usar '.' normal o una versión coloreada
                    # Aquí usaremos '.' normal para que no pierda definición
                    canvas[alto - 1 - y0][x0] = '.'
                if x0 == x1 and y0 == y1:
                    break
                e2 = 2 * err
                if e2 >= dy:
                    err += dy
                    x0 += sx
                if e2 <= dx:
                    err += dx
                    y0 += sy

        # Trazar puntos con bloque coloreado
        for i in range(len(x_scaled)):
            x_pos = x_scaled[i]
            y_pos = alto - 1 - y_scaled[i]
            if 0 <= y_pos < alto and 0 <= x_pos < ancho:
                canvas[y_pos][x_pos] = bloque_color

        # Imprimir la gráfica con ejes y etiquetas Y
        pasos_y = 5  # número de etiquetas Y
        for i in range(alto):
            valor_y = min_y + (max_y - min_y) * (alto - 1 - i) / (alto - 1)
            if i % (alto // pasos_y) == 0:
                etiqueta = f"{valor_y:>5.1f}"
            else:
                etiqueta = "     "
            print(f"{etiqueta} |{''.join(canvas[i])}")

        # Eje X
        print("      " + "-" * (ancho))

        # Etiquetas X
        pasos_x = 10
        x_labels = [min_x + (max_x - min_x) * i / pasos_x for i in range(pasos_x + 1)]
        x_pos = [int((val - min_x) / (max_x - min_x) * (ancho - 10)) for val in x_labels]
        label_line = [' '] * ancho
        for pos, val in zip(x_pos, x_labels):
            val_str = f"{val:.1f}"
            for i, c in enumerate(val_str):
                if 0 <= pos + i < ancho:
                    label_line[pos + i] = c
        print("      " + ''.join(label_line))
    @staticmethod
    def grafica_barras(x, y, color='white', ancho=40, alto=30):
        canvas = Grafica.crear_canvas(ancho, alto)
        max_x = max(x)
        max_y = max(y)
        min_y = min(y)

        if len(y) < len(x):
            y += [0] * (len(x) - len(y))

        colores = {
            'red': '\033[91m█\033[0m',
            'white': '\033[97m█\033[0m',
            'green': '\033[92m█\033[0m',
            'blue': '\033[94m█\033[0m',
            'yellow': '\033[93m█\033[0m'
        }
        barra = colores.get(color.lower(), '█')

        for i in range(len(x)):
            col, base_row = Grafica.escalar(x[i], 0, max_x, min_y, max_y, ancho, alto)
            _, top_row = Grafica.escalar(x[i], y[i], max_x, min_y, max_y, ancho, alto)
            for row in range(min(base_row, top_row), max(base_row, top_row) + 1):
                if 0 <= row < alto and 0 <= col < ancho:
                    canvas[row][col] = barra

        num_etiquetas_y = 10
        etiquetas_usadas = set()
        for n in range(num_etiquetas_y):
            y_val = min_y + (max_y - min_y) * n / (num_etiquetas_y - 1)
            row = alto - 1 - int((y_val - min_y) / (max_y - min_y) * (alto - 1))
            if row in etiquetas_usadas or not (0 <= row < alto):
                continue
            etiquetas_usadas.add(row)
            etiqueta = f"{round(y_val):>3} |"
            for j, char in enumerate(etiqueta):
                canvas[row][j] = char

        for i in range(alto):
            if i not in etiquetas_usadas:
                for j, char in enumerate("    |"):
                    canvas[i][j] = char

        x_line = [' '] * 8 + ['-' for _ in range(ancho - 8)]
        print(''.join(x_line))

        x_labels = [int(max_x * i / 10) for i in range(11)]
        x_pos = [int(i / max_x * (ancho - 10)) + 8 for i in x_labels]
        label_line = [' '] * ancho
        for pos, val in zip(x_pos, x_labels):
            for i, c in enumerate(str(val)):
                if pos + i < ancho:
                    label_line[pos + i] = c
        print(''.join(label_line))

        for fila in canvas:
            print(''.join(fila))
    @staticmethod
    def grafica_pastel(x, y, usar_colores=True):
        ancho = 40
        alto = 30
        canvas = Grafica.crear_canvas(ancho, alto)

        if len(x) < len(y):
            x += [0] * (len(y) - len(x))

        total = sum(x)
        g_p = 360 / total
        grados = []
        porcentaje = []
        radio = min(ancho, alto) // 2 - 1
        centro_x = ancho // 2
        centro_y = alto // 2

        colores = ['\033[91m█\033[0m', '\033[92m█\033[0m', '\033[94m█\033[0m', '\033[93m█\033[0m', '\033[95m█\033[0m']
        simbolos = ['@', '#', '*', '+', '%']

        def distancia(dx, dy):
            return (dx * dx + dy * dy) ** 0.5
        def atan2_aprox(dy, dx):
            from math import atan2, degrees

            ang = degrees(atan2(dy, dx))
            return (ang + 360) % 360

        acumulado = 0
        for valor in x:
            angulo = valor * g_p
            grados.append((acumulado, acumulado + angulo))
            acumulado += angulo
            porcentaje.append(valor / total * 100)

        for i in range(alto):
            for j in range(ancho):
                dx = j - centro_x
                dy = centro_y - i
                if distancia(dx, dy) <= radio:
                    ang = atan2_aprox(dy, dx)
                    for idx, (ini, fin) in enumerate(grados):
                        if ini <= ang < fin or (idx == len(grados) - 1 and ang <= fin):
                            char = colores[idx % len(colores)] if usar_colores else simbolos[idx % len(simbolos)]
                            canvas[i][j] = char
                            break

        print("\nLeyenda:")
        for idx, nombre in enumerate(y):
            marca = colores[idx % len(colores)] if usar_colores else simbolos[idx % len(simbolos)]
            print(f"  {marca} = {nombre} {porcentaje[idx]:.2f}%")

        print("\nGráfico pastel:\n")
        for fila in canvas:
            print(''.join(fila))
