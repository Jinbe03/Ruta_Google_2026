# Comando: enumerate()

Sirve para: Recorrer una lista obteniendo el valor pero también el índice (la posición) de cada cosa.

## Como funciona

Es como pasar asistencia en clase. No solo dices el nombre del alumno, sino también su número en la lista.

## Sintaxis basica

for posicion, valor in enumerate(lista): # Tienes ambos datos disponibles

## Ejemplo real

marcas = [Google, Apple] for i, marca in enumerate(marcas): print(i, marca)

# Resultado: 0 Google, 1 Apple