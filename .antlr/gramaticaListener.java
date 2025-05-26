// Generated from /home/dsantycam/Escritorio/lenguaje/gramatica.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by {@link gramaticaParser#importaciones}.
	 * @param ctx the parse tree
	 */
	void enterImportaciones(gramaticaParser.ImportacionesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#importaciones}.
	 * @param ctx the parse tree
	 */
	void exitImportaciones(gramaticaParser.ImportacionesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#importacion}.
	 * @param ctx the parse tree
	 */
	void enterImportacion(gramaticaParser.ImportacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#importacion}.
	 * @param ctx the parse tree
	 */
	void exitImportacion(gramaticaParser.ImportacionContext ctx);
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
	 * Enter a parse tree produced by the {@code Asi}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterAsi(gramaticaParser.AsiContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Asi}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitAsi(gramaticaParser.AsiContext ctx);
	/**
	 * Enter a parse tree produced by the {@code While}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterWhile(gramaticaParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code While}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitWhile(gramaticaParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code For}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterFor(gramaticaParser.ForContext ctx);
	/**
	 * Exit a parse tree produced by the {@code For}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitFor(gramaticaParser.ForContext ctx);
	/**
	 * Enter a parse tree produced by the {@code DefFunc}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterDefFunc(gramaticaParser.DefFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code DefFunc}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitDefFunc(gramaticaParser.DefFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExprLlamadaMetodoLib}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterExprLlamadaMetodoLib(gramaticaParser.ExprLlamadaMetodoLibContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprLlamadaMetodoLib}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitExprLlamadaMetodoLib(gramaticaParser.ExprLlamadaMetodoLibContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LlamadaFunc}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterLlamadaFunc(gramaticaParser.LlamadaFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LlamadaFunc}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitLlamadaFunc(gramaticaParser.LlamadaFuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Ret}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void enterRet(gramaticaParser.RetContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Ret}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 */
	void exitRet(gramaticaParser.RetContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#definicion_funcion}.
	 * @param ctx the parse tree
	 */
	void enterDefinicion_funcion(gramaticaParser.Definicion_funcionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#definicion_funcion}.
	 * @param ctx the parse tree
	 */
	void exitDefinicion_funcion(gramaticaParser.Definicion_funcionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#llamada_funcion}.
	 * @param ctx the parse tree
	 */
	void enterLlamada_funcion(gramaticaParser.Llamada_funcionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#llamada_funcion}.
	 * @param ctx the parse tree
	 */
	void exitLlamada_funcion(gramaticaParser.Llamada_funcionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(gramaticaParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(gramaticaParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#bloque_funcion}.
	 * @param ctx the parse tree
	 */
	void enterBloque_funcion(gramaticaParser.Bloque_funcionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#bloque_funcion}.
	 * @param ctx the parse tree
	 */
	void exitBloque_funcion(gramaticaParser.Bloque_funcionContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticaParser#retorno}.
	 * @param ctx the parse tree
	 */
	void enterRetorno(gramaticaParser.RetornoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#retorno}.
	 * @param ctx the parse tree
	 */
	void exitRetorno(gramaticaParser.RetornoContext ctx);
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
	 * Enter a parse tree produced by {@link gramaticaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(gramaticaParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticaParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(gramaticaParser.AsignacionContext ctx);
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
	 * Enter a parse tree produced by the {@code ExprLlamadaFunc}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExprLlamadaFunc(gramaticaParser.ExprLlamadaFuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprLlamadaFunc}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExprLlamadaFunc(gramaticaParser.ExprLlamadaFuncContext ctx);
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
	 * Enter a parse tree produced by the {@code Lista}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterLista(gramaticaParser.ListaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Lista}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitLista(gramaticaParser.ListaContext ctx);
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
	 * Enter a parse tree produced by the {@code ExprLlamadaMetodoLibreria}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExprLlamadaMetodoLibreria(gramaticaParser.ExprLlamadaMetodoLibreriaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExprLlamadaMetodoLibreria}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExprLlamadaMetodoLibreria(gramaticaParser.ExprLlamadaMetodoLibreriaContext ctx);
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
	 * Enter a parse tree produced by the {@code Negativo}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterNegativo(gramaticaParser.NegativoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Negativo}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitNegativo(gramaticaParser.NegativoContext ctx);
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
	 * Enter a parse tree produced by the {@code Verdad}
	 * labeled alternative in {@link gramaticaParser#expresion_verdad}.
	 * @param ctx the parse tree
	 */
	void enterVerdad(gramaticaParser.VerdadContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Verdad}
	 * labeled alternative in {@link gramaticaParser#expresion_verdad}.
	 * @param ctx the parse tree
	 */
	void exitVerdad(gramaticaParser.VerdadContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parver}
	 * labeled alternative in {@link gramaticaParser#expresion_verdad}.
	 * @param ctx the parse tree
	 */
	void enterParver(gramaticaParser.ParverContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parver}
	 * labeled alternative in {@link gramaticaParser#expresion_verdad}.
	 * @param ctx the parse tree
	 */
	void exitParver(gramaticaParser.ParverContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Expver}
	 * labeled alternative in {@link gramaticaParser#expresion_verdad}.
	 * @param ctx the parse tree
	 */
	void enterExpver(gramaticaParser.ExpverContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Expver}
	 * labeled alternative in {@link gramaticaParser#expresion_verdad}.
	 * @param ctx the parse tree
	 */
	void exitExpver(gramaticaParser.ExpverContext ctx);
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
	/**
	 * Enter a parse tree produced by the {@code Intsi}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 */
	void enterIntsi(gramaticaParser.IntsiContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Intsi}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 */
	void exitIntsi(gramaticaParser.IntsiContext ctx);
}