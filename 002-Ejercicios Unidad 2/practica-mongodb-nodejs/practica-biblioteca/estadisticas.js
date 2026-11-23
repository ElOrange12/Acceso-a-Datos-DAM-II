const { MongoClient } = require("mongodb");
const cliente = new MongoClient("mongodb://127.0.0.1:27017");

async function main() {
  try {
    await cliente.connect();
    const libros = cliente.db("biblioteca").collection("libros");
    const total = await libros.countDocuments();
    const disponibles = await libros.countDocuments({ disponible: true });
    const prestados = await libros.countDocuments({ disponible: false });
    const masLargo = await libros.findOne({}, { sort: { paginas: -1 } });

    console.log("Total de libros: " + total);
    console.log("Disponibles: " + disponibles);
    console.log("Prestados: " + prestados);
    if (masLargo) {
      console.log("Más páginas: " + masLargo.titulo + " (" + masLargo.paginas + ")");
    }
  } catch (error) {
    console.log("Error: " + error.message);
  } finally {
    await cliente.close();
  }
}

main();
