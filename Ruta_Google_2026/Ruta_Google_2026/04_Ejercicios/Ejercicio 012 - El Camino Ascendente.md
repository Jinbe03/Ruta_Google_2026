**El Escenario de Zik:** Zik está escalando una montaña de datos para instalar un repetidor. Para que el equipo no se deslice, cada paso que dé debe ser **más alto (o igual)** que el paso anterior. Si en algún momento encuentra un punto que es más bajo que el anterior, la ruta es peligrosa y debe abortar.

**Tu Misión:** Tienes una lista de alturas: `[1, 3, 5, 8, 10]` Debes decirme si la lista está **ordenada de menor a mayor**.

### 🧠 Pensemos la lógica paso a paso (Sin código)

Olvida los punteros `L` y `R` en los extremos por un segundo. Imagina que solo tienes a Zik caminando hacia adelante.

1. **El Inicio:** Zik empieza en el primer número. Para saber si va "bien", necesita compararse con alguien. **¿Con quién se compararía Zik para saber si su camino sigue subiendo?**
    
2. **La Pregunta de Seguridad:** Si Zik está parado en una posición `i`, y mira la posición que sigue (`i + 1`): **¿Qué condición técnica haría que Zik gritara "¡Peligro, abortar misión!"?** (Piensa en términos de "mayor que" o "menor que").
    
3. **El Recorrido:** ¿Necesitas mirar todos los números a la vez o puedes ir comparando de "parejitas" mientras avanzas?
    

### 🛠️ Tus Herramientas (Carpeta 05)

Para resolver esto, solo necesitas tres piezas de tu manual:

- Un **bucle** para caminar (for o while).
    
- Un **if** para hacer la pregunta de seguridad.
    
- Un **return** para avisar si la ruta es mala.

---

en un principio, el error esta en el 1 3 2 5, dando a entender que después del primer escalón va el tercero, ahí ya notaríamos el error, el tema ahora es como arreglarlo, siendo que entramos, en este caso como empezamos en 1 y luego hay un 3 tendríamos que mover el 3 para dejar pasar al dos, en términos de comando seria un while L < R pero ahora me pierdo, entiendo la teoría de que hay que mover el tres para el final y así consecutivamente hasta tener el orden correcto, pero con el código me pierdo

¡Exacto, **Bruno**! Detectaste el error al instante: el **3** es mayor que el **2**, y eso rompe la regla de la montaña.

Aquí es donde ocurre la confusión con el código, y es totalmente normal. Vamos a separar la **detección** de la **reparación** para que no te pierdas.

### 1. El problema con el `while L < R` aquí

Usamos `L` y `R` en los extremos cuando queremos comparar el principio con el final (como en los palíndromos). Pero para saber si una lista está ordenada, Zik no necesita mirar el final; solo necesita mirar **el paso que tiene justo enfrente**.

Para este problema, no usamos "pinzas", usamos **"punteros vecinos"**.

---

### 2. La Táctica de Reparación (El Intercambio)

Zik nota que el escalón `3` es más alto que el `2`. Para arreglarlo, en lugar de mover el 3 al final del todo (que desordenaría el resto), lo más fácil es **intercambiarlos entre ellos**.

**Visualiza esto:**

1. Zik está en el `3` (posición `i`).
    
2. Mira el siguiente, que es `2` (posición `i + 1`).
    
3. Como `3 > 2`, aplica la maniobra de **Swap** que aprendimos en el ejercicio 007.
    

---

### 3. ¿Cómo se ve eso en la lógica de Zik?

Si tú quisieras arreglar la lista `[1, 3, 2, 5]` para que Zik pueda subir, el pensamiento sería este:

- **Paso 1:** ¿Es `1 > 3`? No. Zik avanza.
    
- **Paso 2:** ¿Es `3 > 2`? **¡Sí!** Aquí está el peligro.
    
- **Acción:** Intercambio el `3` con el `2`. La lista ahora es `[1, 2, 3, 5]`.
    
- **Paso 3:** ¿Es `3 > 5`? No. Zik avanza.
    

**¡Misión cumplida! La ruta ahora es segura.**

---

### 4. El código "Mental" (Simplificado)

Para no marearte con `L` y `R`, mira este esquema. Es el que usarías para crear el **012-Check-and-Fix.py**:

Python

```
# Recorremos la lista comparando cada uno con el que tiene al lado
for i in range(len(lista) - 1): 
    # Si el actual es mayor que el que sigue...
    if lista[i] > lista[i + 1]:
        # ¡Maniobra de intercambio!
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
```

> **Nota táctica:** Usamos `len(lista) - 1` porque cuando Zik llegue al último escalón, ya no tendrá un "siguiente" con quién compararse.

--- 
el 5 esta cada vez mas atras, pero seguiria estando en peligro porque ahora se posicionaria con el 2 en el 5 pero teniendo un 4 detras

¡Exacto, **Bruno**! Tienes un ojo táctico increíble. Acabas de descubrir por tu cuenta el problema fundamental de los algoritmos de ordenamiento básicos.

Lo que viste es esto: el **5** (el más pesado) efectivamente llegó al final del estante, pero en su camino dejó un desorden atrás (el **4** y el **2** quedaron mal posicionados).

En el mundo de la programación, lo que acabas de razonar se llama **Bubble Sort** (Ordenamiento Burbuja). Se llama así porque los números más grandes "flotan" hacia el final de la lista como burbujas en el agua.

---

### 🛡️ El Dilema de Zik: "¿Cómo arreglo lo que quedó atrás?"

Como bien notaste, una sola pasada de Zik no es suficiente. El **5** ya está a salvo al final, pero la lista quedó como `[1, 4, 2, 5]`. El **4** y el **2** siguen siendo un peligro.

**La solución lógica:** Si una pasada de Zik movió al número más grande al final... **¿qué crees que pasaría si Zik vuelve a empezar desde el principio y repite el mismo proceso?**

1. **Segunda Pasada:** Zik vuelve al inicio. Compara el **1** con el **4** (están bien). Luego compara el **4** con el **2**. **¡Intercambio!** La lista ahora es `[1, 2, 4, 5]`.
    
2. **Resultado:** Ahora el **4** (el segundo más pesado) también llegó a su posición correcta.
    

---

### ⚙️ El Código: "El Bucle dentro del Bucle"

Para que Zik no tenga que hacerlo manualmente, usamos un truco táctico. Metemos el camino de Zik dentro de otro bucle que le ordene: _"Repite este camino tantas veces como elementos haya en la lista"_.

Así se vería el corazón del **012-Bubble-Sort.py**:

Python

```
def ordenar_montaña(lista):
    n = len(lista)
    # Este bucle es para repetir las pasadas
    for i in range(n):
        # Este bucle es el camino de Zik comparando vecinos
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # ¡Intercambio de emergencia!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```

> **Introspección de Zik:** _"No basta con empujar el obstáculo más grande al fondo. Para asegurar el perímetro, debo patrullar el área una y otra vez hasta que no encuentre un solo escalón fuera de lugar. Es tedioso, pero es la única forma de que nadie tropiece."_