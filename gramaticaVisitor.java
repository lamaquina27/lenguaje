// Generated from gramatica.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link gramaticaParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface gramaticaVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#programa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrograma(gramaticaParser.ProgramaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#instrucciones}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInstrucciones(gramaticaParser.InstruccionesContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Dec}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDec(gramaticaParser.DecContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Imp}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImp(gramaticaParser.ImpContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Condi}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondi(gramaticaParser.CondiContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Asi}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsi(gramaticaParser.AsiContext ctx);
	/**
	 * Visit a parse tree produced by the {@code While}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhile(gramaticaParser.WhileContext ctx);
	/**
	 * Visit a parse tree produced by the {@code For}
	 * labeled alternative in {@link gramaticaParser#instruccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor(gramaticaParser.ForContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#declaracion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracion(gramaticaParser.DeclaracionContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#impresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImpresion(gramaticaParser.ImpresionContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#asignacion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAsignacion(gramaticaParser.AsignacionContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#condicion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondicion(gramaticaParser.CondicionContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#condicion_si_no}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondicion_si_no(gramaticaParser.Condicion_si_noContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#ciclo_for}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCiclo_for(gramaticaParser.Ciclo_forContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticaParser#ciclo_while}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCiclo_while(gramaticaParser.Ciclo_whileContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Par}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPar(gramaticaParser.ParContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Suma}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSuma(gramaticaParser.SumaContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Palabras}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPalabras(gramaticaParser.PalabrasContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMod(gramaticaParser.ModContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Mul}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMul(gramaticaParser.MulContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Id}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitId(gramaticaParser.IdContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Int}
	 * labeled alternative in {@link gramaticaParser#expresion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt(gramaticaParser.IntContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Idsi}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdsi(gramaticaParser.IdsiContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Igu}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIgu(gramaticaParser.IguContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Intsi}
	 * labeled alternative in {@link gramaticaParser#expresion_si}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntsi(gramaticaParser.IntsiContext ctx);
}