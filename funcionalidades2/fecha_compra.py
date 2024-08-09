import json
def fechacompra():
    fecha = input("ingrese la fecha de compra = ")
    fecha
    nombre = input("ingrese la informacion del proevedor = (nombre y apellido)")
    nombre
    data = {
        'fecha' : fecha,
        'nombre' : nombre,
    }
    with open('guardar_informacion.json', 'w') as jf: 
        json.dump(data, jf, ensure_ascii=False, indent=2)
        
    import compras
    compras.menuprincipal(1)

