# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#programa.
    def visitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#importaciones.
    def visitImportaciones(self, ctx:gramaticaParser.ImportacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#importacion.
    def visitImportacion(self, ctx:gramaticaParser.ImportacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#instrucciones.
    def visitInstrucciones(self, ctx:gramaticaParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Dec.
    def visitDec(self, ctx:gramaticaParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Imp.
    def visitImp(self, ctx:gramaticaParser.ImpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Condi.
    def visitCondi(self, ctx:gramaticaParser.CondiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Asi.
    def visitAsi(self, ctx:gramaticaParser.AsiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#While.
    def visitWhile(self, ctx:gramaticaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#For.
    def visitFor(self, ctx:gramaticaParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#DefFunc.
    def visitDefFunc(self, ctx:gramaticaParser.DefFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#LlamadaFunc.
    def visitLlamadaFunc(self, ctx:gramaticaParser.LlamadaFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Ret.
    def visitRet(self, ctx:gramaticaParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#definicion_funcion.
    def visitDefinicion_funcion(self, ctx:gramaticaParser.Definicion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:gramaticaParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#argumentos.
    def visitArgumentos(self, ctx:gramaticaParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#bloque_funcion.
    def visitBloque_funcion(self, ctx:gramaticaParser.Bloque_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#retorno.
    def visitRetorno(self, ctx:gramaticaParser.RetornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#declaracion.
    def visitDeclaracion(self, ctx:gramaticaParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#impresion.
    def visitImpresion(self, ctx:gramaticaParser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#asignacion.
    def visitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condicion.
    def visitCondicion(self, ctx:gramaticaParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condicion_si_no.
    def visitCondicion_si_no(self, ctx:gramaticaParser.Condicion_si_noContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ciclo_for.
    def visitCiclo_for(self, ctx:gramaticaParser.Ciclo_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ciclo_while.
    def visitCiclo_while(self, ctx:gramaticaParser.Ciclo_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ExprLlamadaFunc.
    def visitExprLlamadaFunc(self, ctx:gramaticaParser.ExprLlamadaFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Par.
    def visitPar(self, ctx:gramaticaParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Suma.
    def visitSuma(self, ctx:gramaticaParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Palabras.
    def visitPalabras(self, ctx:gramaticaParser.PalabrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mod.
    def visitMod(self, ctx:gramaticaParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Mul.
    def visitMul(self, ctx:gramaticaParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ExprLlamadaMetodoLibreria.
    def visitExprLlamadaMetodoLibreria(self, ctx:gramaticaParser.ExprLlamadaMetodoLibreriaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Id.
    def visitId(self, ctx:gramaticaParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Negativo.
    def visitNegativo(self, ctx:gramaticaParser.NegativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Int.
    def visitInt(self, ctx:gramaticaParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Idsi.
    def visitIdsi(self, ctx:gramaticaParser.IdsiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Igu.
    def visitIgu(self, ctx:gramaticaParser.IguContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Intsi.
    def visitIntsi(self, ctx:gramaticaParser.IntsiContext):
        return self.visitChildren(ctx)



del gramaticaParser