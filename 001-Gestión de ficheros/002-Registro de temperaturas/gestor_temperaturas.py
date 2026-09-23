NOMBRE_FICHERO_TEMPERATURAS = "temperaturas.txt"
NOMBRE_FICHERO_CONTADOR = "contador.bin"

def escribir_temperaturas():
    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "w")
    flujo.write("18.5\n")
    flujo.write("21.0\n")
    flujo.write("19.2\n")
    flujo.close()

def leer_temperaturas():
    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    contenido = flujo.read()
    flujo.close()
    print("--- Todas las temperaturas ---")
    print(contenido)
    
def saltar_primera_temperatura():
    flujo = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    flujo.readline()             
    posicion = flujo.tell()      
    flujo.seek(0)                
    flujo.seek(posicion)         
    resto = flujo.read()         
    flujo.close()
    print("Nos saltamos la primera temperatura y leemos el resto:")
    print(resto)

def comprobar_fichero_configuracion():
    try:
        flujo = open("configuracion.txt", "r")
        flujo.close()
    except FileNotFoundError:
        print("--- Comprobando configuración ---")
        print("Aviso: El fichero de configuración no existe.")
        
def guardar_numero_registros():
    datos = bytes([3])
    
    flujo_salida = open(NOMBRE_FICHERO_CONTADOR, "wb")
    flujo_salida.write(datos)
    flujo_salida.close()

    flujo_entrada = open(NOMBRE_FICHERO_CONTADOR, "rb")
    leido = flujo_entrada.read()
    flujo_entrada.close()
    
    print("--- Número de registros en binario ---")
    print(f"Total de temperaturas guardadas: {list(leido)[0]}")

def main():
    escribir_temperaturas()
    leer_temperaturas()
    saltar_primera_temperatura()
    comprobar_fichero_configuracion()
    guardar_numero_registros()

if __name__ == "__main__":
    main()

