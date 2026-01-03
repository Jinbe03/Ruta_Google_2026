class Solution(object):
    def moveZeroes(self, nums):
        # L (el puntero lento) marca donde debe caer el proximo numero util
        L = 0
        
        # R (el explorador) recorre toda la lista
        for R in range(len(nums)):
            # Si encontramos una celda operativa (distinta de 0)
            if nums[R] != 0:
                # Hacemos el intercambio (swap)
                nums[L], nums[R] = nums[R], nums[L]
                
                # Solo entonces, el puntero lento avanza un paso
                L += 1
        
        return nums

# Prueba de campo
sol = Solution()
estante = [0, 1, 0, 3, 12]
print("Estante organizado:", sol.moveZeroes(estante))