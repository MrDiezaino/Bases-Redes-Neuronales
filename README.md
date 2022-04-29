# Red Neuronal

### ¿Que és?

Es una red de neuronas conectadas entre si, que están constantemente enviando información entre si.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

1. Dendrita: Recibe la información.
2. Soma: Procesa la información.
3. Axon: Devuelve la información.

El modelo que pasaremos al PC se llamará neurona artificial, o **perceptrón**.

### Aprendizaje Supervisado

Vamos a darle una serie de ejemplos/guías a la neurona para que aprenda.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

# Neurona Artificial

### Basándonos en una neurona convencional

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

La neurona artificial va a tener algo conocido como "pesos"**(w)**.
- Los pesos de encargarán de multiplicar a las entradas.

La entrada **(x)**,va a multiplicar al peso **(w)** y entrará al núcleo, donde se sumarán todos.

 **Σ(x1·w1+x2·w2+x3·w3)**

# Neurona Completa

### Función Activación

Usamos el "Sigmoide" para ver la probabilidad de algo.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

A partir del sigmoide/FA hemos obtenido __la respuesta__

### ¿Que tan buena es la __respuesta__?

Digamos que obtenemos de salida un "1", osea, que queremos como resultado un "1".
Sin embargo la neurona nos devuelve "0.9", básicamente, se equivocó, o **no está tan bien como queremos**.

### ¿Como sabemos que tan mal está?

Usando el **Gradiente descendente**

Esto lo que nos dice es que tan alejados estamos del "objetivo". Por lo que iría entrenando poco a poco reduciendo el error y acercándose a la meta.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

Con la fórmula del error cuadrático.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

La sumatoria de un medio de la salida (el valor deseado / meta) menos el valor de la función de activación al cuadrado.
Cuanto menor sea el resultado, mejor.

### Gradiente

Gradiente = y * (1 - y)

Se basa en encontrar el mínimo de una función.

### Ajuste de pesos

AJ = Entrada * Error * Gradiente

### Épocas

La cantidad de eṕocas serán las veces que se llevará a cabo el "estudio" por parte de nuestra red.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)
