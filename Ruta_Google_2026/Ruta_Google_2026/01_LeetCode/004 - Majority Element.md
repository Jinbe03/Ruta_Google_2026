## Estrategia Tecnica

Este problema utiliza el patron de conteo de frecuencias. La diferencia es que añadimos una condicion de salida temprana: apenas un numero supera la mitad del tamaño de la lista (n/2), sabemos que es el ganador.

## Logica del Algoritmo

1. Definir el umbral de victoria como el tamaño de la lista dividido por dos (usando // para entero).
    
2. Crear un diccionario de conteo vacio.
    
3. Recorrer cada numero en la lista.
    
4. Actualizar el contador del numero actual en el diccionario.
    
5. Si el contador del numero actual supera el umbral, retornar el numero inmediatamente.
    

## Codigo en Python

class Solution(object): def majorityElement(self, nums): umbral = len(nums) // 2 conteo = {}

```
    for n in nums:
        conteo[n] = conteo.get(n, 0) + 1
        if conteo[n] > umbral:
            return n
```

## Analisis de Complejidad

Tiempo: O(n). Solo pasamos por la lista una vez. Espacio: O(n). En el peor caso guardamos varios numeros en el diccionario hasta encontrar al ganador.

|**Método**|**Estilo**|**Ventaja**|
|---|---|---|
|**if / else**|Manual / Explícito|Es más visual. Ves claramente cuándo creas la entrada y cuándo la sumas.|
|**.get(n, 0)**|Profesional / Mid|Es más corto. Reduce las líneas de código y el riesgo de errores de espacios (indentación).|