// Generated from /home/deivi/Desktop/visual/lenguaje joathon/gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class gramaticaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PRINCIPAL=1, VAR=2, MUECHE=3, CHI=4, SINO=5, MIENTRAS=6, PARA=7, MAS=8, 
		MENOS=9, MUL=10, DIV=11, IGUAL=12, MODULO=13, ELEVACION=14, PAR_DER=15, 
		PAR_IZQ=16, LLAVE_DER=17, LLAVE_IZQ=18, ID=19, NUMERO=20, PALABRAS=21, 
		PUNTO_COMA=22, WS=23, IGUALDAD=24, DIFERENTE=25, MAYOR=26, MENOR=27, MAYOR_IGUAL=28, 
		MENOR_IGUAL=29, AND=30, OR=31, COMILLAS=32, STRING=33;
	public static final int
		RULE_programa = 0, RULE_instrucciones = 1, RULE_instruccion = 2, RULE_declaracion = 3, 
		RULE_impresion = 4, RULE_asignacion = 5, RULE_condicion = 6, RULE_condicion_si_no = 7, 
		RULE_ciclo_for = 8, RULE_ciclo_while = 9, RULE_expresion = 10, RULE_expresion_verdad = 11, 
		RULE_expresion_si = 12, RULE_atomo = 13, RULE_atomo_si = 14;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "instrucciones", "instruccion", "declaracion", "impresion", 
			"asignacion", "condicion", "condicion_si_no", "ciclo_for", "ciclo_while", 
			"expresion", "expresion_verdad", "expresion_si", "atomo", "atomo_si"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'principal'", "'var'", "'mueche'", "'chi'", "'sino'", "'mientras'", 
			"'para'", "'+'", "'-'", "'*'", "'/'", "'='", "'%'", "'^'", "')'", "'('", 
			"'}'", "'{'", null, null, null, "';'", null, "'=='", "'!='", "'>'", "'<'", 
			"'>='", "'<='", "'&&'", "'||'", "'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PRINCIPAL", "VAR", "MUECHE", "CHI", "SINO", "MIENTRAS", "PARA", 
			"MAS", "MENOS", "MUL", "DIV", "IGUAL", "MODULO", "ELEVACION", "PAR_DER", 
			"PAR_IZQ", "LLAVE_DER", "LLAVE_IZQ", "ID", "NUMERO", "PALABRAS", "PUNTO_COMA", 
			"WS", "IGUALDAD", "DIFERENTE", "MAYOR", "MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", 
			"AND", "OR", "COMILLAS", "STRING"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public gramaticaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PRINCIPAL() { return getToken(gramaticaParser.PRINCIPAL, 0); }
		public TerminalNode LLAVE_IZQ() { return getToken(gramaticaParser.LLAVE_IZQ, 0); }
		public TerminalNode LLAVE_DER() { return getToken(gramaticaParser.LLAVE_DER, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(PRINCIPAL);
			setState(31);
			match(LLAVE_IZQ);
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 524508L) != 0)) {
				{
				setState(32);
				instrucciones();
				}
			}

			setState(35);
			match(LLAVE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionesContext extends ParserRuleContext {
		public List<InstruccionContext> instruccion() {
			return getRuleContexts(InstruccionContext.class);
		}
		public InstruccionContext instruccion(int i) {
			return getRuleContext(InstruccionContext.class,i);
		}
		public InstruccionesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instrucciones; }
	}

	public final InstruccionesContext instrucciones() throws RecognitionException {
		InstruccionesContext _localctx = new InstruccionesContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_instrucciones);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(37);
				instruccion();
				}
				}
				setState(40); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 524508L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InstruccionContext extends ParserRuleContext {
		public InstruccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instruccion; }
	 
		public InstruccionContext() { }
		public void copyFrom(InstruccionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DecContext extends InstruccionContext {
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public DecContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondiContext extends InstruccionContext {
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CondiContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AsiContext extends InstruccionContext {
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public AsiContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ForContext extends InstruccionContext {
		public Ciclo_forContext ciclo_for() {
			return getRuleContext(Ciclo_forContext.class,0);
		}
		public ForContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WhileContext extends InstruccionContext {
		public Ciclo_whileContext ciclo_while() {
			return getRuleContext(Ciclo_whileContext.class,0);
		}
		public WhileContext(InstruccionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ImpContext extends InstruccionContext {
		public ImpresionContext impresion() {
			return getRuleContext(ImpresionContext.class,0);
		}
		public ImpContext(InstruccionContext ctx) { copyFrom(ctx); }
	}

	public final InstruccionContext instruccion() throws RecognitionException {
		InstruccionContext _localctx = new InstruccionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_instruccion);
		try {
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				_localctx = new DecContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				declaracion();
				}
				break;
			case MUECHE:
				_localctx = new ImpContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				impresion();
				}
				break;
			case CHI:
				_localctx = new CondiContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(44);
				condicion();
				}
				break;
			case ID:
				_localctx = new AsiContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(45);
				asignacion();
				}
				break;
			case MIENTRAS:
				_localctx = new WhileContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(46);
				ciclo_while();
				}
				break;
			case PARA:
				_localctx = new ForContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(47);
				ciclo_for();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracionContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(gramaticaParser.VAR, 0); }
		public TerminalNode ID() { return getToken(gramaticaParser.ID, 0); }
		public TerminalNode IGUAL() { return getToken(gramaticaParser.IGUAL, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(gramaticaParser.PUNTO_COMA, 0); }
		public DeclaracionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracion; }
	}

	public final DeclaracionContext declaracion() throws RecognitionException {
		DeclaracionContext _localctx = new DeclaracionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_declaracion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(VAR);
			setState(51);
			match(ID);
			setState(52);
			match(IGUAL);
			setState(53);
			expresion(0);
			setState(54);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImpresionContext extends ParserRuleContext {
		public TerminalNode MUECHE() { return getToken(gramaticaParser.MUECHE, 0); }
		public TerminalNode PAR_IZQ() { return getToken(gramaticaParser.PAR_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAR_DER() { return getToken(gramaticaParser.PAR_DER, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(gramaticaParser.PUNTO_COMA, 0); }
		public ImpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_impresion; }
	}

	public final ImpresionContext impresion() throws RecognitionException {
		ImpresionContext _localctx = new ImpresionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_impresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(MUECHE);
			setState(57);
			match(PAR_IZQ);
			setState(58);
			expresion(0);
			setState(59);
			match(PAR_DER);
			setState(60);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(gramaticaParser.ID, 0); }
		public TerminalNode IGUAL() { return getToken(gramaticaParser.IGUAL, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(gramaticaParser.PUNTO_COMA, 0); }
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(ID);
			setState(63);
			match(IGUAL);
			setState(64);
			expresion(0);
			setState(65);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode CHI() { return getToken(gramaticaParser.CHI, 0); }
		public TerminalNode PAR_IZQ() { return getToken(gramaticaParser.PAR_IZQ, 0); }
		public Expresion_verdadContext expresion_verdad() {
			return getRuleContext(Expresion_verdadContext.class,0);
		}
		public TerminalNode PAR_DER() { return getToken(gramaticaParser.PAR_DER, 0); }
		public TerminalNode LLAVE_IZQ() { return getToken(gramaticaParser.LLAVE_IZQ, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLAVE_DER() { return getToken(gramaticaParser.LLAVE_DER, 0); }
		public Condicion_si_noContext condicion_si_no() {
			return getRuleContext(Condicion_si_noContext.class,0);
		}
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_condicion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(CHI);
			setState(68);
			match(PAR_IZQ);
			setState(69);
			expresion_verdad(0);
			setState(70);
			match(PAR_DER);
			setState(71);
			match(LLAVE_IZQ);
			setState(72);
			instrucciones();
			setState(73);
			match(LLAVE_DER);
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SINO) {
				{
				setState(74);
				condicion_si_no();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condicion_si_noContext extends ParserRuleContext {
		public TerminalNode SINO() { return getToken(gramaticaParser.SINO, 0); }
		public TerminalNode LLAVE_IZQ() { return getToken(gramaticaParser.LLAVE_IZQ, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLAVE_DER() { return getToken(gramaticaParser.LLAVE_DER, 0); }
		public Condicion_si_noContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion_si_no; }
	}

	public final Condicion_si_noContext condicion_si_no() throws RecognitionException {
		Condicion_si_noContext _localctx = new Condicion_si_noContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_condicion_si_no);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(SINO);
			setState(78);
			match(LLAVE_IZQ);
			setState(79);
			instrucciones();
			setState(80);
			match(LLAVE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Ciclo_forContext extends ParserRuleContext {
		public TerminalNode PARA() { return getToken(gramaticaParser.PARA, 0); }
		public TerminalNode PAR_IZQ() { return getToken(gramaticaParser.PAR_IZQ, 0); }
		public DeclaracionContext declaracion() {
			return getRuleContext(DeclaracionContext.class,0);
		}
		public Expresion_siContext expresion_si() {
			return getRuleContext(Expresion_siContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(gramaticaParser.PUNTO_COMA, 0); }
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public TerminalNode PAR_DER() { return getToken(gramaticaParser.PAR_DER, 0); }
		public TerminalNode LLAVE_IZQ() { return getToken(gramaticaParser.LLAVE_IZQ, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLAVE_DER() { return getToken(gramaticaParser.LLAVE_DER, 0); }
		public Ciclo_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo_for; }
	}

	public final Ciclo_forContext ciclo_for() throws RecognitionException {
		Ciclo_forContext _localctx = new Ciclo_forContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ciclo_for);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(PARA);
			setState(83);
			match(PAR_IZQ);
			setState(84);
			declaracion();
			setState(85);
			expresion_si(0);
			setState(86);
			match(PUNTO_COMA);
			setState(87);
			asignacion();
			setState(88);
			match(PAR_DER);
			setState(89);
			match(LLAVE_IZQ);
			setState(90);
			instrucciones();
			setState(91);
			match(LLAVE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Ciclo_whileContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(gramaticaParser.MIENTRAS, 0); }
		public TerminalNode PAR_IZQ() { return getToken(gramaticaParser.PAR_IZQ, 0); }
		public Expresion_verdadContext expresion_verdad() {
			return getRuleContext(Expresion_verdadContext.class,0);
		}
		public TerminalNode PAR_DER() { return getToken(gramaticaParser.PAR_DER, 0); }
		public TerminalNode LLAVE_IZQ() { return getToken(gramaticaParser.LLAVE_IZQ, 0); }
		public InstruccionesContext instrucciones() {
			return getRuleContext(InstruccionesContext.class,0);
		}
		public TerminalNode LLAVE_DER() { return getToken(gramaticaParser.LLAVE_DER, 0); }
		public Ciclo_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo_while; }
	}

	public final Ciclo_whileContext ciclo_while() throws RecognitionException {
		Ciclo_whileContext _localctx = new Ciclo_whileContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_ciclo_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(MIENTRAS);
			setState(94);
			match(PAR_IZQ);
			setState(95);
			expresion_verdad(0);
			setState(96);
			match(PAR_DER);
			setState(97);
			match(LLAVE_IZQ);
			setState(98);
			instrucciones();
			setState(99);
			match(LLAVE_DER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	 
		public ExpresionContext() { }
		public void copyFrom(ExpresionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParContext extends ExpresionContext {
		public TerminalNode PAR_IZQ() { return getToken(gramaticaParser.PAR_IZQ, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PAR_DER() { return getToken(gramaticaParser.PAR_DER, 0); }
		public ParContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Atomo_unoContext extends ExpresionContext {
		public AtomoContext atomo() {
			return getRuleContext(AtomoContext.class,0);
		}
		public Atomo_unoContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SumaContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode MAS() { return getToken(gramaticaParser.MAS, 0); }
		public TerminalNode MENOS() { return getToken(gramaticaParser.MENOS, 0); }
		public SumaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PalabrasContext extends ExpresionContext {
		public TerminalNode PALABRAS() { return getToken(gramaticaParser.PALABRAS, 0); }
		public PalabrasContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ModContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode MODULO() { return getToken(gramaticaParser.MODULO, 0); }
		public TerminalNode ELEVACION() { return getToken(gramaticaParser.ELEVACION, 0); }
		public ModContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(gramaticaParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(gramaticaParser.DIV, 0); }
		public MulContext(ExpresionContext ctx) { copyFrom(ctx); }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expresion, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PAR_IZQ:
				{
				_localctx = new ParContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(102);
				match(PAR_IZQ);
				setState(103);
				expresion(0);
				setState(104);
				match(PAR_DER);
				}
				break;
			case PALABRAS:
				{
				_localctx = new PalabrasContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(106);
				match(PALABRAS);
				}
				break;
			case ID:
			case NUMERO:
				{
				_localctx = new Atomo_unoContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(107);
				atomo();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(121);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(119);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new SumaContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(110);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(111);
						((SumaContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MAS || _la==MENOS) ) {
							((SumaContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(112);
						expresion(7);
						}
						break;
					case 2:
						{
						_localctx = new MulContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(113);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(114);
						((MulContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((MulContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(115);
						expresion(6);
						}
						break;
					case 3:
						{
						_localctx = new ModContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(116);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(117);
						((ModContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MODULO || _la==ELEVACION) ) {
							((ModContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(118);
						expresion(5);
						}
						break;
					}
					} 
				}
				setState(123);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expresion_verdadContext extends ParserRuleContext {
		public Expresion_verdadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_verdad; }
	 
		public Expresion_verdadContext() { }
		public void copyFrom(Expresion_verdadContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VerdadContext extends Expresion_verdadContext {
		public Token op;
		public List<Expresion_verdadContext> expresion_verdad() {
			return getRuleContexts(Expresion_verdadContext.class);
		}
		public Expresion_verdadContext expresion_verdad(int i) {
			return getRuleContext(Expresion_verdadContext.class,i);
		}
		public TerminalNode AND() { return getToken(gramaticaParser.AND, 0); }
		public TerminalNode OR() { return getToken(gramaticaParser.OR, 0); }
		public VerdadContext(Expresion_verdadContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParverContext extends Expresion_verdadContext {
		public TerminalNode PAR_IZQ() { return getToken(gramaticaParser.PAR_IZQ, 0); }
		public Expresion_verdadContext expresion_verdad() {
			return getRuleContext(Expresion_verdadContext.class,0);
		}
		public TerminalNode PAR_DER() { return getToken(gramaticaParser.PAR_DER, 0); }
		public ParverContext(Expresion_verdadContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpverContext extends Expresion_verdadContext {
		public Expresion_siContext expresion_si() {
			return getRuleContext(Expresion_siContext.class,0);
		}
		public ExpverContext(Expresion_verdadContext ctx) { copyFrom(ctx); }
	}

	public final Expresion_verdadContext expresion_verdad() throws RecognitionException {
		return expresion_verdad(0);
	}

	private Expresion_verdadContext expresion_verdad(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expresion_verdadContext _localctx = new Expresion_verdadContext(_ctx, _parentState);
		Expresion_verdadContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expresion_verdad, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PAR_IZQ:
				{
				_localctx = new ParverContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(125);
				match(PAR_IZQ);
				setState(126);
				expresion_verdad(0);
				setState(127);
				match(PAR_DER);
				}
				break;
			case ID:
			case NUMERO:
				{
				_localctx = new ExpverContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(129);
				expresion_si(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(137);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new VerdadContext(new Expresion_verdadContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_expresion_verdad);
					setState(132);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(133);
					((VerdadContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
						((VerdadContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(134);
					expresion_verdad(4);
					}
					} 
				}
				setState(139);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expresion_siContext extends ParserRuleContext {
		public Expresion_siContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_si; }
	 
		public Expresion_siContext() { }
		public void copyFrom(Expresion_siContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Atomo_dosContext extends Expresion_siContext {
		public Atomo_siContext atomo_si() {
			return getRuleContext(Atomo_siContext.class,0);
		}
		public Atomo_dosContext(Expresion_siContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IguContext extends Expresion_siContext {
		public Token op;
		public List<Expresion_siContext> expresion_si() {
			return getRuleContexts(Expresion_siContext.class);
		}
		public Expresion_siContext expresion_si(int i) {
			return getRuleContext(Expresion_siContext.class,i);
		}
		public TerminalNode IGUALDAD() { return getToken(gramaticaParser.IGUALDAD, 0); }
		public TerminalNode DIFERENTE() { return getToken(gramaticaParser.DIFERENTE, 0); }
		public TerminalNode MAYOR() { return getToken(gramaticaParser.MAYOR, 0); }
		public TerminalNode MAYOR_IGUAL() { return getToken(gramaticaParser.MAYOR_IGUAL, 0); }
		public TerminalNode MENOR() { return getToken(gramaticaParser.MENOR, 0); }
		public TerminalNode MENOR_IGUAL() { return getToken(gramaticaParser.MENOR_IGUAL, 0); }
		public IguContext(Expresion_siContext ctx) { copyFrom(ctx); }
	}

	public final Expresion_siContext expresion_si() throws RecognitionException {
		return expresion_si(0);
	}

	private Expresion_siContext expresion_si(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expresion_siContext _localctx = new Expresion_siContext(_ctx, _parentState);
		Expresion_siContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_expresion_si, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Atomo_dosContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(141);
			atomo_si();
			}
			_ctx.stop = _input.LT(-1);
			setState(148);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new IguContext(new Expresion_siContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_expresion_si);
					setState(143);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(144);
					((IguContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1056964608L) != 0)) ) {
						((IguContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(145);
					expresion_si(3);
					}
					} 
				}
				setState(150);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtomoContext extends ParserRuleContext {
		public AtomoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomo; }
	 
		public AtomoContext() { }
		public void copyFrom(AtomoContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdContext extends AtomoContext {
		public TerminalNode ID() { return getToken(gramaticaParser.ID, 0); }
		public IdContext(AtomoContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends AtomoContext {
		public TerminalNode NUMERO() { return getToken(gramaticaParser.NUMERO, 0); }
		public IntContext(AtomoContext ctx) { copyFrom(ctx); }
	}

	public final AtomoContext atomo() throws RecognitionException {
		AtomoContext _localctx = new AtomoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_atomo);
		try {
			setState(153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMERO:
				_localctx = new IntContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				match(NUMERO);
				}
				break;
			case ID:
				_localctx = new IdContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(152);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Atomo_siContext extends ParserRuleContext {
		public Atomo_siContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomo_si; }
	 
		public Atomo_siContext() { }
		public void copyFrom(Atomo_siContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IdsiContext extends Atomo_siContext {
		public TerminalNode ID() { return getToken(gramaticaParser.ID, 0); }
		public IdsiContext(Atomo_siContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntsiContext extends Atomo_siContext {
		public TerminalNode NUMERO() { return getToken(gramaticaParser.NUMERO, 0); }
		public IntsiContext(Atomo_siContext ctx) { copyFrom(ctx); }
	}

	public final Atomo_siContext atomo_si() throws RecognitionException {
		Atomo_siContext _localctx = new Atomo_siContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_atomo_si);
		try {
			setState(157);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMERO:
				_localctx = new IntsiContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(155);
				match(NUMERO);
				}
				break;
			case ID:
				_localctx = new IdsiContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(156);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expresion_sempred((ExpresionContext)_localctx, predIndex);
		case 11:
			return expresion_verdad_sempred((Expresion_verdadContext)_localctx, predIndex);
		case 12:
			return expresion_si_sempred((Expresion_siContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_sempred(ExpresionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}
	private boolean expresion_verdad_sempred(Expresion_verdadContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 3);
		}
		return true;
	}
	private boolean expresion_si_sempred(Expresion_siContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001!\u00a0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0003\u0000\"\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0004\u0001\'\b\u0001\u000b\u0001\f\u0001(\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u00021\b\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006L\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\nm\b\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0005\nx\b\n\n\n\f\n{\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0083"+
		"\b\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b\u0088\b\u000b"+
		"\n\u000b\f\u000b\u008b\t\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0005\f\u0093\b\f\n\f\f\f\u0096\t\f\u0001\r\u0001\r\u0003\r\u009a"+
		"\b\r\u0001\u000e\u0001\u000e\u0003\u000e\u009e\b\u000e\u0001\u000e\u0000"+
		"\u0003\u0014\u0016\u0018\u000f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u0000\u0005\u0001\u0000\b\t\u0001"+
		"\u0000\n\u000b\u0001\u0000\r\u000e\u0001\u0000\u001e\u001f\u0001\u0000"+
		"\u0018\u001d\u00a2\u0000\u001e\u0001\u0000\u0000\u0000\u0002&\u0001\u0000"+
		"\u0000\u0000\u00040\u0001\u0000\u0000\u0000\u00062\u0001\u0000\u0000\u0000"+
		"\b8\u0001\u0000\u0000\u0000\n>\u0001\u0000\u0000\u0000\fC\u0001\u0000"+
		"\u0000\u0000\u000eM\u0001\u0000\u0000\u0000\u0010R\u0001\u0000\u0000\u0000"+
		"\u0012]\u0001\u0000\u0000\u0000\u0014l\u0001\u0000\u0000\u0000\u0016\u0082"+
		"\u0001\u0000\u0000\u0000\u0018\u008c\u0001\u0000\u0000\u0000\u001a\u0099"+
		"\u0001\u0000\u0000\u0000\u001c\u009d\u0001\u0000\u0000\u0000\u001e\u001f"+
		"\u0005\u0001\u0000\u0000\u001f!\u0005\u0012\u0000\u0000 \"\u0003\u0002"+
		"\u0001\u0000! \u0001\u0000\u0000\u0000!\"\u0001\u0000\u0000\u0000\"#\u0001"+
		"\u0000\u0000\u0000#$\u0005\u0011\u0000\u0000$\u0001\u0001\u0000\u0000"+
		"\u0000%\'\u0003\u0004\u0002\u0000&%\u0001\u0000\u0000\u0000\'(\u0001\u0000"+
		"\u0000\u0000(&\u0001\u0000\u0000\u0000()\u0001\u0000\u0000\u0000)\u0003"+
		"\u0001\u0000\u0000\u0000*1\u0003\u0006\u0003\u0000+1\u0003\b\u0004\u0000"+
		",1\u0003\f\u0006\u0000-1\u0003\n\u0005\u0000.1\u0003\u0012\t\u0000/1\u0003"+
		"\u0010\b\u00000*\u0001\u0000\u0000\u00000+\u0001\u0000\u0000\u00000,\u0001"+
		"\u0000\u0000\u00000-\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u0000"+
		"0/\u0001\u0000\u0000\u00001\u0005\u0001\u0000\u0000\u000023\u0005\u0002"+
		"\u0000\u000034\u0005\u0013\u0000\u000045\u0005\f\u0000\u000056\u0003\u0014"+
		"\n\u000067\u0005\u0016\u0000\u00007\u0007\u0001\u0000\u0000\u000089\u0005"+
		"\u0003\u0000\u00009:\u0005\u0010\u0000\u0000:;\u0003\u0014\n\u0000;<\u0005"+
		"\u000f\u0000\u0000<=\u0005\u0016\u0000\u0000=\t\u0001\u0000\u0000\u0000"+
		">?\u0005\u0013\u0000\u0000?@\u0005\f\u0000\u0000@A\u0003\u0014\n\u0000"+
		"AB\u0005\u0016\u0000\u0000B\u000b\u0001\u0000\u0000\u0000CD\u0005\u0004"+
		"\u0000\u0000DE\u0005\u0010\u0000\u0000EF\u0003\u0016\u000b\u0000FG\u0005"+
		"\u000f\u0000\u0000GH\u0005\u0012\u0000\u0000HI\u0003\u0002\u0001\u0000"+
		"IK\u0005\u0011\u0000\u0000JL\u0003\u000e\u0007\u0000KJ\u0001\u0000\u0000"+
		"\u0000KL\u0001\u0000\u0000\u0000L\r\u0001\u0000\u0000\u0000MN\u0005\u0005"+
		"\u0000\u0000NO\u0005\u0012\u0000\u0000OP\u0003\u0002\u0001\u0000PQ\u0005"+
		"\u0011\u0000\u0000Q\u000f\u0001\u0000\u0000\u0000RS\u0005\u0007\u0000"+
		"\u0000ST\u0005\u0010\u0000\u0000TU\u0003\u0006\u0003\u0000UV\u0003\u0018"+
		"\f\u0000VW\u0005\u0016\u0000\u0000WX\u0003\n\u0005\u0000XY\u0005\u000f"+
		"\u0000\u0000YZ\u0005\u0012\u0000\u0000Z[\u0003\u0002\u0001\u0000[\\\u0005"+
		"\u0011\u0000\u0000\\\u0011\u0001\u0000\u0000\u0000]^\u0005\u0006\u0000"+
		"\u0000^_\u0005\u0010\u0000\u0000_`\u0003\u0016\u000b\u0000`a\u0005\u000f"+
		"\u0000\u0000ab\u0005\u0012\u0000\u0000bc\u0003\u0002\u0001\u0000cd\u0005"+
		"\u0011\u0000\u0000d\u0013\u0001\u0000\u0000\u0000ef\u0006\n\uffff\uffff"+
		"\u0000fg\u0005\u0010\u0000\u0000gh\u0003\u0014\n\u0000hi\u0005\u000f\u0000"+
		"\u0000im\u0001\u0000\u0000\u0000jm\u0005\u0015\u0000\u0000km\u0003\u001a"+
		"\r\u0000le\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000lk\u0001\u0000"+
		"\u0000\u0000my\u0001\u0000\u0000\u0000no\n\u0006\u0000\u0000op\u0007\u0000"+
		"\u0000\u0000px\u0003\u0014\n\u0007qr\n\u0005\u0000\u0000rs\u0007\u0001"+
		"\u0000\u0000sx\u0003\u0014\n\u0006tu\n\u0004\u0000\u0000uv\u0007\u0002"+
		"\u0000\u0000vx\u0003\u0014\n\u0005wn\u0001\u0000\u0000\u0000wq\u0001\u0000"+
		"\u0000\u0000wt\u0001\u0000\u0000\u0000x{\u0001\u0000\u0000\u0000yw\u0001"+
		"\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z\u0015\u0001\u0000\u0000"+
		"\u0000{y\u0001\u0000\u0000\u0000|}\u0006\u000b\uffff\uffff\u0000}~\u0005"+
		"\u0010\u0000\u0000~\u007f\u0003\u0016\u000b\u0000\u007f\u0080\u0005\u000f"+
		"\u0000\u0000\u0080\u0083\u0001\u0000\u0000\u0000\u0081\u0083\u0003\u0018"+
		"\f\u0000\u0082|\u0001\u0000\u0000\u0000\u0082\u0081\u0001\u0000\u0000"+
		"\u0000\u0083\u0089\u0001\u0000\u0000\u0000\u0084\u0085\n\u0003\u0000\u0000"+
		"\u0085\u0086\u0007\u0003\u0000\u0000\u0086\u0088\u0003\u0016\u000b\u0004"+
		"\u0087\u0084\u0001\u0000\u0000\u0000\u0088\u008b\u0001\u0000\u0000\u0000"+
		"\u0089\u0087\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000"+
		"\u008a\u0017\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000"+
		"\u008c\u008d\u0006\f\uffff\uffff\u0000\u008d\u008e\u0003\u001c\u000e\u0000"+
		"\u008e\u0094\u0001\u0000\u0000\u0000\u008f\u0090\n\u0002\u0000\u0000\u0090"+
		"\u0091\u0007\u0004\u0000\u0000\u0091\u0093\u0003\u0018\f\u0003\u0092\u008f"+
		"\u0001\u0000\u0000\u0000\u0093\u0096\u0001\u0000\u0000\u0000\u0094\u0092"+
		"\u0001\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u0019"+
		"\u0001\u0000\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0097\u009a"+
		"\u0005\u0014\u0000\u0000\u0098\u009a\u0005\u0013\u0000\u0000\u0099\u0097"+
		"\u0001\u0000\u0000\u0000\u0099\u0098\u0001\u0000\u0000\u0000\u009a\u001b"+
		"\u0001\u0000\u0000\u0000\u009b\u009e\u0005\u0014\u0000\u0000\u009c\u009e"+
		"\u0005\u0013\u0000\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009d\u009c"+
		"\u0001\u0000\u0000\u0000\u009e\u001d\u0001\u0000\u0000\u0000\f!(0Klwy"+
		"\u0082\u0089\u0094\u0099\u009d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}