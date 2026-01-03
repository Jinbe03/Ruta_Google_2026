Escenario de Zik:

Zik está frente a una consola de energía bloqueada. Para abrirla, necesita conectar dos celdas de energía cuya suma de voltajes sea exactamente igual al Target del sistema. Las celdas están alineadas en un riel y ya están ordenadas de menor a mayor.

> **Ejemplo:**
> 
> - Celdas: `[2, 7, 11, 15]`
>     
> - Target: `9`
>     
> - Solución: Las celdas en los índices 0 y 1 ($2 + 7 = 9$).
>     

#### ¿Por qué no usar un Diccionario aquí?

Podrías usarlo (como en el Ejercicio 001), pero como la lista ya está **ordenada**, Google espera que uses **Dos Punteros**. Es más elegante y no consume memoria extra.

### 🎮 La Táctica de la "Balanza"

Imagina que tienes un puntero en cada extremo. Sumas lo que ven ambos:

1. **Si la Suma es muy ALTA:** Necesitas reducir el voltaje. La única forma de hacerlo es mover el puntero de la **derecha** hacia la izquierda (hacia números más chicos).
    
2. **Si la Suma es muy BAJA:** Necesitas más voltaje. Mueves el puntero de la **izquierda** hacia la derecha (hacia números más grandes).
    
3. **Si la Suma es IGUAL:** ¡Puerta abierta!
    

### 🧠 Ejercicio de Razonamiento Bruno:

Tienes esta lista: `[1, 3, 4, 5, 8, 10]` y tu **Target** es **13**.

- **Paso 1:** `L` apunta a **1**, `R` apunta a **10**. Suma = **11**.
    
    - **Pregunta:** ¿La suma es mayor o menor al Target? ¿Qué puntero moverías tú?
        
- **Paso 2:** Basado en tu respuesta anterior, ¿cuál sería la siguiente suma que compararías?