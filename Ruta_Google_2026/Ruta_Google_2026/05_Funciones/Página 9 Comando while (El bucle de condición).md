## Cómo funciona

A diferencia del `for` (que recorre una lista de inicio a fin), el `while` es como un **guardia de seguridad en una puerta**. Él te deja pasar y repetir la acción una y otra vez, siempre y cuando cumplas la regla. En el momento en que la regla ya no se cumple, el guardia te detiene y el programa sigue adelante.

## Sintaxis básica

Python

```
while condicion:
    # Este código se repite
    # IMPORTANTE: Aquí dentro debe pasar algo que 
    # eventualmente haga que la condición sea falsa
```

## Ejemplo real (Cuenta regresiva)

Python

```
energia = 3
while energia > 0:
    print("Sistema activo...")
    energia -= 1  # Gastamos energía en cada paso
print("Sistema apagado.")
```

## Diferencia con el Bucle for

- **for**: Sabes de antemano cuántas veces vas a repetir (ejemplo: por cada letra en una palabra).
    
- **while**: No sabes exactamente cuántas veces será, solo sabes que debe seguir mientras la regla se cumpla (ejemplo: mientras el personaje de la izquierda no choque con el de la derecha).