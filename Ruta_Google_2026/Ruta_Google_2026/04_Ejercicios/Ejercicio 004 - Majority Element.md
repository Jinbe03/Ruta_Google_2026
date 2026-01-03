## Sintaxis Clave

- // 2: Division entera para calcular el umbral (la mitad de la lista).
    
- if/else manual: Para decidir si sumar 1 a un contador existente o crear uno nuevo en 1.
    
- if conteo[n] > umbral: Una segunda condicion dentro del mismo bucle para detectar al ganador.
    

## Flujo del Codigo

Calculamos el umbral con len(nums) // 2. Iniciamos el bucle for. Usamos un if/else para actualizar el diccionario de conteo. Inmediatamente despues, dentro del mismo for, usamos otro if para comparar el valor actual contra el umbral. Si se cumple, usamos return para entregar el numero ganador y cerrar el programa.