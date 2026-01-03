## Sintaxis Clave

- enumerate(nums): Para obtener la posicion (i) y el valor (n) al mismo tiempo.
    
- if complemento in memoria: Para buscar si ya vimos el numero que nos falta.
    
- diccionario[llave] = valor: Para guardar el numero actual y su posicion.
    

## Flujo del Codigo

Usamos un bucle for con enumerate para recorrer la lista. En cada paso, calculamos una resta (target - n). Usamos un if para ver si ese resultado ya esta en nuestro diccionario. Si no esta, usamos la asignacion memoria[n] = i para guardarlo y seguir buscando.