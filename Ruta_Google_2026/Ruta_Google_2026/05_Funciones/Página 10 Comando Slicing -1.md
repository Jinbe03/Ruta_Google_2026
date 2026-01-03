# Comando: Slicing [::-1]

Sirve para: Invertir una lista o un texto de forma instantánea.

## Cómo funciona

Python tiene una sintaxis especial que te permite decir: "Toma esta lista desde el inicio hasta el final, pero camina hacia atrás".

## Ejemplo del "Truco Sucio" para Palíndromos:

Python

```
def es_palindromo(lista):
    return lista == lista[::-1]
```

reverses elements]

**¿Por qué te enseño esto si ya aprendimos Dos Punteros?** Porque en una entrevista de Google, primero debes mostrar que sabes la lógica difícil (Dos Punteros) para demostrar que entiendes cómo funciona la memoria. Pero luego, mencionar: _"En Python, también podríamos usar slicing para que el código sea más legible"_, te hace ver como un experto que conoce sus herramientas a fondo.