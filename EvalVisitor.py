from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor


class EvalVisitor(gramaticaVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}

    def visitPalabras(self, ctx):
        string = ctx.getText()  # ya devuelve el contenido, por ejemplo: "<Hola>"
        return string [1:-1]
     
    # devuelve el entero
    def visitInt(self,ctx):
        return int(ctx.NUMERO().getText())
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
    def visitDec(self,ctx):
        variable = ctx.declaracion().ID().getText()
        
        valor = self.visit(ctx.declaracion().expresion())
        self.memory[variable] = valor
        
        return valor
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
        return None
    def visitAsi(self,ctx):
        nombre = ctx.asignacion().ID().getText()
        
        if self.memory[nombre]:
            valor = self.visit(ctx.asignacion().expresion())
            
            self.memory[nombre] = valor
            
            return self.memory[nombre]
        else:
            print("por favor declara la variable antes de")
            return 
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
        condicion=self.visit(ctx.ciclo_for().expresion_si())
        declaracion=self.visit(ctx.ciclo_for().declaracion())
