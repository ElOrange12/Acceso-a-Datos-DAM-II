# Ejercicio práctico: biblioteca con Python y MySQL

## Preparación

Instala MySQL Server y Python. Desde esta carpeta, instala el conector:

```bash
python -m pip install -r requirements.txt
```

Ejecuta primero el SQL de preparación como administrador de MySQL:

```bash
mysql -u root -p < crear_biblioteca.sql
```

Después ejecuta los ejercicios en orden:

```bash
python 1_conexion.py
python 2_pool.py
python 3_errores.py
python 4_estructura.py
```

El ejercicio 4 elimina la tabla `socios` al final, tal como pide el enunciado.
Las capturas incluidas en el documento son simulaciones ilustrativas y no una
ejecución real contra MySQL.
