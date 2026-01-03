class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        # Creamos una lista llena de ceros del mismo tamaño
        resultado = [0] * n
        
        L = 0
        R = n - 1
        # El puntero 'pos' marca donde pondremos el siguiente numero (al final)
        pos = n - 1
        
        while L <= R:
            izq_cuadrado = nums[L] ** 2
            der_cuadrado = nums[R] ** 2
            
            if izq_cuadrado > der_cuadrado:
                # El de la izquierda es mayor, lo ponemos al final
                resultado[pos] = izq_cuadrado
                L += 1
            else:
                # El de la derecha es mayor o igual, lo ponemos al final
                resultado[pos] = der_cuadrado
                R -= 1
            
            # Movemos la posicion de llenado un paso hacia la izquierda
            pos -= 1
            
        return resultado

# Prueba de campo para Zik
sol = Solution()
sensores = [-4, -1, 0, 3, 10]
print("Sensores calibrados y ordenados:", sol.sortedSquares(sensores))