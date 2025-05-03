grammar gramatica;

options { visitor = true; }

programa: importaciones? PRINCIPAL LLAVE_IZQ instrucciones? LLAVE_DER;

importaciones: importacion+;
importacion: TRAIGASE ID PUNTO_COMA;

instrucciones: instruccion+;


instruccion
    : declaracion #Dec
    | impresion #Imp
    | condicion #Condi
    | asignacion #Asi
    | ciclo_while #While
    | ciclo_for #For
    | definicion_funcion #DefFunc
    | llamada_funcion #LlamadaFunc
    | retorno #Ret
    ;

definicion_funcion: FUNCA ID PREG_IZQ argumentos? PREG_DER BLOQUE_FUNCION;
llamada_funcion: PUNTOPUNTO nombre=ID PAR_IZQ argumentos? PAR_DER PUNTO_COMA;
argumentos: expresion (PUNTO_COMA expresion)*;

bloque_funcion: COMILLAS instrucciones? COMILLAS;

retorno: MANDELE expresion PUNTO_COMA;


declaracion: VAR ID IGUAL expresion PUNTO_COMA; 
impresion: MUECHE PAR_IZQ expresion PAR_DER PUNTO_COMA;
asignacion: ID IGUAL expresion PUNTO_COMA;
condicion: CHI PAR_IZQ expresion_si PAR_DER LLAVE_IZQ instrucciones LLAVE_DER (condicion_si_no)?;
condicion_si_no: SINO LLAVE_IZQ instrucciones LLAVE_DER;
ciclo_for: PARA PAR_IZQ declaracion  expresion_si PUNTO_COMA asignacion PAR_DER LLAVE_IZQ instrucciones LLAVE_DER;
ciclo_while:MIENTRAS PAR_IZQ expresion_si PAR_DER LLAVE_IZQ instrucciones LLAVE_DER;


expresion
    : expresion op=(MAS|MENOS) expresion # Suma
    | expresion op=(MUL|DIV) expresion  #Mul
    | expresion op=(MODULO|ELEVACION) expresion #Mod
    | PUNTOPUNTO ID PAR_IZQ argumentos? PAR_DER #ExprLlamadaFunc  // ← NUEVA
    | PAR_IZQ expresion PAR_DER #Par
    | NUMERO #Int
    | PALABRAS #Palabras
    | ID #Id
    ;
expresion_si
    : expresion_si op=(IGUALDAD|DIFERENTE|MAYOR|MAYOR_IGUAL|MENOR|MENOR_IGUAL) expresion_si #Igu
    | NUMERO #Intsi
    | ID #Idsi
    ;
PRINCIPAL:'principal';
VAR:'var';
MUECHE:'mueche';
CHI:'chi';
SINO:'sino';
MIENTRAS:'mientras';
PARA:'para';
MANDELE: 'mandele';



BLOQUE_FUNCION: '"' ( . | '\r' | '\n' )*? '"';


TRAIGASE: 'traigase';
FUNCA: 'funca';
PUNTO: '.';
PUNTOPUNTO : '..';
PREG_DER:'?';
PREG_IZQ:'¿';


MAS : '+';
MENOS:'-';
MUL:'*';
DIV:'/';
IGUAL:'=';
MODULO:'%';
ELEVACION:'^';
PAR_DER:')';
PAR_IZQ:'(';
LLAVE_DER:'}';
LLAVE_IZQ:'{';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO:[0-9]+;
PALABRAS:'<' (~[<>])+ '>';
PUNTO_COMA:';';
NL: ('\n'|'\r')+ -> skip;
WS: [ \t]+ -> skip;


IGUALDAD: '==';
DIFERENTE: '!=';
MAYOR: '>';
MENOR: '<';
MAYOR_IGUAL: '>=';
MENOR_IGUAL: '<=';
AND: '&&';
OR: '||';
NOT: '!';
COMILLAS: '"' -> channel(HIDDEN);
