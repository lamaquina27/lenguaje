// Generated from /home/deivi/Desktop/visual/lenguaje joathon/gramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramaticaParser}.
 */
public interface gramaticaListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(gramaticaParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(gramaticaParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void enterInstrucciones(gramaticaParser.InstruccionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#instrucciones}.
	 * @param ctx the parse tree
	 */
	void exitInstrucciones(gramaticaParser.InstruccionesContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Dec}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterDec(gramaticaParser.DecContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Dec}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitDec(gramaticaParser.DecContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Imp}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterImp(gramaticaParser.ImpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Imp}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitImp(gramaticaParser.ImpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Condi}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterCondi(gramaticaParser.CondiContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Condi}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitCondi(gramaticaParser.CondiContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracion(gramaticaParser.DeclaracionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#declaracion}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracion(gramaticaParser.DeclaracionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#impresion}.
	 * @param ctx the parse tree
	 */
	void enterImpresion(gramaticaParser.ImpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#impresion}.
	 * @param ctx the parse tree
	 */
	void exitImpresion(gramaticaParser.ImpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(gramaticaParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(gramaticaParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#condicion_si_no}.
	 * @param ctx the parse tree
	 */
	void enterCondicion_si_no(gramaticaParser.Condicion_si_noContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#condicion_si_no}.
	 * @param ctx the parse tree
	 */
	void exitCondicion_si_no(gramaticaParser.Condicion_si_noContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#ciclo_for}.
	 * @param ctx the parse tree
	 */
	void enterCiclo_for(gramaticaParser.Ciclo_forContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#ciclo_for}.
	 * @param ctx the parse tree
	 */
	void exitCiclo_for(gramaticaParser.Ciclo_forContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#ciclo_while}.
	 * @param ctx the parse tree
	 */
	void enterCiclo_while(gramaticaParser.Ciclo_whileContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#ciclo_while}.
	 * @param ctx the parse tree
	 */
	void exitCiclo_while(gramaticaParser.Ciclo_whileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Par}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterPar(gramaticaParser.ParContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Par}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitPar(gramaticaParser.ParContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Suma}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterSuma(gramaticaParser.SumaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Suma}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitSuma(gramaticaParser.SumaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Palabras}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterPalabras(gramaticaParser.PalabrasContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Palabras}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitPalabras(gramaticaParser.PalabrasContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterMod(gramaticaParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitMod(gramaticaParser.ModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterMul(gramaticaParser.MulContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitMul(gramaticaParser.MulContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Id}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterId(gramaticaParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Id}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitId(gramaticaParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Int}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterInt(gramaticaParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Int}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitInt(gramaticaParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Idsi}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 */
	void enterIdsi(gramaticaParser.IdsiContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Idsi}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 */
	void exitIdsi(gramaticaParser.IdsiContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Igu}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 */
	void enterIgu(gramaticaParser.IguContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Igu}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 */
	void exitIgu(gramaticaParser.IguContext ctx);
}