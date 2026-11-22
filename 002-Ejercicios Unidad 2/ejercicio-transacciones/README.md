# Venta de entradas con saldo

Solución del ejercicio de transacciones con Python y MySQL. El proyecto incluye `taquilla.py`, el SQL de inicialización y la dependencia del conector.

## Preparar la base de datos

1. Arranca MySQL en XAMPP.
2. En phpMyAdmin, abre la pestaña SQL y ejecuta el contenido de `preparar_taquilla.sql`. Este script borra y vuelve a crear la base `taquilla`.
3. Instala el conector Python:

   ```bash
   python -m pip install -r requirements.txt
   ```

El ejemplo usa el usuario `root` sin contraseña, como la configuración local por defecto del enunciado. Si tu MySQL tiene otra configuración, actualiza `user` y `password` en `taquilla.py`.

## Ejecutar

```bash
python taquilla.py
```

El programa primero reproduce el fallo sin transacción: la resta del saldo de Laura se confirma y el `INSERT` falla porque usa a propósito la tabla mal escrita `entrada`. Después muestra que Laura quedó con 30 € y sin entrada, devuelve los 20 € para restablecer el estado de partida y prueba las transacciones correctas. Laura compra y queda con 30 € y su entrada; la compra de Marcos se cancela por saldo insuficiente y el `rollback` mantiene 15 € y evita guardar la entrada.

El programa ejecuta las partes del ejercicio en un solo recorrido. Vuelve a ejecutar `preparar_taquilla.sql` antes de repetirlo, ya que cada corrida altera los saldos y añade una entrada.

## Captura de ejemplo

`evidencias_simuladas/resultado.svg` ilustra el resultado esperado y está marcada como **SIMULACIÓN**. No es una captura de una ejecución real en XAMPP; debes ejecutar el programa en tu entorno para obtener evidencia real.
