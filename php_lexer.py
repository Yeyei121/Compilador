import ply.lex as lex
import sys
import re

# Código desarrollado con ayuda de Claude

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
    'INSTANCEOF',

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
    'BITAND',
    'BITOR',
    'SPACESHIP',
    'NULLCOALESCING',
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
t_BITAND = r'&'
t_BITOR = r'\|'

def t_ELSEIF(t):
    r'elseif\b'
    return t

def t_ELSE(t):
    r'else\b'
    return t

def t_IF(t):
    r'if\b'
    return t

def t_WHILE(t):
    r'while\b'
    return t

def t_FOREACH(t):
    r'foreach\b'
    return t

def t_FOR(t):
    r'for\b'
    return t

def t_DO(t):
    r'do\b'
    return t

def t_SWITCH(t):
    r'switch\b'
    return t

def t_CASE(t):
    r'case\b'
    return t

def t_DEFAULT(t):
    r'default\b'
    return t

def t_BREAK(t):
    r'break\b'
    return t

def t_CONTINUE(t):
    r'continue\b'
    return t

def t_RETURN(t):
    r'return\b'
    return t

def t_FUNCTION(t):
    r'function\b'
    return t

def t_CLASS(t):
    r'class\b'
    return t

def t_PUBLIC(t):
    r'public\b'
    return t

def t_PRIVATE(t):
    r'private\b'
    return t

def t_PROTECTED(t):
    r'protected\b'
    return t

def t_STATIC(t):
    r'static\b'
    return t

def t_NEW(t):
    r'new\b'
    return t

def t_ECHO(t):
    r'echo\b'
    return t

def t_PRINT(t):
    r'print\b'
    return t

def t_ARRAY(t):
    r'array\b'
    return t

def t_NULL(t):
    r'null\b'
    return t

def t_TRUE(t):
    r'true\b'
    return t

def t_FALSE(t):
    r'false\b'
    return t

def t_AND(t):
    r'and\b'
    return t

def t_OR(t):
    r'or\b'
    return t

def t_NOT(t):
    r'not\b'
    return t

def t_ISSET(t):
    r'isset\b'
    return t

def t_UNSET(t):
    r'unset\b'
    return t

def t_EMPTY(t):
    r'empty\b'
    return t

def t_DIE(t):
    r'die\b'
    return t

def t_EXIT(t):
    r'exit\b'
    return t

def t_INCLUDE_ONCE(t):
    r'include_once\b'
    return t

def t_INCLUDE(t):
    r'include\b'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once\b'
    return t

def t_REQUIRE(t):
    r'require\b'
    return t

def t_TRY(t):
    r'try\b'
    return t

def t_CATCH(t):
    r'catch\b'
    return t

def t_FINALLY(t):
    r'finally\b'
    return t

def t_THROW(t):
    r'throw\b'
    return t

def t_EXTENDS(t):
    r'extends\b'
    return t

def t_IMPLEMENTS(t):
    r'implements\b'
    return t

def t_INTERFACE(t):
    r'interface\b'
    return t

def t_ABSTRACT(t):
    r'abstract\b'
    return t

def t_CONST(t):
    r'const\b'
    return t

def t_VAR(t):
    r'var\b'
    return t

def t_GLOBAL(t):
    r'global\b'
    return t

def t_AS(t):
    r'as\b'
    return t

def t_INSTANCEOF(t):
    r'instanceof\b'
    return t

def t_OPEN_TAG(t):
    r'<\?php'
    return t

def t_CLOSE_TAG(t):
    r'\?>'
    return t

def t_SPACESHIP(t):
    r'<=>'
    return t

def t_IDENTICAL(t):
    r'==='
    return t

def t_NOTIDENTICAL(t):
    r'!=='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'<>'
    return t

def t_LOGICALAND(t):
    r'&&'
    return t

def t_LOGICALOR(t):
    r'\|\|'
    return t

def t_NULLCOALESCING(t):
    r'\?\?'
    return t

def t_POWER(t):
    r'\*\*'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_PLUSEQUAL(t):
    r'\+='
    return t

def t_MINUSMINUS(t):
    r'--'
    return t

def t_MINUSEQUAL(t):
    r'-='
    return t

def t_TIMESEQUAL(t):
    r'\*='
    return t

def t_DIVIDEEQUAL(t):
    r'/='
    return t

def t_MODULOEQUAL(t):
    r'%='
    return t

def t_ARROW(t):
    r'->'
    return t

def t_DOUBLEARROW(t):
    r'=>'
    return t

def t_DOUBLECOLON(t):
    r'::'
    return t

def t_DOTEQUAL(t):
    r'\.='
    return t

def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"|\'([^\\\']|\\.)*\''
    return t

def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_DOLLAR(t):
    r'\$(?=[\$\{])'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?([eE][+-]?\d+)?\w*'
    if not re.fullmatch(r'\d+(\.\d+)?([eE][+-]?\d+)?', t.value):
        print(f"Lexical error: número mal formado '{t.value}' en línea {t.lineno}")
        return None
    if '.' in t.value or 'e' in t.value.lower():
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|[\r\n])*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

def t_comments_line(t):
    r'//[^\n]*'
    pass

def t_comments_hash(t):
    r'\#[^\n]*'
    pass

def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

lexer = lex.lex(reflags=re.IGNORECASE | re.VERBOSE)

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'evaluacion.php'
    f = open(fin, 'r', encoding='utf-8')
    data = f.read()
    print(data)
    lexer.input(data)
    test(data, lexer)