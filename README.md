# 🧠 Lenguaje Personal con ANTLR4 - `gramatica.g4`

¡Bienvenido a este proyecto de lenguaje personalizado creado con [ANTLR4](https://www.antlr.org/)!  
Aquí encontrarás una gramática diseñada para definir un lenguaje estructurado con un sabor único en su sintaxis y palabras clave.

---

## 📜 Descripción

Este lenguaje fue diseñado con el objetivo de explorar conceptos fundamentales de análisis léxico y sintáctico.  
Incluye estructuras comunes como declaraciones, condiciones, ciclos, funciones y llamadas, con una estética particular usando palabras clave personalizadas como `traigase`, `mueche`, `chi`, `mandele`, y más.

---

## 🧩 Características de la Gramática

- ✅ Importaciones (`traigase`)
- ✅ Función principal (`inicio`)
- ✅ Declaraciones de variables (`var`)
- ✅ Impresiones (`mueche`)
- ✅ Condicionales (`chi`, `sino`)
- ✅ Ciclos (`para`, `mientras`)
- ✅ Funciones (`funca`, `mandele`)
- ✅ Llamadas a funciones y métodos
- ✅ Expresiones aritméticas y lógicas

---

## 🧾 Ejemplos rápidos de uso

| 🧱 Instrucción                  | 💡 Ejemplo                                          | 🗣️ Descripción                               |
|----------------------------------|-----------------------------------------------------|-----------------------------------------------|
| **Importación**                  | `traigase matematicas;`                             | Importa una librería externa.                 |
| **Declaración de variable**      | `var edad = 25;`                                    | Declara una variable con valor inicial.       |
| **Impresión**                    | `mueche(<hola mundo>);`                             | Imprime un mensaje al usuario.                |
| **Asignación**                   | `edad = 30;`                                        | Reasigna el valor de una variable.            |
| **Condicional `if`**             | `chi (edad > 18) { mueche(<mayor de edad>); }`      | Ejecuta si la condición es verdadera.         |
| **Condicional `else`**           | `sino { mueche(<menor de edad>); }`                 | Ejecuta si la condición anterior fue falsa.   |
| **Ciclo `while`**                | `mientras (edad < 30) { edad = edad + 1; }`         | Repite mientras se cumpla la condición.       |
| **Ciclo `for`**                  | `para (var i = 0; i < 5; i = i + 1) { mueche(i); }` | Bucle con inicialización, condición y paso.   |
| **Definición de función**        | `funca saludar¿nombre? "{ mueche(nombre); }"`       | Crea una función con argumento(s).            |
| **Llamada a función**            | `..saludar(<deyvy>);`                               | Ejecuta una función definida anteriormente.   |
| **Llamada a método de librería** | `..matematicas.redondear(3.7);`                     | Llama a un método dentro de una librería.     |
| **Retorno (`return`)**           | `mandele resultado;`                                | Devuelve un valor desde una función.          |

---

## 🧠 Estructura Principal


