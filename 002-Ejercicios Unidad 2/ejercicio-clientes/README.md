# Ejercicio práctico de clientes

Los tres archivos reproducen las operaciones pedidas en el enunciado usando la conexión y la base `accesoadatos2526`:

1. `004-insertar.py` inserta Ana Martinez Ruiz con el correo `ana@martinezruiz.com`.
2. `005-actualizar.py` cambia su nombre a Ana Maria.
3. `006-eliminar.py` elimina la fila insertada.

## Antes de ejecutar

Instala el conector si aún no está instalado:

```bash
python -m pip install -r requirements.txt
```

Comprueba que MySQL está activo y que la base de datos existe. Ejecuta los tres programas una sola vez y en ese orden. Después de insertar, consulta `SELECT * FROM clientes;` y anota el identificador que MySQL haya asignado. El script de actualización y el de borrado usan el 4, como supone el enunciado; si el identificador real es distinto, cambia ese número en ambos antes de ejecutarlos.

Al terminar, vuelve a consultar la tabla: Ana ya no debe aparecer y las demás filas deben seguir igual. Si vuelves a ejecutar la inserción tras borrar a Ana, `AUTO_INCREMENT` puede asignar otro identificador.

## Evidencia ilustrativa

`evidencias_simuladas/resultado.svg` representa la fila tras inserción, actualización y eliminación. Lleva la marca **SIMULACIÓN**; no es una captura de MySQL ni una consulta ejecutada en tu servidor.
