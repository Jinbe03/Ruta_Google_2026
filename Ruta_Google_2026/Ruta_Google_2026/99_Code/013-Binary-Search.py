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