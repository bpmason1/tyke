grammar Mamba;

/*
 * parser rules
 */
program: funcdef+ ;

expression: ALPHANUMERIC+ ;
expressionList: (expression ';')+ ;
funcdef: signature '{' expressionList? '}' ;
signature: KW_DEF NAME '->' RETURN_TYPE ;


/*
 * lexer rules
 */
ALPHANUMERIC : [a-z] | [A-Z] | [0-9] ;
fragment ID_START : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE : ID_START | [0-9] ;
INTEGER: ZERO | NON_ZERO_INTEGER;
KW_DEF: 'def' ;
KW_DOUBLE: 'double' ;
KW_INT: 'int' ;
KW_VOID: 'void';
NAME: ID_START ID_CONTINUE* ;
fragment NON_ZERO_INTEGER: SIGN? POSITIVE_INTEGER  ;
fragment POSITIVE_INTEGER: [1-9] [0-9]* ;
RETURN_TYPE: VAR_TYPE | KW_VOID ;
fragment SIGN: '+' | '-' ;
VAR_TYPE : KW_DOUBLE | KW_INT ;
ZERO : '0' ;

/*
 * ignore rules
 */

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

Whitespace
    :   [ \t]+
        -> skip
    ;
