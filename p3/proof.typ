= Problema 3

== Orden

=== Definición

Dado un grafo `G=(V,E)` y un entero `K`, determine si existe un cometa de tamaño `2K` en el grafo.
- Un cometa consiste en un *clique* de tamaño `K` y `K` nodos adicionales en una *cola*.
- La cola es un camino de nodos conectado a 1 nodo del *clique*.
- El *clique* y la *cola* no comparten nodos.

Formalmente, la entrada del problema consiste en el grafo `G` y un entero `K`. La salida son 2 conjuntos de tamaño `K`, `C` y `T`, tales que `C` es un *clique* de tamaño `K`, `T` es una *cola* de tamaño `K`, y el grafo inducido por `C` y `T` es un cometa de tamaño `2K` en `G`.

El objetivo es demostrar que este problema es *NP-Completo*.

== Demostración

Para demostrar que este problema es *NP-Completo*, necesitamos demostrar dos cosas: que el problema pertenece a *NP* y que es reducible a algún problema *NP-Hard*.

=== NP

Para demostrar que el problema pertenece a *NP*, necesitamos demostrar que, dada una solución, podemos verificar en tiempo polinomial si es correcta.

Dada una solución que consiste en un grafo `G` y un subgrafo solución `G'` de tamaño `2K`, dividido en su supuesto *clique* `C` y *cola* `T`, podemos verificar en tiempo polinomial si `G'` es un cometa de tamaño `2K` en `G`. Para ello, necesitamos verificar que:
- `G'` consiste en un *clique* de tamaño `K` y una *cola* de tamaño `K`,
- La *cola* está conectada a exactamente un nodo del *clique*, y
- El *clique* y la *cola* no comparten nodos.

1. Comprobar que `C` es un *clique* de tamaño `K`. Esto se puede hacer en tiempo `O(K^2)` verificando que cada par de nodos en `C` está conectado en el grafo original.
2. Verificar que todos los vértices en `T` están conectados entre sí y que existe uno de ellos conectado a un nodo en `C`. Esto se puede hacer en tiempo `O(K^2)`.
3. Comprobar que la intersección de `C` y `T` es vacía. Esto se puede hacer en tiempo `O(K log K)`, usando un conjunto para almacenar los nodos de `C` y verificando si algún nodo de `T` está en el conjunto.

En total, la verificación de una solución toma tiempo `O(K^2) + O(K^2) + O(K log K) = O(K^2) = O(n^2)`, donde `n` es el tamaño del grafo `G`.

Por tanto, podemos verificar en tiempo polinomial si una solución es correcta, lo que demuestra que el problema pertenece a *NP*.

=== Reducción a NP-Hard

Usemos el problema de *Clique* para demostrar que este problema es *NP-Hard*. El problema de *Clique* consiste en determinar si un grafo `G` tiene un *clique* de tamaño `K`.

Empecemos con una instancia del problema de *Clique*, un grafo `G` y un entero `K`, y luego vamos a transformarlo en una instancia de nuestro problema.

Vamos a copiar el grafo `G` exactamente como está.

#figure(
  image("1.png", width: 30%),
  caption: [
    Un grafo inicial con 3 vértices
  ],
)

Luego, por cada nodo de `G`, vamos a agregar un nodo adicional, es decir, vamos a copiar los nodos pero no las aristas. Esto resultará en un nuevo grafo `G'` con `2V` vértices.

#figure(
  image("2.png", width: 30%),
  caption: [
    Añadiendo nodos adicionales
  ],
)

Luego, vamos a agregar aristas entre cada uno de los nodos originales y sus respectivas copias. Además, conectaremos cada uno de los nodos copias con su "siguiente" (las comillas son porque si el nodo es el último, se conecta con el primero, como en este ejemplo donde el nodo `3'` se conecta con el `1'`). El resultado será un camino que une a todos los nodos copias (una cola), y cada uno tendrá una conexión con algún nodo del posible *clique* en el grafo original.

#figure(
  image("3.png", width: 30%),
  caption: [
    Añadiendo aristas
  ],
)

La creación de este grafo `G'` se puede hacer en `O(|V|)`, es decir, en tiempo polinomial, lo cual es indispensable para poder hacer la reducción.

Ahora veamos cómo se desempeña la conversión de solución de esta nueva instancia del problema del cometa con la del *clique*.

La solución del problema del cometa resuelve dos conjuntos de nodos disjuntos: el *clique* `C` y la *cola* `T`. Los nuevos nodos que añadimos no forman parte de un *clique*, ya que cada uno de esos nodos está conectado solo a un nodo del grafo original y, como mucho, a dos de los nuevos nodos. El único caso donde podrían formar un *clique* es si $K #sym.lt.eq 3$ , pero ese caso es trivial.

Por tanto, en la posible solución del cometa, todos los nodos de `C` están en `G`, el grafo original del problema de *Clique*, y todos los nodos de `T` están en `G'`. Para convertir de nuevo el problema al de *Clique*, basta con quitar todas las aristas que creamos y quedarnos con el grafo original.

¿Qué sucede si no hubo solución en el problema del cometa? Por construcción, siempre va a existir una cola `T` de cualquier tamaño ≤ `|V|` conectada a cada uno de los nodos de `G`. Por lo tanto, el problema no es que no exista un cometa, sino que en `G` no exista un *clique* de tamaño `K`. Por tanto, si el cometa no tiene solución, entonces el *clique* tampoco la tiene.

Por tanto, vamos a dejar clara la correctitud de la reducción demostrando que:

*Solución de Cometa #sym.arrow.l.r.double Solución de Clique*:

1. Si existe un cometa de tamaño `2K` en `G'`, consistente en un *clique* de tamaño `K` y una *cola* de tamaño `K`, simplemente eliminamos los nodos de la cola y los nodos que resultan forman un *clique* de tamaño `K`.
2. Si tenemos una solución de *clique*, creamos un grafo `G'` con la construcción anterior y la solución de *clique* es la solución de cometa.

Por tanto, el problema del cometa es *NP-Hard*, ya que se puede reducir en tiempo polinomial al problema de *Clique*, que es *NP-Hard*.

== Solución Fuerza Bruta

Como el problema es *NP-Completo*, el único camino posible para resolverlo sin aproximaciones es con *fuerza bruta*. La solución consiste en generar todas las combinaciones posibles de `K` nodos y verificar si forman un *clique*. Luego, por cada combinación de `K` nodos, se verifica si se puede formar un cometa con esos nodos.
