**Escenario de Zik:** Zik está en medio de un campo de asteroides. Tiene una lista de frecuencias de radio enemigas **ordenadas** de menor a mayor: `[10, 20, 30, 40, 50, 60, 70, 80, 90]`. Necesita encontrar la posición exacta de la frecuencia **70** para interceptar la comunicación.

> **El Problema:** Si Zik busca una por una (Búsqueda Lineal), y la lista tiene 1 millón de frecuencias, tardará demasiado. **La Solución:** Dividir el terreno a la mitad en cada paso.

#### 🎮 La Táctica de "Dividir y Conquistar"

Aquí usamos dos punteros, `Low` (Inicio) y `High` (Fin), pero el protagonista es el **punto medio (Mid)**.

1. **Cálculo del Medio:** Zik mira el centro de la lista.
    
2. **Comparación Táctica:**
    
    - ¿El número en el medio es **igual** al que busco? ¡Misión cumplida!
        
    - ¿El número en el medio es **más chico**? Entonces mi objetivo está a la **derecha**. Muevo mi puntero `Low` al medio + 1.
        
    - ¿El número en el medio es **más grande**? Entonces mi objetivo está a la **izquierda**. Muevo mi puntero `High` al medio - 1.
        

---

### 🧠 Razonamiento para Bruno:

Si tienes la lista `[10, 20, 30, 40, 50, 60, 70, 80, 90]` y buscas el **70**:

1. `Low` es 0 (valor 10), `High` es 8 (valor 90). El medio es 4 (valor 50).
    
2. **Pregunta:** El 50 es **menor** que el 70. Según la lógica de Zik, ¿hacia qué lado deberías descartar la búsqueda? ¿Qué puntero moverías y a qué posición?
### 🛠️ Código Maestro (013-Binary-Search.py)

Este código es fundamental. Agrégalo a tu **99_Code**. Fíjate en cómo el área de búsqueda se encoge a la mitad en cada vuelta del `while`:

Python

```
class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            # Calculamos el punto medio
            mid = (low + high) // 2
            
            # Caso 1: ¡Lo encontramos!
            if nums[mid] == target:
                return mid
            
            # Caso 2: El medio es muy pequeño, descartamos la izquierda
            if nums[mid] < target:
                low = mid + 1
            
            # Caso 3: El medio es muy grande, descartamos la derecha
            else:
                high = mid - 1
                
        return -1 # Si no se encuentra

# Prueba táctica
sol = Solution()
frecuencias = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70
print(f"Frecuencia localizada en el índice: {sol.search(frecuencias, target)}")
```