**Patrón:** Dos Punteros (Pinza + Construcción Inversa).

> **Introspección de Zik:** "Los sensores descalibrados tienen sus valores más extremos en las fronteras. Al elevarlos al cuadrado, la magnitud manda. Lleno mi registro desde el valor más pesado hacia el más leve, asegurando un orden absoluto bajo presión."

- **Lógica Táctica:** Comparar los cuadrados de los extremos. El mayor se coloca en la última posición disponible de la lista de resultados (`pos = n-1`) y se mueve el puntero correspondiente hacia el centro.
    
- **Código Maestro:**
    

Python

```
def sortedSquares(self, nums):
    L, R, pos = 0, len(nums) - 1, len(nums) - 1
    res = [0] * len(nums)
    while L <= R:
        if nums[L]**2 > nums[R]**2:
            res[pos] = nums[L]**2
            L += 1
        else:
            res[pos] = nums[R]**2
            R -= 1
        pos -= 1
    return res
```