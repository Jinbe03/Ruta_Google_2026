class Solution(object):
    def isAnagram(self, s, t):
        # Si no miden lo mismo, no perdemos tiempo
        if len(s) != len(t):
            return False
        
        # Creamos dos diccionarios para contar
        conteo_s = {}
        conteo_t = {}
        
        # Contamos las letras de la primera palabra
        for letra in s:
            conteo_s[letra] = conteo_s.get(letra, 0) + 1
            
        # Contamos las letras de la segunda palabra
        for letra in t:
            conteo_t[letra] = conteo_t.get(letra, 0) + 1

        print(f"Diccionario de '{s}: {conteo_s}")
        print(f"Diccionario de '{t}: {conteo_t}")
            
        # Comparamos los diccionarios
        return conteo_s == conteo_t

# Crear una instancia de tu solución
solucion = Solution()

# Probar con un caso real
palabra1 = "anagrama"
banana = "nagarama"

resultado = solucion.isAnagram(palabra1, banana)

print("¿Es anagrama?:", resultado)