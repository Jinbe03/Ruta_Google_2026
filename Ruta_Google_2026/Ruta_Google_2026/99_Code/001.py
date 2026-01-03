frutas = ['manzana', 'pera', 'manzana', 'platano', 'pera', 'manzana']
inventario = {}

for fruta in frutas:
    if fruta in inventario:
        inventario[fruta] += 1
    else:
        inventario[fruta] = 1

    
    # ESCRIBE AQUÍ TU IF/ELSE
    # 1. Si la fruta ya está en inventario, súmale 1
    # 2. Si no está, agrégala con valor 1

print(inventario)