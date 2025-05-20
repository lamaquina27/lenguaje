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
        4,1,45,265,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,
        1,0,1,0,3,0,56,8,0,1,0,1,0,1,1,4,1,61,8,1,11,1,12,1,62,1,2,1,2,1,
        2,1,2,1,3,4,3,70,8,3,11,3,12,3,71,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,87,8,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,5,
        1,5,1,5,1,5,3,5,99,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,108,8,6,1,
        6,1,6,1,6,1,7,1,7,1,7,5,7,116,8,7,10,7,12,7,119,9,7,1,8,1,8,3,8,
        123,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,156,8,13,1,14,1,14,1,14,1,14,1,
        14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,5,17,187,
        8,17,10,17,12,17,190,9,17,3,17,192,8,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,3,17,203,8,17,1,17,1,17,1,17,1,17,1,17,3,17,
        210,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,220,8,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,231,8,17,10,17,12,
        17,234,9,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,242,8,18,1,18,1,18,
        1,18,5,18,247,8,18,10,18,12,18,250,9,18,1,19,1,19,1,19,3,19,255,
        8,19,1,19,1,19,1,19,5,19,260,8,19,10,19,12,19,263,9,19,1,19,0,3,
        34,36,38,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,0,5,1,0,17,18,1,0,19,20,1,0,22,23,1,0,42,43,1,0,36,41,282,0,43,
        1,0,0,0,2,60,1,0,0,0,4,64,1,0,0,0,6,69,1,0,0,0,8,92,1,0,0,0,10,94,
        1,0,0,0,12,103,1,0,0,0,14,112,1,0,0,0,16,120,1,0,0,0,18,126,1,0,
        0,0,20,130,1,0,0,0,22,136,1,0,0,0,24,142,1,0,0,0,26,147,1,0,0,0,
        28,157,1,0,0,0,30,162,1,0,0,0,32,173,1,0,0,0,34,219,1,0,0,0,36,241,
        1,0,0,0,38,254,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,45,1,0,0,0,
        43,41,1,0,0,0,43,44,1,0,0,0,44,49,1,0,0,0,45,43,1,0,0,0,46,48,3,
        6,3,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,
        52,1,0,0,0,51,49,1,0,0,0,52,53,5,2,0,0,53,55,5,27,0,0,54,56,3,6,
        3,0,55,54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,26,0,0,58,
        1,1,0,0,0,59,61,3,4,2,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,
        0,62,63,1,0,0,0,63,3,1,0,0,0,64,65,5,11,0,0,65,66,5,30,0,0,66,67,
        5,33,0,0,67,5,1,0,0,0,68,70,3,8,4,0,69,68,1,0,0,0,70,71,1,0,0,0,
        71,69,1,0,0,0,71,72,1,0,0,0,72,7,1,0,0,0,73,93,3,20,10,0,74,93,3,
        22,11,0,75,93,3,26,13,0,76,93,3,24,12,0,77,93,3,32,16,0,78,93,3,
        30,15,0,79,93,3,10,5,0,80,81,5,14,0,0,81,82,5,30,0,0,82,83,5,13,
        0,0,83,84,5,30,0,0,84,86,5,25,0,0,85,87,3,14,7,0,86,85,1,0,0,0,86,
        87,1,0,0,0,87,88,1,0,0,0,88,89,5,24,0,0,89,93,5,33,0,0,90,93,3,12,
        6,0,91,93,3,18,9,0,92,73,1,0,0,0,92,74,1,0,0,0,92,75,1,0,0,0,92,
        76,1,0,0,0,92,77,1,0,0,0,92,78,1,0,0,0,92,79,1,0,0,0,92,80,1,0,0,
        0,92,90,1,0,0,0,92,91,1,0,0,0,93,9,1,0,0,0,94,95,5,12,0,0,95,96,
        5,30,0,0,96,98,5,16,0,0,97,99,3,14,7,0,98,97,1,0,0,0,98,99,1,0,0,
        0,99,100,1,0,0,0,100,101,5,15,0,0,101,102,5,10,0,0,102,11,1,0,0,
        0,103,104,5,14,0,0,104,105,5,30,0,0,105,107,5,25,0,0,106,108,3,14,
        7,0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,5,24,
        0,0,110,111,5,33,0,0,111,13,1,0,0,0,112,117,3,34,17,0,113,114,5,
        33,0,0,114,116,3,34,17,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,15,1,0,0,0,119,117,1,0,0,0,120,122,5,
        45,0,0,121,123,3,6,3,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,
        0,0,0,124,125,5,45,0,0,125,17,1,0,0,0,126,127,5,9,0,0,127,128,3,
        34,17,0,128,129,5,33,0,0,129,19,1,0,0,0,130,131,5,3,0,0,131,132,
        5,30,0,0,132,133,5,21,0,0,133,134,3,34,17,0,134,135,5,33,0,0,135,
        21,1,0,0,0,136,137,5,4,0,0,137,138,5,25,0,0,138,139,3,34,17,0,139,
        140,5,24,0,0,140,141,5,33,0,0,141,23,1,0,0,0,142,143,5,30,0,0,143,
        144,5,21,0,0,144,145,3,34,17,0,145,146,5,33,0,0,146,25,1,0,0,0,147,
        148,5,5,0,0,148,149,5,25,0,0,149,150,3,36,18,0,150,151,5,24,0,0,
        151,152,5,27,0,0,152,153,3,6,3,0,153,155,5,26,0,0,154,156,3,28,14,
        0,155,154,1,0,0,0,155,156,1,0,0,0,156,27,1,0,0,0,157,158,5,6,0,0,
        158,159,5,27,0,0,159,160,3,6,3,0,160,161,5,26,0,0,161,29,1,0,0,0,
        162,163,5,8,0,0,163,164,5,25,0,0,164,165,3,20,10,0,165,166,3,36,
        18,0,166,167,5,33,0,0,167,168,3,24,12,0,168,169,5,24,0,0,169,170,
        5,27,0,0,170,171,3,6,3,0,171,172,5,26,0,0,172,31,1,0,0,0,173,174,
        5,7,0,0,174,175,5,25,0,0,175,176,3,36,18,0,176,177,5,24,0,0,177,
        178,5,27,0,0,178,179,3,6,3,0,179,180,5,26,0,0,180,33,1,0,0,0,181,
        182,6,17,-1,0,182,191,5,29,0,0,183,188,3,34,17,0,184,185,5,1,0,0,
        185,187,3,34,17,0,186,184,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,
        0,188,189,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,191,183,1,0,0,
        0,191,192,1,0,0,0,192,193,1,0,0,0,193,220,5,28,0,0,194,195,5,18,
        0,0,195,220,3,34,17,7,196,197,5,14,0,0,197,198,5,30,0,0,198,199,
        5,13,0,0,199,200,5,30,0,0,200,202,5,25,0,0,201,203,3,14,7,0,202,
        201,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,220,5,24,0,0,205,
        206,5,14,0,0,206,207,5,30,0,0,207,209,5,25,0,0,208,210,3,14,7,0,
        209,208,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,220,5,24,0,0,
        212,213,5,25,0,0,213,214,3,34,17,0,214,215,5,24,0,0,215,220,1,0,
        0,0,216,220,5,31,0,0,217,220,5,32,0,0,218,220,5,30,0,0,219,181,1,
        0,0,0,219,194,1,0,0,0,219,196,1,0,0,0,219,205,1,0,0,0,219,212,1,
        0,0,0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,232,1,
        0,0,0,221,222,10,11,0,0,222,223,7,0,0,0,223,231,3,34,17,12,224,225,
        10,10,0,0,225,226,7,1,0,0,226,231,3,34,17,11,227,228,10,9,0,0,228,
        229,7,2,0,0,229,231,3,34,17,10,230,221,1,0,0,0,230,224,1,0,0,0,230,
        227,1,0,0,0,231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,
        35,1,0,0,0,234,232,1,0,0,0,235,236,6,18,-1,0,236,237,5,25,0,0,237,
        238,3,36,18,0,238,239,5,24,0,0,239,242,1,0,0,0,240,242,3,38,19,0,
        241,235,1,0,0,0,241,240,1,0,0,0,242,248,1,0,0,0,243,244,10,3,0,0,
        244,245,7,3,0,0,245,247,3,36,18,4,246,243,1,0,0,0,247,250,1,0,0,
        0,248,246,1,0,0,0,248,249,1,0,0,0,249,37,1,0,0,0,250,248,1,0,0,0,
        251,252,6,19,-1,0,252,255,5,31,0,0,253,255,5,30,0,0,254,251,1,0,
        0,0,254,253,1,0,0,0,255,261,1,0,0,0,256,257,10,3,0,0,257,258,7,4,
        0,0,258,260,3,38,19,4,259,256,1,0,0,0,260,263,1,0,0,0,261,259,1,
        0,0,0,261,262,1,0,0,0,262,39,1,0,0,0,263,261,1,0,0,0,23,43,49,55,
        62,71,86,92,98,107,117,122,155,188,191,202,209,219,230,232,241,248,
        254,261
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'inicio'", "'var'", "'mueche'", 
                     "'chi'", "'sino'", "'mientras'", "'para'", "'mandele'", 
                     "<INVALID>", "'traigase'", "'funca'", "'.'", "'..'", 
                     "'?'", "'\\u00BF'", "'+'", "'-'", "'*'", "'/'", "'='", 
                     "'%'", "'^'", "')'", "'('", "'}'", "'{'", "']'", "'['", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "';'", "<INVALID>", 
                     "<INVALID>", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'&&'", "'||'", "'!'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PRINCIPAL", "VAR", "MUECHE", 
                      "CHI", "SINO", "MIENTRAS", "PARA", "MANDELE", "BLOQUE_FUNCION", 
                      "TRAIGASE", "FUNCA", "PUNTO", "PUNTOPUNTO", "PREG_DER", 
                      "PREG_IZQ", "MAS", "MENOS", "MUL", "DIV", "IGUAL", 
                      "MODULO", "ELEVACION", "PAR_DER", "PAR_IZQ", "LLAVE_DER", 
                      "LLAVE_IZQ", "COR_DER", "COR_IZQ", "ID", "NUMERO", 
                      "PALABRAS", "PUNTO_COMA", "NL", "WS", "IGUALDAD", 
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
    RULE_retorno = 9
    RULE_declaracion = 10
    RULE_impresion = 11
    RULE_asignacion = 12
    RULE_condicion = 13
    RULE_condicion_si_no = 14
    RULE_ciclo_for = 15
    RULE_ciclo_while = 16
    RULE_expresion = 17
    RULE_expresion_verdad = 18
    RULE_expresion_si = 19

    ruleNames =  [ "programa", "importaciones", "importacion", "instrucciones", 
                   "instruccion", "definicion_funcion", "llamada_funcion", 
                   "argumentos", "bloque_funcion", "retorno", "declaracion", 
                   "impresion", "asignacion", "condicion", "condicion_si_no", 
                   "ciclo_for", "ciclo_while", "expresion", "expresion_verdad", 
                   "expresion_si" ]

    EOF = Token.EOF
    T__0=1
    PRINCIPAL=2
    VAR=3
    MUECHE=4
    CHI=5
    SINO=6
    MIENTRAS=7
    PARA=8
    MANDELE=9
    BLOQUE_FUNCION=10
    TRAIGASE=11
    FUNCA=12
    PUNTO=13
    PUNTOPUNTO=14
    PREG_DER=15
    PREG_IZQ=16
    MAS=17
    MENOS=18
    MUL=19
    DIV=20
    IGUAL=21
    MODULO=22
    ELEVACION=23
    PAR_DER=24
    PAR_IZQ=25
    LLAVE_DER=26
    LLAVE_IZQ=27
    COR_DER=28
    COR_IZQ=29
    ID=30
    NUMERO=31
    PALABRAS=32
    PUNTO_COMA=33
    NL=34
    WS=35
    IGUALDAD=36
    DIFERENTE=37
    MAYOR=38
    MENOR=39
    MAYOR_IGUAL=40
    MENOR_IGUAL=41
    AND=42
    OR=43
    NOT=44
    COMILLAS=45

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

        def importaciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ImportacionesContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ImportacionesContext,i)


        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.InstruccionesContext,i)


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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 40
                self.importaciones()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073763256) != 0):
                self.state = 46
                self.instrucciones()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(gramaticaParser.PRINCIPAL)
            self.state = 53
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073763256) != 0):
                self.state = 54
                self.instrucciones()


            self.state = 57
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 59
                    self.importacion()

                else:
                    raise NoViableAltException(self)
                self.state = 62 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            self.state = 64
            self.match(gramaticaParser.TRAIGASE)
            self.state = 65
            self.match(gramaticaParser.ID)
            self.state = 66
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 68
                    self.instruccion()

                else:
                    raise NoViableAltException(self)
                self.state = 71 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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



    class RetContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def retorno(self):
            return self.getTypedRuleContext(gramaticaParser.RetornoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)


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


    class ExprLlamadaMetodoLibContext(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUNTOPUNTO(self):
            return self.getToken(gramaticaParser.PUNTOPUNTO, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)
        def PUNTO(self):
            return self.getToken(gramaticaParser.PUNTO, 0)
        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)
        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)
        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)
        def argumentos(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLlamadaMetodoLib" ):
                listener.enterExprLlamadaMetodoLib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLlamadaMetodoLib" ):
                listener.exitExprLlamadaMetodoLib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamadaMetodoLib" ):
                return visitor.visitExprLlamadaMetodoLib(self)
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
        self._la = 0 # Token type
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.DecContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.declaracion()
                pass

            elif la_ == 2:
                localctx = gramaticaParser.ImpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.impresion()
                pass

            elif la_ == 3:
                localctx = gramaticaParser.CondiContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.condicion()
                pass

            elif la_ == 4:
                localctx = gramaticaParser.AsiContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.asignacion()
                pass

            elif la_ == 5:
                localctx = gramaticaParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.ciclo_while()
                pass

            elif la_ == 6:
                localctx = gramaticaParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.ciclo_for()
                pass

            elif la_ == 7:
                localctx = gramaticaParser.DefFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.definicion_funcion()
                pass

            elif la_ == 8:
                localctx = gramaticaParser.ExprLlamadaMetodoLibContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.match(gramaticaParser.PUNTOPUNTO)
                self.state = 81
                self.match(gramaticaParser.ID)
                self.state = 82
                self.match(gramaticaParser.PUNTO)
                self.state = 83
                self.match(gramaticaParser.ID)
                self.state = 84
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8086896640) != 0):
                    self.state = 85
                    self.argumentos()


                self.state = 88
                self.match(gramaticaParser.PAR_DER)
                self.state = 89
                self.match(gramaticaParser.PUNTO_COMA)
                pass

            elif la_ == 9:
                localctx = gramaticaParser.LlamadaFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 90
                self.llamada_funcion()
                pass

            elif la_ == 10:
                localctx = gramaticaParser.RetContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 91
                self.retorno()
                pass


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
            self.state = 94
            self.match(gramaticaParser.FUNCA)
            self.state = 95
            self.match(gramaticaParser.ID)
            self.state = 96
            self.match(gramaticaParser.PREG_IZQ)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8086896640) != 0):
                self.state = 97
                self.argumentos()


            self.state = 100
            self.match(gramaticaParser.PREG_DER)
            self.state = 101
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
            self.state = 103
            self.match(gramaticaParser.PUNTOPUNTO)
            self.state = 104
            localctx.nombre = self.match(gramaticaParser.ID)
            self.state = 105
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8086896640) != 0):
                self.state = 106
                self.argumentos()


            self.state = 109
            self.match(gramaticaParser.PAR_DER)
            self.state = 110
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
            self.state = 112
            self.expresion(0)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 113
                self.match(gramaticaParser.PUNTO_COMA)
                self.state = 114
                self.expresion(0)
                self.state = 119
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
            self.state = 120
            self.match(gramaticaParser.COMILLAS)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073763256) != 0):
                self.state = 121
                self.instrucciones()


            self.state = 124
            self.match(gramaticaParser.COMILLAS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MANDELE(self):
            return self.getToken(gramaticaParser.MANDELE, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(gramaticaParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = gramaticaParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(gramaticaParser.MANDELE)
            self.state = 127
            self.expresion(0)
            self.state = 128
            self.match(gramaticaParser.PUNTO_COMA)
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
        self.enterRule(localctx, 20, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(gramaticaParser.VAR)
            self.state = 131
            self.match(gramaticaParser.ID)
            self.state = 132
            self.match(gramaticaParser.IGUAL)
            self.state = 133
            self.expresion(0)
            self.state = 134
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
        self.enterRule(localctx, 22, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(gramaticaParser.MUECHE)
            self.state = 137
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 138
            self.expresion(0)
            self.state = 139
            self.match(gramaticaParser.PAR_DER)
            self.state = 140
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
        self.enterRule(localctx, 24, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(gramaticaParser.ID)
            self.state = 143
            self.match(gramaticaParser.IGUAL)
            self.state = 144
            self.expresion(0)
            self.state = 145
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
        self.enterRule(localctx, 26, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(gramaticaParser.CHI)
            self.state = 148
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 149
            self.expresion_verdad(0)
            self.state = 150
            self.match(gramaticaParser.PAR_DER)
            self.state = 151
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 152
            self.instrucciones()
            self.state = 153
            self.match(gramaticaParser.LLAVE_DER)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 154
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
        self.enterRule(localctx, 28, self.RULE_condicion_si_no)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(gramaticaParser.SINO)
            self.state = 158
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 159
            self.instrucciones()
            self.state = 160
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


        def expresion_verdad(self):
            return self.getTypedRuleContext(gramaticaParser.Expresion_verdadContext,0)


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
        self.enterRule(localctx, 30, self.RULE_ciclo_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(gramaticaParser.PARA)
            self.state = 163
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 164
            self.declaracion()
            self.state = 165
            self.expresion_verdad(0)
            self.state = 166
            self.match(gramaticaParser.PUNTO_COMA)
            self.state = 167
            self.asignacion()
            self.state = 168
            self.match(gramaticaParser.PAR_DER)
            self.state = 169
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 170
            self.instrucciones()
            self.state = 171
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
        self.enterRule(localctx, 32, self.RULE_ciclo_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(gramaticaParser.MIENTRAS)
            self.state = 174
            self.match(gramaticaParser.PAR_IZQ)
            self.state = 175
            self.expresion_verdad(0)
            self.state = 176
            self.match(gramaticaParser.PAR_DER)
            self.state = 177
            self.match(gramaticaParser.LLAVE_IZQ)
            self.state = 178
            self.instrucciones()
            self.state = 179
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


    class ExprLlamadaFuncContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUNTOPUNTO(self):
            return self.getToken(gramaticaParser.PUNTOPUNTO, 0)
        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)
        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)
        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)
        def argumentos(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLlamadaFunc" ):
                listener.enterExprLlamadaFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLlamadaFunc" ):
                listener.exitExprLlamadaFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamadaFunc" ):
                return visitor.visitExprLlamadaFunc(self)
            else:
                return visitor.visitChildren(self)


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


    class ListaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COR_IZQ(self):
            return self.getToken(gramaticaParser.COR_IZQ, 0)
        def COR_DER(self):
            return self.getToken(gramaticaParser.COR_DER, 0)
        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
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


    class ExprLlamadaMetodoLibreriaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUNTOPUNTO(self):
            return self.getToken(gramaticaParser.PUNTOPUNTO, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)
        def PUNTO(self):
            return self.getToken(gramaticaParser.PUNTO, 0)
        def PAR_IZQ(self):
            return self.getToken(gramaticaParser.PAR_IZQ, 0)
        def PAR_DER(self):
            return self.getToken(gramaticaParser.PAR_DER, 0)
        def argumentos(self):
            return self.getTypedRuleContext(gramaticaParser.ArgumentosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLlamadaMetodoLibreria" ):
                listener.enterExprLlamadaMetodoLibreria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLlamadaMetodoLibreria" ):
                listener.exitExprLlamadaMetodoLibreria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamadaMetodoLibreria" ):
                return visitor.visitExprLlamadaMetodoLibreria(self)
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


    class NegativoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MENOS(self):
            return self.getToken(gramaticaParser.MENOS, 0)
        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativo" ):
                return visitor.visitNegativo(self)
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = gramaticaParser.ListaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 182
                self.match(gramaticaParser.COR_IZQ)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8086896640) != 0):
                    self.state = 183
                    self.expresion(0)
                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 184
                        self.match(gramaticaParser.T__0)
                        self.state = 185
                        self.expresion(0)
                        self.state = 190
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 193
                self.match(gramaticaParser.COR_DER)
                pass

            elif la_ == 2:
                localctx = gramaticaParser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 194
                self.match(gramaticaParser.MENOS)
                self.state = 195
                self.expresion(7)
                pass

            elif la_ == 3:
                localctx = gramaticaParser.ExprLlamadaMetodoLibreriaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                self.match(gramaticaParser.PUNTOPUNTO)
                self.state = 197
                self.match(gramaticaParser.ID)
                self.state = 198
                self.match(gramaticaParser.PUNTO)
                self.state = 199
                self.match(gramaticaParser.ID)
                self.state = 200
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8086896640) != 0):
                    self.state = 201
                    self.argumentos()


                self.state = 204
                self.match(gramaticaParser.PAR_DER)
                pass

            elif la_ == 4:
                localctx = gramaticaParser.ExprLlamadaFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                self.match(gramaticaParser.PUNTOPUNTO)
                self.state = 206
                self.match(gramaticaParser.ID)
                self.state = 207
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8086896640) != 0):
                    self.state = 208
                    self.argumentos()


                self.state = 211
                self.match(gramaticaParser.PAR_DER)
                pass

            elif la_ == 5:
                localctx = gramaticaParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 212
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 213
                self.expresion(0)
                self.state = 214
                self.match(gramaticaParser.PAR_DER)
                pass

            elif la_ == 6:
                localctx = gramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 216
                self.match(gramaticaParser.NUMERO)
                pass

            elif la_ == 7:
                localctx = gramaticaParser.PalabrasContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 217
                self.match(gramaticaParser.PALABRAS)
                pass

            elif la_ == 8:
                localctx = gramaticaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 218
                self.match(gramaticaParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 230
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.SumaContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 221
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 222
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 223
                        self.expresion(12)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.MulContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 224
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 225
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 226
                        self.expresion(11)
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ModContext(self, gramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 227
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 228
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 229
                        self.expresion(10)
                        pass

             
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expresion_verdad, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = gramaticaParser.ParverContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 236
                self.match(gramaticaParser.PAR_IZQ)
                self.state = 237
                self.expresion_verdad(0)
                self.state = 238
                self.match(gramaticaParser.PAR_DER)
                pass
            elif token in [30, 31]:
                localctx = gramaticaParser.ExpverContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 240
                self.expresion_si(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.VerdadContext(self, gramaticaParser.Expresion_verdadContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_verdad)
                    self.state = 243
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 244
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==42 or _la==43):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.expresion_verdad(4) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expresion_si, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = gramaticaParser.IntsiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 252
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [30]:
                localctx = gramaticaParser.IdsiContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 253
                self.match(gramaticaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 261
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.IguContext(self, gramaticaParser.Expresion_siContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion_si)
                    self.state = 256
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 257
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 258
                    self.expresion_si(4) 
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self._predicates[17] = self.expresion_sempred
        self._predicates[18] = self.expresion_verdad_sempred
        self._predicates[19] = self.expresion_si_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

    def expresion_verdad_sempred(self, localctx:Expresion_verdadContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

    def expresion_si_sempred(self, localctx:Expresion_siContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




