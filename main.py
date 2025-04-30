from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from EvalVisitor import EvalVisitor   
import sys

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    input_stream = FileStream(input_file, encoding="utf-8") if input_file else StdinStream()

    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticaParser(token_stream)
    tree = parser.programa()  # Empieza desde la regla principal
    
    visitor = EvalVisitor()         # <-- Crea instancia de tu Visitor
    visitor.visit(tree)  # Aquí obtienes el resultado

    
if __name__ == "__main__":
    main()
