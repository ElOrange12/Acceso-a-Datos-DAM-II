# Práctica CRUD de una agenda con MongoDB y Node.js

Incluye un guion para los ejercicios de mongosh y los cuatro programas Node.js de la Parte B.

## Parte A: mongosh

Con MongoDB funcionando en la máquina virtual, desde esta carpeta ejecuta:

```cmd
mongosh --file mongosh\parte-a.js
```

El guion reinicia `agenda.contactos` y reproduce inserción, lectura, filtro por ciudad, actualización del teléfono de Luis y eliminación de Pedro. Al terminar quedan Ana López, Luis Martín (teléfono actualizado), Marta Ruiz y Lucía Sanz.

## Parte B: Node.js

Instala la dependencia una vez:

```cmd
npm install
```

Ejecuta los programas en este orden:

```cmd
node crear.js
node leer.js
node actualizar.js
node borrar.js
node leer.js
```

`crear.js` se ejecuta una sola vez: añade a Sara Díaz y deja cinco contactos. Después se cambia Marta a Castellón y se elimina a Sara. El estado final vuelve a cuatro contactos. Para repetir desde el inicio, ejecuta de nuevo el guion de mongosh; eso borra y recrea la colección inicial.

Para copiar el proyecto a la carpeta compartida sin `node_modules`, usa la orden del enunciado (cambia `Z:` si tu carpeta compartida usa otra letra):

```cmd
robocopy %USERPROFILE%\Desktop\agenda-contactos Z:\agenda-contactos /E /XD node_modules
```

## Entrega y evidencias

El enunciado pide capturas de los ejercicios y entregar la carpeta Node.js sin `node_modules`. `evidencias_simuladas/resultado.svg` es un mockup marcado como **SIMULACIÓN**, no una captura real. La guía de la práctica incluye el comando Robocopy para copiar el proyecto a la carpeta compartida excluyendo `node_modules`.
