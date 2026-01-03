**Concepto:** Usar dos índices (punteros) para recorrer una estructura de datos desde distintas direcciones o a distintas velocidades.

## ¿Cuándo se usa?

- Para procesar listas ordenadas.
    
- Para comparar elementos en los extremos (como en los palíndromos).
    
- Para buscar pares de números que cumplan una condición.
    

> ### Lógica de Operación: Dos Punteros
> 
> 1. **Puntero Izquierdo (L):** Empieza en el índice `0`.
>     
> 2. **Puntero Derecho (R):** Empieza en el índice `len(lista) - 1`.
>     
> 3. **Bucle while:** Mientras `L < R`, los personajes se mueven.
>     
> 4. **Acción:** Comparamos lo que ve `L` con lo que ve `R`.
>     
>     - Si queremos acercarnos: `L += 1` y `R -= 1`.

**Nota Mental:** En el patrón de Dos Punteros, el `return False` dentro del bucle funciona como un "botón de pánico". Apenas los punteros ven algo distinto, se acaba la ejecución. El `return True` final solo se alcanza si los punteros sobrevivieron a todo el camino sin encontrar errores.

No solo sirve para comparar (palíndromos), sino también para modificar listas. Al usar `L` y `R` para intercambiar valores y moverse al centro, podemos invertir cualquier lista sin gastar memoria extra (sin crear una lista nueva).

**Variación: Movimiento Condicional por Suma**

- No siempre movemos ambos punteros a la vez.
    
- En problemas de búsqueda de objetivos, movemos solo **uno a la vez** dependiendo de si nos pasamos o nos falta para llegar al resultado.
    
- Esta lógica solo funciona si la lista está **ordenada**.