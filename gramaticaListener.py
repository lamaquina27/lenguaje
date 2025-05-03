# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#programa.
    def enterPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#programa.
    def exitPrograma(self, ctx:gramaticaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#importaciones.
    def enterImportaciones(self, ctx:gramaticaParser.ImportacionesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#importaciones.
    def exitImportaciones(self, ctx:gramaticaParser.ImportacionesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#importacion.
    def enterImportacion(self, ctx:gramaticaParser.ImportacionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#importacion.
    def exitImportacion(self, ctx:gramaticaParser.ImportacionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#instrucciones.
    def enterInstrucciones(self, ctx:gramaticaParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#instrucciones.
    def exitInstrucciones(self, ctx:gramaticaParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Dec.
    def enterDec(self, ctx:gramaticaParser.DecContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Dec.
    def exitDec(self, ctx:gramaticaParser.DecContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Imp.
    def enterImp(self, ctx:gramaticaParser.ImpContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Imp.
    def exitImp(self, ctx:gramaticaParser.ImpContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Condi.
    def enterCondi(self, ctx:gramaticaParser.CondiContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Condi.
    def exitCondi(self, ctx:gramaticaParser.CondiContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Asi.
    def enterAsi(self, ctx:gramaticaParser.AsiContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Asi.
    def exitAsi(self, ctx:gramaticaParser.AsiContext):
        pass


    # Enter a parse tree produced by gramaticaParser#While.
    def enterWhile(self, ctx:gramaticaParser.WhileContext):
        pass

    # Exit a parse tree produced by gramaticaParser#While.
    def exitWhile(self, ctx:gramaticaParser.WhileContext):
        pass


    # Enter a parse tree produced by gramaticaParser#For.
    def enterFor(self, ctx:gramaticaParser.ForContext):
        pass

    # Exit a parse tree produced by gramaticaParser#For.
    def exitFor(self, ctx:gramaticaParser.ForContext):
        pass


    # Enter a parse tree produced by gramaticaParser#DefFunc.
    def enterDefFunc(self, ctx:gramaticaParser.DefFuncContext):
        pass

    # Exit a parse tree produced by gramaticaParser#DefFunc.
    def exitDefFunc(self, ctx:gramaticaParser.DefFuncContext):
        pass


    # Enter a parse tree produced by gramaticaParser#LlamadaFunc.
    def enterLlamadaFunc(self, ctx:gramaticaParser.LlamadaFuncContext):
        pass

    # Exit a parse tree produced by gramaticaParser#LlamadaFunc.
    def exitLlamadaFunc(self, ctx:gramaticaParser.LlamadaFuncContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Ret.
    def enterRet(self, ctx:gramaticaParser.RetContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Ret.
    def exitRet(self, ctx:gramaticaParser.RetContext):
        pass


    # Enter a parse tree produced by gramaticaParser#definicion_funcion.
    def enterDefinicion_funcion(self, ctx:gramaticaParser.Definicion_funcionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#definicion_funcion.
    def exitDefinicion_funcion(self, ctx:gramaticaParser.Definicion_funcionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:gramaticaParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:gramaticaParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#argumentos.
    def enterArgumentos(self, ctx:gramaticaParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by gramaticaParser#argumentos.
    def exitArgumentos(self, ctx:gramaticaParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by gramaticaParser#bloque_funcion.
    def enterBloque_funcion(self, ctx:gramaticaParser.Bloque_funcionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#bloque_funcion.
    def exitBloque_funcion(self, ctx:gramaticaParser.Bloque_funcionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#retorno.
    def enterRetorno(self, ctx:gramaticaParser.RetornoContext):
        pass

    # Exit a parse tree produced by gramaticaParser#retorno.
    def exitRetorno(self, ctx:gramaticaParser.RetornoContext):
        pass


    # Enter a parse tree produced by gramaticaParser#declaracion.
    def enterDeclaracion(self, ctx:gramaticaParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#declaracion.
    def exitDeclaracion(self, ctx:gramaticaParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#impresion.
    def enterImpresion(self, ctx:gramaticaParser.ImpresionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#impresion.
    def exitImpresion(self, ctx:gramaticaParser.ImpresionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#asignacion.
    def enterAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#asignacion.
    def exitAsignacion(self, ctx:gramaticaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condicion.
    def enterCondicion(self, ctx:gramaticaParser.CondicionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condicion.
    def exitCondicion(self, ctx:gramaticaParser.CondicionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condicion_si_no.
    def enterCondicion_si_no(self, ctx:gramaticaParser.Condicion_si_noContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condicion_si_no.
    def exitCondicion_si_no(self, ctx:gramaticaParser.Condicion_si_noContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ciclo_for.
    def enterCiclo_for(self, ctx:gramaticaParser.Ciclo_forContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ciclo_for.
    def exitCiclo_for(self, ctx:gramaticaParser.Ciclo_forContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ciclo_while.
    def enterCiclo_while(self, ctx:gramaticaParser.Ciclo_whileContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ciclo_while.
    def exitCiclo_while(self, ctx:gramaticaParser.Ciclo_whileContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ExprLlamadaFunc.
    def enterExprLlamadaFunc(self, ctx:gramaticaParser.ExprLlamadaFuncContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ExprLlamadaFunc.
    def exitExprLlamadaFunc(self, ctx:gramaticaParser.ExprLlamadaFuncContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Par.
    def enterPar(self, ctx:gramaticaParser.ParContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Par.
    def exitPar(self, ctx:gramaticaParser.ParContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Suma.
    def enterSuma(self, ctx:gramaticaParser.SumaContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Suma.
    def exitSuma(self, ctx:gramaticaParser.SumaContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Palabras.
    def enterPalabras(self, ctx:gramaticaParser.PalabrasContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Palabras.
    def exitPalabras(self, ctx:gramaticaParser.PalabrasContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Mod.
    def enterMod(self, ctx:gramaticaParser.ModContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Mod.
    def exitMod(self, ctx:gramaticaParser.ModContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Mul.
    def enterMul(self, ctx:gramaticaParser.MulContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Mul.
    def exitMul(self, ctx:gramaticaParser.MulContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Id.
    def enterId(self, ctx:gramaticaParser.IdContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Id.
    def exitId(self, ctx:gramaticaParser.IdContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Int.
    def enterInt(self, ctx:gramaticaParser.IntContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Int.
    def exitInt(self, ctx:gramaticaParser.IntContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Idsi.
    def enterIdsi(self, ctx:gramaticaParser.IdsiContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Idsi.
    def exitIdsi(self, ctx:gramaticaParser.IdsiContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Igu.
    def enterIgu(self, ctx:gramaticaParser.IguContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Igu.
    def exitIgu(self, ctx:gramaticaParser.IguContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Intsi.
    def enterIntsi(self, ctx:gramaticaParser.IntsiContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Intsi.
    def exitIntsi(self, ctx:gramaticaParser.IntsiContext):
        pass



del gramaticaParser