# Ejercicios con Locks

## Cola FIFO compartida

El siguiente archivo python contiene la definición de la clase _ColaFIFO_ que implementa una cola First In, First Out.

```
colaFIFO.py
```

El contenido de la cola se almacena en una atributo lista llamado “_elementos_”

La clase contiene 7 métodos

**_Constructor_** : inicializa la lista “elementos” para el contenido de la cola

**_insertar(dato)_** : inserta un elemento en la cola

**_extraer(dato)_** extrae un elemento en la cola

**_ultimo()_** : muestra el último elemento de la cola

**_primero()_** : muestra el primer elemento de la cola (próximo a salir)

**_cola_vacia()_** : devuelve Verdadero si la cola está vacia

**_cantidad_elementos()_** : retorna la cantidad de elementos en la cola

El script incluye una función **_main()_** cuyo propósito es probar los métodos.

## Ejercicio

1. Leer y analizar que hace el código de este programa.
   **Analizar hasta comprender todas las líneas del código**
   En la funcion main:

    - linea 29: se crea un objeto ColaFIFO llamado
    - linea 33: se imprime por pantalla si la cola esta vacia(True o False)
    - linea 35/36: Bucle for que inserta en la cola el valor de i en ese momento
    - linea 38: se imprime por pantalla si la cola esta vacia(True o False)
    - linea 39: se imprime por pantalla la cantidad de elementos de la cola
    - linea 41: se imprime por pantala el objeto en la primera posicion de la cola y el objeto en la ultima posicion
    - linea 42: se extrae un objeto de la cola(en que esta en la posicion 0)
    - linea 43: se imprime por pantala el objeto en la primera posicion de la cola y el objeto en la ultima posicion
    - lineas 46 al 49: se extraen 4 veces el objeto que esta en la posicion 0
    - linea 51: se imprime por pantalla si la cola esta vacia(True o False)
    - linea 52: se imprime por pantalla la cantidad de elementos de la cola

2. En un archivo python separado, importar la clase ColaFIFO, instanciar una cola de ésta clase y luego implementar un programa que ejecute las siguientes threads:

   - Una thread (productor) que ejecute un loop infinito que en cada iteración inserte en la cola un valor numérico generado aleatoriamente (con valores entre 0 y 100), imprima un mensaje de logging indicando que se realizó la inserción y espere (sleep) y luego espere 2 segundos.

     **Esta thread debe recibir como argumentos un objeto ColaFIFO y un valor numérico (retardo), inicialmente de 2 segundos.**
     Por ejemplo:

     ```
       # a partir de una clase derivada de Thread
       c1 = Cons(cola, 2)

       # directamente desde el módulo threading
       c1 = threading.Thread(target=cons, args=(cola, 2))
     ```

   - Una thread (consumidor) que ejecute un loop infinito que en cada iteración extraiga un elemento de la cola, genere un mensaje de logging con el valor del elemento extraído y luego espere (sleep) dos segundos.

     **Esta thread debe recibir como argumentos un objeto ColaFIFO y un valor numérico (retardo), inicialmente de 2 segundos.**

   Ejemplos:

   ```
     # a partir de una clase derivada de Thread
     p1 = Prod(cola, 2)

     # directamente desde el módulo threading
     p1 = threading.Thread(target=prod, args=(cola, 2))
   ```

   **Preferentemente, implementar estas threads a partir de clases derivadas de Thread que reciban como argumento el objeto de clase ColaFIFO instanciado y el valor numérico de retardo, en vez de hacerlo directamente del módulo threading.**

   **Las threads deben permanecer ejecutándose indefinidamente, no debe terminar el programa después de lanzarlas. Coloque todo el código que sea necesario para esto.**

3. Ejecute el programa y analice los resultados. Obtiene en alguna de las ejecuciones datos inconsistentes o errores? En caso afirmativo, analice los resultados identificando las causas de las inconsistencias o errores.

Existe una grave inconsistencia en el codigo con respecto a la consumicion, ya que puede existir el caso en donde el consumidor consuma de la cola pero no haya nada para consumir en esta. Es decir si la cola esta vacia y el consumidor intenta consumir el codigo se rompe. 

4. Como modificaría la clase **_ColaFIFO_** de modo que su constructor reciba un argumento “size” que establezca el tamaño máximo (cantidad de elementos) de la cola, y modifique los métodos que sean necesarios para asegurar que la cantidad de elementos en la cola no supere esa cantidad de elementos.

5. Modifique el programa de modo de instanciar una nueva cola de tamaño (size) 10 y modifique los retardos de productor y consumidor de modo que queden los dos iguales (1 segundo).

6. Ejecute el programa y observe los resultados explicando lo que observa.
