<?php
// Funciones con errores lexicos para probar el analizador

// Funcion sin parametros ni retorno
function mostrarSaludo() {
    echo "¡Hola, bienvenido a PHP!<br>";   // ¡ dentro de un string: NO es error
}

// Funcion con parametros y valor de retorno
function sumarNumeros($num1, $num2) {
    $ resultado = 5x + $num2;
    return $resultado;
}

// Funcion para calcular un descuento
function calcularDescuento($precio) {
    $porcentaje = 15°;
    $descuento = $precio * 3.5kg / 100;
    return $precio - $descuento;
}

// Variable con nombre invalido
$2valor = 100;

// Simbolos fuera del alfabeto
$ciudad = ¿Pereira?;
$edad = 20 ¬ 5;

// Invocacion de las funciones
mostrarSaludo(); // ¿Esto es error? No, esta dentro de un comentario

$total = sumarNumeros(5, 10);
echo "La suma es: " . $total;

// String sin cerrar (debe ir al final del archivo)
$mensaje = "Texto sin cerrar;
?>