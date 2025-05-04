from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor
from gramaticaLexer import gramaticaLexer
from antlr4 import InputStream
from antlr4 import CommonTokenStream
import importlib


class EvalVisitor(gramaticaVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}
        self.librerias = {}  # Nuevo diccionario para las librerías importadas
        self.funciones = {}


    #---------------funciones----------
    


    def parsear_instrucciones(self, bloque_texto):
        input_stream = InputStream(bloque_texto.strip('"'))  # Quitar comillas del bloque
        lexer = gramaticaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = gramaticaParser(token_stream)
        return parser.instrucciones()



    def visitDefFunc(self, ctx):
        definicion = ctx.getChild(0)  # Esto es definicion_funcionContext

        nombre = definicion.ID().getText()

        parametros = []
        if definicion.argumentos():
            parametros = [p.getText() for p in definicion.argumentos().expresion()]


        bloque_texto = definicion.BLOQUE_FUNCION().getText()
        instrucciones_ctx = self.parsear_instrucciones(bloque_texto)


        self.funciones[nombre] = {
            "parametros": parametros,
            "cuerpo": instrucciones_ctx
        }

        print(f"Función {nombre} definida con parámetros {parametros}")

        return None
    


    
    def visitLlamada_funcion(self, ctx):
        nombre = ctx.nombre.text
        argumentos = []

        if ctx.argumentos():
            argumentos = [self.visit(e) for e in ctx.argumentos().expresion()]

        # Función definida internamente
        if nombre in self.funciones:
            funcion = self.funciones[nombre]
            if len(funcion["parametros"]) != len(argumentos):
                raise Exception("Número incorrecto de argumentos.")
            
            memoria_anterior = self.memory.copy()
            self.valor_retorno = None  # <-- LIMPIAR retorno previo

            for param, arg in zip(funcion["parametros"], argumentos):
                self.memory[param] = arg
            self.visit(funcion["cuerpo"])
            resultado = self.valor_retorno  # <-- CAPTURAR retorno
            self.memory = memoria_anterior
            return resultado

        # Función en librerías
        for libreria in self.librerias.values():
            if hasattr(libreria, nombre):
                metodo = getattr(libreria, nombre)
                return metodo(*argumentos)

        raise Exception(f"Función '{nombre}' no encontrada.")

    

    """def visitLlamadaFunc(self, ctx):
        nombre = ctx.getChild(1).getText()
        if nombre is None:
            raise Exception("Error: llamada de función sin nombre.")

        argumentos = []

        if ctx.argumentos():
            argumentos = [self.visit(e) for e in ctx.argumentos().expresion()]

        # Verificar si es función interna
        if nombre in self.funciones:
            funcion = self.funciones[nombre]

            if len(funcion["parametros"]) != len(argumentos):
                raise Exception("Número incorrecto de argumentos.")

            # Guardar memoria temporal
            memoria_anterior = self.memory.copy()

            for param, arg in zip(funcion["parametros"], argumentos):
                self.memory[param] = arg

            # Ejecutar cuerpo
            self.visit(funcion["cuerpo"])

            # Restaurar memoria
            self.memory = memoria_anterior

            return None

        # Verificar si es librería
        for libreria in self.librerias.values():
            if hasattr(libreria, nombre):
                metodo = getattr(libreria, nombre)
                return metodo(*argumentos)

        raise Exception(f"Función '{nombre}' no encontrada.")



"""


    def visitExprLlamadaFunc(self, ctx):
        nombre = ctx.ID().getText()
        argumentos = []

        if ctx.argumentos():
            argumentos = [self.visit(e) for e in ctx.argumentos().expresion()]

        # Función interna
        if nombre in self.funciones:
            funcion = self.funciones[nombre]

            if len(funcion["parametros"]) != len(argumentos):
                raise Exception("Número incorrecto de argumentos.")

            memoria_anterior = self.memory.copy()
            self.valor_retorno = None

            for param, arg in zip(funcion["parametros"], argumentos):
                self.memory[param] = arg

            self.visit(funcion["cuerpo"])

            self.memory = memoria_anterior
            return self.valor_retorno

        # Función de librería
        for libreria in self.librerias.values():
            if hasattr(libreria, nombre):
                metodo = getattr(libreria, nombre)
                return metodo(*argumentos)

        raise Exception(f"Función '{nombre}' no encontrada.")


    
    def visitRet(self, ctx):
        valor = self.visit(ctx.retorno().expresion())
        self.valor_retorno = valor
        return valor



    #---------Libs----------------------------
    def visitImportacion(self, ctx):
        nombre_lib = ctx.ID().getText()
        try:
            modulo = importlib.import_module(f"libs.{nombre_lib}")

            # Intenta obtener la clase que tenga el mismo nombre que el módulo
            clase_libreria = getattr(modulo, nombre_lib.capitalize(), None)

            if clase_libreria is None:
                raise Exception(f"La librería {nombre_lib} no tiene una clase '{nombre_lib.capitalize()}'.")

            self.librerias[nombre_lib] = clase_libreria()
            print(f"Librería '{nombre_lib}' importada.")
        except Exception as e:
            print(f"Error al importar la librería {nombre_lib}: {e}")



    def visitExprLlamadaMetodoLibreria(self, ctx):
        libreria = ctx.ID(0).getText()
        metodo = ctx.ID(1).getText()

        argumentos = []
        if ctx.argumentos():
            argumentos = [self.visit(e) for e in ctx.argumentos().expresion()]

        if libreria not in self.librerias:
            raise Exception(f"Librería '{libreria}' no importada.")

        libreria_obj = self.librerias[libreria]

        if not hasattr(libreria_obj, metodo):
            raise Exception(f"La librería '{libreria}' no tiene el método '{metodo}'.")

        metodo_obj = getattr(libreria_obj, metodo)
        return metodo_obj(*argumentos)



    
    



    # devuelve el entero
    def visitInt(self,ctx):
        return int(ctx.NUMERO().getText())
    

    #texto
    def visitPalabras(self, ctx):
        texto = ctx.getText()  # Ejemplo: <Hola>
        
        # Remover solo < y >
        if texto.startswith('<') and texto.endswith('>'):
            texto = texto[1:-1]
        
        return texto
    

    #devuelve la suma o la resta de los numeros 
    def visitSuma(self,ctx):
        izq=self.visit(ctx.expresion(0))
        der=self.visit(ctx.expresion(1))
        
        if ctx.op.type == gramaticaParser.MAS:
            if isinstance(izq, str) or isinstance (der, str):
                return str(izq) + str(der)
            else:
                return izq + der
        else:
            return izq - der 

    #devuelve la multiplicacion o la division de los numeros 
    def visitMul(self,ctx):
        izq=self.visit(ctx.expresion(0))
        der=self.visit(ctx.expresion(1))
        if ctx.op.type == gramaticaParser.MUL:
            return izq * der
        else:
            return izq / der 
        

    #devuelve ell modulo o la potencia de los numeros 
    def visitMod(self,ctx):
        izq=self.visit(ctx.expresion(0))
        der=self.visit(ctx.expresion(1))
        if ctx.op.type == gramaticaParser.MODULO:
            return izq % der
        else:
            return izq ** der 
        

    #evaua la expresion de lo parentesis
    def visitPar(self,ctx):
    
        return self.visit(ctx.expresion())
    

    #guarda la variable en el diccionario de la memoria
    def visitDeclaracion(self, ctx):
        variable = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.memory[variable] = valor
        
        return self.memory[variable]

    def visitDec(self, ctx):
        
        return self.visit(ctx.declaracion())  # Esto ahora llama correctamente a visitDeclaracion

    #obtiene el valor de la variable almacenada
    def visitId(self, ctx):
        nombre = ctx.ID().getText()

        #cambios soporte libs
         # Si es una variable ya almacenada
        if nombre in self.memory:
            return self.memory[nombre]

        # Si no es variable, buscar en librerías importadas
        for libreria in self.librerias.values():
            if hasattr(libreria, nombre):
                metodo = getattr(libreria, nombre)
                return metodo()
        # Si no se encontró
        raise Exception(f"Variable o función '{nombre}' no definida.")
            
        #return self.memory.get(nombre)
    

    def visitPrograma(self, ctx):
        return self.visitChildren(ctx)

    def visitInstrucciones(self, ctx):
        for instr in ctx.instruccion():
            self.visit(instr)
    

    #imprime el valor de la expresion
    def visitImp(self, ctx):
        impre = self.visit(ctx.impresion().expresion())
        print(impre)
        return impre
    

    def visitAsignacion(self,ctx):
        nombre = ctx.ID().getText()
        
        if self.memory[nombre] or self.memory[nombre]==0 :
            valor = self.visit(ctx.expresion())
            
            self.memory[nombre] = valor
            
            return valor
        else:
            print("por favor declara la variable antes de")
            return 
        

    def visitAsi(self,ctx):
        return self.visit(ctx.asignacion())
    #------------------------------------funciones de expresion_si-----------------------------
    #obtiene el valor de la variable almacenada
    def visitIdsi(self, ctx):
        
        return self.visitId(ctx)
    
    #evalua si la expresion es == o !=
    def visitIgu(self, ctx):
        
        izq = self.visit(ctx.expresion_si(0))
        der = self.visit(ctx.expresion_si(1))
        
        if ctx.op.type == gramaticaParser.IGUALDAD:
            return izq == der
        elif ctx.op.type == gramaticaParser.DIFERENTE:
            return izq != der
        elif ctx.op.type == gramaticaParser.MAYOR:
            return izq > der
        elif ctx.op.type == gramaticaParser.MAYOR_IGUAL:
            return izq >= der
        elif ctx.op.type == gramaticaParser.MENOR:
            return izq < der
        elif ctx.op.type == gramaticaParser.MENOR_IGUAL:
            return izq <= der
        

    #se encarga de verificar si entra en el if o sigue en el else
    def visitCondi(self, ctx):

        condicion = self.visit(ctx.condicion().expresion_si())
        
        if condicion:
            self.visit(ctx.condicion().instrucciones())
        elif ctx.condicion().condicion_si_no() is not None:
            self.visit(ctx.condicion().condicion_si_no().instrucciones())

    def visitExpresion_si(self, ctx):
    
    
        return self.visitChildren(ctx)

    def visitIntsi(self,ctx):
        return self.visitInt(ctx)

    #---------------------------------------funcion visti para while-------------------------
    def visitWhile(self,ctx):
        condicion=self.visit(ctx.ciclo_while().expresion_si())
        if condicion:
            while(condicion):
                self.visit(ctx.ciclo_while().instrucciones())
                condicion=self.visit(ctx.ciclo_while().expresion_si())


    def visitFor(self,ctx):
            # Ejecuta la declaración: var x = 0;
        self.visit(ctx.ciclo_for().declaracion())

        # Ejecuta el bucle
        while self.visit(ctx.ciclo_for().expresion_si()):
            # Ejecuta las instrucciones del cuerpo
            self.visit(ctx.ciclo_for().instrucciones())
            
            # Ejecuta la asignación: x = x + 1;
            self.visit(ctx.ciclo_for().asignacion())

#-----------Cambio necesario para funcion basada en ejecución no lineal (Beta)

    def visitCiclo_While(self,ctx):
        condicion=self.visit(ctx.expresion_si())
        if condicion:
            while(condicion):
                self.visit(ctx.instrucciones())
                condicion=self.visit(ctx.expresion_si())


    def visitCiclo_For(self,ctx):
            # Ejecuta la declaración: var x = 0;
        self.visit(ctx.declaracion())

        # Ejecuta el bucle
        while self.visit(ctx.expresion_si()):
            # Ejecuta las instrucciones del cuerpo
            self.visit(ctx.instrucciones())
            
            # Ejecuta la asignación: x = x + 1;
            self.visit(ctx.asignacion())
     
       