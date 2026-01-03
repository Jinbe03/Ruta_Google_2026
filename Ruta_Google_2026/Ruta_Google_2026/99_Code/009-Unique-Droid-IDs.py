class Solution(object):
    def removeDuplicates(self, nums):
        if not nums: return 0
        
        # L empieza en la primera posicion (el primer numero siempre es unico)
        L = 0
        
        # R empieza desde la segunda posicion buscando cambios
        for R in range(1, len(nums)):
            # Si el explorador R encuentra un numero DIFERENTE al que tiene L
            if nums[R] != nums[L]:
                # Movemos a L un espacio adelante
                L += 1
                # Traemos el nuevo numero a esa posicion
                nums[L] = nums[R]
        
        # Al final, L + 1 nos dice cuantos numeros unicos hay
        return L + 1