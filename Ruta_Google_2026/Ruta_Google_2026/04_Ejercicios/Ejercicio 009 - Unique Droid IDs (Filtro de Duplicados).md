**Patrón:** Punteros de Persecución (Sobrescritura).

> **Introspección de Zik:** "No borres el pasado, simplemente escribe un futuro mejor encima. Si encuentro un ID de droide que no he visto antes, lo muevo al frente. Lo que queda atrás ya no importa."

- **Lógica Táctica:** Comparar `nums[R]` con `nums[L]`. Si son distintos, encontramos un valor nuevo. Avanzamos `L` y sobreescribimos: `nums[L] = nums[R]`.