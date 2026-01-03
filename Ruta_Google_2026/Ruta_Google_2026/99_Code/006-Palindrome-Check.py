class Solution(object):
    def isPalindrome(self, lista):
        # 1. Definir posiciones iniciales
        L = 0
        R = len(lista) - 1 # Usaste len() aquí, ¡perfecto!
        
        # 2. El bucle de movimiento
        while L < R:
            # 3. La pregunta de seguridad
            if lista[L] != lista[R]:
                return False # Tu idea del return para salir rápido
            
            # 4. Mover la pinza hacia el centro
            L += 1
            R -= 1
            
        # 5. Si el bucle termina y nadie activó el 'return False'
        return True

# --- PRUEBA ESTO CUANDO VUELVAS ---
sol = Solution()
print("¿Es [1,2,3,2,1] palíndromo?:", sol.isPalindrome([1,2,3,2,1]))
print("¿Es [1,2,3,4,1] palíndromo?:", sol.isPalindrome([1,2,3,4,1]))