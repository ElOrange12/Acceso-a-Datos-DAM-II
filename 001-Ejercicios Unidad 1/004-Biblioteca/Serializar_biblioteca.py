import json

NOMBRE_FICHERO = "biblioteca.dat"


def crear_lista_libros():
	################ Creamos una lista de diccionarios con los libros ####################
	libros = [
		{
			"titulo": "Don Quijote de la Mancha",
			"autor": "Miguel de Cervantes",
			"anio": 1605,
			"paginas": ~1000
		},
		{
			"titulo": "Cien años de soledad",
			"autor": "Gabriel García Márquez",
			"anio": 1967,
			"paginas": ~400
		},
		{
			"titulo": "1984",
			"autor": "George Orwell",
			"anio": 1949,
			"paginas": ~320
		}
	]

	return libros


def serializar_libros(libros):
	################ Convertimos la lista de Python en texto JSON ####################
	cadena = json.dumps(libros)

	print("\n--- Lista convertida a JSON ---")
	print(cadena)
	print("Tipo:", type(cadena))

	return cadena


def guardar_en_fichero(cadena):
	################ Guardamos la cadena JSON en un fichero ####################
	flujo = open(NOMBRE_FICHERO, "w")

	flujo.write(cadena)

	flujo.close()

	print(f"\nSe ha guardado '{NOMBRE_FICHERO}' correctamente.")


def main():
	libros = crear_lista_libros()

	print("--- Lista de libros ---")
	print(libros)
	print("Tipo:", type(libros))

	cadena = serializar_libros(libros)

	guardar_en_fichero(cadena)


if __name__ == "__main__":
	main()


