class Solution(object):
    def wordCounter(self, frase):
        # Convertimos la frase en una lista de palabras
        palabras = frase.split()
        
        # 1. Crea tu memoria (diccionario vacío)
        conteo = {}
        
        # 2. Recorre cada palabra en la lista
        for p in palabras:
            # 3. Usa el método para contar (si no existe, empieza en 0 y suma 1)
            conteo[p] = conteo.get(p, 0) + 1
            
        return conteo

# --- PRUEBA EN VS CODE ---
sol = Solution()
mensaje = "fuego fuego en el sector cuatro fuego"
print("Resultado del análisis:", sol.wordCounter(mensaje))