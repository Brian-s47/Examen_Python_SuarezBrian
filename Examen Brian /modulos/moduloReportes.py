import json
import utils.ctrlActions as ctrl
import modulos.menus as menu
import modulos.mensajes as msg
import modulos.funcionesDirectorio as fdir

def moduloReportes():
        while(True):
            ctrl.borrar_pantalla()
            print(menu.menuPrincipalReportes)
            opcionPrincipal = int(input('/: '))       
            match opcionPrincipal:
                case 1:  
                    ctrl.borrar_pantalla()
                    serviciosDis = fdir.validarServicios()
                    print(f'Servicios Disponibles {serviciosDis}')
                    print('Favor El servicio del cual desea generar el reporte: ')
                    servicio = input('/: ')
                    base = fdir.abrirBase()
                    for nameServicio, dirServicio in base['servicios'].items():
                        if dirServicio['nameServicio'] == servicio:
                            print(f'{'nameServicio'}:{dirServicio["nombre"]}\n')

                case 2: #Servicios mas popular 
                    pass
                case 3: #Cantidad de usuarios por servicio
                    pass
                case 4: #Volver al Menu Anterior 
                    ctrl.borrar_pantalla()
                    print(msg.mensajeSalida)
                    ctrl.pausar_pantalla()
                    break 
                case _:
                    ctrl.borrar_pantalla()
                    print(msg.mensajeError)
                    ctrl.pausar_pantalla()