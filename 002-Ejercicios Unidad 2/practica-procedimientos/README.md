# Biblioteca con procedimientos almacenados y Python

Solución de la práctica de MySQL y `mysql-connector-python`.

## Preparar MySQL

En Workbench, conectado como administrador, ejecuta todo `preparar_biblioteca.sql`. El script vuelve a crear la base, la tabla, los cuatro libros, los procedimientos y el usuario `app_biblioteca`. También restablece los ejemplares del Quijote a 3.

El script de Python se conecta como `app_biblioteca`, con permiso `EXECUTE` solamente a nivel de la base `biblioteca`; no recibe permiso `SELECT` sobre la tabla. Los procedimientos se crean bajo la cuenta administradora y usan el contexto `SQL SECURITY DEFINER` predeterminado de MySQL para consultar o modificar la tabla.

## Ejecutar Python

```bash
python -m pip install -r requirements.txt
python practica.py
```

La salida reproduce el orden del enunciado: listado, búsqueda por autor, recuento, préstamo correcto del libro 1, rechazo del préstamo del libro 4 y acceso directo denegado. La conexión usa `autocommit=True`, tal como pide el ejercicio; `commit()` y `rollback()` hacen explícito el resultado de cada llamada que cambia datos.

Para volver al estado inicial, ejecuta de nuevo `preparar_biblioteca.sql` en Workbench antes de correr el programa.

## Evidencias

Guarda en `evidencias/` capturas de las consultas y llamadas a procedimientos realizadas en MySQL.
