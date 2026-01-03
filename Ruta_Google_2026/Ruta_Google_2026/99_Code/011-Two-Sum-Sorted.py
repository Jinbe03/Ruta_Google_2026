class Solution(object):
    def twoSum(self, numbers, target):
        # 1. Posicionamos a los exploradores en los extremos
        L = 0
        R = len(numbers) - 1
        
        # 2. Iniciamos el protocolo de búsqueda
        while L < R:
            suma_actual = numbers[L] + numbers[R]
            
            # CASO A: ¡Blanco encontrado!
            if suma_actual == target:
                # Nota: Este problema suele pedir indices basados en 1 (1-indexed)
                return [L + 1, R + 1]
            
            # CASO B: La suma es demasiado alta (exceso de energía)
            if suma_actual > target:
                R -= 1  # Movemos el puntero derecho a un valor menor
                
            # CASO C: La suma es demasiado baja (falta energía)
            else:
                L += 1  # Movemos el puntero izquierdo a un valor mayor
        
        return []

# --- BLOQUE DE PRUEBA PARA TU TERMINAL ---
sol = Solution()
celdas = [2, 7, 11, 15]
objetivo = 9

print(f"Buscando target {objetivo}...")
resultado = sol.twoSum(celdas, objetivo)
print(f"Celdas de energía localizadas en posiciones: {resultado}")