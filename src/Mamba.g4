grammar Mamba;

/*
 * parser rules
 */

program: funcdef+ ;

// funcdef: 'def' NAME '->' TYPE '{' expression* '}' ;
funcdef: signature '{' expression* '}' ;

signature: 'def' NAME inputArgs '->' VAR_TYPE ;
inputArgs: '(' typedValueList? ')' ;

expression: ( assignment | returnStmt | funcCall | NAME+ ) ';'  ;
expressionList: expression*;
returnStmt: 'return' (NAME | INTEGER)? ;
typedValue: NAME ':' VAR_TYPE;
assignment: NAME '=' (INTEGER | NAME | funcCall) ;

typedValueList: typedValue (',' typedValue)* ;

funcCall : NAME '(' ')' ;

/*
 * lexer rules
 */

NAME: ID_START ID_CONTINUE* ;

INTEGER: '0' | NON_ZERO_INTEGER ;

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

// ARITHMETIC_OPERATOR: '+' | '-' | '*' | '/' ;

ALPHANUMERIC : [a-z] | [A-Z] | [0-9] ;

SIGN: '+' | '-' ;

VAR_TYPE : VOID_KW | INT_KW | DOUBLE_KW ;

VOID_KW : 'void' ;
INT_KW : 'int' ;
DOUBLE_KW : 'double' ;

// fragment POSITIVE_INTEGER: [1-9] [0-9]* ;
fragment NON_ZERO_INTEGER: SIGN? [1-9] [0-9]*  ;
fragment ID_START : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE : ID_START | [0-9] ;
