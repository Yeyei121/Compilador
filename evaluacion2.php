<?php


// TOKENS VALIDOS
function ejemplo($a, $b) {
    $c = $a + $b;
    $d = $a * 3.14;
    $e = 1e5;
    echo "Hola mundo";
    return $c;
}
if (true) { } elseif (false) { } else { }
while ($x < 10) { break; }
for ($i = 0; $i < 5; $i++) { continue; }
foreach ($arr as $k => $v) { }
do { } while (false);
switch ($x) { case 1: break; default: break; }
class MiClase extends Otra implements Interf {
    public $a; private $b; protected $c; static $d;
    const X = 1; var $e;
}
try { throw new Exception("e"); } catch (Exception $e) { } finally { }
include "a.php"; include_once "b.php";
require "c.php"; require_once "d.php";
$a += 1; $a -= 1; $a *= 2; $a /= 2; $a %= 3; $a .= "x";
$a++; $a--;
$r = ($a == $b); $r = ($a === $b); $r = ($a != $b); $r = ($a !== $b);
$r = ($a <> $b); $r = ($a <= $b); $r = ($a >= $b); $r = ($a <=> $b);
$r = ($a && $b); $r = ($a || $b); $r = ($a ** 2); $r = ($a ?? "d");
$r = $obj->prop; $r = Cls::CONST_VAL; $r = @func();
$r = ($a instanceof MiClase);
global $g; isset($a); unset($a); empty($a);
$s1 = "Escape \"ok\""; $s2 = 'Escape \'ok\'';
// Comentario linea
# Comentario hash
/* Comentario bloque */

//  ERROR 1: Numeros mal formados (numero + letras) 
$e1 = 5x;              // numero seguido de letra
$e2 = 10abc;            // numero seguido de multiples letras
$e3 = 3.5kg;            // decimal seguido de letras
$e4 = 100ml;            // numero con sufijo de unidad
$e5 = 1e2e3;            // notacion cientifica doble

// ERROR 2: Variable que empieza con numero ($+digito) 
$1var = 10;             // $ seguido de digito
$99nombre = 99;         // $ seguido de digitos y letras

// ERROR 3: Dolar suelto ($ sin identificador valido) 
$ resultado = 5;        // $ + espacio + identificador
$ = 10;                 // $ solo

// ERROR 4: Caracteres fuera del alfabeto PHP 
$a = ¿pregunta?;       // signo de interrogacion invertido
$b = ¡exclamacion!;    // signo de exclamacion invertido
$c = 5 ¬ 3;            // negacion logica (no es ! de PHP)
$d = 15°;              // simbolo de grado
$e = €100;             // simbolo euro
$f = £50;              // simbolo libra

// ERROR 5: Operadores unicode (no son operadores ASCII) 
$g = 5 × 3;            // multiplicacion unicode (no es *)
$h = 10 ÷ 2;           // division unicode (no es /)

// ERROR 6: Backslash suelto fuera de string 
$bs = \;                // backslash fuera de string

// ERROR 7: Combinacion de multiples errores en una linea 
$1x = 5abc;             // variable invalida + numero mal formado
$r = 5 ¬ 3 × 2;        // caracteres ilegales multiples

// ERROR 8: Errores dentro de estructuras 
function errorParam($1p) { return $1p; }  // variable invalida en parametro
if ($x == 5abc) { echo "e"; }             // numero mal formado en condicion
$arr = array(1abc, 2px);                  // numeros mal formados en array

// ERROR 9: Recuperacion del lexer despues de errores 
¡¿¬°;                                    // multiples caracteres ilegales seguidos
echo "Este echo debe tokenizarse bien";  // token valido despues de errores
$final = 42;                             // asignacion valida al final

// ERROR 10: String sin cerrar (DEBE ir al final del archivo) 
$mensaje = "Texto sin cerrar;
?>
