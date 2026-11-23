// Guion de los ejercicios 2 a 11 de la Parte A.
// Ejecutar con: mongosh --file mongosh/parte-a.js
const biblioteca = db.getSiblingDB("biblioteca");
const libros = biblioteca.collection("libros");

// Estado limpio para que el guion se pueda repetir.
libros.drop();

// Ejercicios 2 y 3: El Quijote y los otros cinco libros.
libros.insertOne({
  titulo: "El Quijote",
  autor: "Miguel de Cervantes",
  anio: 1605,
  genero: "novela",
  paginas: 1250,
  disponible: true,
});

libros.insertMany([
  {
    titulo: "Cien años de soledad",
    autor: "Gabriel García Márquez",
    anio: 1967,
    genero: "novela",
    paginas: 471,
    disponible: true,
  },
  {
    titulo: "La sombra del viento",
    autor: "Carlos Ruiz Zafón",
    anio: 2001,
    genero: "misterio",
    paginas: 576,
    disponible: true,
  },
  {
    titulo: "El principito",
    autor: "Antoine de Saint-Exupéry",
    anio: 1943,
    genero: "infantil",
    paginas: 96,
    disponible: true,
  },
  {
    titulo: "Patria",
    autor: "Fernando Aramburu",
    anio: 2016,
    genero: "novela",
    paginas: 648,
    disponible: true,
  },
  {
    titulo: "Harry Potter y la piedra filosofal",
    autor: "J. K. Rowling",
    anio: 1997,
    genero: "fantasía",
    paginas: 256,
    disponible: true,
  },
]);

// Ejercicios 4 a 8: conteos, filtros, proyección y orden.
print("Ejercicio 4 · Total:", libros.countDocuments());
print("Ejercicio 5 · Novelas:", libros.countDocuments({ genero: "novela" }));
print("Ejercicio 6 · Publicados después de 2000:");
printjson(libros.find({ anio: { $gt: 2000 } }).toArray());
print("Ejercicio 7 · Título y autor, por año:");
printjson(libros.find({}, { titulo: 1, autor: 1, _id: 0 }).sort({ anio: 1 }).toArray());
print("Ejercicio 8 · Menos de 300 páginas:");
printjson(libros.find({ paginas: { $lt: 300 } }, { titulo: 1, paginas: 1, _id: 0 }).toArray());

// Ejercicios 9 y 10: prestar El principito y contar ejemplares.
libros.updateOne({ titulo: "El principito" }, { $set: { disponible: false } });
libros.updateMany({}, { $set: { ejemplares: 1 } });
libros.updateOne({ titulo: "El Quijote" }, { $inc: { ejemplares: 2 } });
print("Ejercicio 9 · No disponibles:");
printjson(libros.find({ disponible: false }, { titulo: 1, _id: 0 }).toArray());
print("Ejercicio 10 · Ejemplares de El Quijote:");
printjson(libros.findOne({ titulo: "El Quijote" }, { projection: { titulo: 1, ejemplares: 1 } }));

// Ejercicio 11: retirar Harry Potter.
libros.deleteOne({ titulo: "Harry Potter y la piedra filosofal" });
print("Ejercicio 11 · Total tras retirar Harry Potter:", libros.countDocuments());
