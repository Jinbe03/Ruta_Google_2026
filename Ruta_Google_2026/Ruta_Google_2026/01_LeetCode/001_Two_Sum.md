# Problema: Two Sum

Plataforma: LeetCode 1 Dificultad: Easy Categoría: Arrays y HashMaps

### 1. Preparar la memoria

Lógica: Necesito un lugar para anotar los números que voy viendo. Código: `vistos = {}` Por qué: Las llaves indican un Diccionario. Es la mejor herramienta porque buscar en él es instantáneo.

### 2. Empezar a caminar y observar

Lógica: Tengo que revisar cada número de la lista, pero necesito saber tanto el número como su posición. Código: `for i, n in enumerate(nums):` Por qué: El `for` es el bucle. `enumerate` es una función especial que te entrega dos datos a la vez: `i` (la posición) y `n` (el valor del número). Sin `enumerate`, tendrías que crear un contador manual, lo cual es más desordenado.

### 3. Hacer el cálculo matemático

Lógica: Si el objetivo es 10 y tengo un 3, me falta un 7. Código: `necesito = target - n` Por qué: Creamos una variable llamada `necesito` para guardar ese resultado. Es más fácil leer `necesito` que escribir la resta cada vez.

### 4. Consultar la memoria

Lógica: ¿Ya vi ese 7 antes? Código: `if necesito in vistos:` Por qué: Esta es la línea más potente. En Python, el `if algo in diccionario` es extremadamente rápido. No le pedimos al código que busque en toda la lista, le preguntamos directamente a la memoria.

### 5. Entregar el resultado

Lógica: Si el 7 está en la memoria, dame su posición y la posición donde estoy parado ahora. Código: `return [vistos[necesito], i]` Por qué: `vistos[necesito]` te devuelve el valor que guardamos antes (la posición del número que nos faltaba). El `i` es tu posición actual. Los ponemos entre corchetes `[]` para devolver una lista, como pidió el problema.

### 6. Anotar en la memoria

Lógica: Si no encontré lo que buscaba, anoto el número actual en mi libreta para que los que vienen después puedan encontrarme. Código: `vistos[n] = i` Por qué: Aquí guardamos el número como llave y su posición como valor. Es como escribir en una agenda: Nombre (Número) y Teléfono (Posición).