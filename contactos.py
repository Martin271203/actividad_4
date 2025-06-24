import re

# Lista para almacenar contactos
contactos = []

# Validar formato de correo electrónico
def es_correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

# Crear un nuevo contacto
def crear_contacto():
    nombre = input("Ingrese el nombre (máx 50 caracteres): ")[:50]
    telefono = input("Ingrese el teléfono (11 dígitos): ")
    
    if len(telefono) != 11 or not telefono.isdigit():
        print("Teléfono inválido. Debe tener exactamente 11 dígitos.")
        return
    
    direccion = input("Ingrese la dirección (máx 60 caracteres): ")[:60]
    correo = input("Ingrese el correo electrónico: ")
    
    if not es_correo_valido(correo):
        print("Correo electrónico inválido.")
        return

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "correo": correo
    }

    contactos.append(contacto)
    print(" Contacto agregado exitosamente.")

# Modificar un contacto
def modificar_contacto():
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print("Contacto encontrado. Ingrese los nuevos datos:")
            contacto["nombre"] = input("Nuevo nombre: ")[:50]
            nuevo_tel = input("Nuevo teléfono (11 dígitos): ")
            if len(nuevo_tel) != 11 or not nuevo_tel.isdigit():
                print("Teléfono inválido.")
                return
            contacto["telefono"] = nuevo_tel
            contacto["direccion"] = input("Nueva dirección: ")[:60]
            nuevo_correo = input("Nuevo correo electrónico: ")
            if not es_correo_valido(nuevo_correo):
                print("Correo inválido.")
                return
            contacto["correo"] = nuevo_correo
            print(" Contacto modificado.")
            return
    print(" Contacto no encontrado.")

# Eliminar un contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    for i, contacto in enumerate(contactos):
        if contacto["nombre"].lower() == nombre.lower():
            del contactos[i]
            print(" Contacto eliminado.")
            return
    print("Contacto no encontrado.")

# Listar todos los contactos
def listar_contactos():
    if not contactos:
        print("No hay contactos registrados.")
        return
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto}")

# Buscar contactos
def buscar_contactos():
    print("""
    1. Buscar por Nombre
    2. Buscar por Teléfono
    3. Buscar por Dirección
    4. Buscar por Correo
    """)
    opcion = input("Seleccione una opción de búsqueda: ")

    clave = input("Ingrese el valor a buscar: ").lower()
    encontrados = []

    for contacto in contactos:
        if opcion == "1" and clave in contacto["nombre"].lower():
            encontrados.append(contacto)
        elif opcion == "2" and clave in contacto["telefono"]:
            encontrados.append(contacto)
        elif opcion == "3" and clave in contacto["direccion"].lower():
            encontrados.append(contacto)
        elif opcion == "4" and clave in contacto["correo"].lower():
            encontrados.append(contacto)

    if encontrados:
        print("🔍 Contactos encontrados:")
        for c in encontrados:
            print(c)
    else:
        print("No se encontraron coincidencias.")

# Menú principal
def menu():
    while True:
        print("""
    ---> MENU SISTEMA DE GESTION DE CONTACTOS <---

        1. Crear Contacto
        2. Modificar Contacto
        3. Eliminar Contacto
        4. Listar Contactos
        5. Buscar Contactos
        6. Salir
        """)
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                crear_contacto()
            elif opcion == 2:
                modificar_contacto()
            elif opcion == 3:
                eliminar_contacto()
            elif opcion == 4:
                listar_contactos()
            elif opcion == 5:
                buscar_contactos()
            elif opcion == 6:
                print(" Hasta luego.")
                break
            else:
                print(" Opción inválida. Intente nuevamente.")
        except ValueError:
            print(" Ingrese un número válido.")

# Ejecutar el menú
menu()
