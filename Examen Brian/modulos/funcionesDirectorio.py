import json

def abrirBase():
        with open('./movistar.json', 'r') as abrir:
            base = json.load(abrir)
        return (base)

def guardarBase (base):
    with open('./movistar.json', 'w') as abrir:
        json.dump(base, abrir, indent=4)

def contarUsuarios ():
    base = abrirBase()
    cantidadUsuarios= len(base['usuarios'])
    return (cantidadUsuarios)

def validarServicios():
    base = abrirBase()
    servicios = []
    for nombreservicio, dirServicio in base['servicios'].items():
        servicios.append(nombreservicio) 
    return(servicios)
    
    