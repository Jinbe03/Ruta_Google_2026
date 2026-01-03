## 🎯 Objetivo de la Misión

Reforzar el uso de **Diccionarios** para frecuencia y dominar el **Patrón de Dos Punteros** en sus tres variantes (Pinza, Persecución y Balanza) para optimizar la memoria táctica.

## 🛡️ Fase 1: Calentamiento de Campo

- **Búsqueda Instantánea:** Confirmamos que para verificar existencia en bases de datos masivas (1M+), el operador `in` sobre un diccionario es la ruta más rápida.
    
- **Radar de Posición:** Reafirmamos que `enumerate()` es la herramienta de élite cuando necesitamos el valor y su ubicación (índice) al mismo tiempo.
    
- **Secuencias Exactas:** Ajustamos el uso de `range(n)` para ejecutar protocolos con un número de intentos definido.
    

## 📊 Fase 2: Análisis de Frecuencias (Ejercicio 005)

- **Problema:** Word Counter.
    
- **Herramienta Clave:** `.get(llave, 0)`.
    
- **Lección Táctica:** Aprendimos a agrupar datos repetidos en una "memoria inteligente" (Diccionario) para mapear eventos.
    

## ⚔️ Fase 3: Patrón de Dos Punteros (La Pinza)

Cambiamos de sensor: dejamos de "contar" para empezar a **"comparar y mover"**.

- **Ejercicio 006 (Palindrome Check):** Dos exploradores caminando desde los extremos hacia el centro. `while L < R`.
    
- **Ejercicio 007 (Reverse Weights):** Inversión de listas mediante **In-place Swap** (`lista[L], lista[R] = lista[R], lista[L]`).
    

## 🏃 Fase 4: Punteros de Persecución (Limpieza y Filtro)

Evolucionamos la técnica: los punteros ya no se enfrentan, ahora uno "persigue" al otro en la misma dirección.

- **Ejercicio 008 (Move Zeroes):** Un puntero lento (`L`) marca la posición de guardado mientras el rápido (`R`) escanea unidades operativas (no ceros).
    
- **Ejercicio 009 (Unique Droid IDs):** Eliminación de duplicados en listas ordenadas mediante sobrescritura. Si `nums[R] != nums[L]`, el dato es nuevo.
    

## ⚖️ Fase 5: Construcción y Balanza (Nivel Senior)

- **Ejercicio 010 (Squares of a Sorted Array):** Combinamos la pinza con la **construcción inversa**. Llenamos una lista nueva desde el final (`pos = n-1`) comparando los cuadrados más grandes en los extremos.
    
- **Ejercicio 011 (Two Sum II - Sorted):** La técnica de la **Balanza**. Si la suma es alta, movemos `R`; si es baja, movemos `L`. Solo funciona en listas ordenadas.
    

## 🔄 Fase 6: Patrullaje Repetitivo (Burbuja)

- **Ejercicio 012 (Bubble Sort):** Introducción a los **bucles anidados**. Zik compara vecinos (`i` e `i+1`) e intercambia si están desordenados.
    
- **Advertencia Táctica:** Es un método lento con una complejidad de $O(n^2)$. Requiere múltiples pasadas para asegurar el perímetro.
    

## 📓 Comandos y Atajos del Manual (Carpeta 05)

1. **while:** Bucle de condición activa.
    
2. **Slicing [::-1]:** Inversión rápida en una línea.
    
3. **Swap:** Intercambio simultáneo de valores.   

## 🧠 Introspección y Notas Finales

La jornada de hoy marcó la transición de "escribir código" a "diseñar eficiencia". El paso de los diccionarios a los punteros redujo la carga de memoria del sistema de Zik. La mayor revelación fue la **versatilidad de los punteros**: no son solo flechas, son herramientas de decisión aritmética y espacial.

**Estado del Sistema:** Óxido eliminado. Arsenal de 12 protocolos verificado y funcional.