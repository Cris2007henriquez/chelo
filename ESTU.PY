capacidad_maxima = 40 
cupos_dispo = 40
cliente_normal = 0
cliente_suscriptor = 0
tarifa_hora = 1200
descuento = 0
ganancias = 0
espacios_usados = 0


while True:
    print("=== MENÚ DE CONTROL SMARTPARK ===")
    print("1. Consultar cupos disponibles")
    print("2. Ingresar vehículo")
    print("3. Retirar vehículo")
    print("4. Reporte de ganancias del día")
    print("5. Salir del sistema")

    opcion_menu = int(input("ingrese la accion que desea ejecutar: "))

    match opcion_menu :
        case 1:
            print(f"la cantidad de cupos disponibles es de {cupos_dispo}")

        case 2:
            while True:
                try:
                  horas = int(input("ingrese la cantidad de horas de su estadia: "))
                  if horas > 0:
                      cupos_dispo = cupos_dispo - 1
                      espacios_usados = cupos_dispo + 1
                      break
                  elif horas <= 0:
                      print("error debe ser un numero entero positivo mayor a 0")
                except Exception:
                    print("error debe ser un numero entero positivo")

            tipo_cliente = int(input("ingrese su tipo de cliente(normal = 1 , scriptor = 2): "))
            if tipo_cliente == 2:
                descuento = descuento + 0.15
                tarifa_hora = tarifa_hora - (tarifa_hora * descuento)
            else:
                descuento = 0

            ganancias = tarifa_hora * espacios_usados

        case 3:
            if cupos_dispo == 40:
                print("error no hay ningun vehiculo estacionado")
            else:
                retirar = int(input("ingrese cuantos vehiculos desea retirar: "))
                if retirar < 40:
                    cupos_dispo = cupos_dispo + retirar
                
        case 4:
            print(f"las ganancias totales del dia fueron {ganancias}")

        case 5:
            print("Cierre de caja exitoso. ¡Hasta mañana!")

            break