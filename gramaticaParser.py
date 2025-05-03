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
        4,1,41,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,1,0,1,
        0,3,0,43,8,0,1,0,1,0,1,1,4,1,48,8,1,11,1,12,1,49,1,2,1,2,1,2,1,2,
        1,3,4,3,57,8,3,11,3,12,3,58,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        69,8,4,1,5,1,5,1,5,1,5,3,5,75,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,
        6,84,8,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,92,8,7,10,7,12,7,95,9,7,1,8,
        1,8,3,8,99,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,128,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,162,
        8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,173,8,16,
        10,16,12,16,176,9,16,1,17,1,17,1,17,3,17,181,8,17,1,17,1,17,1,17,
        5,17,186,8,17,10,17,12,17,189,9,17,1,17,0,2,32,34,18,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,0,4,1,0,15,16,1,0,17,18,1,0,
        20,21,1,0,32,37,196,0,37,1,0,0,0,2,47,1,0,0,0,4,51,1,0,0,0,6,56,
        1,0,0,0,8,68,1,0,0,0,10,70,1,0,0,0,12,79,1,0,0,0,14,88,1,0,0,0,16,
        96,1,0,0,0,18,102,1,0,0,0,20,108,1,0,0,0,22,114,1,0,0,0,24,119,1,
        0,0,0,26,129,1,0,0,0,28,134,1,0,0,0,30,145,1,0,0,0,32,161,1,0,0,
        0,34,180,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,37,38,1,0,0,0,38,39,
        1,0,0,0,39,40,5,1,0,0,40,42,5,25,0,0,41,43,3,6,3,0,42,41,1,0,0,0,
        42,43,1,0,0,0,43,44,1,0,0,0,44,45,5,24,0,0,45,1,1,0,0,0,46,48,3,
        4,2,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,
        3,1,0,0,0,51,52,5,9,0,0,52,53,5,26,0,0,53,54,5,29,0,0,54,5,1,0,0,
        0,55,57,3,8,4,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,7,1,0,0,0,60,69,3,18,9,0,61,69,3,20,10,0,62,69,3,24,12,
        0,63,69,3,22,11,0,64,69,3,30,15,0,65,69,3,28,14,0,66,69,3,10,5,0,
        67,69,3,12,6,0,68,60,1,0,0,0,68,61,1,0,0,0,68,62,1,0,0,0,68,63,1,
        0,0,0,68,64,1,0,0,0,68,65,1,0,0,0,68,66,1,0,0,0,68,67,1,0,0,0,69,
        9,1,0,0,0,70,71,5,10,0,0,71,72,5,26,0,0,72,74,5,14,0,0,73,75,3,14,
        7,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,13,0,0,77,
        78,5,8,0,0,78,11,1,0,0,0,79,80,5,12,0,0,80,81,5,26,0,0,81,83,5,23,
        0,0,82,84,3,14,7,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,
        86,5,22,0,0,86,87,5,29,0,0,87,13,1,0,0,0,88,93,3,32,16,0,89,90,5,
        29,0,0,90,92,3,32,16,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,
        93,94,1,0,0,0,94,15,1,0,0,0,95,93,1,0,0,0,96,98,5,41,0,0,97,99,3,
        6,3,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,41,0,
        0,101,17,1,0,0,0,102,103,5,2,0,0,103,104,5,26,0,0,104,105,5,19,0,
        0,105,106,3,32,16,0,106,107,5,29,0,0,107,19,1,0,0,0,108,109,5,3,
        0,0,109,110,5,23,0,0,110,111,3,32,16,0,111,112,5,22,0,0,112,113,
        5,29,0,0,113,21,1,0,0,0,114,115,5,26,0,0,115,116,5,19,0,0,116,117,
        3,32,16,0,117,118,5,29,0,0,118,23,1,0,0,0,119,120,5,4,0,0,120,121,
        5,23,0,0,121,122,3,34,17,0,122,123,5,22,0,0,123,124,5,25,0,0,124,
        125,3,6,3,0,125,127,5,24,0,0,126,128,3,26,13,0,127,126,1,0,0,0,127,
        128,1,0,0,0,128,25,1,0,0,0,129,130,5,5,0,0,130,131,5,25,0,0,131,
        132,3,6,3,0,132,133,5,24,0,0,133,27,1,0,0,0,134,135,5,7,0,0,135,
        136,5,23,0,0,136,137,3,18,9,0,137,138,3,34,17,0,138,139,5,29,0,0,
        139,140,3,22,11,0,140,141,5,22,0,0,141,142,5,25,0,0,142,143,3,6,
        3,0,143,144,5,24,0,0,144,29,1,0,0,0,145,146,5,6,0,0,146,147,5,23,
        0,0,147,148,3,34,17,0,148,149,5,22,0,0,149,150,5,25,0,0,150,151,
        3,6,3,0,151,152,5,24,0,0,152,31,1,0,0,0,153,154,6,16,-1,0,154,155,
        5,23,0,0,155,156,3,32,16,0,156,157,5,22,0,0,157,162,1,0,0,0,158,
        162,5,27,0,0,159,162,5,28,0,0,160,162,5,26,0,0,161,153,1,0,0,0,161,
        158,1,0,0,0,161,159,1,0,0,0,161,160,1,0,0,0,162,174,1,0,0,0,163,
        164,10,7,0,0,164,165,7,0,0,0,165,173,3,32,16,8,166,167,10,6,0,0,
        167,168,7,1,0,0,168,173,3,32,16,7,169,170,10,5,0,0,170,171,7,2,0,
        0,171,173,3,32,16,6,172,163,1,0,0,0,172,166,1,0,0,0,172,169,1,0,
        0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,33,1,0,0,
        0,176,174,1,0,0,0,177,178,6,17,-1,0,178,181,5,27,0,0,179,181,5,26,
        0,0,180,177,1,0,0,0,180,179,1,0,0,0,181,187,1,0,0,0,182,183,10,3,
        0,0,183,184,7,3,0,0,184,186,3,34,17,4,185,182,1,0,0,0,186,189,1,
        0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,35,1,0,0,0,189,187,1,0,
        0,0,15,37,42,49,58,68,74,83,93,98,127,161,172,174,180,187
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'principal'", "'var'", "'mueche'", "'chi'", 
                     "'sino'", "'mientras'", "'para'", "<INVALID>", "'traigase'", 
                     "'funca'", "'.'", "'..'", "'?'", "'\\u00BF'", "'+'", 
                     "'-'", "'*'", "'/'", "'='", "'%'", "'^'", "')'", "'('", 
                     "'}'", "'{'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "<INVALID>", "<INVALID>", "'=='", "'!='", "'>'", 
                     "'<'", "'>='", "'<='", "'&&'", "'||'", "'!'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "PRINCIPAL", "VAR", "MUECHE", "CHI", 
                      "SINO", "MIENTRAS", "PARA", "BLOQUE_FUNCION", "TRAIGASE", 
                      "FUNCA", "PUNTO", "PUNTOPUNTO", "PREG_DER", "PREG_IZQ", 
                      "MAS", "MENOS", "MUL", "DIV", "IGUAL", "MODULO", "ELEVACION", 
                      "PAR_DER", "PAR_IZQ", "LLAVE_DER", "LLAVE_IZQ", "ID", 
                      "NUMERO", "PALABRAS", "PUNTO_COMA", "NL", "WS", "IGUALDAD", 
                      "DIFERENTE", "MAYOR", "MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", 
                      "AND", "OR", "NOT", "COMILLAS" ]

    RULE_programa = 0
    RULE_importaciones = 1
    RULE_importacion = 2
    RULE_instrucciones = 3
    RULE_instruccion = 4
    RULE_definicion_funcion = 5
    RULE_llamada_funcion = 6
    RULE_argumentos = 7
    RULE_bloque_funcion = 8
    RULE_declaracion = 9
    RULE_impresion = 10
    RULE_asignacion = 11
    RULE_condicion = 12
    RULE_condicion_si_no = 13
    RULE_ciclo_for = 14
    RULE_ciclo_while = 15
    RULE_expresion = 16
    RULE_expresion_si = 17

    ruleNames =  [ "programa", "importaciones", "importacion", "instrucciones", 
                   "instruccion", "definicion_funcion", "llamada_funcion", 
                   "argumentos", "bloque_funcion", "declaracion", "impresion", 
                   "asignacion", "condicion", "condicion_si_no", "ciclo_for", 
                   "ciclo_while", "expresion", "expresion_si" ]

    EOF = Token.EOF
    PRINCIPAL=1
    VAR=2
    MUECHE=3
    CHI=4
    SINO=5
    MIENTRAS=6
    PARA=7
    BLOQUE_FUNCION=8
    TRAIGASE=9
    FUNCA=10
    PUNTO=11
    PUNTOPUNTO=12
    PREG_DER=13
    PREG_IZQ=14
    MAS=15
    MENOS=16
    MUL=17
    DIV=18
    IGUAL=19
    MODULO=20
    ELEVACION=21
    PAR_DER=22
    PAR_IZQ=23
    LLAVE_DER=24
    LLAVE_IZQ=25
    ID=26
    NUMERO=27
    PALABRAS=28
    PUNTO_COMA=29
    NL=30
    WS=31
    IGUALDAD=32
    DIFERENTE=33
    MAYOR=34
    MENOR=35
    MAYOR_IGUAL=36
    MENOR_IGUAL=37
    AND=38
    OR=39
    NOT=40
    COMILLAS=41

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

        def importaciones(self):
            return self.getTypedRuleContext(gramaticaParser.ImportacionesContext,0)


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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 36
                self.importaciones()


            self.state = 39
            self.match(gramaticaParser.PRINCIPAL)
            self.state = 40
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67114204) != 0):
                self.state = 41
                self.instrucciones()


            self.state = 44
            self.match(gramaticaParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ImportacionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ImportacionContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_importaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportaciones" ):
                listener.enterImportaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportaciones" ):
                listener.exitImportaciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportaciones" ):
                return visitor.visitImportaciones(self)
            else:
                return visitor.visitChildren(self)




    def importaciones(self):

        localctx = gramaticaParser.ImportacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.importacion()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRAIGASE(self):
            return self.getToken(gramaticaParser.TRAIGASE, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_importacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportacion" ):
                listener.enterImportacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportacion" ):
                listener.exitImportacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportacion" ):
                return visitor.visitImportacion(self)
            else:
                return visitor.visitChildren(self)




    def importacion(self):

        localctx = gramaticaParser.ImportacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(gramaticaParser.TRAIGASE)
            self.state = 52
            self.match(gramaticaParser.ID)
            self.state = 53
            self.match(gramaticaParser.PUNTO_COMA)
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
        self.enterRule(localctx, 6, self.RULE_instrucciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.instruccion()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67114204) != 0)):
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


    class DefFuncContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def definicion_funcion(self):
            return self.getTypedRuleContext(gramaticaParser.Definicion_funcionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefFunc" ):
                listener.enterDefFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefFunc" ):
                listener.exitDefFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefFunc" ):
                return visitor.visitDefFunc(self)
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


    class LlamadaFuncContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def llamada_funcion(self):
            return self.getTypedRuleContext(gramaticaParser.Llamada_funcionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFunc" ):
                listener.enterLlamadaFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFunc" ):
                listener.exitLlamadaFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFunc" ):
                return visitor.visitLlamadaFunc(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = gramaticaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruccion)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = gramaticaParser.DecContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.declaracion()
                pass
            elif token in [3]:
                localctx = gramaticaParser.ImpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.impresion()
                pass
            elif token in [4]:
                localctx = gramaticaParser.CondiContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.condicion()
                pass
            elif token in [26]:
                localctx = gramaticaParser.AsiContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.asignacion()
                pass
            elif token in [6]:
                localctx = gramaticaParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.ciclo_while()
                pass
            elif token in [7]:
                localctx = gramaticaParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.ciclo_for()
                pass
            elif token in [10]:
                localctx = gramaticaParser.DefFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.definicion_funcion()
                pass
            elif token in [12]:
                localctx = gramaticaParser.LlamadaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 67
                self.llamada_funcion()
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


    class Definicion_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCA(self):
            return self.getToken(gramaticaParser.FUNCA, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def PREG_IZQ(self):
            return self.getToken(gramaticaParser.PREG_IZQ, 0)

        def PREG_DER(self):
            return self.getToken(gramaticaParser.PREG_DER, 0)

        def BLOQUE_FUNCION(self):
            return self.getToken(gramaticaParser.BLOQUE_FUNCION, 0)

        def argumentos(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_definicion_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicion_funcion" ):
                listener.enterDefinicion_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicion_funcion" ):
                listener.exitDefinicion_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicion_funcion" ):
                return visitor.visitDefinicion_funcion(self)
            else:
                return visitor.visitChildren(self)




    def definicion_funcion(self):

        localctx = gramaticaParser.Definicion_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_definicion_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(gramaticaParser.FUNCA)
            self.state = 71
            self.match(gramaticaParser.ID)
            self.state = 72
            self.match(gramaticaParser.PREG_IZQ)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 478150656) != 0):
                self.state = 73
                self.argumentos()


            self.state = 76
            self.match(gramaticaParser.PREG_DER)
            self.state = 77
            self.match(gramaticaParser.BLOQUE_FUNCION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nombre = None # Token

        def PUNTOPUNTO(self):
            return self.getToken(gramaticaParser.PUNTOPUNTO, 0)

        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)

        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def argumentos(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion" ):
                return visitor.visitLlamada_funcion(self)
            else:
                return visitor.visitChildren(self)




    def llamada_funcion(self):

        localctx = gramaticaParser.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_llamada_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(gramaticaParser.PUNTOPUNTO)
            self.state = 80
            localctx.nombre = self.match(gramaticaParser.ID)
            self.state = 81
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 478150656) != 0):
                self.state = 82
                self.argumentos()


            self.state = 85
            self.match(gramaticaParser.PAR_DER)
            self.state = 86
            self.match(gramaticaParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def PUNTO_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.PUNTO_COMA)
            else:
                return self.getToken(gramaticaParser.PUNTO_COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = gramaticaParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.expresion(0)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 89
                self.match(gramaticaParser.PUNTO_COMA)
                self.state = 90
                self.expresion(0)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloque_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMILLAS(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMILLAS)
            else:
                return self.getToken(gramaticaParser.COMILLAS, i)

        def instrucciones(self):
            return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_bloque_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque_funcion" ):
                listener.enterBloque_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque_funcion" ):
                listener.exitBloque_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque_funcion" ):
                return visitor.visitBloque_funcion(self)
            else:
                return visitor.visitChildren(self)




    def bloque_funcion(self):

        localctx = gramaticaParser.Bloque_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloque_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(gramaticaParser.COMILLAS)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67114204) != 0):
                self.state = 97
                self.instrucciones()


            self.state = 100
            self.match(gramaticaParser.COMILLAS)
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
        self.enterRule(localctx, 18, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(gramaticaParser.VAR)
            self.state = 103
            self.match(gramaticaParser.ID)
            self.state = 104
            self.match(gramaticaParser.IGUAL)
            self.state = 105
            self.expresion(0)
            self.state = 106
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
        self.enterRule(localctx, 20, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(gramaticaParser.MUECHE)
            self.state = 109
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 110
            self.expresion(0)
            self.state = 111
            self.match(gramaticaParser.PAR_DER)
            self.state = 112
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
        self.enterRule(localctx, 22, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(gramaticaParser.ID)
            self.state = 115
            self.match(gramaticaParser.IGUAL)
            self.state = 116
            self.expresion(0)
            self.state = 117
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

        def expresion_si(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_siContext,0)


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
        self.enterRule(localctx, 24, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(gramaticaParser.CHI)
            self.state = 120
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 121
            self.expresion_si(0)
            self.state = 122
            self.match(gramaticaParser.PAR_DER)
            self.state = 123
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 124
            self.instrucciones()
            self.state = 125
            self.match(gramaticaParser.LLAVE_DER)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 126
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
        self.enterRule(localctx, 26, self.RULE_condicion_si_no)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(gramaticaParser.SINO)
            self.state = 130
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 131
            self.instrucciones()
            self.state = 132
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
        self.enterRule(localctx, 28, self.RULE_ciclo_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(gramaticaParser.PARA)
            self.state = 135
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 136
            self.declaracion()
            self.state = 137
            self.expresion_si(0)
            self.state = 138
            self.match(gramaticaParser.PUNTO_COMA)
            self.state = 139
            self.asignacion()
            self.state = 140
            self.match(gramaticaParser.PAR_DER)
            self.state = 141
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 142
            self.instrucciones()
            self.state = 143
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

        def expresion_si(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_siContext,0)


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
        self.enterRule(localctx, 30, self.RULE_ciclo_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(gramaticaParser.MIENTRAS)
            self.state = 146
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 147
            self.expresion_si(0)
            self.state = 148
            self.match(gramaticaParser.PAR_DER)
            self.state = 149
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 150
            self.instrucciones()
            self.state = 151
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


    class IdContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
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


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
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



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = gramaticaParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 154
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 155
                self.expresion(0)
                self.state = 156
                self.match(gramaticaParser.PAR_DER)
                pass
            elif token in [27]:
                localctx = gramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [28]:
                localctx = gramaticaParser.PalabrasContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(gramaticaParser.PALABRAS)
                pass
            elif token in [26]:
                localctx = gramaticaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 172
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.SumaContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 163
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 164
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 165
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.MulContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 166
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 167
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ModContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 169
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 170
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 171
                        self.expresion(6)
                        pass

             
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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


    class IdsiContext(Expresion_siContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_siContext
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


    class IntsiContext(Expresion_siContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.Expresion_siContext
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



    def expresion_si(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.Expresion_siContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expresion_si, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = gramaticaParser.IntsiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 178
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [26]:
                localctx = gramaticaParser.IdsiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.IguContext(self, gramaticaParser.Expresion_siContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_si)
                    self.state = 182
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 183
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 270582939648) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 184
                    self.expresion_si(4) 
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expresion_sempred
        self._predicates[17] = self.expresion_si_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

    def expresion_si_sempred(self, localctx:Expresion_siContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




