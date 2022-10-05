# 3.Adivina_un_numero_valentina_villalobos

https://github.com/valuvilla/3.Adivina_un_numero_valentina_villalobos.git

1. Descripción del juego

Va a crear un programa para terminal que va a escoger un número aleatoriamente, entre 0 y 99, y a continuación, le va a pedir al usuario que adivine este número.
Tras cada intento, le responderá indicándole si se ha quedado corto o se ha pasado, hasta que encuentre el número. Entonces, mostrará el número de intentos que han hecho falta para encontrar este número y el programa se terminará.
2. Pistas
A continuación te detallo unas cuantas pistas para avanzar en el juego
a. Gestión del azar

Va a pedirle al ordenador que escoja un número aleatoriamente, entre 0 y 99. Esto se hace así:
import random 
numero = random.randint(0, 100) 
La primera línea permite importar el módulo que contiene todas las funciones que permiten gestionar el azar (las principales se presentarán con detalle en este libro). La segunda línea permite generar un número y asignarlo a la variable llamada numero.
b. Etapas del desarrollo

No intente desarrollar el programa entero de golpe. Empiece generando el número aleatorio (en una variable que llamaremos numero), y luego pida al usuario que introduzca un número (en una variable llamada intento). Convierta esta variable en un valor entero, y compruebe que esté comprendido entre 0 y 99. En caso contrario, consideraremos que se trata de un error de escritura y no que se trata de una jugada (de modo que no la descontaremos).
Para hacer todo esto, tendrá que utilizar lo que hemos visto hasta el momento y tendrá que probar su programa con regularidad, aunque solo sea para asegurarse de que se comporta como se ha previsto y que no se ha olvidado de ningún caso de uso.
A continuación, comparará el número aleatorio con el número introducido por el usuario y mostrará «Demasiado pequeño», «Demasiado grande» o incluso «¡Ha ganado!». Podrá mostrar, también, de manera provisional, el número generado aleatoriamente para poder comprobar el programa que está escribiendo.
En una segunda etapa, escribirá el código que le permita pedir la información al usuario y responderle dentro de un nuevo bucle, que se repetirá hasta que el jugador haya acertado.
Sepa que hay varias soluciones posibles y que la propuesta aquí no es necesariamente la más conveniente, aunque es la mejor adaptada a la progresión pedagógica que hemos querido desarrollar aquí.
Existe una propuesta de solución en el archivo 11_JUEGO_guess_the_number.py.
3. Para ir más allá

Para ir más allá, puede plantearse nuevos objetivos.
He aquí un ejemplo de partida, con una ayuda para el usuario:
$ python3 ejemplo.py 
Adivine el número entre 0 y 99 incluidos: 50 
Demasiado grande 
Adivine el número entre 0 y 49 incluidos: 25 
Demasiado pequeño 
Adivine el número entre 26 y 49 incluidos: 42 
¡Ha ganado! 
También puede pedirle al usuario que escoja los límites mínimo y máximo antes de jugar. De este modo, podrá adivinar un número entre 1 y diez millones, si es amante de los desafíos.

