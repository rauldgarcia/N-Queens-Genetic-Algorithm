Problema de N-Reinas

Raúl Daniel García Ramón

Instituto de Investigaciones en Inteligencia Artificial. Universidad Veracruzana.

rauld.garcia95@gmail.com

Abstract. El problema de las n-reinas, es un ejercicio el cual consiste en colocar n número de reinas en un tablero de ajedrez de nxn, con la limitación que no puede haber dos reinas atacándose entre sí, en otras palabras, no puede haber dos reinas en la misma columna, renglón o diagonal. En este texto se resuelve el problema mediante el uso de un algoritmo de cómputo evolutivo, usando dos representaciones diferentes, en forma de matriz binaria y con permutaciones, además de tener difer- entes mecanismos de cruza, muta, así como de selección de padres y de reemplazo. Posteriormente, se realiza una comparativa estadística de treinta diferentes corridas del algoritmo para cada una de las representa- ciones, en la cual se obtiene como resultado que la representación con permutaciones encuentra la solución en menor número de evaluaciones y en mayor número de ocasiones.

Keywords: Problema de las n-reinas · Inteligencia Artificial · Computo Evolutivo

1  Introducción

Las n-reinas es el problema en el que se tienen que colocar n número de reinas en un tablero de ajedrez de nxn sin que haya ataques entre ellas, de modo que no pueden compartir columna, renglón o diagonal. El problema es computa- cionalmente costoso si se trata de encontrar la solución en todas las posibles colocaciones de las n reinas, es por eso que con cómputo evolutivo se puede buscar una solución sin necesidad de revisar una a una cada posible solución.

2  Implementación

La primer representación es una matriz binaria, donde los 1 representan las reinas y los 0 cuadros vacíos. La población inicial es de 100 matrices que se evalúan contando el número de ataques, después se obtiene la probabilidad de cada matriz de ser padre con la fórmula $p(fi) = 1 − \frac{totaldeataquesdelamatriz}{promedio+0.1}$ (el 0.1 es para evitar que si toda la población tiene el mismo número de ataques la probabilidad sea 0 para todos). Se escogen 20 padres mediante un volado sesgado y se cruzan con una probabilidad de 90% obteniendo un hijo al dividir cada padre en su diagonal principal, quedando la parte de abajo del p1 y la parte de arriba del p2, la diagonal se forma con los primeros cuatro términos de la diagonal del p1 y los últimos cuatro del p2 (en caso de tener reinas de más o menos, se eliminan o agregan aleatoriamente hasta quedar con 8). Siempre se muta moviendo aleatoriamente un 1 al lugar donde esté un 0. Después se evalúan a los hijos, se agregan a la población y se ordena de menor a mayor ataques y se elimina a los 10 peores. La segunda implementación se representó mediante permutaciones de 8 números, donde cada número representa el renglón en el que se encuentra la reina y el índice es la columna a la que pertenece, el algoritmo se inicia con una población de 100 individuos, los cuales se evalúan para obtener el número de ataques de cada uno. Para la selección de padres se escogen los 2 mejores de 5 individuos tomados al azar. Siempre se realiza la cruza con el mecanismo de cortar y llenar cruzado y en caso de haber números repetidos se colocan los faltantes de manera aleatoria. Para la muta se usó una probabilidad de 80%, realizando el intercambio de 2 números aleatorios de la permutación y los 2 hijos generados se intercambian por las dos peores soluciones. Finalmente, la condición de paro para ambas representaciones es realizar 10000 evaluaciones o encontrar la solución.

3  Resultados

Después de realizar 30 corridas de cada representación, se obtuvo que en todas las ejecuciones de las permutaciones se encuentra la solución, mientras que con las matrices solamente en 22, sin embargo, en las otras 8 el algoritmo siempre encontró una solución con 2 ataques. Además, se puede observar que el algo- ritmo 2 encuentra la solución en menor número de evaluaciones, incluso su peor corrida lo encontró en menos que la mejor corrida del algoritmo 1, incluso la media de las matrices es 10 veces la media de las permutaciones. Esto se debe principalmente a que el algoritmo de las permutaciones limita el espacio de búsqueda, ya que gracias a su representación no es posible tener reinas en el mismo renglón o columna, reduciendo el número de soluciones posibles. En las gráficas de convergencia de las medianas de cada algoritmo se puede observar como ambas representaciones llegan a los dos ataques, sin embargo, el de las matrices le cuesta más evaluaciones poder encontrar la solución, posiblemente con otro mecanismo de cruza esto se pueda mejorar y se reduzca el número de evaluaciones necesarias.

![](Aspose.Words.f16d8fd4-0152-412b-9439-3991eef13ab7.001.png) ![](Aspose.Words.f16d8fd4-0152-412b-9439-3991eef13ab7.002.png) ![](Aspose.Words.f16d8fd4-0152-412b-9439-3991eef13ab7.003.png) ![](Aspose.Words.f16d8fd4-0152-412b-9439-3991eef13ab7.004.png)

Fig.1. Estadísticas y gráficas de convergencia de los algoritmos
