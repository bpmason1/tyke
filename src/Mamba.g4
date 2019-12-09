grammar Mamba;

/*
 * parser rules
 */
program: package funcdef+ ;

package: PACKAGE NAME SEMICOLON;
funcdef: signature '{' statementList? '}' ;
signature: 'def' NAME funcDefArgList '->' returnType ;

// statements
statementList: statement+ ;
statement: returnStmt | funcCallStmt | assigmentStmt;
returnStmt: 'return' (INTEGER | DOUBLE | funcCall | NAME)?  SEMICOLON;
funcCallStmt: funcCall SEMICOLON;
assigmentStmt : NAME '=' (INTEGER | DOUBLE | NAME) SEMICOLON ;

funcDefArgList : '(' typedArgList? ')' ;
typedArgList: typedArg ( ',' typedArg )* ;
typedArg: NAME ':' varType ;

// arithmetic
addition : data '+' data ;

funcCall: NAME funcCallDataList ;
funcCallDataList: '(' dataList? ')' ;
dataList: data (',' data)* ;
data: NAME | DOUBLE | INTEGER ;

returnType: ('void' | 'int' | 'double') ;
varType : ('double' | 'int') ;



/*
 * lexer rules
 */
PACKAGE : 'package' ;
SEMICOLON : ';' ;
KW_DOUBLE: 'double' ;
KW_INT: 'int' ;
VOID: 'void';

DOUBLE: INTEGER '.' [0-9]+ ;
INTEGER: '0' | NON_ZERO_INTEGER ;

RETURN_TYPE: VAR_TYPE | VOID ;
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
