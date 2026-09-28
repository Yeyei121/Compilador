<?php

// Variables y asignaciones
$nombre = "Hola Mundo";
$edad = 25;
$precio = 99.99;
$activo = true;

// Estructura if-elseif-else
if ($edad >= 18) {
    echo $nombre;
} elseif ($edad > 12) {
    echo "Adolescente";
} else {
    echo "Menor";
}

// Ciclo while
$i = 0;
while ($i < 10) {
    $i++;
}

// Ciclo for
for ($j = 0; $j <= 5; $j++) {
    echo $j;
}

// Foreach
$arreglo = array(1, 2, 3);
foreach ($arreglo as $valor) {
    echo $valor;
}

// Funcion
function sumar($a, $b) {
    return $a + $b;
}

// Clase
class Persona {
    public $nombre;
    private $edad;
    protected $correo;

    public static function crear($nombre) {
        $obj = new Persona();
        $obj->nombre = $nombre;
        return $obj;
    }
}

// Switch
switch ($edad) {
    case 18:
        echo "Mayor de edad";
        break;
    default:
        echo "Otra edad";
        break;
}

// Operadores
$resultado = (10 + 5) * 3 - 2 / 1;
$modulo = 10 % 3;
$potencia = 2 ** 3;
$concatenar = "Hola" . " Mundo";
$concatenar .= "!";

// Operadores de comparacion
$igual = ($a == $b);
$identico = ($a === $b);
$diferente = ($a != $b);
$noIdentico = ($a !== $b);

// Operadores logicos
$and_result = ($a && $b);
$or_result = ($a || $b);
$and_word = ($a and $b);
$or_word = ($a or $b);

// Try-catch
try {
    throw new Exception("Error");
} catch (Exception $e) {
    die("Error fatal");
} finally {
    echo "Fin";
}

// Include y require
include 'archivo.php';
require 'otro.php';
include_once 'unico.php';
require_once 'unico2.php';

// Isset, unset, empty
isset($nombre);
unset($nombre);
empty($nombre);

// Doble dos puntos
Persona::crear("Juan");

// Variable global y constante
global $config;
const MAX_SIZE = 100;

// Exit
exit;

?>
