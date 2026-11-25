// Guion para reproducir los ejercicios 2 a 7 en mongosh.
// Ejecutar desde la carpeta del proyecto: mongosh --file mongosh/parte-a.js
const agenda = db.getSiblingDB("agenda");
const contactos = agenda.getCollection("contactos");

// Empieza en limpio para que los IDs y el resultado sean repetibles.
contactos.drop();

// Ejercicio 2: Ana López.
contactos.insertOne({
  nombre: "Ana López",
  telefono: "600111222",
  ciudad: "Valencia",
});
print("Ejercicio 2 · Primer contacto:");
printjson(contactos.find().toArray());

// Ejercicio 3: añadir los otros cuatro contactos.
contactos.insertMany([
  { nombre: "Luis Martín", telefono: "600333444", ciudad: "Madrid" },
  { nombre: "Marta Ruiz", telefono: "600555666", ciudad: "Valencia" },
  { nombre: "Pedro Gómez", telefono: "600777888", ciudad: "Sevilla" },
  { nombre: "Lucía Sanz", telefono: "600999000", ciudad: "Barcelona" },
]);

// Ejercicio 4: mostrar y contar.
print("Ejercicio 4 · Total:", contactos.countDocuments());

// Ejercicio 5: buscar Valencia y proyectar nombre/teléfono.
print("Ejercicio 5 · Contactos de Valencia:");
printjson(contactos.find({ ciudad: "Valencia" }).toArray());
printjson(contactos.find({ ciudad: "Valencia" }, { nombre: 1, telefono: 1, _id: 0 }).toArray());

// Ejercicio 6: cambiar el teléfono de Luis.
contactos.updateOne(
  { nombre: "Luis Martín" },
  { $set: { telefono: "611222333" } },
);
print("Ejercicio 6 · Luis actualizado:");
printjson(contactos.findOne({ nombre: "Luis Martín" }));

// Ejercicio 7: borrar a Pedro y mostrar el estado final de la Parte A.
contactos.deleteOne({ nombre: "Pedro Gómez" });
print("Ejercicio 7 · Total tras borrar a Pedro:", contactos.countDocuments());
printjson(contactos.find({}, { nombre: 1, _id: 0 }).toArray());
