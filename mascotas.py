def MostrarMenu():
    print("\n=== SISTEMA VETERINARIO ANIMALIA ===")
    print("1. Registrar mascota")
    print("2. Buscar mascota por chip")
    print("3. Dar de baja (Eliminar)")
    print("4. Evaluar estado nutricional")
    print("5. Mostrar listado de pacientes")
    print("6. Salir")
def OpcionMenu():
    while True:
        try:
            op_menu = int(input("Ingrese la opcion que desea ejecutar: "))
            if op_menu <= 0 and op_menu > 6:
                print("Error ingrese una opcion valida (1-6)")
            return op_menu
        except ValueError:
            print("Error: debe ingresar un numero entero mayor a 0")
def ValidarChip(ChipValido):
    if ChipValido.strip() == "":
        return False
    else:
        return True
def ValidarEdad(EdadValida):
    try:
        EdadValida = int(EdadValida)
        if EdadValida >= 0:
            return True
        else:
            return False
    except ValueError:
        print("Error: debe ingresar un numero entero positivo")
def ValidarPeso(PesoValido):
    try:
        PesoValido = float(PesoValido)
        if PesoValido <= 0:
            return False
        else:
            return True
    except ValueError:
        print("Error: Debe ingresar un numero entero positivo mayor a 0")
def AgregarMascota(lista):
    chip = input("Ingrese el chip de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ") 
    peso = input("Ingrese el peso de la mascota: ")
    Chipcorrecto = ValidarChip(chip)
    Edadcorrecta = ValidarEdad(edad)
    Pesocorrecto = ValidarPeso(peso)
    if Chipcorrecto == True and Edadcorrecta == True and Pesocorrecto == True:
        Mascota = {
            "Chip": chip,
            "Edad": int(edad),
            "Peso": float(peso),
            "Dieta_especial": False
        }
        lista.append(Mascota)
    else:
        print("Error de validacion no se pudo registrar la mascota.")
def Buscarchip(lista, chip):
    for indice, Mascota in enumerate(lista):
        if Mascota["Chip"] == chip:
            return indice
    return -1
listaMascotas = []
while True:
    MostrarMenu()
    opcion = OpcionMenu()
    match opcion:
        case 1:
            AgregarMascota(listaMascotas)
        case 2:
            encontrarchip = input("\nIngrese el chip que desea buscar: ")
            posicion = Buscarchip(listaMascotas, encontrarchip)
            if posicion != -1:
                print(f"Mascota encontrada en la posicion: {posicion}")
                chipencontrado = listaMascotas[posicion]
                print(f"Chip: {chipencontrado['Chip']}")
                print(f"Edad: {chipencontrado['Edad']}")
                print(f"Peso: {chipencontrado['Peso']}")
            else:
                print("La mascota no se encuentra registrada.")