grammar Mamba;

/*
 * parser rules
 */
program: package typedef* funcdef+ ;

package: PACKAGE NAME SEMICOLON;
typedef: TYPE STRUCT '{' typedArgList? '}' NAME SEMICOLON;
funcdef: signature '{' statementList? '}' ;
signature: 'def' NAME funcDefArgList '->' returnType ;

ifStmt : IF comparisonExpr '{' statementList? '}' ;
elifStmt : ELIF comparisonExpr '{' statementList? '}' ;
elseStmt : ELSE '{' statementList? '}' ;
conditionalStmt : ifStmt elifStmt* elseStmt? ;

fieldInit: NAME ':' expression ;
fieldInitList: fieldInit (',' fieldInit)* ;
makeStructExpr : NAME '{' fieldInitList? '}' ;
whileStmt: WHILE comparisonExpr '{' statementList? '}' ;

loopStmt: whileStmt;
// statements
statementList: statement+ ;

statement: returnStmt | funcCallStmt | assigmentStmt | declareAndAssignStmt | conditionalStmt | loopStmt;
returnStmt: 'return' (simpleExpression | multiArthimeticExpr)?  SEMICOLON;
funcCallStmt: funcCall SEMICOLON;

declareAndAssignStmt : varDeclare '=' expression SEMICOLON ;

assigmentStmt : NAME '=' expression SEMICOLON ;

funcDefArgList : '(' typedArgList? ')' ;
typedArgList: typedArg ( ',' typedArg )* ;
typedArg: NAME ':' varType ;

varDeclare: LET MUT? NAME ;

arithmetic_op : ADD | SUBTRACT | MULTIPLY | DIVIDE ;
arthimeticExpr : simpleExpression (arithmetic_op simpleExpression)* |
                '(' simpleExpression (arithmetic_op simpleExpression)* ')' ;
multiArthimeticExpr : arthimeticExpr ( arithmetic_op arthimeticExpr)* ;

comparisonExpr: simpleExpression bool_comparison_op simpleExpression |
                '(' simpleExpression bool_comparison_op simpleExpression ')' ;
bool_comparison_op : EQ | NEQ | LT | LTE | GT | GTE ;
booleanLiteral : TRUE | FALSE ;
// simpleBooleanTerm : (booleanLiteral | numeric | NAME | funcCall) ;

numeric : DOUBLE | INTEGER ;
field : NAME FIELD_REF+ ;
simpleExpression : (numeric | NAME | field | funcCall) ;
expression : simpleExpression | arthimeticExpr | multiArthimeticExpr | comparisonExpr | makeStructExpr;

funcCall: NAME funcCallDataList ;
funcCallDataList: '(' dataList? ')' ;
dataList: data (',' data)* ;
data: STRING | NAME | DOUBLE | INTEGER;

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

DOUBLE: INTEGER '.' [0-9]+ ;
INTEGER: '0' | NON_ZERO_INTEGER ;

FIELD_REF : '.' NAME;

// RETURN_TYPE: VAR_TYPE | VOID ;
NAME: ID_START ID_CONTINUE*;
STRING: SHORT_STRING ;

fragment ID_START : '_' | [A-Z] | [a-z] ;
fragment ID_CONTINUE : ID_START | [0-9] ;
fragment NON_ZERO_INTEGER: SIGN? POSITIVE_INTEGER  ;
fragment POSITIVE_INTEGER: [1-9] [0-9]* ;
// fragment VAR_TYPE : (KW_DOUBLE | KW_INT) ;
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
