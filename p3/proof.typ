= Problema 3

== Orden

=== Definicion

Dado un grafo `G=(V,E)` y un entero `K` determine si existe un cometa de tamano `2K` en el grafo.
- Un cometa consiste de un clique de tamano `K` y `K` nodos adicionales en una cola
- La cola es un camino de nodos conectado a 1 nodo del clique
- El clique y la cola no comparten nodos

Formalmente la entrada del problema consiste en el grafo G y un entero K y la salida son 2 conjuntos de tamano K, C y T, tal que C es un clique de tamano K, T es una cola de tamano K y el grafo inducido por C y T es un cometa de tamano 2K en G.

El objetivo es demostrar que este problema es NP-Completo.

== Demostracion

Para demostrar que este problema es NP-Completo necesitamos demostrar 2 cosas: que el problema es NP y que es reducible a algun problema NP-Hard.

=== NP

Para demostrar que el problema es NP, necesitamos demostrar que dada una solucion, podemos verificar en tiempo polinomial si es correcta.

Dada una solucion consistiendo en un grafo G y un subgrafo solucion G' de tamaño 2K, dividido en su supuesto clique C y cola T, podemos verificar en tiempo polinomial si G' es un cometa de tamaño 2K en G. Para esto, necesitamos verificar que G' consiste de un clique de tamaño K y una cola de tamaño K, que la cola esta conectada a exactamente 1 nodo del clique y que el clique y la cola no comparten nodos.

1. Comprobar que C es un clique de tamaño K. Esto se puede hacer en tiempo O(K^2) verificando que cada par de nodos en C esta conectado en el grafo original.
2. Verificar que todos los vertices en T estan conectados entre si y existe uno de ellos conectado a un nodo en C. Esto se puede hacer en tiempo O(K^2)
3. Comprobar que la interseccion de C y T es vacia. Esto se puede hacer en tiempo O(Klog(k)), usando un set para almacenar los nodos de C y verificando si algun nodo de T esta en el set.

> En total, la verificacion de una solucion toma tiempo O(K^2) + O(K^2) + O(Klog(K)) = O(K^2) = O(n^2) donde n es el tamaño del grafo G.

Por tanto, podemos verificar en tiempo polinomial si una solucion es correcta, por lo que el problema es NP.

=== Reduccion a NP-Hard

Usemos el problema de Clique para demostrar que el problema es NP-Hard. El problema de Clique consiste en determinar si un grafo G tiene un clique de tamaño K.

Empecemos con una instancia del problema de Clique, un grafo G y un entero K, luego vamos a transformarlo en una instancia de nuestro problema.

Vamos a copiar el grafo G exactamente como esta.

#figure(
  image("1.png", width: 30%),
  caption: [
    Un grafo inicial con 3 vertices
  ],
)

Luego por cada nodo de G vamos a agregar un nodo adicional, o sea vamos a copiar los nodos pero no las aristas. Resultando en un nuevo grafo G' con 2V vertices.

#figure(
  image("2.png", width: 30%),
  caption: [
    Añadiendo nodos adicionales
  ],
)

Luego vamos a agregar aristas entre cada uno de los nodos originales y sus respectivas copias. Y ademas vamos a conectar cada uno de los nodos copias con su "siguiente" (las comillas es pq si el nodo es el ultimo se conecta con el primero, como en este ejemplo el 3' se conecta con el 1'). Resultando en camino que une a todos los nodos copias (o una cola) y cada uno tiene una conexion con cualquier nodo del posible clique en el grafo original.

#figure(
  image("3.png", width: 30%),
  caption: [
    Añadiendo aristas
  ],
)

La creacion de este grafo G' se puede hacer en O(|V|), o sea polinomial, lo cual es indispensable para poder hacer la reduccion.

Ahora vamos a ver como se desempeña la conversion de solucion de esta nueva instancia del problema del cometa con la del clique.

La solucion del problema del cometa resuelve 2 conjuntos de nodos disjuntos: el clique C y la cola T. Los nuevos nodos que yo añadi no forman parte de un clique, de eso podemos estar seguros, ya que cada uno de esos nodos esta conectado con solo 1 nodo del grafo original, y con a lo sumo 2 de los nuevos. El unico caso donde puedan formar un clique es si K es 2 pero ese caso es trivial.

Por tanto, en la posible solucion del cometa, todos los nodos de C estan en G, el grafo original del problema del clique, y todos los nodos de T estan en G'. Luego para convertir de nuevo el problema a clique basta con quitar todas las aristas q creamos y quedarnos con el grafo original.

Que sucede si no hubo solucion en el problema del cometa? Por construccion siempre va a existir una cola T de cualquier tamano <= |V| conectada a cada uno de los nodos de G, por lo que el problema no es que no exista un cometa, es que en G no exista un clique de tamaño K. Por tanto si el cometa no tiene solucion, entonces el clique tampoco tiene la tiene.

Por tanto vamos a dejar claro la correctitud de la reduccion demostrando que Solucion de Cometa <--> Solucion de Clique:

1. Si existe un cometa de tamaño 2K en G', consistiendo en un clique de tamaño K y una cola de tamaño K, simplemente dejamos ir a los nodos de la cola y los nodos q resultan son un clique de tamano K.
2. Si tenemos una solucion de clique, creamos un grafo G' con la construccion anterior y la solucion de clique es la solucion de cometa.

Por tanto, el problema del cometa es NP-Hard, ya que se puede reducir en tiempo polinomial al problema de Clique, que es NP-Hard.

Por tanto, como el problema es NP y es NP-Hard, el problema del cometa es NP-Completo.

== Solucion Fuerza Bruta

Como el problema es NP-Completo el unico camino posible de resolverlo sin aproximaciones es con fuerta brutar. La solucion consiste en generar todas las combinaciones posibles de K nodos y verificar si forman un clique. Luego por cada combinacion de K nodos, se verifica si se puede formar un cometa con esos nodos.