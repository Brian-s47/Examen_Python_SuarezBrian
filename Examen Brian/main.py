import utils.ctrlActions as ctrl
import modulos.mensajes as msg
import modulos.menus as menu
import modulos.moduloUsuarios as mdUsu
import modulos.moduloGestion as mdGes

if __name__ == '__main__':
    while(True):
        ctrl.borrar_pantalla()
        print(msg.mensajeInicial)
        print(menu.menuInicial)
        opcionPrincipal = int(input('/: '))
        match opcionPrincipal:
            case 1: #Gestion de usuario
                ctrl.borrar_pantalla()
                mdUsu.moduloUsuarios()
            case 2: #Gestion de Servicios
                ctrl.borrar_pantalla()
                mdGes.moduloGestionServicios()
            case 3: #Modulo de reportes
                pass
            case 4: #Salir del Programa
                ctrl.borrar_pantalla()
                print(msg.mensajeSalida)
                ctrl.pausar_pantalla()
                break
            case _:
                ctrl.borrar_pantalla()
                print(msg.mensajeError)
                ctrl.pausar_pantalla()



        
