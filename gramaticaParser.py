# Generated from gramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,160,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,3,0,34,8,0,1,0,1,0,1,1,4,1,39,8,1,11,1,12,
        1,40,1,2,1,2,1,2,1,2,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,76,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,109,8,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,120,8,10,10,10,12,10,123,9,10,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,131,8,11,1,11,1,11,1,11,5,11,136,8,11,10,
        11,12,11,139,9,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,147,8,12,10,
        12,12,12,150,9,12,1,13,1,13,3,13,154,8,13,1,14,1,14,3,14,158,8,14,
        1,14,0,3,20,22,24,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,5,
        1,0,8,9,1,0,10,11,1,0,13,14,1,0,30,31,1,0,24,29,162,0,30,1,0,0,0,
        2,38,1,0,0,0,4,48,1,0,0,0,6,50,1,0,0,0,8,56,1,0,0,0,10,62,1,0,0,
        0,12,67,1,0,0,0,14,77,1,0,0,0,16,82,1,0,0,0,18,93,1,0,0,0,20,108,
        1,0,0,0,22,130,1,0,0,0,24,140,1,0,0,0,26,153,1,0,0,0,28,157,1,0,
        0,0,30,31,5,1,0,0,31,33,5,18,0,0,32,34,3,2,1,0,33,32,1,0,0,0,33,
        34,1,0,0,0,34,35,1,0,0,0,35,36,5,17,0,0,36,1,1,0,0,0,37,39,3,4,2,
        0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,3,1,
        0,0,0,42,49,3,6,3,0,43,49,3,8,4,0,44,49,3,12,6,0,45,49,3,10,5,0,
        46,49,3,18,9,0,47,49,3,16,8,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,
        1,0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,5,1,0,0,0,50,
        51,5,2,0,0,51,52,5,19,0,0,52,53,5,12,0,0,53,54,3,20,10,0,54,55,5,
        22,0,0,55,7,1,0,0,0,56,57,5,3,0,0,57,58,5,16,0,0,58,59,3,20,10,0,
        59,60,5,15,0,0,60,61,5,22,0,0,61,9,1,0,0,0,62,63,5,19,0,0,63,64,
        5,12,0,0,64,65,3,20,10,0,65,66,5,22,0,0,66,11,1,0,0,0,67,68,5,4,
        0,0,68,69,5,16,0,0,69,70,3,22,11,0,70,71,5,15,0,0,71,72,5,18,0,0,
        72,73,3,2,1,0,73,75,5,17,0,0,74,76,3,14,7,0,75,74,1,0,0,0,75,76,
        1,0,0,0,76,13,1,0,0,0,77,78,5,5,0,0,78,79,5,18,0,0,79,80,3,2,1,0,
        80,81,5,17,0,0,81,15,1,0,0,0,82,83,5,7,0,0,83,84,5,16,0,0,84,85,
        3,6,3,0,85,86,3,24,12,0,86,87,5,22,0,0,87,88,3,10,5,0,88,89,5,15,
        0,0,89,90,5,18,0,0,90,91,3,2,1,0,91,92,5,17,0,0,92,17,1,0,0,0,93,
        94,5,6,0,0,94,95,5,16,0,0,95,96,3,22,11,0,96,97,5,15,0,0,97,98,5,
        18,0,0,98,99,3,2,1,0,99,100,5,17,0,0,100,19,1,0,0,0,101,102,6,10,
        -1,0,102,103,5,16,0,0,103,104,3,20,10,0,104,105,5,15,0,0,105,109,
        1,0,0,0,106,109,5,21,0,0,107,109,3,26,13,0,108,101,1,0,0,0,108,106,
        1,0,0,0,108,107,1,0,0,0,109,121,1,0,0,0,110,111,10,6,0,0,111,112,
        7,0,0,0,112,120,3,20,10,7,113,114,10,5,0,0,114,115,7,1,0,0,115,120,
        3,20,10,6,116,117,10,4,0,0,117,118,7,2,0,0,118,120,3,20,10,5,119,
        110,1,0,0,0,119,113,1,0,0,0,119,116,1,0,0,0,120,123,1,0,0,0,121,
        119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,121,1,0,0,0,124,125,
        6,11,-1,0,125,126,5,16,0,0,126,127,3,22,11,0,127,128,5,15,0,0,128,
        131,1,0,0,0,129,131,3,24,12,0,130,124,1,0,0,0,130,129,1,0,0,0,131,
        137,1,0,0,0,132,133,10,3,0,0,133,134,7,3,0,0,134,136,3,22,11,4,135,
        132,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,
        23,1,0,0,0,139,137,1,0,0,0,140,141,6,12,-1,0,141,142,3,28,14,0,142,
        148,1,0,0,0,143,144,10,2,0,0,144,145,7,4,0,0,145,147,3,24,12,3,146,
        143,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,
        25,1,0,0,0,150,148,1,0,0,0,151,154,5,20,0,0,152,154,5,19,0,0,153,
        151,1,0,0,0,153,152,1,0,0,0,154,27,1,0,0,0,155,158,5,20,0,0,156,
        158,5,19,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,29,1,0,0,0,12,33,
        40,48,75,108,119,121,130,137,148,153,157
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'principal'", "'var'", "'mueche'", "'chi'", 
                     "'sino'", "'mientras'", "'para'", "'+'", "'-'", "'*'", 
                     "'/'", "'='", "'%'", "'^'", "')'", "'('", "'}'", "'{'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'", "<INVALID>", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", 
                     "'||'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "PRINCIPAL", "VAR", "MUECHE", "CHI", 
                      "SINO", "MIENTRAS", "PARA", "MAS", "MENOS", "MUL", 
                      "DIV", "IGUAL", "MODULO", "ELEVACION", "PAR_DER", 
                      "PAR_IZQ", "LLAVE_DER", "LLAVE_IZQ", "ID", "NUMERO", 
                      "PALABRAS", "PUNTO_COMA", "WS", "IGUALDAD", "DIFERENTE", 
                      "MAYOR", "MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", "AND", 
                      "OR", "COMILLAS", "STRING" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_declaracion = 3
    RULE_impresion = 4
    RULE_asignacion = 5
    RULE_condicion = 6
    RULE_condicion_si_no = 7
    RULE_ciclo_for = 8
    RULE_ciclo_while = 9
    RULE_expresion = 10
    RULE_expresion_verdad = 11
    RULE_expresion_si = 12
    RULE_atomo = 13
    RULE_atomo_si = 14

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "impresion", "asignacion", "condicion", "condicion_si_no", 
                   "ciclo_for", "ciclo_while", "expresion", "expresion_verdad", 
                   "expresion_si", "atomo", "atomo_si" ]

    EOF = Token.EOF
    PRINCIPAL=1
    VAR=2
    MUECHE=3
    CHI=4
    SINO=5
    MIENTRAS=6
    PARA=7
    MAS=8
    MENOS=9
    MUL=10
    DIV=11
    IGUAL=12
    MODULO=13
    ELEVACION=14
    PAR_DER=15
    PAR_IZQ=16
    LLAVE_DER=17
    LLAVE_IZQ=18
    ID=19
    NUMERO=20
    PALABRAS=21
    PUNTO_COMA=22
    WS=23
    IGUALDAD=24
    DIFERENTE=25
    MAYOR=26
    MENOR=27
    MAYOR_IGUAL=28
    MENOR_IGUAL=29
    AND=30
    OR=31
    COMILLAS=32
    STRING=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINCIPAL(self):
            return self.getToken(gramaticaParser.PRINCIPAL, 0)

        def LLAVE_IZQ(self):
            return self.getToken(gramaticaParser.LLAVE_IZQ, 0)

        def LLAVE_DER(self):
            return self.getToken(gramaticaParser.LLAVE_DER, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = gramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(gramaticaParser.PRINCIPAL)
            self.state = 31
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 524508) != 0):
                self.state = 32
                self.instrucciones()


            self.state = 35
            self.match(gramaticaParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = gramaticaParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.instruccion()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 524508) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DecContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def declaracion(self):
            return self.getTypedRuleContext(gramaticaParser.DeclaracionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec" ):
                return visitor.visitDec(self)
            else:
                return visitor.visitChildren(self)


    class CondiContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicion(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondi" ):
                listener.enterCondi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondi" ):
                listener.exitCondi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondi" ):
                return visitor.visitCondi(self)
            else:
                return visitor.visitChildren(self)


    class AsiContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asignacion(self):
            return self.getTypedRuleContext(gramaticaParser.AsignacionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsi" ):
                listener.enterAsi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsi" ):
                listener.exitAsi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsi" ):
                return visitor.visitAsi(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ciclo_for(self):
            return self.getTypedRuleContext(gramaticaParser.Ciclo_forContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ciclo_while(self):
            return self.getTypedRuleContext(gramaticaParser.Ciclo_whileContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class ImpContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def impresion(self):
            return self.getTypedRuleContext(gramaticaParser.ImpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImp" ):
                listener.enterImp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImp" ):
                listener.exitImp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImp" ):
                return visitor.visitImp(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = gramaticaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = gramaticaParser.DecContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.declaracion()
                pass
            elif token in [3]:
                localctx = gramaticaParser.ImpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.impresion()
                pass
            elif token in [4]:
                localctx = gramaticaParser.CondiContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.condicion()
                pass
            elif token in [19]:
                localctx = gramaticaParser.AsiContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.asignacion()
                pass
            elif token in [6]:
                localctx = gramaticaParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.ciclo_while()
                pass
            elif token in [7]:
                localctx = gramaticaParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.ciclo_for()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(gramaticaParser.VAR, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def IGUAL(self):
            return self.getToken(gramaticaParser.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = gramaticaParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(gramaticaParser.VAR)
            self.state = 51
            self.match(gramaticaParser.ID)
            self.state = 52
            self.match(gramaticaParser.IGUAL)
            self.state = 53
            self.expresion(0)
            self.state = 54
            self.match(gramaticaParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUECHE(self):
            return self.getToken(gramaticaParser.MUECHE, 0)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = gramaticaParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(gramaticaParser.MUECHE)
            self.state = 57
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 58
            self.expresion(0)
            self.state = 59
            self.match(gramaticaParser.PAR_DER)
            self.state = 60
            self.match(gramaticaParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def IGUAL(self):
            return self.getToken(gramaticaParser.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(gramaticaParser.ID)
            self.state = 63
            self.match(gramaticaParser.IGUAL)
            self.state = 64
            self.expresion(0)
            self.state = 65
            self.match(gramaticaParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHI(self):
            return self.getToken(gramaticaParser.CHI, 0)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)

        def expresion_verdad(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_verdadContext,0)


        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def LLAVE_IZQ(self):
            return self.getToken(gramaticaParser.LLAVE_IZQ, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,0)


        def LLAVE_DER(self):
            return self.getToken(gramaticaParser.LLAVE_DER, 0)

        def condicion_si_no(self):
            return self.getTypedRuleContext(gramaticaParser.Condicion_si_noContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = gramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(gramaticaParser.CHI)
            self.state = 68
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 69
            self.expresion_verdad(0)
            self.state = 70
            self.match(gramaticaParser.PAR_DER)
            self.state = 71
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 72
            self.instrucciones()
            self.state = 73
            self.match(gramaticaParser.LLAVE_DER)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 74
                self.condicion_si_no()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condicion_si_noContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(gramaticaParser.SINO, 0)

        def LLAVE_IZQ(self):
            return self.getToken(gramaticaParser.LLAVE_IZQ, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,0)


        def LLAVE_DER(self):
            return self.getToken(gramaticaParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_condicion_si_no

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion_si_no" ):
                listener.enterCondicion_si_no(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion_si_no" ):
                listener.exitCondicion_si_no(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion_si_no" ):
                return visitor.visitCondicion_si_no(self)
            else:
                return visitor.visitChildren(self)




    def condicion_si_no(self):

        localctx = gramaticaParser.Condicion_si_noContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion_si_no)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(gramaticaParser.SINO)
            self.state = 78
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 79
            self.instrucciones()
            self.state = 80
            self.match(gramaticaParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ciclo_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(gramaticaParser.PARA, 0)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)

        def declaracion(self):
            return self.getTypedRuleContext(gramaticaParser.DeclaracionContext,0)


        def expresion_si(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_siContext,0)


        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def asignacion(self):
            return self.getTypedRuleContext(gramaticaParser.AsignacionContext,0)


        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def LLAVE_IZQ(self):
            return self.getToken(gramaticaParser.LLAVE_IZQ, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,0)


        def LLAVE_DER(self):
            return self.getToken(gramaticaParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_ciclo_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo_for" ):
                listener.enterCiclo_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo_for" ):
                listener.exitCiclo_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo_for" ):
                return visitor.visitCiclo_for(self)
            else:
                return visitor.visitChildren(self)




    def ciclo_for(self):

        localctx = gramaticaParser.Ciclo_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ciclo_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(gramaticaParser.PARA)
            self.state = 83
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 84
            self.declaracion()
            self.state = 85
            self.expresion_si(0)
            self.state = 86
            self.match(gramaticaParser.PUNTO_COMA)
            self.state = 87
            self.asignacion()
            self.state = 88
            self.match(gramaticaParser.PAR_DER)
            self.state = 89
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 90
            self.instrucciones()
            self.state = 91
            self.match(gramaticaParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ciclo_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(gramaticaParser.MIENTRAS, 0)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)

        def expresion_verdad(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_verdadContext,0)


        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def LLAVE_IZQ(self):
            return self.getToken(gramaticaParser.LLAVE_IZQ, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,0)


        def LLAVE_DER(self):
            return self.getToken(gramaticaParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_ciclo_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo_while" ):
                listener.enterCiclo_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo_while" ):
                listener.exitCiclo_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo_while" ):
                return visitor.visitCiclo_while(self)
            else:
                return visitor.visitChildren(self)




    def ciclo_while(self):

        localctx = gramaticaParser.Ciclo_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ciclo_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(gramaticaParser.MIENTRAS)
            self.state = 94
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 95
            self.expresion_verdad(0)
            self.state = 96
            self.match(gramaticaParser.PAR_DER)
            self.state = 97
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 98
            self.instrucciones()
            self.state = 99
            self.match(gramaticaParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)

        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class Atomo_unoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomo(self):
            return self.getTypedRuleContext(gramaticaParser.AtomoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomo_uno" ):
                listener.enterAtomo_uno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomo_uno" ):
                listener.exitAtomo_uno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomo_uno" ):
                return visitor.visitAtomo_uno(self)
            else:
                return visitor.visitChildren(self)


    class SumaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)

        def MAS(self):
            return self.getToken(gramaticaParser.MAS, 0)
        def MENOS(self):
            return self.getToken(gramaticaParser.MENOS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class PalabrasContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PALABRAS(self):
            return self.getToken(gramaticaParser.PALABRAS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPalabras" ):
                listener.enterPalabras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPalabras" ):
                listener.exitPalabras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPalabras" ):
                return visitor.visitPalabras(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)

        def MODULO(self):
            return self.getToken(gramaticaParser.MODULO, 0)
        def ELEVACION(self):
            return self.getToken(gramaticaParser.ELEVACION, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(gramaticaParser.MUL, 0)
        def DIV(self):
            return self.getToken(gramaticaParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = gramaticaParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 103
                self.expresion(0)
                self.state = 104
                self.match(gramaticaParser.PAR_DER)
                pass
            elif token in [21]:
                localctx = gramaticaParser.PalabrasContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(gramaticaParser.PALABRAS)
                pass
            elif token in [19, 20]:
                localctx = gramaticaParser.Atomo_unoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.atomo()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.SumaContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expresion(7)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.MulContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 113
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expresion(6)
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ModContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 116
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expresion(5)
                        pass

             
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expresion_verdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_expresion_verdad

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VerdadContext(Expresion_verdadContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_verdadContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion_verdad(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Expresion_verdadContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Expresion_verdadContext,i)

        def AND(self):
            return self.getToken(gramaticaParser.AND, 0)
        def OR(self):
            return self.getToken(gramaticaParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerdad" ):
                listener.enterVerdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerdad" ):
                listener.exitVerdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerdad" ):
                return visitor.visitVerdad(self)
            else:
                return visitor.visitChildren(self)


    class ParverContext(Expresion_verdadContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_verdadContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)
        def expresion_verdad(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_verdadContext,0)

        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParver" ):
                listener.enterParver(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParver" ):
                listener.exitParver(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParver" ):
                return visitor.visitParver(self)
            else:
                return visitor.visitChildren(self)


    class ExpverContext(Expresion_verdadContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_verdadContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion_si(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_siContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpver" ):
                listener.enterExpver(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpver" ):
                listener.exitExpver(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpver" ):
                return visitor.visitExpver(self)
            else:
                return visitor.visitChildren(self)



    def expresion_verdad(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Expresion_verdadContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expresion_verdad, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = gramaticaParser.ParverContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 125
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 126
                self.expresion_verdad(0)
                self.state = 127
                self.match(gramaticaParser.PAR_DER)
                pass
            elif token in [19, 20]:
                localctx = gramaticaParser.ExpverContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.expresion_si(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.VerdadContext(self, gramaticaParser.Expresion_verdadContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_verdad)
                    self.state = 132
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 133
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==30 or _la==31):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.expresion_verdad(4) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expresion_siContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_expresion_si

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Atomo_dosContext(Expresion_siContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_siContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomo_si(self):
            return self.getTypedRuleContext(gramaticaParser.Atomo_siContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomo_dos" ):
                listener.enterAtomo_dos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomo_dos" ):
                listener.exitAtomo_dos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomo_dos" ):
                return visitor.visitAtomo_dos(self)
            else:
                return visitor.visitChildren(self)


    class IguContext(Expresion_siContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_siContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion_si(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Expresion_siContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Expresion_siContext,i)

        def IGUALDAD(self):
            return self.getToken(gramaticaParser.IGUALDAD, 0)
        def DIFERENTE(self):
            return self.getToken(gramaticaParser.DIFERENTE, 0)
        def MAYOR(self):
            return self.getToken(gramaticaParser.MAYOR, 0)
        def MAYOR_IGUAL(self):
            return self.getToken(gramaticaParser.MAYOR_IGUAL, 0)
        def MENOR(self):
            return self.getToken(gramaticaParser.MENOR, 0)
        def MENOR_IGUAL(self):
            return self.getToken(gramaticaParser.MENOR_IGUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgu" ):
                listener.enterIgu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgu" ):
                listener.exitIgu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgu" ):
                return visitor.visitIgu(self)
            else:
                return visitor.visitChildren(self)



    def expresion_si(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Expresion_siContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expresion_si, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = gramaticaParser.Atomo_dosContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 141
            self.atomo_si()
            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.IguContext(self, gramaticaParser.Expresion_siContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_si)
                    self.state = 143
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 144
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 145
                    self.expresion_si(3) 
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_atomo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdContext(AtomoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.AtomoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(AtomoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.AtomoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def atomo(self):

        localctx = gramaticaParser.AtomoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_atomo)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = gramaticaParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [19]:
                localctx = gramaticaParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomo_siContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticaParser.RULE_atomo_si

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdsiContext(Atomo_siContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Atomo_siContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdsi" ):
                listener.enterIdsi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdsi" ):
                listener.exitIdsi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdsi" ):
                return visitor.visitIdsi(self)
            else:
                return visitor.visitChildren(self)


    class IntsiContext(Atomo_siContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Atomo_siContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntsi" ):
                listener.enterIntsi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntsi" ):
                listener.exitIntsi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntsi" ):
                return visitor.visitIntsi(self)
            else:
                return visitor.visitChildren(self)



    def atomo_si(self):

        localctx = gramaticaParser.Atomo_siContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_atomo_si)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = gramaticaParser.IntsiContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [19]:
                localctx = gramaticaParser.IdsiContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expresion_sempred
        self._predicates[11] = self.expresion_verdad_sempred
        self._predicates[12] = self.expresion_si_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

    def expresion_verdad_sempred(self, localctx:Expresion_verdadContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

    def expresion_si_sempred(self, localctx:Expresion_siContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




