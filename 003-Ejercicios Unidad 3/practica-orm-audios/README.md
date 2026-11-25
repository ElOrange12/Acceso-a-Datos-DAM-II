# Práctica guardar audios con SQLAlchemy

Incluye los dos programas del ejercicio, el archivo real `0802.mp3` y `audios.db` con los datos del MP3 guardados tras ejecutar `guardar_mp3.py`.

## Instalar dependencias

Desde esta carpeta:

```bash
python -m pip install SQLAlchemy pydub
```

En Python 3.13 o superior, instala también `audioop-lts`. Pydub requiere FFmpeg instalado en el sistema; comprueba la instalación con `ffmpeg -version`.

## Ejecutar la práctica CRUD

```bash
python practica.py
```

Salida esperada:

```text
1 llamada.mp3 8000 8 30.5
2 cancion_cd.mp3 44100 16 210.0
1 llamada.mp3 45.0
```

Este programa borra y vuelve a crear la tabla al inicio, guarda dos audios de ejemplo, imprime sus datos, cambia la duración de la llamada y elimina la canción.

## Guardar el MP3 real

```bash
python guardar_mp3.py
```

Salida obtenida con el archivo proporcionado:

```text
1 0802.mp3 44100 16 166.4
```

El script también borra y vuelve a crear la tabla antes de registrar el MP3. Por eso `audios.db`, que se incluye como resultado final, contiene la fila de `0802.mp3`; si ejecutas antes `practica.py`, la base pasará a contener los datos CRUD de ejemplo. `guardar_mp3.py` vuelve a reemplazarlos por los del archivo real.

## Evidencias visuales

Guarda en `evidencias/` capturas de las salidas de `practica.py` y `guardar_mp3.py`.
