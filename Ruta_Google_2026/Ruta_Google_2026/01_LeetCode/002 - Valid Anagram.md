## Estrategia Técnica

Para verificar si dos palabras son anagramas, comparamos la frecuencia de sus caracteres. Si ambas palabras tienen las mismas letras en las mismas cantidades, son anagramas.

## Lógica del Algoritmo

1. Validar el largo de las cadenas. Si son distintos, retornar False.
2. Crear un diccionario de frecuencia para cada palabra.
3. Comparar ambos diccionarios. En Python, la comparación directa de diccionarios (==) es eficiente.

## Código en Python

class Solution(object): def isAnagram(self, s, t): if len(s) != len(t): return False

```
    conteo_s = {}
    conteo_t = {}
    
    for char in s:
        conteo_s[char] = conteo_s.get(char, 0) + 1
    for char in t:
        conteo_t[char] = conteo_t.get(char, 0) + 1
        
    return conteo_s == conteo_t
```

## Análisis de Complejidad

Tiempo: O(n). Recorremos cada palabra una vez. Espacio: O(1) o O(k). Aunque usamos diccionarios, el espacio está limitado por el alfabeto (máximo 26 letras si es inglés), por lo que se considera espacio constante en muchos contextos.


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
            
        # Comparamos los diccionarios
        return conteo_s == conteo_t