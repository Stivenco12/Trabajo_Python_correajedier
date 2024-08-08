import os 
import funcionalidades.info_cliente
import funcionalidades.infor_empleado
import funcionalidades.producto_vendidos
import funcionalidades.ventas_fecha

def menuprincipal(op):
    os.system("cls")
    menuprincipalop = "1. fecha de ventas \n2 informacion del cliente \n3 informacion del empleado \n4 productos vendidos \n5 volver   "
    if (op !=5):
        print ("menu de registro de ventas")
        print (menuprincipalop)
        try:
            opcion = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menuprincipal(0)
        else: 
            match (opcion):
                case 1:
                    print("hasta")
                case 2:
                    print("hasta")
                case 3:
                    print("1")
                case 4:
                    print("2")
                case 5:
                    import prin
                    prin.menuprincipal
