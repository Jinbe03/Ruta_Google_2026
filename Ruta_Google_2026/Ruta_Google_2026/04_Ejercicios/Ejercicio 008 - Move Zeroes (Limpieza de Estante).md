**Patrón:** Dos Punteros (Persecución).

> **Introspección de Zik:** "Las celdas quemadas (ceros) solo estorban en el fragor del combate. Mi explorador rápido escanea el terreno y le lanza las unidades operativas al marcador lento. El resultado: un frente de batalla limpio y listo."

- **Lógica Táctica:** Un puntero lento (`L`) marca dónde poner la próxima unidad buena. El rápido (`R`) recorre la lista. Si `nums[R] != 0`, se intercambian y `L` avanza.