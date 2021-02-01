grammar Tyke;

/*
 * parser rules
 */
program: package typedef* funcdef+ ;

package: PACKAGE NAME SEMICOLON;
typedef: TYPE STRUCT '{' typedArgList? '}' NAME SEMICOLON;
funcdef: signature '{' statementList? '}' ;
signature: 'def' NAME funcDefArgList '->' returnType ;

ifStmt : IF booleanExpression '{' statementList? '}' ;
elifStmt : ELIF booleanExpression '{' statementList? '}' ;
elseStmt : ELSE '{' statementList? '}' ;
conditionalStmt : ifStmt elifStmt* elseStmt? ;

fieldInit: NAME ':' expression ;
fieldInitList: fieldInit (',' fieldInit)* ;
makeStructExpr : NAME '{' fieldInitList? '}' ;
whileStmt: WHILE booleanExpression '{' statementList? '}' ;

loopStmt: whileStmt;
// statements
statementList: statement+ ;

statement: returnStmt | funcCallStmt | assigmentStmt | declareAndAssignStmt | conditionalStmt | loopStmt;
returnStmt: 'return' (simpleExpression | multiArthimeticExpr)?  SEMICOLON;
funcCallStmt: funcCall SEMICOLON;

declareAndAssignStmt : varDeclare '=' expression SEMICOLON ;

assigmentStmt : (NAME | field) '=' expression SEMICOLON ;

funcDefArgList : '(' typedArgList? ')' ;
typedArgList: typedArg ( ',' typedArg )* ;
typedArg: NAME ':' varType ;

varDeclare: LET MUT? NAME ;

arithmetic_op : ADD | SUBTRACT | MULTIPLY | DIVIDE ;
factor: simpleExpression (KW_POWER simpleExpression)? | '(' factor ')';
arthimeticExpr : factor (arithmetic_op factor)* |
                '(' factor (arithmetic_op factor)* ')' ;
multiArthimeticExpr : arthimeticExpr ( arithmetic_op arthimeticExpr)* ;

comparisonExpr: simpleExpression numeric_comparison_op simpleExpression |
                '(' simpleExpression numeric_comparison_op simpleExpression ')' ;

simpleBooleanExpression : booleanLiteral | NAME | funcCall | comparisonExpr ;
booleanExpression : simpleBooleanExpression (boolean_comparison_op simpleBooleanExpression)* |
                    '(' simpleBooleanExpression (boolean_comparison_op simpleBooleanExpression)* ')';

boolean_comparison_op : AND | OR | XOR ;
numeric_comparison_op : EQ | NEQ | LT | LTE | GT | GTE ;
booleanLiteral : TRUE | FALSE ;

numeric : DOUBLE | INTEGER ;
primitive : numeric | STRING ;
field : NAME FIELD_REF+ ;
simpleExpression : (primitive | NAME | field | funcCall) ;
expression : simpleExpression | arthimeticExpr | multiArthimeticExpr | booleanExpression | makeStructExpr;

funcCall: NAME funcCallDataList ;
funcCallDataList: '(' dataList? ')' ;
dataList: data (',' data)* ;
data: expression;

returnType: ('void' | 'int' | 'double' | BOOL | NAME) ;
varType : ('double' | 'int' | NAME) ;



/*
 * lexer rules
 */
EQ : '==' ;
NEQ : '!=' ;
LT : '<' ;
LTE : '<=' ;
GT : '>' ;
GTE : '>=' ;

AND : 'and';
OR : 'or';
XOR : 'xor';

TRUE : 'true' ;
FALSE : 'false' ;

LET : 'let' ;
MUT : 'mut' ;
IF : 'if' ;
ELIF : 'elif' ;
ELSE : 'else' ;
BOOL : 'bool' ;
PACKAGE : 'package' ;
SEMICOLON : ';' ;
STRUCT: 'struct' ;
TYPE: 'type' ;
WHILE: 'while' ;
KW_DOUBLE: 'double' ;
KW_INT: 'int' ;
VOID: 'void';
ADD: '+' ;
SUBTRACT: '-' ;
MULTIPLY: '*' ;
DIVIDE: '/' ;
KW_POWER: '**';
DOUBLE: INTEGER '.' [0-9]+ ;
INTEGER: '0' | NON_ZERO_INTEGER ;

FIELD_REF : '.' NAME;

// RETURN_TYPE: VAR_TYPE | VOID ;
NAME: ID_START ID_CONTINUE*;
STRING: SHORT_STRING ;

fragment ID_START : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE : ID_START | [0-9] ;
fragment NON_ZERO_INTEGER: '-'? POSITIVE_INTEGER  ;
fragment POSITIVE_INTEGER: [1-9] [0-9]* ;
// fragment VAR_TYPE : (KW_DOUBLE | KW_INT) ;
// fragment SIGN: '+' | '-' ;

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
