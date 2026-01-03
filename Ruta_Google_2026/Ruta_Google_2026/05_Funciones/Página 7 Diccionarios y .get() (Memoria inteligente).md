# Comando: Diccionarios y .get()

Sirve para: Guardar y buscar información de forma ultra rápida.

## Como funciona

El diccionario es como una biblioteca organizada por temas. El método .get() es como preguntarle al bibliotecario por un libro; si no existe, te da una respuesta amable en lugar de entrar en pánico.

## Sintaxis basica

memoria = {} valor = memoria.get(llave, valor_por_defecto)

## Ejemplo real

votos = {azul: 10} print(votos.get(rojo, 0))

# Resultado: 0 (Porque rojo no existe)