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

breakStmt: BREAK INTEGER? SEMICOLON ;
branchStmt: breakStmt ;

// statements
statementList: statement+ ;

statement: returnStmt | funcCallStmt | assigmentStmt | declareAndAssignStmt | conditionalStmt | loopStmt | branchStmt ;
returnStmt: 'return' (simpleExpression | arthimeticExpr)?  SEMICOLON;
funcCallStmt: funcCall SEMICOLON;

declareAndAssignStmt : varDeclare '=' expression SEMICOLON ;

assigmentStmt : (NAME | field) '=' expression SEMICOLON ;

funcDefArgList : '(' typedArgList? ')' ;
typedArgList: typedArg ( ',' typedArg )* ;
typedArg: NAME ':' varType ;

varDeclare: LET MUT? NAME ;

arith_factor_op: MULTIPLY | DIVIDE ;
arith_term_op: ADD | SUBTRACT ;
arithmetic_op : ADD | SUBTRACT | MULTIPLY | DIVIDE ;
arith_atom: simpleExpression | '(' arthimeticExpr ')';
power: arith_atom (KW_POWER arith_atom)*;
factor: power (arith_factor_op power)*;
term : factor (arith_term_op factor)*;
arthimeticExpr : term;

comparisonExpr: simpleExpression numeric_comparison_op simpleExpression |
                '(' simpleExpression numeric_comparison_op simpleExpression ')' ;

simpleBooleanExpression : booleanLiteral | NAME | funcCall | comparisonExpr ;
bool_atom: simpleBooleanExpression | '(' booleanExpression ')';
andBooleanExpression: bool_atom (AND bool_atom)*;
orBooleanExpression: andBooleanExpression (OR andBooleanExpression)*;
booleanExpression : orBooleanExpression;

boolean_comparison_op : AND | OR | XOR ;
numeric_comparison_op : EQ | NEQ | LT | LTE | GT | GTE ;
booleanLiteral : TRUE | FALSE ;

numeric : DOUBLE | INTEGER ;
primitive : numeric | STRING ;
field : NAME FIELD_REF+ ;
simpleExpression : (primitive | NAME | field | funcCall) ;
expression : simpleExpression | arthimeticExpr | booleanExpression | makeStructExpr;

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
BREAK : 'break' ;
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

LineComment
    :   '#' ~[\r\n]*
        -> skip
    ;
