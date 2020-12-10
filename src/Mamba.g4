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
assigmentStmt : NAME '=' (INTEGER | DOUBLE | NAME | funcCall | arthimeticExpr | multiArthimeticExpr) SEMICOLON ;

funcDefArgList : '(' typedArgList? ')' ;
typedArgList: typedArg ( ',' typedArg )* ;
typedArg: NAME ':' varType ;

arithmetic_op : ADD | SUBTRACT | MULTIPLY | DIVIDE ;
arthimeticExpr : simpleExpression (arithmetic_op simpleExpression)* |
                '(' simpleExpression (arithmetic_op simpleExpression)* ')' ;
multiArthimeticExpr : arthimeticExpr ( arithmetic_op arthimeticExpr)+ ;

numeric : DOUBLE | INTEGER ;
simpleExpression : (numeric | NAME | funcCall) ;

funcCall: NAME funcCallDataList ;
funcCallDataList: '(' dataList? ')' ;
dataList: data (',' data)* ;
data: STRING | NAME | DOUBLE | INTEGER;

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
ADD: '+' ;
SUBTRACT: '-' ;
MULTIPLY: '*' ;
DIVIDE: '/' ;

DOUBLE: INTEGER '.' [0-9]+ ;
INTEGER: '0' | NON_ZERO_INTEGER ;

RETURN_TYPE: VAR_TYPE | VOID ;
NAME: ID_START ID_CONTINUE*;
STRING: SHORT_STRING ;

fragment ID_START : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE : ID_START | [0-9] ;
fragment NON_ZERO_INTEGER: SIGN? POSITIVE_INTEGER  ;
fragment POSITIVE_INTEGER: [1-9] [0-9]* ;
fragment VAR_TYPE : (KW_DOUBLE | KW_INT) ;
fragment SIGN: '+' | '-' ;

fragment SHORT_STRING
 : '\'' ( ~[\\\r\n\f'] )* '\''
 | '"' ( ~[\\\r\n\f"] )* '"'
 ;

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
