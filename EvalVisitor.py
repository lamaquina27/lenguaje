from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor


class EvalVisitor(gramaticaVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}
    # devuelve el entero
    def visitInt(self,ctx):
        return int(ctx.NUMERO().getText())
    #devuelve la suma o la resta de los numeros 
    def visitSuma(self,ctx):
        izq=self.visit(ctx.expresion(0))
        der=self.visit(ctx.expresion(1))
        
        if ctx.op.type == gramaticaParser.MAS:
            
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
        
        return self.memory.get(nombre)
    def visitPrograma(self, ctx):
        return self.visitChildren(ctx)

    def visitInstrucciones(self, ctx):
        return self.visitChildren(ctx)
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

        condicion = self.visit(ctx.condicion().expresion_verdad())
        
        if condicion:
            self.visit(ctx.condicion().instrucciones())
        elif ctx.condicion().condicion_si_no() is not None:
            self.visit(ctx.condicion().condicion_si_no().instrucciones())

    def visitExpresion_si(self, ctx):
        return self.visitChildren(ctx)
    def visitVerdad(self,ctx):
        izq = self.visit(ctx.expresion_verdad(0))
        der = self.visit(ctx.expresion_verdad(1))
        
        if ctx.op.type == gramaticaParser.AND:
            return izq and der
        elif ctx.op.type == gramaticaParser.OR:
            return izq or der
    def visitParver(self,ctx):
        return self.visit(ctx.expresion_verdad()) 
        
    def visitIntsi(self,ctx):
        return self.visitInt(ctx)

    #---------------------------------------funcion visti para while-------------------------
    def visitWhile(self,ctx):
        condicion=self.visit(ctx.ciclo_while().expresion_verdad())
        if condicion:
            while(condicion):
                self.visit(ctx.ciclo_while().instrucciones())
                condicion=self.visit(ctx.ciclo_while().expresion_verdad())
    def visitFor(self,ctx):
            # Ejecuta la declaración: var x = 0;
        self.visit(ctx.ciclo_for().declaracion())

        # Ejecuta el bucle
        while self.visit(ctx.ciclo_for().expresion_si()):
            # Ejecuta las instrucciones del cuerpo
            self.visit(ctx.ciclo_for().instrucciones())
            
            # Ejecuta la asignación: x = x + 1;
            self.visit(ctx.ciclo_for().asignacion())
     
       