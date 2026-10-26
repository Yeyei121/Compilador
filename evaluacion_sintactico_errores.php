<?php
// Prueba del analizador sintactico con errores
// Cada bloque ERROR tiene un solo error sintactico (22 en total); el resto del codigo es valido

// CODIGO VALIDO
function sumar($a, $b) {
    return $a + $b;
}
$total = sumar(4, 6);
echo "Total: " . $total;

// ERROR 1: falta ';' al final de la asignacion
$precio = 2500
$cantidad = 3;

// ERROR 2: falta ')' en la condicion del if
if ($cantidad > 2 {
    echo "Varios productos";
}

// ERROR 3: falta '(' en el while
while $cantidad > 0) {
    $cantidad--;
}

// ERROR 4: parentesis de mas en la condicion
if (($precio > 1000))) {
    echo "Caro";
}

// ERROR 5: operador sin operando derecho
$iva = $precio * ;

// ERROR 6: dos operadores seguidos
$descuento = $precio * / 10;

// ERROR 7: asignacion a un numero
100 = $precio;

// ERROR 8: else sin if
else {
    echo "Sin if";
}

// ERROR 9: for con comas en lugar de punto y coma
for ($i = 0, $i < 10, $i++) {
    echo $i;
}

// ERROR 10: foreach sin la palabra as
foreach ($lista $item) {
    echo $item;
}

// ERROR 11: funcion sin nombre
function ($x) {
    return $x * 2;
}

// ERROR 12: parametros sin coma
function restar($a $b) {
    return $a - $b;
}

// ERROR 13: llamada a funcion sin cerrar el parentesis
$resultado = sumar(10, 20;

// ERROR 14: arreglo sin cerrar el corchete
$notas = [4.5, 3.2, 5.0;

// ERROR 15: case sin los dos puntos
switch ($cantidad) {
    case 1
        echo "Uno";
        break;
    default:
        echo "Otro";
}

class Producto {
    // ERROR 16: propiedad sin ';'
    public $nombre
    private $valor = 0;

    // ERROR 17: metodo sin la palabra function
    public mostrar() {
        echo $this->nombre;
    }
}

// ERROR 18: echo sin expresion
echo ;

// ERROR 19: variable sin '$' en una asignacion
contador = 0;

// ERROR 20: operador ternario sin ':'
$estado = $total > 10 ? "alto" ;

// ERROR 21: falta la llave que cierra la funcion
function sinCerrar($n) {
    if ($n > 0) {
        echo "positivo";
    }

function despues() {
    echo "fin";
}

// ERROR 22: llave de cierre de mas
}

echo "Fin de la prueba";
?>
