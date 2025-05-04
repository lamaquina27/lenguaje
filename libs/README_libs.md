
# Convención Oficial de Librerías para el Lenguaje

Moachos, leanse esto pa que se guien del las libs o la cagamos.


## Ubicación 

Todas las librerías deben estar ubicadas dentro de la carpeta:

```

/libs/

```
Por ende tienen que meter las que creen ahí mismito como un aarchivo new.

Cada librería debe tener su propio archivo, unico con el nombre en minúsculas que representa la librería (conn ese se importa y se accede, tienen que ponerlos faciles, nada de: lib_joa_12es_do_intento1. coman mierda, cosas sencillas... Les propongo nombres de los profes pa que quede standard):

```

libs/darwin.py
libs/robayito.py
libs/camilo.py

````



## Estructura de la Librería

Por dentro todos los archivos deben tener al menos una clase (la principal y prefiero que la unica) con el **mismo nombre que el archivo, pero en PascalCase** (Por si no se acuerdan PascalCase es la del camello pero empezando en mayus, es decir DarwinMartinez pero prefiero que sea solo un nombre o apellido y mas brevas: Darwin) (O sea definan por ejemplo Class Darwin, aunque el archivo se llame darwin.py siempre uno en minus y el otro con Pascal).

Ejemplos:

| Archivo | Clase |
|---------|-------|
| darwin.py | Darwin |
| robayito.py | Robayito |
| Camilo.py | camilo |

La clase es la que será instanciada automáticamente por el lenguaje al hacer `traigase` (el import nuestro es traigase).


## Tipos de Métodos Permitidos

Se permiten los siguientes tipos de métodos (No creo ni que se acuerden pero toca pensar en ir documentando, por si se van a poner a que chat les haga todo, si meten otro metodo se rompe el lenguaje):

### Métodos Estáticos (`@staticmethod`)
- Se utilizan para operaciones simples que no dependen de la instancia o clase.
- Ejemplos: suma, resta, multiplicar, dividir, módulo.

### Métodos de Clase (`@classmethod`)
- Se utilizan para operaciones que requieren acceso a la clase o cálculos internos comunes.
- Ejemplos: factorial, sin, cos, tan (usando series de Taylor).

> **NO se permite el uso de `@property` ni de instancias externas a menos que se especifique lo contrario. (Y como leen, aún no especifico lo contrario, solo puse eso porque puede ser que en la de perceptron se necesite y tenga que hacerlo compatible... por ahora NO)**

---

## Restricciones (Pedidas por Joaquin, no la vayan a cagar)

- **NO se permite usar librerías de Python como `math` o `random`**.
- Todas las operaciones deben ser implementadas desde cero usando:
  - Operadores básicos (`+`, `-`, `*`, `/`, `**`, `%`)
  - Bucles (`for`, `while`)
  - Condicionales (`if`, `else`)
  - Algoritmos propios (ejemplo: series de Taylor, aproximaciones, algoritmos de raíz).




## Manejo de errores

Los métodos que puedan causar errores **deben lanzar `Exception` con un mensaje claro** (O se nos rompe esta vuelta).

Ejemplos:

```python
if b == 0:
    raise Exception("No se puede dividir entre 0")

if x < 0 and n % 2 == 0:
    raise Exception("No se puede calcular raíz par de un número negativo")
````


## 📚 Ejemplo de implementación (La primera versión del que hice, ya la compliqué un tole más así que wachense esta por facilidad)

```python
class Darwin:

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def raiz(a, n=2):
        if a < 0 and n % 2 == 0:
            raise Exception("No se puede calcular raíz par de un número negativo")
        return a ** (1 / n)

    @classmethod
    def factorial(cls, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @classmethod
    def sin(cls, x):
        result = 0
        for i in range(10):
            sign = (-1) ** i
            result += sign * (x ** (2 * i + 1)) / cls.factorial(2 * i + 1)
        return result
```


## Ejemplo de uso desde el lenguaje (Como se va usar para que hagan pruebas en ejemplo.txt)

```plaintext
traigase darwin;

principal {

    var raiz = ..darwin.raiz(25);
    mueche(raiz);

    var seno = ..darwin.sin(1);
    mueche(seno);
}
```


## Notas impotantosas

* Me vale chimba cuanto se compliquen la vida o que tanto metan en las libs mientras que respeten estas reglas, si no, se rompe y en serio estuvo una verga lograrlo así de chimbita.
* Si ven que la librería debe almacenar valores o estados internos (Que no creo que lo necesitemos), me avisan pa meterle porque tengo en pausa la convención para **Librerías con Estado** (Me ha costado, sorry la demora).
* Pongan las funciones de manera que se entienda, estamos manejando casi todo en español así que no van a empezar con mierdas en inglés ni en Alemán, cosas claras y bien descritas que el lenguaje está lindo pero ya está un verguero.

