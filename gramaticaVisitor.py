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


    # Visit a parse tree produced by gramaticaParser#Par.
    def visitPar(self, ctx:gramaticaParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Atomo_uno.
    def visitAtomo_uno(self, ctx:gramaticaParser.Atomo_unoContext):
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


    # Visit a parse tree produced by gramaticaParser#Verdad.
    def visitVerdad(self, ctx:gramaticaParser.VerdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Parver.
    def visitParver(self, ctx:gramaticaParser.ParverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Expver.
    def visitExpver(self, ctx:gramaticaParser.ExpverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Atomo_dos.
    def visitAtomo_dos(self, ctx:gramaticaParser.Atomo_dosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Igu.
    def visitIgu(self, ctx:gramaticaParser.IguContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Int.
    def visitInt(self, ctx:gramaticaParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Id.
    def visitId(self, ctx:gramaticaParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Intsi.
    def visitIntsi(self, ctx:gramaticaParser.IntsiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Idsi.
    def visitIdsi(self, ctx:gramaticaParser.IdsiContext):
        return self.visitChildren(ctx)



del gramaticaParser