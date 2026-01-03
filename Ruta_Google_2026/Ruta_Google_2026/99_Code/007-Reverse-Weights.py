class Solution(object):
    def reverseWeights(self, pesos):
        L = 0
        R = len(pesos) - 1
        
        while L < R:
            # Esta es la maniobra de intercambio
            pesos[L], pesos[R] = pesos[R], pesos[L]
            
            # Los exploradores avanzan al centro
            L += 1
            R -= 1
            
        return pesos

# Prueba de campo para Zik
sol = Solution()
suministros = [10, 20, 30, 40, 50]
print("Pesos invertidos:", sol.reverseWeights(suministros))