## O(1) - Tiempo Constante

Es la eficiencia máxima. Significa que la operación tarda lo mismo sin importar si tienes 10 datos o 10 billones.

Ejemplo: Buscar una llave en un diccionario de Python. Es un acceso directo, no hay que recorrer nada.

## O(n) - Tiempo Lineal

El tiempo de ejecución crece en la misma medida que los datos. Ejemplo: Un bucle for que recorre una lista completa.

## Como crear una memoria (Diccionario)

Usa llaves: nombre_diccionario = {} Para guardar: diccionario[llave] = valor Para buscar: if llave in diccionario

## Como recorrer una lista con posicion (Enumerate)

Sintaxis: for posicion, valor in enumerate(lista): Esto evita tener que usar contadores manuales.

## Como devolver resultados

Usa corchetes para listas: return [dato1, dato2]

## El concepto del Complemento

En lugar de buscar una pareja hacia adelante, calculamos que nos falta (Target - Actual) y lo buscamos en el pasado (la memoria del Diccionario).

**Complejidad Táctica (Big O):** Este método es **lento** ($O(n^2)$) porque por cada elemento de la lista
($n$), tenemos que recorrer la lista entera otra vez ($n$). Si la lista crece, el trabajo de Zik aumenta al cuadrado.