class Solution(object):
    def majorityElement(self, nums):
        umbral = len(nums) // 2
        conteo = {}
        
        for n in nums:
            if n in conteo:
                conteo[n] += 1
            else:
                conteo[n] = 1
            
            if conteo[n] > umbral:
                return n
            # 1. Cuenta el número n en el diccionario
            # 2. Revisa si el valor de n en el diccionario es mayor a umbral
            # 3. Si es mayor, return n
            
        return None
    
sol = Solution()
print("El ganador es:", sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))