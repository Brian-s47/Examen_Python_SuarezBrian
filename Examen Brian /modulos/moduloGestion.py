import json
import utils.ctrlActions as ctrl
import modulos.menus as menu
import modulos.mensajes as msg
import modulos.funcionesDirectorio as fdir

def moduloGestionServicios():
    while(True):
        ctrl.borrar_pantalla()
        print(menu.menuPrincipalServicios)
        opcionPrincipal = int(input('/: '))       
        match opcionPrincipal:
            case 1: #Agregar
                ctrl.borrar_pantalla()
                serviciosDis = fdir.validarServicios()
                print(f'Servicios Disponibles {serviciosDis}')
                print('Ingrese el nombre del nuevo servicio')
                nombreNuevoSer = input(':/ ')
                print('Ingrese Las caracteristicas del nuevo servicio')
                caracteristicas = input(':/ ')
                print('Ingrese el precio del nuevo servicio')
                precio = input(':/ ')
                nuevoServicio ={
                "caracteristicas": caracteristicas,
                "precio": precio
                },
                with open('./movistar.json', 'r+') as abrir:
                    base = json.load(abrir)
                    base['servicios'][nombreNuevoSer] = nuevoServicio
                    abrir.seek(0)
                    json.dump(base, abrir, indent=4)
            case 2: #Modificar
                ctrl.borrar_pantalla()
                serviciosDis = fdir.validarServicios()
                print(f'Servicios Disponibles {serviciosDis}')
                print('Ingrese de la lista anterior el servicio que desea modificar (Tener en cuenta mayuzculas y minusculas)')
                servicioMod = input(':/ ')
                print(menu.menuModificarServicios)
                opcionServicios = int(input(':/ '))
                match opcionServicios:
                    case 1:
                        base = fdir.abrirBase()
                        for nombreservicio, dirServicio in base['servicios'].items():
                            if nombreservicio == servicioMod:
                                print('Ingrese las nuevas caracteristicas para el servicio:')
                                nuevaCaracteristicas = input('/: ')
                                dirServicio['caracteristicas'] = nuevaCaracteristicas
                                fdir.guardarBase(base)
                                print('Las modificaciones se realizacon correctamente')
                                ctrl.pausar_pantalla()
                    case 1:
                        base = fdir.abrirBase()
                        for nombreservicio, dirServicio in base['servicios'].items():
                            if nombreservicio == servicioMod:
                                print('Ingrese el nuevo precio para el servicio:')
                                nuevoPrecio = input('/: ')
                                dirServicio['precio'] = nuevoPrecio
                                fdir.guardarBase(base)
                                print('Las modificaciones se realizacon correctamente')
                                ctrl.pausar_pantalla()
            case 3: #Eliminar
                ctrl.borrar_pantalla()
            case 4: #Volver al Menu Anterior 
                ctrl.borrar_pantalla()
                break
            case _:
                ctrl.borrar_pantalla()
                print(msg.mensajeError)
                ctrl.pausar_pantalla()




