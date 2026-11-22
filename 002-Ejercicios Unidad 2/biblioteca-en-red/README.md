# Práctica Biblioteca en red

Proyecto de apoyo para completar la práctica del enunciado: MongoDB desde Node.js y MySQL desde Python con SQLAlchemy, ambos en Docker dentro de Ubuntu Server.

## 1. Preparar el servidor Ubuntu

Sigue en VirtualBox los pasos 1 a 6 del enunciado: crea Ubuntu Server con adaptador puente, instala OpenSSH y Docker, y vuelve a iniciar la sesión SSH tras añadir tu usuario al grupo `docker`. Desde Windows confirma que puedes conectar con `ssh alumno@IP_DE_LA_VM`.

La IP `192.168.1.50` usada como ejemplo no es necesariamente la de tu red. En Ubuntu consulta `ip a` y sustituye la IP del ejemplo por la dirección de la interfaz `enp0s3`.

## 2. Arrancar las bases de datos

Copia `docker-compose.yml` a `~/biblioteca` en Ubuntu. Desde esa carpeta ejecuta:

```bash
docker compose up -d
docker ps
docker network ls
```

Debes ver los servicios `mongo` y `mysql` en ejecución, con los puertos 27017 y 3306 publicados. Las bases de datos usan volúmenes Docker para conservar los datos.

## 3. Ejecutar MongoDB desde Windows

En PowerShell, dentro de `biblioteca-en-red/mongo`, ejecuta:

```powershell
npm install
$env:IP_VM="IP_DE_LA_VM"
npm start
```

El programa crea tres documentos con campos distintos, consulta los anteriores a 1900, cambia el autor de *La Regenta*, elimina *Nada* y cuenta los documentos. Para comprobar el contenido desde Ubuntu:

```bash
docker exec -it mongo mongosh biblioteca --quiet --eval "db.libros.find()"
```

## 4. Ejecutar SQLAlchemy desde Windows

En otra carpeta de PowerShell, dentro de `biblioteca-en-red/orm`, crea un entorno virtual e instala las dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
$env:IP_VM="IP_DE_LA_VM"
py biblioteca_orm.py
```

Se crean las tablas `socios` y `libros`, se insertan dos socios y tres libros, se registra el préstamo de *El Quijote* a Ana, se consulta y actualiza *La Regenta* y se elimina *Nada*. **El programa borra las tablas antes de recrearlas**, tal como indica el enunciado para empezar de cero.

En Ubuntu puedes revisar las filas con:

```bash
docker exec -it mysql mysql -u alumno -palumno123 biblioteca -e "SELECT * FROM libros;"
```

## 5. Comprobar rollback y persistencia

En la carpeta `orm`, ejecuta:

```powershell
py transaccion.py
```

El segundo libro no tiene título, por lo que MySQL rechaza la transacción. El `rollback()` debe dejar el recuento igual que antes.

Después, en Ubuntu, dentro de `~/biblioteca`, ejecuta:

```bash
docker compose down
docker compose up -d
docker exec -it mysql mysql -u alumno -palumno123 biblioteca -e "SELECT COUNT(*) FROM libros;"
```

Los contenedores se recrean y los datos permanecen porque `down` conserva los volúmenes. No uses `docker compose down -v` si quieres conservarlos.

## Comparación final

| Aspecto | MongoDB con Node.js | MySQL con SQLAlchemy |
|---|---|---|
| Modelo | Documentos en colecciones | Filas en tablas relacionadas |
| Esquema | Flexible; documentos pueden tener campos distintos | Definido por las entidades y columnas |
| Conexión | Driver oficial `mongodb` | ORM SQLAlchemy y driver PyMySQL |
| CRUD | Métodos como `insertMany`, `find`, `updateOne` y `deleteOne` | Objetos ORM, consultas `select` y `commit` |
| Relaciones | Los documentos suelen agrupar datos relacionados | Claves ajenas y `relationship()` |
| Persistencia | Volúmenes Docker | Volúmenes Docker |

## Evidencias que debes capturar en tu equipo

El enunciado pide comprobar pasos que dependen de la máquina virtual y de la red real. Para acreditar tu ejecución, guarda capturas propias de: IP de Ubuntu y prueba SSH; `docker ps` con ambos contenedores; salida CRUD de Node.js; consulta MongoDB dentro del contenedor; salida de SQLAlchemy y filas MySQL; recuento antes y después del rollback; y recuento tras recrear contenedores.

La carpeta `evidencias_simuladas` contiene ejemplos visuales de algunas salidas esperadas. Todas las imágenes llevan una marca visible de **SIMULACIÓN**; son mockups para orientar la comprobación y no acreditan que el laboratorio se haya ejecutado.

Al terminar el laboratorio, ejecuta `docker compose down` en Ubuntu y luego `sudo poweroff`.
