def ordenar_montaña(lista):
    n = len(lista)
    # Este bucle es para repetir las pasadas
    for i in range(n):
        # Este bucle es el camino de Zik comparando vecinos
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # ¡Intercambio de emergencia!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista