# ORM y pickle juntos

Solución del ejercicio de copia de seguridad y restauración de clientes con SQLAlchemy, SQLite y `pickle`.

## Preparación

```bash
python -m pip install -r requirements.txt
```

Abre una terminal en esta carpeta. Para empezar desde cero, elimina `tienda.db` y `copia.bin` si existen.

## Ejecutar en orden

```bash
python modelos.py
python crear.py
python leer.py
python copia.py
python borrar_todo.py
python leer.py
python restaurar.py
python leer.py
```

Antes de borrar, `leer.py` muestra los tres clientes. La siguiente ejecución muestra 0 clientes. Tras `restaurar.py`, vuelve a mostrar Ana, Luis y Marta. `copia.bin` conserva una lista de diccionarios con sus nombres y ciudades. `tienda.db` incluida en el paquete corresponde al estado final restaurado.

## Archivos de datos

- `tienda.db`: base SQLite, administrada por SQLAlchemy.
- `copia.bin`: copia serializada por pickle.

`copia.py` y `restaurar.py` abren los archivos con `with` para cerrarlos correctamente. La restauración presupone que `copia.bin` procede de este ejercicio y no está manipulado.

La carpeta `evidencias_simuladas` contiene una imagen de terminal ilustrativa marcada como **SIMULACIÓN**; no es una captura de Visual Studio Code ejecutándose en el ordenador del alumno.
