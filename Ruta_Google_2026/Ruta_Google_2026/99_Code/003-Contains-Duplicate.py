class Solution(object):
    def containsDuplicate(self, nums):
        # 1. Crea tu memoria
        memoria = {}
        
        # 2. Empieza el bucle for
        for numero in nums:
            if numero in memoria:
                return True
            else:
                memoria[numero] = 1
        
        # 3. El return False debe ir FUERA del bucle
        # Solo llegamos aquí si recorrimos TODA la lista y no hubo True
        return False
        #    Si sí: return True
        # 4. Si no estaba: Agrégalo a la memoria
        # 5. Si el bucle termina y no encontró nada: return False
solucion = Solution()
# Caso con duplicado
lista1 = [1, 2, 3, 1]
print(f"Lista {lista1} - ¿Tiene duplicados?:", solucion.containsDuplicate(lista1))
# Caso sin duplicado
lista2 = [1, 2, 3, 4]
print(f"Lista {lista2} - ¿Tiene duplicados?:", solucion.containsDuplicate(lista2))
