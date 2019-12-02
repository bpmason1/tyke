grammar Mamba;

/*
 * parser rules
 */
program: funcdef+ ;

funcdef: signature '{' statementList? '}' ;
signature: 'def' NAME funcDefArgList '->' returnType ;
statementList: statement+ ;
statement: returnStmt ;
returnStmt: 'return' (integer | double)?  SEMICOLON;
funcDefArgList : '(' typedArgList? ')' ;
typedArgList: typedArg ( ',' typedArg )* ;
typedArg: NAME ':' varType ;

double: DOUBLE;
integer:  INTEGER;
name: NAME ;
returnType: ('void' | 'int' | 'double') ;
varType : ('double' | 'int') ;

/*
 * lexer rules
 */
KW_DOUBLE: 'double' ;
KW_INT: 'int' ;
KW_VOID: 'void';
SEMICOLON : ';' ;

DOUBLE: INTEGER '.' [0-9]+ ;
INTEGER: '0' | NON_ZERO_INTEGER ;

RETURN_TYPE: VAR_TYPE | KW_VOID ;
NAME: ID_START ID_CONTINUE*;

fragment ID_START : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE : ID_START | [0-9] ;
fragment NON_ZERO_INTEGER: SIGN? POSITIVE_INTEGER  ;
fragment POSITIVE_INTEGER: [1-9] [0-9]* ;
fragment VAR_TYPE : (KW_DOUBLE | KW_INT) ;
fragment SIGN: '+' | '-' ;
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
