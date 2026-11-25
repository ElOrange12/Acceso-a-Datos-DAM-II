# Práctica ORM de libros

Solución paso a paso con SQLAlchemy 2 y SQLite para la práctica de la tabla `libros`. El script se ejecutó en este entorno y produjo la salida esperada; `biblioteca.db` contiene el estado final generado por esa ejecución.

## Ejecución

Instala SQLAlchemy y ejecuta el programa desde esta carpeta:

```bash
python -m pip install -r requirements.txt
python biblioteca.py
```

Salida esperada en una ejecución desde una base limpia:

```text
Don Quijote de la Mancha - Miguel de Cervantes
Don Quijote de la Mancha 1250
La casa de los espíritus 480
1 Don Quijote de la Mancha 1250
3 Platero y yo 150
```

SQLAlchemy crea `biblioteca.db` en la carpeta actual. Como el enunciado vuelve a insertar los tres libros cada vez que se ejecuta el script, borra `biblioteca.db` antes de repetirlo para que los identificadores y la salida coincidan con el resultado esperado.

## Qué demuestra

- `Mapped[str]` define columnas de texto obligatorias y `Mapped[Optional[int]]` permite que `paginas` quede vacío.
- `create_all` crea la tabla; `Session` agrupa inserciones y cambios confirmados mediante `commit`.
- Las consultas usan `get` y `select` y el ORM genera las instrucciones SQL.
- Se actualiza Platero y yo y se elimina La casa de los espíritus.

Guarda en `evidencias/` una captura de la ejecución de `biblioteca.py`.
