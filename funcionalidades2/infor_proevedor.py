import json
def fechacompra():
    nombre = input("ingrese la informacion del proevedor = (nombre y apellido)")

    nombre
    data = {
    
        'nombre' : nombre
    }
    with open('guardar_informacion.json', 'w') as jf: 
        json.dump(data, jf, ensure_ascii=False, indent=2)
        
    import compras
    compras.menuprincipal(1)
