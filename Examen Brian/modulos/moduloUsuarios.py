import json
import utils.ctrlActions as ctrl
import modulos.menus as menu
import modulos.mensajes as msg
import modulos.funcionesDirectorio as fdir

def moduloUsuarios():
    while (True):
        ctrl.borrar_pantalla()
        print(menu.menuPrincipalUsuarios)
        opcionPrincipal = int(input('/: '))       
        match opcionPrincipal:
            case 1:
                ctrl.borrar_pantalla()
                print('Favor diligenciar los siguientes datos segun se indica: ')
                nombre = input('Nombre: ')
                numId = input('Numero de indentificacion (Solo numeros): ')
                direccion = input('Direccion: ')
                fechaInicio = input('Fecha ingreso del usuario: ')
                servicios = []
                while (True):                   
                    print('Si desea agregar servicios al usuario presione "1" si no presione "2"')
                    opcionServicios = int(input('/: '))
                    match opcionServicios:
                        case 1:  
                            print(msg.serviciosDisponibles)                  
                            print('De la lista anterior ingrese el servicio que desea agregar')
                            servicio = input('/: ')
                            servicios.append(servicio)
                            ctrl.pausar_pantalla()
                        case 2:
                            break
                        case _:
                            ctrl.borrar_pantalla()
                            print(msg.mensajeError)
                            ctrl.pausar_pantalla()
                nuevoUsuario = {
                        "nombre": nombre,
                        "numId": numId,
                        "direccion": direccion,
                        "fechaInicio": fechaInicio,
                        "serviciosActivos": servicios,
                        "serviciosRetirados": [],
                        "tipoCliente": "nuevo",
                        "interacciones": {
                            "quejas": "",
                            "sugerencias": "",
                            "preguntas": ""
                        }
                      }
                numeroUsuarios = fdir.contarUsuarios()
                nombreUsuario = "usuario" + str(numeroUsuarios)
                with open('./movistar.json', 'r+') as abrir:
                    base = json.load(abrir)
                    base['usuarios'][nombreUsuario] = nuevoUsuario
                    abrir.seek(0)
                    json.dump(base, abrir, indent=4)          
            case 2:
                ctrl.borrar_pantalla()
                print('Favor ingresar el numero de identificacion (Solo numeros) del ususario que desea visualizar la informacion: ')
                iD = input('/: ')
                base = fdir.abrirBase()
                for nameUsuario, dirUsuario in base['usuarios'].items():
                    if dirUsuario["numId"] == iD:
                        print(f'nombre:{dirUsuario["nombre"]}\nIdentificacion:{dirUsuario["numId"]}\nDireccion:{dirUsuario["direccion"]}\nFecha De inicio:{dirUsuario["fechaInicio"]}\nServicios Adquiridos:{dirUsuario["servicios"]}\nTipo de Cliente:{dirUsuario["tipoCliente"]}\n\n')
                        print(f'Interacciones:\nQuejas:{dirUsuario["interacciones"]["quejas"]}\nSugerencias:{dirUsuario["interacciones"]["sugerencias"]}\nPreguntas:{dirUsuario["interacciones"]["preguntas"]}')
                        ctrl.pausar_pantalla()
            case 3:
                ctrl.borrar_pantalla()
                print('Favor ingresarl el numero de identificacion (Solo numeros) del ususario que desea Modificar la informacion: ')
                iD = input('/: ')
                base = fdir.abrirBase()
                for nameUsuario, dirUsuario in base['usuarios'].items():
                    if dirUsuario["numId"] == iD:
                        print(menu.menuModificarUsuarios)
                        opcionMod = int(input(':/ '))
                        match opcionMod:
                            case 1:
                                print('Favor ingresar Nuevo Nombre: ')
                                nombreNuevo = input('/: ')
                                dirUsuario['nombre'] = nombreNuevo
                                print('Favor ingresar Nuevo Numero de Identificacion: ')
                                nuevoId = input('/: ')
                                dirUsuario['numId'] = nuevoId
                                fdir.guardarBase(base)
                                print('Nuevo nombre ingresado e identificacion ingresada')
                                ctrl.pausar_pantalla()
                            case 2:
                                print('Favor ingresar la nueva direccion:')
                                nuveaDireccion = input('/: ')
                                dirUsuario['direccion'] = nuveaDireccion
                                fdir.guardarBase()
                                print('Nueva Direccion Ingresada')
                                ctrl.pausar_pantalla()
                            case 3:
                                print(msg.tiposUsuarios)
                                print(f'\nEl cliente incio servicios el: {dirUsuario["fechaInicio"]}')
                                print('Segun la tabla indicada y fecha de inicio ingrese el nuevo tipo de cliente: ')
                                nuevoTipo = input('/: ')
                                dirUsuario['tipoCliente'] = nuevoTipo
                                fdir.guardarBase(base)
                                print('Cambio de tipo de usuario ingresado correctamente')
                                ctrl.pausar_pantalla()
                            case 4:
                                pass
                            case 5:
                                break
                            case _:
                                ctrl.borrar_pantalla()
                                print(msg.mensajeError)
                                ctrl.pausar_pantalla()
            case 4:
                pass
            case 5:
                ctrl.pausar_pantalla()
            case _:
                ctrl.borrar_pantalla()
                print(msg.mensajeError)
                ctrl.pausar_pantalla()

