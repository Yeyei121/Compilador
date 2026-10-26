<?php
// Prueba del analizador sintactico: este archivo NO tiene errores
# Usa todas las estructuras que reconoce el parser

/* Comentario de varias lineas
   para comprobar que el conteo de lineas sigue bien */

include "config.php";
include_once 'utilidades.php';
require "conexion.php";
require_once 'funciones.php';

const MAXIMO = 100;
define('MINIMO', 1);

interface Figura {
    public function area(): float;
    public function nombre(): string;
}

interface Imprimible extends Figura, Countable {
    function imprimir();
}

abstract class Base implements Figura {
    protected static $contador = 0;
    public const VERSION = "1.0";
    const AUTOR = 'Grupo de compiladores';

    abstract public function area(): float;

    public function nombre(): string {
        return static::class;
    }
}

class Rectangulo extends Base implements Imprimible {
    private float $ancho;
    private ?float $alto = null;
    public int|float $escala = 1;
    var $etiquetas = [];

    public function __construct(float $ancho, float $alto = 1.0) {
        $this->ancho = $ancho;
        $this->alto = $alto;
        self::$contador++;
    }

    public function area(): float {
        return $this->ancho * $this->alto;
    }

    public function imprimir() {
        echo "Area: ", $this->area(), PHP_EOL;
    }

    public static function crear(array $datos): Rectangulo {
        return new Rectangulo($datos['ancho'], $datos['alto'] ?? 1);
    }
}

function fibonaci($i) {
    if ($i == 0) {
        return 0;
    }
    if ($i == 1)
        return 1;
    return fibonaci($i - 1) + fibonaci($i - 2);
}

function intercambiar(&$a, &$b): void {
    $temporal = $a;
    $a = $b;
    $b = $temporal;
}

function contarLlamadas(?int $inicio = null) {
    static $llamadas = 0, $total;
    global $configuracion, $usuario;
    $llamadas += $inicio ?? 1;
    return $llamadas;
}

$numeros = array(5, 3, 8, 1,);
$persona = ['nombre' => "Ana", 'edad' => 21, 'notas' => [4.5, 3.8]];
$vacio = [];
$figura = new Rectangulo(3, 4.5);
$otra = new Rectangulo;
$suma = 0;

for ($i = 0, $j = 10; $i < count($numeros); $i++, $j--) {
    $suma += $numeros[$i] ** 2;
}

for (;;) {
    break;
}

foreach ($persona as $clave => $valor) {
    echo $clave, ": ", $valor, "\n";
}

foreach ($numeros as &$numero) {
    $numero *= 2;
}

$k = 0;
while ($k < 10) {
    if ($k % 2 == 0) {
        $k++;
        continue;
    } elseif ($k === 7) {
        break;
    } else if ($k <> 3) {
        $k += 2;
    } else {
        --$k;
    }
}

if ($k > 5) echo "mayor"; else echo "menor";

do {
    $k--;
} while ($k > 0 && !empty($numeros) || $k != -1);

switch ($persona['edad']) {
    case 18:
    case 19:
        echo "Recien cumple";
        break;
    case 20 + 1:
        print "Tiene veintiuno";
        break;
    default:
        echo "Otra edad";
}

try {
    if (!isset($persona['correo'], $persona['telefono'])) {
        throw new Exception("Faltan datos");
    }
} catch (InvalidArgumentException | TypeError $e) {
    echo $e->getMessage();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} finally {
    unset($temporal, $persona['notas']);
}

$mayor = ($suma > 50) ? "grande" : "pequena";
$texto = $persona['apodo'] ?? $persona['nombre'];
$valor = $suma ?: 10;
$orden = $suma <=> 100;
$entero = (int) "42" + (float)$suma;
$bits = 6 & 3 | 8;
$esFigura = $figura instanceof Figura;
$distinto = $suma !== 10 and $suma >= 0 or $suma <= -5;
$archivo = @file_get_contents("datos.txt") or die("No se pudo leer");
$referencia = &$suma;
$nombreVariable = 'suma';
echo $$nombreVariable, ${'nombre' . 'Variable'};
$funcion = 'fibonaci';
echo $funcion(5) . PHP_EOL;
echo Rectangulo::crear($persona)->area(), Base::VERSION;
$figura->imprimir();
$numeros[] = 13;
$figura->etiquetas[0] = "uno";
$suma .= " puntos";
$suma -= -1;
$suma /= 2;
$suma %= 3;
$mensaje = "Texto en
dos lineas";
echo strtoupper(substr("compiladores", 0, 4)), !true, -$suma, +$k;
exit(0);
?>
