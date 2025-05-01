grammar gramatica;

programa: PRINCIPAL LLAVE_IZQ instrucciones? LLAVE_DER;

instrucciones: instruccion+;

instruccion
    : declaracion #Dec
    | impresion #Imp
    | condicion #Condi
    | asignacion #Asi
    | ciclo_while #While
    | ciclo_for #For
    ;

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
    | PAR_IZQ expresion PAR_DER #Par
    | NUMERO #Int
    | ID #Id
    | PALABRAS #Palabras
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
ID:[a-zA-Z_][A-Za-z0-9]*; 
NUMERO:[0-9]+;
PALABRAS:MENOR [a-zA-Z]+ MENOR;
PUNTO_COMA:';';
WS:[ \t\n\r]-> skip;

IGUALDAD: '==';
DIFERENTE: '!=';
MAYOR: '>';
MENOR: '<';
MAYOR_IGUAL: '>=';
MENOR_IGUAL: '<=';
AND: '&&';
OR: '||';
NOT: '!';
COMILLAS:'"';

STRING: PAR_IZQ PALABRAS PAR_DER;