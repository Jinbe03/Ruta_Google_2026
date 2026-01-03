### 🛡️ Ejercicio 005: Word Counter (Análisis de Transmisiones)

**Patrón:** Frecuencia con Diccionarios.

> **Introspección de Zik:** "En el campo de batalla, la información desordenada es ruido. Agrupar datos repetidos en una memoria inteligente me permite ver patrones donde otros solo ven caos. No solo cuento palabras; identifico la señal dentro del ruido."

- **Lógica Táctica:** Usar un diccionario `{}` y el método `.get(p, 0)` para registrar cada "invitado" y sumarle un punto de importancia.
    
- **Código Maestro:**
    

Python

```
def wordCounter(self, frase):
    palabras = frase.split()
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return conteo
```