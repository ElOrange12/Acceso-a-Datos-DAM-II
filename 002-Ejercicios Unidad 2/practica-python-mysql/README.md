# Práctica Python y MySQL

Script completo `practica.py` para crear la base de datos `tienda`, crear y rellenar la tabla `productos`, consultar, filtrar, actualizar y borrar filas.

## Preparación

1. Arranca el servidor MySQL (por ejemplo, desde XAMPP).
2. Instala el conector: `python -m pip install -r requirements.txt`.
3. Revisa la conexión al principio de `practica.py`. Por defecto usa `root` con contraseña `1234`, como indica el enunciado; cambia los datos si tu servidor usa otra configuración.
4. Ejecuta `python practica.py` desde esta carpeta.

El programa recrea la tabla `productos` en cada ejecución, por lo que elimina primero los datos anteriores. La base de datos completa no se elimina. La salida de las bases internas de MySQL puede variar entre instalaciones; debe aparecer `tienda`.

La carpeta `evidencias_simuladas` incluye un mockup con la salida final esperada, marcado como **SIMULACIÓN**. No se ejecutó contra MySQL en este entorno; necesitarás tu servidor local para obtener una captura real.
