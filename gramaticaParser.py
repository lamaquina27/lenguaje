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
        4,1,33,136,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,3,0,28,
        8,0,1,0,1,0,1,1,4,1,33,8,1,11,1,12,1,34,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,43,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,70,8,6,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,107,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,118,8,10,10,10,12,10,121,9,10,1,11,1,11,1,11,3,11,126,
        8,11,1,11,1,11,1,11,5,11,131,8,11,10,11,12,11,134,9,11,1,11,0,2,
        20,22,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,1,0,9,10,1,0,11,12,1,
        0,14,15,1,0,24,29,139,0,24,1,0,0,0,2,32,1,0,0,0,4,42,1,0,0,0,6,44,
        1,0,0,0,8,50,1,0,0,0,10,56,1,0,0,0,12,61,1,0,0,0,14,71,1,0,0,0,16,
        76,1,0,0,0,18,90,1,0,0,0,20,106,1,0,0,0,22,125,1,0,0,0,24,25,5,1,
        0,0,25,27,5,19,0,0,26,28,3,2,1,0,27,26,1,0,0,0,27,28,1,0,0,0,28,
        29,1,0,0,0,29,30,5,18,0,0,30,1,1,0,0,0,31,33,3,4,2,0,32,31,1,0,0,
        0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,43,3,
        6,3,0,37,43,3,8,4,0,38,43,3,12,6,0,39,43,3,10,5,0,40,43,3,18,9,0,
        41,43,3,16,8,0,42,36,1,0,0,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,
        0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,5,1,0,0,0,44,45,5,2,0,0,45,
        46,5,20,0,0,46,47,5,13,0,0,47,48,3,20,10,0,48,49,5,22,0,0,49,7,1,
        0,0,0,50,51,5,3,0,0,51,52,5,17,0,0,52,53,3,20,10,0,53,54,5,16,0,
        0,54,55,5,22,0,0,55,9,1,0,0,0,56,57,5,20,0,0,57,58,5,13,0,0,58,59,
        3,20,10,0,59,60,5,22,0,0,60,11,1,0,0,0,61,62,5,4,0,0,62,63,5,17,
        0,0,63,64,3,22,11,0,64,65,5,16,0,0,65,66,5,19,0,0,66,67,3,2,1,0,
        67,69,5,18,0,0,68,70,3,14,7,0,69,68,1,0,0,0,69,70,1,0,0,0,70,13,
        1,0,0,0,71,72,5,5,0,0,72,73,5,19,0,0,73,74,3,2,1,0,74,75,5,18,0,
        0,75,15,1,0,0,0,76,77,5,7,0,0,77,78,5,17,0,0,78,79,3,6,3,0,79,80,
        5,22,0,0,80,81,3,22,11,0,81,82,5,22,0,0,82,83,5,20,0,0,83,84,5,9,
        0,0,84,85,5,21,0,0,85,86,5,16,0,0,86,87,5,19,0,0,87,88,3,2,1,0,88,
        89,5,18,0,0,89,17,1,0,0,0,90,91,5,6,0,0,91,92,5,17,0,0,92,93,3,22,
        11,0,93,94,5,16,0,0,94,95,5,19,0,0,95,96,3,2,1,0,96,97,5,18,0,0,
        97,19,1,0,0,0,98,99,6,10,-1,0,99,100,5,17,0,0,100,101,3,20,10,0,
        101,102,5,16,0,0,102,107,1,0,0,0,103,107,5,21,0,0,104,107,5,8,0,
        0,105,107,5,20,0,0,106,98,1,0,0,0,106,103,1,0,0,0,106,104,1,0,0,
        0,106,105,1,0,0,0,107,119,1,0,0,0,108,109,10,7,0,0,109,110,7,0,0,
        0,110,118,3,20,10,8,111,112,10,6,0,0,112,113,7,1,0,0,113,118,3,20,
        10,7,114,115,10,5,0,0,115,116,7,2,0,0,116,118,3,20,10,6,117,108,
        1,0,0,0,117,111,1,0,0,0,117,114,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,21,1,0,0,0,121,119,1,0,0,0,122,123,6,
        11,-1,0,123,126,5,21,0,0,124,126,5,20,0,0,125,122,1,0,0,0,125,124,
        1,0,0,0,126,132,1,0,0,0,127,128,10,3,0,0,128,129,7,3,0,0,129,131,
        3,22,11,4,130,127,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,
        1,0,0,0,133,23,1,0,0,0,134,132,1,0,0,0,9,27,34,42,69,106,117,119,
        125,132
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'principal'", "'var'", "'mueche'", "'chi'", 
                     "'sino'", "'mientras'", "'para'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'='", "'%'", "'^'", "')'", "'('", 
                     "'}'", "'{'", "<INVALID>", "<INVALID>", "';'", "<INVALID>", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'&&'", 
                     "'||'", "'!'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "PRINCIPAL", "VAR", "MUECHE", "CHI", 
                      "SINO", "MIENTRAS", "PARA", "PALABRAS", "MAS", "MENOS", 
                      "MUL", "DIV", "IGUAL", "MODULO", "ELEVACION", "PAR_DER", 
                      "PAR_IZQ", "LLAVE_DER", "LLAVE_IZQ", "ID", "NUMERO", 
                      "PUNTO_COMA", "WS", "IGUALDAD", "DIFERENTE", "MAYOR", 
                      "MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", "AND", "OR", 
                      "NOT", "COMILLAS" ]

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
    RULE_expresion_si = 11

    ruleNames =  [ "programa", "instrucciones", "instruccion", "declaracion", 
                   "impresion", "asignacion", "condicion", "condicion_si_no", 
                   "ciclo_for", "ciclo_while", "expresion", "expresion_si" ]

    EOF = Token.EOF
    PRINCIPAL=1
    VAR=2
    MUECHE=3
    CHI=4
    SINO=5
    MIENTRAS=6
    PARA=7
    PALABRAS=8
    MAS=9
    MENOS=10
    MUL=11
    DIV=12
    IGUAL=13
    MODULO=14
    ELEVACION=15
    PAR_DER=16
    PAR_IZQ=17
    LLAVE_DER=18
    LLAVE_IZQ=19
    ID=20
    NUMERO=21
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
    NOT=32
    COMILLAS=33

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
            self.state = 24
            self.match(gramaticaParser.PRINCIPAL)
            self.state = 25
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1048796) != 0):
                self.state = 26
                self.instrucciones()


            self.state = 29
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
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.instruccion()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1048796) != 0)):
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = gramaticaParser.DecContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.declaracion()
                pass
            elif token in [3]:
                localctx = gramaticaParser.ImpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.impresion()
                pass
            elif token in [4]:
                localctx = gramaticaParser.CondiContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.condicion()
                pass
            elif token in [20]:
                localctx = gramaticaParser.AsiContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.asignacion()
                pass
            elif token in [6]:
                localctx = gramaticaParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.ciclo_while()
                pass
            elif token in [7]:
                localctx = gramaticaParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 41
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
            self.state = 44
            self.match(gramaticaParser.VAR)
            self.state = 45
            self.match(gramaticaParser.ID)
            self.state = 46
            self.match(gramaticaParser.IGUAL)
            self.state = 47
            self.expresion(0)
            self.state = 48
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
            self.state = 50
            self.match(gramaticaParser.MUECHE)
            self.state = 51
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 52
            self.expresion(0)
            self.state = 53
            self.match(gramaticaParser.PAR_DER)
            self.state = 54
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
            self.state = 56
            self.match(gramaticaParser.ID)
            self.state = 57
            self.match(gramaticaParser.IGUAL)
            self.state = 58
            self.expresion(0)
            self.state = 59
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
        self.enterRule(localctx, 12, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(gramaticaParser.CHI)
            self.state = 62
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 63
            self.expresion_si(0)
            self.state = 64
            self.match(gramaticaParser.PAR_DER)
            self.state = 65
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 66
            self.instrucciones()
            self.state = 67
            self.match(gramaticaParser.LLAVE_DER)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 68
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
            self.state = 71
            self.match(gramaticaParser.SINO)
            self.state = 72
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 73
            self.instrucciones()
            self.state = 74
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


        def PUNTO_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.PUNTO_COMA)
            else:
                return self.getToken(gramaticaParser.PUNTO_COMA, i)

        def expresion_si(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_siContext,0)


        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def MAS(self):
            return self.getToken(gramaticaParser.MAS, 0)

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

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
            self.state = 76
            self.match(gramaticaParser.PARA)
            self.state = 77
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 78
            self.declaracion()
            self.state = 79
            self.match(gramaticaParser.PUNTO_COMA)
            self.state = 80
            self.expresion_si(0)
            self.state = 81
            self.match(gramaticaParser.PUNTO_COMA)
            self.state = 82
            self.match(gramaticaParser.ID)
            self.state = 83
            self.match(gramaticaParser.MAS)
            self.state = 84
            self.match(gramaticaParser.NUMERO)
            self.state = 85
            self.match(gramaticaParser.PAR_DER)
            self.state = 86
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 87
            self.instrucciones()
            self.state = 88
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
        self.enterRule(localctx, 18, self.RULE_ciclo_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(gramaticaParser.MIENTRAS)
            self.state = 91
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 92
            self.expresion_si(0)
            self.state = 93
            self.match(gramaticaParser.PAR_DER)
            self.state = 94
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 95
            self.instrucciones()
            self.state = 96
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = gramaticaParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 99
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 100
                self.expresion(0)
                self.state = 101
                self.match(gramaticaParser.PAR_DER)
                pass
            elif token in [21]:
                localctx = gramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 103
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [8]:
                localctx = gramaticaParser.PalabrasContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(gramaticaParser.PALABRAS)
                pass
            elif token in [20]:
                localctx = gramaticaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.SumaContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 108
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 109
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 110
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.MulContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 111
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 112
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ModContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 114
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 115
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.expresion(6)
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expresion_si, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = gramaticaParser.IntsiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 123
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [20]:
                localctx = gramaticaParser.IdsiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 132
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.IguContext(self, gramaticaParser.Expresion_siContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_si)
                    self.state = 127
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 128
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 129
                    self.expresion_si(4) 
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self._predicates[10] = self.expresion_sempred
        self._predicates[11] = self.expresion_si_sempred
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
         




