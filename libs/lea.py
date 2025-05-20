class Lea:
    
    @staticmethod
    def leer(archivo):
        try:
            with open(archivo, 'r') as f:
                print(f.read())
        except Exception as e:
            raise Exception(f"Error al leer el archivo {archivo}: {str(e)}")

    @staticmethod
    def escribir(archivo, texto):
        try:
            with open(archivo, 'w') as f:
                f.write(texto)
        except Exception as e:
            raise Exception(f"Error al escribir en el archivo {archivo}: {str(e)}")

    @staticmethod
    def escribir_ultimo(archivo, texto):
        try:
            with open(archivo, 'a') as f:
                f.write(texto)
        except Exception as e:
            raise Exception(f"Error al agregar texto en el archivo {archivo}: {str(e)}")
