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