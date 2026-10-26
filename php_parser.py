import ply.yacc as yacc
import ply.lex as lex
from php_lexer_corregido import tokens
import php_lexer_corregido
import sys

VERBOSE = 1
VENTANA = 6  # tokens siguientes que deben encajar para aceptar una reparacion

lexer = php_lexer_corregido.lexer
errores = []
pendientes = []

CIERRES = ('SEMICOLON', 'RPAREN', 'RBRACKET', 'RBLOCK', 'COMMA', 'COLON')
APERTURAS = ('LPAREN', 'LBLOCK', 'OPEN_TAG')
SIMBOLOS = {
    'SEMICOLON': ';', 'RPAREN': ')', 'RBRACKET': ']', 'RBLOCK': '}', 'COMMA': ',',
    'COLON': ':', 'LPAREN': '(', 'LBLOCK': '{', 'OPEN_TAG': '<?php',
}

# El if sin else tiene menor precedencia que ELSE/ELSEIF (else colgante)
precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSEIF', 'ELSE'),
)

def p_program_1(p):
    'program : OPEN_TAG declaration_list CLOSE_TAG'
    pass

def p_program_2(p):
    'program : OPEN_TAG declaration_list'
    pass

def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
    pass

def p_declaration_list_2(p):
    'declaration_list : empty'
    pass

def p_declaration(p):
    '''declaration : fun_declaration
                   | class_declaration
                   | interface_declaration
                   | statement'''
    pass

# Funciones

def p_fun_declaration(p):
    'fun_declaration : FUNCTION ID LPAREN params RPAREN return_type compound_stmt'
    pass

def p_return_type_1(p):
    'return_type : COLON type_specifier'
    pass

def p_return_type_2(p):
    'return_type : empty'
    pass

def p_type_specifier_1(p):
    'type_specifier : simple_type'
    pass

def p_type_specifier_2(p):
    'type_specifier : QUESTIONMARK simple_type'
    pass

def p_type_specifier_3(p):
    'type_specifier : type_specifier BITOR simple_type'
    pass

def p_simple_type(p):
    '''simple_type : ID
                   | ARRAY'''
    pass

def p_params_1(p):
    'params : param_list'
    pass

def p_params_2(p):
    'params : empty'
    pass

def p_param_list_1(p):
    'param_list : param_list COMMA param'
    pass

def p_param_list_2(p):
    'param_list : param'
    pass

def p_param_1(p):
    '''param : param_var
             | param_var EQUAL expression'''
    pass

def p_param_2(p):
    '''param : type_specifier param_var
             | type_specifier param_var EQUAL expression'''
    pass

def p_param_var(p):
    '''param_var : VARIABLE
                 | BITAND VARIABLE'''
    pass

# Clases e interfaces

def p_class_declaration_1(p):
    'class_declaration : CLASS ID class_extends class_implements LBLOCK class_member_list RBLOCK'
    pass

def p_class_declaration_2(p):
    'class_declaration : ABSTRACT CLASS ID class_extends class_implements LBLOCK class_member_list RBLOCK'
    pass

def p_class_extends(p):
    '''class_extends : EXTENDS ID
                     | empty'''
    pass

def p_class_implements(p):
    '''class_implements : IMPLEMENTS id_list
                        | empty'''
    pass

def p_id_list(p):
    '''id_list : id_list COMMA ID
               | ID'''
    pass

def p_interface_declaration(p):
    'interface_declaration : INTERFACE ID interface_extends LBLOCK class_member_list RBLOCK'
    pass

def p_interface_extends(p):
    '''interface_extends : EXTENDS id_list
                         | empty'''
    pass

def p_class_member_list_1(p):
    'class_member_list : class_member_list class_member'
    pass

def p_class_member_list_2(p):
    'class_member_list : empty'
    pass

def p_class_member_1(p):
    '''class_member : modifier_list VARIABLE SEMICOLON
                    | modifier_list VARIABLE EQUAL expression SEMICOLON
                    | modifier_list type_specifier VARIABLE SEMICOLON
                    | modifier_list type_specifier VARIABLE EQUAL expression SEMICOLON'''
    pass

def p_class_member_2(p):
    '''class_member : CONST ID EQUAL expression SEMICOLON
                    | modifier_list CONST ID EQUAL expression SEMICOLON'''
    pass

def p_class_member_3(p):
    '''class_member : FUNCTION ID LPAREN params RPAREN return_type method_body
                    | modifier_list FUNCTION ID LPAREN params RPAREN return_type method_body'''
    pass

def p_method_body(p):
    '''method_body : compound_stmt
                   | SEMICOLON'''
    pass

def p_modifier_list(p):
    '''modifier_list : modifier_list modifier
                     | modifier'''
    pass

def p_modifier(p):
    '''modifier : PUBLIC
                | PRIVATE
                | PROTECTED
                | STATIC
                | ABSTRACT
                | VAR'''
    pass

# Sentencias

def p_compound_stmt(p):
    'compound_stmt : LBLOCK statement_list RBLOCK'
    pass

def p_statement_list_1(p):
    'statement_list : statement_list statement'
    pass

def p_statement_list_2(p):
    'statement_list : empty'
    pass

def p_statement(p):
    '''statement : expression_stmt
                 | compound_stmt
                 | selection_stmt
                 | iteration_stmt
                 | return_stmt
                 | echo_stmt
                 | jump_stmt
                 | global_stmt
                 | static_stmt
                 | const_stmt
                 | unset_stmt
                 | include_stmt
                 | try_stmt
                 | throw_stmt'''
    pass

def p_expression_stmt_1(p):
    'expression_stmt : expression SEMICOLON'
    pass

def p_expression_stmt_2(p):
    'expression_stmt : SEMICOLON'
    pass

def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN statement %prec IFX'
    pass

def p_selection_stmt_2(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
    pass

def p_selection_stmt_3(p):
    'selection_stmt : IF LPAREN expression RPAREN statement elseif_stmt'
    pass

def p_selection_stmt_4(p):
    'selection_stmt : SWITCH LPAREN expression RPAREN LBLOCK case_list RBLOCK'
    pass

def p_elseif_stmt_1(p):
    'elseif_stmt : ELSEIF LPAREN expression RPAREN statement %prec IFX'
    pass

def p_elseif_stmt_2(p):
    'elseif_stmt : ELSEIF LPAREN expression RPAREN statement ELSE statement'
    pass

def p_elseif_stmt_3(p):
    'elseif_stmt : ELSEIF LPAREN expression RPAREN statement elseif_stmt'
    pass

def p_case_list_1(p):
    'case_list : case_list case_stmt'
    pass

def p_case_list_2(p):
    'case_list : empty'
    pass

def p_case_stmt_1(p):
    'case_stmt : CASE expression COLON statement_list'
    pass

def p_case_stmt_2(p):
    'case_stmt : DEFAULT COLON statement_list'
    pass

def p_iteration_stmt_1(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    pass

def p_iteration_stmt_2(p):
    'iteration_stmt : DO compound_stmt WHILE LPAREN expression RPAREN SEMICOLON'
    pass

def p_iteration_stmt_3(p):
    'iteration_stmt : FOR LPAREN for_expression SEMICOLON for_expression SEMICOLON for_expression RPAREN statement'
    pass

def p_iteration_stmt_4(p):
    '''iteration_stmt : FOREACH LPAREN expression AS foreach_var RPAREN statement
                      | FOREACH LPAREN expression AS foreach_var DOUBLEARROW foreach_var RPAREN statement'''
    pass

def p_for_expression(p):
    '''for_expression : args_list
                      | empty'''
    pass

def p_foreach_var(p):
    '''foreach_var : var
                   | BITAND var'''
    pass

def p_return_stmt_1(p):
    'return_stmt : RETURN SEMICOLON'
    pass

def p_return_stmt_2(p):
    'return_stmt : RETURN expression SEMICOLON'
    pass

def p_echo_stmt_1(p):
    'echo_stmt : ECHO args_list SEMICOLON'
    pass

def p_echo_stmt_2(p):
    'echo_stmt : PRINT expression SEMICOLON'
    pass

def p_jump_stmt(p):
    '''jump_stmt : BREAK SEMICOLON
                 | BREAK NUMBER SEMICOLON
                 | CONTINUE SEMICOLON
                 | CONTINUE NUMBER SEMICOLON'''
    pass

def p_global_stmt(p):
    'global_stmt : GLOBAL var_list SEMICOLON'
    pass

def p_var_list(p):
    '''var_list : var_list COMMA VARIABLE
                | VARIABLE'''
    pass

def p_static_stmt(p):
    'static_stmt : STATIC static_list SEMICOLON'
    pass

def p_static_list(p):
    '''static_list : static_list COMMA static_var
                   | static_var'''
    pass

def p_static_var(p):
    '''static_var : VARIABLE
                  | VARIABLE EQUAL expression'''
    pass

def p_const_stmt(p):
    'const_stmt : CONST ID EQUAL expression SEMICOLON'
    pass

def p_unset_stmt(p):
    'unset_stmt : UNSET LPAREN args_list RPAREN SEMICOLON'
    pass

def p_include_stmt(p):
    'include_stmt : include_type expression SEMICOLON'
    pass

def p_include_type(p):
    '''include_type : INCLUDE
                    | INCLUDE_ONCE
                    | REQUIRE
                    | REQUIRE_ONCE'''
    pass

def p_try_stmt(p):
    '''try_stmt : TRY compound_stmt catch_list
                | TRY compound_stmt catch_list FINALLY compound_stmt
                | TRY compound_stmt FINALLY compound_stmt'''
    pass

def p_catch_list(p):
    '''catch_list : catch_list catch_clause
                  | catch_clause'''
    pass

def p_catch_clause(p):
    '''catch_clause : CATCH LPAREN catch_types VARIABLE RPAREN compound_stmt
                    | CATCH LPAREN catch_types RPAREN compound_stmt'''
    pass

def p_catch_types(p):
    '''catch_types : catch_types BITOR ID
                   | ID'''
    pass

def p_throw_stmt(p):
    'throw_stmt : THROW expression SEMICOLON'
    pass

# Expresiones

def p_expression_1(p):
    'expression : var assignop expression'
    pass

def p_expression_2(p):
    'expression : var EQUAL BITAND var'
    pass

def p_expression_3(p):
    'expression : conditional_expression'
    pass

def p_assignop(p):
    '''assignop : EQUAL
                | PLUSEQUAL
                | MINUSEQUAL
                | TIMESEQUAL
                | DIVIDEEQUAL
                | MODULOEQUAL
                | DOTEQUAL'''
    pass

def p_conditional_expression_1(p):
    '''conditional_expression : logical_expression QUESTIONMARK expression COLON conditional_expression
                              | logical_expression QUESTIONMARK COLON conditional_expression'''
    pass

def p_conditional_expression_2(p):
    'conditional_expression : logical_expression NULLCOALESCING conditional_expression'
    pass

def p_conditional_expression_3(p):
    'conditional_expression : logical_expression'
    pass

def p_logical_expression_1(p):
    'logical_expression : logical_expression orop logical_term'
    pass

def p_logical_expression_2(p):
    'logical_expression : logical_term'
    pass

def p_orop(p):
    '''orop : LOGICALOR
            | OR'''
    pass

def p_logical_term_1(p):
    'logical_term : logical_term andop bit_expression'
    pass

def p_logical_term_2(p):
    'logical_term : bit_expression'
    pass

def p_andop(p):
    '''andop : LOGICALAND
             | AND'''
    pass

def p_bit_expression_1(p):
    'bit_expression : bit_expression bitop simple_expression'
    pass

def p_bit_expression_2(p):
    'bit_expression : simple_expression'
    pass

def p_bitop(p):
    '''bitop : BITAND
             | BITOR'''
    pass

def p_simple_expression_1(p):
    'simple_expression : additive_expression relop additive_expression'
    pass

def p_simple_expression_2(p):
    'simple_expression : additive_expression'
    pass

def p_relop(p):
    '''relop : LESS
             | LESSEQUAL
             | GREATER
             | GREATEREQUAL
             | ISEQUAL
             | NOTEQUAL
             | DEQUAL
             | IDENTICAL
             | NOTIDENTICAL
             | SPACESHIP'''
    pass

def p_additive_expression_1(p):
    'additive_expression : additive_expression addop term'
    pass

def p_additive_expression_2(p):
    'additive_expression : term'
    pass

def p_addop(p):
    '''addop : PLUS
             | MINUS
             | DOT'''
    pass

def p_term_1(p):
    'term : term mulop unary_expression'
    pass

def p_term_2(p):
    'term : unary_expression'
    pass

def p_mulop(p):
    '''mulop : TIMES
             | DIVIDE
             | MODULO'''
    pass

def p_unary_expression_1(p):
    '''unary_expression : DISTINT unary_expression
                        | NOT unary_expression
                        | MINUS unary_expression
                        | PLUS unary_expression
                        | AT unary_expression
                        | CAST unary_expression'''
    pass

def p_unary_expression_2(p):
    '''unary_expression : PLUSPLUS var
                        | MINUSMINUS var'''
    pass

def p_unary_expression_3(p):
    'unary_expression : factor POWER unary_expression'
    pass

def p_unary_expression_4(p):
    'unary_expression : factor INSTANCEOF class_name'
    pass

def p_unary_expression_5(p):
    'unary_expression : factor'
    pass

def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    pass

def p_factor_2(p):
    'factor : var'
    pass

def p_factor_3(p):
    'factor : call'
    pass

def p_factor_4(p):
    '''factor : var PLUSPLUS
              | var MINUSMINUS'''
    pass

def p_factor_5(p):
    '''factor : NUMBER
              | STRING
              | TRUE
              | FALSE
              | NULL
              | ID'''
    pass

def p_factor_6(p):
    '''factor : class_name DOUBLECOLON ID
              | class_name DOUBLECOLON CLASS'''
    pass

def p_factor_7(p):
    'factor : array_literal'
    pass

def p_factor_8(p):
    '''factor : NEW class_name
              | NEW class_name LPAREN args RPAREN'''
    pass

def p_factor_9(p):
    '''factor : ISSET LPAREN args_list RPAREN
              | EMPTY LPAREN expression RPAREN'''
    pass

def p_factor_10(p):
    '''factor : EXIT
              | EXIT LPAREN args RPAREN
              | DIE
              | DIE LPAREN args RPAREN'''
    pass

def p_var_1(p):
    'var : simple_var'
    pass

def p_var_2(p):
    '''var : var LBRACKET expression RBRACKET
           | var LBRACKET RBRACKET
           | call LBRACKET expression RBRACKET'''
    pass

def p_var_3(p):
    '''var : var ARROW ID
           | call ARROW ID'''
    pass

def p_var_4(p):
    'var : class_name DOUBLECOLON VARIABLE'
    pass

def p_simple_var(p):
    '''simple_var : VARIABLE
                  | DOLLAR simple_var
                  | DOLLAR LBLOCK expression RBLOCK'''
    pass

def p_call_1(p):
    '''call : ID LPAREN args RPAREN
            | VARIABLE LPAREN args RPAREN'''
    pass

def p_call_2(p):
    '''call : var ARROW ID LPAREN args RPAREN
            | call ARROW ID LPAREN args RPAREN'''
    pass

def p_call_3(p):
    'call : class_name DOUBLECOLON ID LPAREN args RPAREN'
    pass

def p_class_name(p):
    '''class_name : ID
                  | STATIC'''
    pass

def p_array_literal(p):
    '''array_literal : ARRAY LPAREN array_items RPAREN
                     | LBRACKET array_items RBRACKET'''
    pass

def p_array_items(p):
    '''array_items : array_list
                   | array_list COMMA
                   | empty'''
    pass

def p_array_list_1(p):
    'array_list : array_list COMMA array_item'
    pass

def p_array_list_2(p):
    'array_list : array_item'
    pass

def p_array_item(p):
    '''array_item : expression
                  | expression DOUBLEARROW expression
                  | BITAND var'''
    pass

def p_args(p):
    '''args : args_list
            | empty'''
    pass

def p_args_list_1(p):
    'args_list : args_list COMMA expression'
    pass

def p_args_list_2(p):
    'args_list : expression'
    pass

def p_empty(p):
    'empty :'
    pass

# Producciones con el token error: el parser se sincroniza y sigue analizando

def p_declaration_error(p):
    '''declaration : error fun_declaration
                   | error class_declaration
                   | error interface_declaration'''
    p.parser.errok()

def p_statement_error(p):
    '''statement : error SEMICOLON
                 | error compound_stmt'''
    p.parser.errok()

def p_class_declaration_error(p):
    '''class_declaration : CLASS error LBLOCK class_member_list RBLOCK
                         | ABSTRACT CLASS error LBLOCK class_member_list RBLOCK'''
    p.parser.errok()

def p_interface_declaration_error(p):
    'interface_declaration : INTERFACE error LBLOCK class_member_list RBLOCK'
    p.parser.errok()

def p_class_member_error(p):
    '''class_member : error SEMICOLON
                    | error compound_stmt'''
    p.parser.errok()

def p_selection_stmt_error(p):
    'selection_stmt : SWITCH error LBLOCK case_list RBLOCK'
    p.parser.errok()

def p_case_stmt_error(p):
    'case_stmt : CASE error COLON statement_list'
    p.parser.errok()

def p_iteration_stmt_error(p):
    'iteration_stmt : FOR LPAREN error RPAREN statement'
    p.parser.errok()

def p_catch_clause_error(p):
    'catch_clause : CATCH error compound_stmt'
    p.parser.errok()

# Intenta insertar, descartar o cambiar un token; si nada encaja, actuan las producciones error

def p_error(p):
    if not VERBOSE:
        raise Exception('syntax', 'error')
    if p is None:
        return reparar_fin_de_archivo()
    # PLY vuelve a llamar a p_error con el simbolo error durante su propia recuperacion
    if p.type == 'error':
        return None
    siguientes = leer_adelante(VENTANA)
    for faltante in CIERRES:
        if acepta([faltante, p.type] + siguientes[:VENTANA - 1]):
            return insertar(faltante, p)
    if acepta(siguientes):
        reportar(p.lineno, "NO SE ESPERABA EL TOKEN '%s'" % p.value)
        parser.errok()
        return None
    for faltante in CIERRES:
        if acepta([faltante] + siguientes):
            reportar(p.lineno, "NO SE ESPERABA EL TOKEN '%s', SE ESPERABA '%s'" % (p.value, SIMBOLOS[faltante]))
            parser.errok()
            return crear_token(faltante, p.lineno, p.lexpos)
    for faltante in APERTURAS:
        if acepta([faltante, p.type] + siguientes[:VENTANA - 1]):
            return insertar(faltante, p)
    reportar(p.lineno, "NO SE ESPERABA EL TOKEN '%s'" % p.value)

def reparar_fin_de_archivo():
    linea = linea_anterior() or lexer.lineno
    opciones = [t for t in CIERRES + APERTURAS if acepta([t, '$end'])]
    opciones += [t for t in ('RPAREN', 'RBRACKET', 'RBLOCK') if acepta([t])]
    if not opciones:
        reportar(linea, 'FIN DE ARCHIVO INESPERADO')
        return None
    reportar(linea, "FALTA '%s' AL FINAL DEL ARCHIVO" % SIMBOLOS[opciones[0]])
    parser.errok()
    return crear_token(opciones[0], linea, lexer.lexpos)

def insertar(faltante, p):
    anterior = linea_anterior()
    if anterior and anterior < p.lineno:
        reportar(anterior, "FALTA '%s' AL FINAL DE LA LINEA" % SIMBOLOS[faltante])
    else:
        reportar(p.lineno, "FALTA '%s' ANTES DE '%s'" % (SIMBOLOS[faltante], p.value))
    pendientes.insert(0, p)
    parser.errok()
    return crear_token(faltante, p.lineno, p.lexpos)

# Simula el automata LALR sobre una copia de la pila; True si la secuencia es valida
def acepta(tipos):
    pila = list(parser.statestack)
    for tipo in tipos:
        while True:
            estado = pila[-1]
            if estado in parser.defaulted_states:
                accion = parser.defaulted_states[estado]
            else:
                accion = parser.action[estado].get(tipo)
            if accion is None:
                return False
            if accion == 0:
                return True
            if accion > 0:
                pila.append(accion)
                break
            regla = parser.productions[-accion]
            if regla.len:
                del pila[-regla.len:]
            pila.append(parser.goto[pila[-1]][regla.name])
    return True

# Los tokens leidos por adelantado quedan en pendientes y se entregan antes que los del lexer
def leer_adelante(n):
    while len(pendientes) < n:
        tok = lexer.token()
        if tok is None:
            break
        pendientes.append(tok)
    return [tok.type for tok in pendientes[:n]]

def siguiente_token():
    if pendientes:
        return pendientes.pop(0)
    return lexer.token()

def crear_token(tipo, linea, posicion):
    tok = lex.LexToken()
    tok.type = tipo
    tok.value = SIMBOLOS[tipo]
    tok.lineno = linea
    tok.lexpos = posicion
    return tok

# Linea del ultimo token reconocido; None si todavia no se ha reconocido ninguno
def linea_anterior():
    for simbolo in reversed(parser.symstack):
        if hasattr(simbolo, 'endlineno'):
            return simbolo.endlineno
        if isinstance(simbolo, lex.LexToken):
            return simbolo.lineno
    return None

def reportar(linea, mensaje):
    errores.append(linea)
    print('ERROR SINTACTICO EN LA LINEA %d: %s' % (linea, mensaje))

parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'evaluacion_sintactico_errores.php'

    with open(fin, 'r', encoding='utf-8') as f:
        data = f.read()
    parser.parse(data, lexer=lexer, tracking=True, tokenfunc=siguiente_token)

    print()
    if errores:
        print('Total de errores sintacticos: %d' % len(errores))
        print('Lineas con errores: ' + ', '.join(str(linea) for linea in errores))
    if lexer.errores_lexicos:
        print('Total de errores lexicos: %d' % lexer.errores_lexicos)
    if not errores and not lexer.errores_lexicos:
        print('Tengo el placer de informar que Tu parser reconocio correctamente todo. Felicitaciones')
