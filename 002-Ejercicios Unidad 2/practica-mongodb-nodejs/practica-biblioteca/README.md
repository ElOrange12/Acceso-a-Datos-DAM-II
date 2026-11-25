# Práctica MongoDB y Node.js

Proyecto Node.js de los ejercicios 13 a 18, más un guion de `mongosh` para los ejercicios 2 a 11. Forma parte de una práctica que también requiere Windows 10 dentro de VirtualBox y capturas hechas en la máquina virtual.

## Parte A: poblar y consultar MongoDB

Instala MongoDB Community Server, `mongosh` y Node.js en la VM siguiendo el enunciado. Inicia MongoDB y, desde cmd en la carpeta del proyecto, ejecuta:

```cmd
mongosh --file mongosh\parte-a.js
```

El guion limpia la colección y recorre los ejercicios de la Parte A en orden. Al terminar quedan cinco libros: Quijote, Cien años de soledad, La sombra del viento, El principito y Patria. Harry Potter se elimina al final. El principito queda no disponible y El Quijote queda con 3 ejemplares.

Para practicar escribiendo las órdenes a mano, usa las operaciones del guion una por una dentro de `mongosh` según los ejercicios 2 a 11 del enunciado.

## Parte B: Node.js

Abre cmd en esta carpeta e instala la dependencia:

```cmd
npm install
```

Ejecuta los archivos en este orden:

```cmd
node conexion.js
node listar.js
node insertar.js
node buscar.js
node prestar.js
node estadisticas.js
```

`insertar.js` se ejecuta una sola vez para evitar duplicar `Nada`. En `buscar.js`, la variable empieza en `novela`; para la segunda comprobación, cambia su valor a `infantil` y vuelve a ejecutar el archivo.

Resultados previstos al completar la secuencia: la colección tiene seis libros; cuatro disponibles y dos prestados (El principito y La sombra del viento); el libro más largo es El Quijote con 1250 páginas. El guion mongosh se puede volver a ejecutar para restablecer el estado de los seis libros originales antes de empezar Node.js.

## Entrega

El enunciado también pide capturas de cada ejercicio: `winver`, versiones de Node/npm/MongoDB, resultados de mongosh, programas Node y MongoDB Compass. Guarda las capturas de tu ejecución en `evidencias/`. Para entregar, copia la carpeta a `entrega-mongodb` sin `node_modules`.
