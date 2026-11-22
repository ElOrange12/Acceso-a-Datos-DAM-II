const { MongoClient } = require("mongodb");

const IP_VM = process.env.IP_VM || "192.168.1.50";
const cliente = new MongoClient(`mongodb://${IP_VM}:27017`);

async function main() {
  try {
    await cliente.connect();
    console.log(`Conectado a MongoDB en ${IP_VM}`);

    const libros = cliente.db("biblioteca").collection("libros");
    await libros.deleteMany({});

    const res = await libros.insertMany([
      {
        titulo: "El Quijote",
        autor: "Cervantes",
        anio: 1605,
        generos: ["novela", "aventuras"],
      },
      { titulo: "La Regenta", autor: "Clarín", anio: 1884 },
      {
        titulo: "Nada",
        autor: "Carmen Laforet",
        anio: 1945,
        premio: "Nadal",
      },
    ]);
    console.log(`Libros guardados: ${res.insertedCount}`);

    const antiguos = await libros.find({ anio: { $lt: 1900 } }).toArray();
    console.log("Libros anteriores a 1900:");
    for (const libro of antiguos) {
      console.log(`- ${libro.titulo} (${libro.anio}) de ${libro.autor}`);
    }

    await libros.updateOne(
      { titulo: "La Regenta" },
      { $set: { autor: "Leopoldo Alas (Clarín)" } },
    );
    console.log("Actualizado el autor de La Regenta");

    await libros.deleteOne({ titulo: "Nada" });
    console.log("Borrado el libro Nada");
    console.log(`Quedan ${await libros.countDocuments()} libros en la colección`);
  } finally {
    await cliente.close();
  }
}

main().catch((error) => {
  console.error("No se pudo completar la operación:", error.message);
  process.exitCode = 1;
});
