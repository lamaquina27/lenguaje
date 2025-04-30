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