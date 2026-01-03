**Patrón:** Dos Punteros (In-place Swap).

> **Introspección de Zik:** "No desperdicies recursos construyendo un nuevo hangar si solo necesitas reordenar las cajas. El intercambio en el sitio es la firma de un ingeniero que respeta su memoria."

- **Lógica Táctica:** Usar la pinza para realizar un `swap` simultáneo: `lista[L], lista[R] = lista[R], lista[L]`. Eficiencia máxima de memoria.