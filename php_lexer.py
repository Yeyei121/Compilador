import ply.lex as lex
import sys

# lista de tokens
tokens = (
    # Reserved words
    'IF',
    'ELSE',
    'ELSEIF',
    'WHILE',
    'FOR',
    'FOREACH',
    'DO',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'BREAK',
    'CONTINUE',
    'RETURN',
    'FUNCTION',
    'CLASS',
    'PUBLIC',
    'PRIVATE',
    'PROTECTED',
    'STATIC',
    'NEW',
    'ECHO',
    'PRINT',
    'ARRAY',
    'NULL',
    'TRUE',
    'FALSE',
    'AND',
    'OR',
    'NOT',
    'ISSET',
    'UNSET',
    'EMPTY',
    'DIE',
    'EXIT',
    'INCLUDE',
    'REQUIRE',
    'INCLUDE_ONCE',
    'REQUIRE_ONCE',
    'TRY',
    'CATCH',
    'FINALLY',
    'THROW',
    'EXTENDS',
    'IMPLEMENTS',
    'INTERFACE',
    'ABSTRACT',
    'CONST',
    'VAR',
    'GLOBAL',
    'AS',

    # Symbols
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'TIMESEQUAL',
    'DIVIDE',
    'DIVIDEEQUAL',
    'MODULO',
    'MODULOEQUAL',
    'POWER',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'ISEQUAL',
    'DISTINT',
    'NOTEQUAL',
    'IDENTICAL',
    'NOTIDENTICAL',
    'LOGICALAND',
    'LOGICALOR',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'DOT',
    'DOTEQUAL',
    'ARROW',
    'DOUBLECOLON',
    'DOUBLEARROW',
    'AT',
    'DOLLAR',
    'QUESTIONMARK',

    # Others
    'VARIABLE',
    'ID',
    'NUMBER',
    'STRING',
    'OPEN_TAG',
    'CLOSE_TAG',
)

# Regular expression rules for simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'\{'
t_RBLOCK   = r'\}'
t_COLON   = r':'
t_DOT = r'\.'
t_AT = r'@'
t_QUESTIONMARK = r'\?'

# Reserved words - functions
def t_ELSEIF(t):
    r'elseif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IF(t):
    r'if'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_DO(t):
    r'do'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_NEW(t):
    r'new'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_NULL(t):
    r'null'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_NOT(t):
    r'not'
    return t

def t_ISSET(t):
    r'isset'
    return t

def t_UNSET(t):
    r'unset'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_DIE(t):
    r'die'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_INCLUDE_ONCE(t):
    r'include_once'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_TRY(t):
    r'try'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INTERFACE(t):
    r'interface'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_CONST(t):
    r'const'
    return t

def t_VAR(t):
    r'var'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_AS(t):
    r'as'
    return t