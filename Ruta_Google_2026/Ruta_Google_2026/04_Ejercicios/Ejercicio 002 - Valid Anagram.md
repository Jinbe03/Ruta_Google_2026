## Sintaxis Clave

- if len(s) != len(t): El uso de len para comparar tamaños y salir rapido con return False.
    
- .get(letra, 0): Para buscar en el diccionario sin que el programa de error si la letra es nueva.
    
- return dic1 == dic2: Comparacion directa de dos estructuras completas.
    

## Flujo del Codigo

Primero usamos un if para descartar palabras de distinto largo. Luego, usamos dos bucles for independientes para llenar dos diccionarios. Dentro de cada bucle, usamos la formula de conteo: diccionario[letra] = diccionario.get(letra, 0) + 1. Finalmente, comparamos ambos resultados con un solo return.