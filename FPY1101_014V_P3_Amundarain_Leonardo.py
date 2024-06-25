# ¡¡Autos Seguros Leonardo!!

# Definir funciones para registrar

def grabar_vehiculo():
    tipo_vehiculo = input("Ingrese el tipo de vehiculo (auto, camioneta, camion o moto): ")
    marca = input("Ingrese la marca del vehiculo: ")
    precio = float(input("Ingrese el precio del vehiculo (mayor a $5.000.000): "))
    tiene_multa = input("¿Tiene multa? (SI/NO): ").lower()

    if tiene_multa == "si":
        monto_multa = float(input("Ingrese el monto de la multa: "))
        fecha_multa = input("Ingrese la fecha de la multa (YYYY-MM-DD): ")
    else:
        monto_multa = None
        fecha_multa = None

    nombre_dueno = input("Ingrese el nombre del dueño: ")
    patente = input("Ingrese la patente del vehículo (4 consonantes sin M, N, Ñ): ")

    while not patente.isalpha() or len(patente) != 4 or any(letra in "mnñ" for letra in patente.lower()):
        patente = input("Patente invalida. Ingrese nuevamente (4 consonantes sin M, N, Ñ): ")

    vehiculo_registrado = {
        "tipo": tipo_vehiculo,
        "marca": marca,
        "precio": precio,
        "tiene_multa": tiene_multa,
        "monto_multa": monto_multa,
        "fecha_multa": fecha_multa,
        "nombre_dueno": nombre_dueno,
        "patente": patente
    }

# Donde empiezo a registras o agregar
    vehiculos_registrados.append(vehiculo_registrado)  
    print(f"Vehiculo registrado: \nTipo: {tipo_vehiculo}\nMarca: {marca}\nPatente: {patente}\nValor: ${precio:,.2f}\nMulta: {monto_multa:.2f} Fecha: {fecha_multa}")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehiculo: ")

    for vehiculo in vehiculos_registrados:
        if vehiculo["patente"].lower() == patente.lower():
            print(f"Vehiculo encontrado: {vehiculo}")
            return

    print(f"Vehiculo con patente {patente} no encontrado.")

def imprimir_certificado():

    patente = input("Ingrese la patente del vehículo para el certificado: ")

    for vehiculo in vehiculos_registrados:
        
        if vehiculo["patente"].lower() == patente.lower():
            

            print(f"Generando certificado para vehículo: {vehiculo['marca']} {vehiculo['patente']}")
           
            return

    print(f"Vehículo con patente {patente} no encontrado. No se puede generar certificado.")

def salir():
    print("Saliendo del programa. ¡Gracias por usar Autos Seguros!")
    exit()

# lista para ya los registrados
vehiculos_registrados = []

# Menu principal 

while True:
    print("\n\nMenu Principal:")
    print("1. Registrar vehiculo")
    print("2. Buscar vehículo")
    print("3. Imprimir certificado")
    print("4. Salir")

    opcion = input("Ingrese la opcion deseada: ")

    if opcion == "1":
        grabar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        imprimir_certificado()
    elif opcion == "4":
        salir()
    else:
        print("Opcion invalida. Intente nuevamente por favor.")
