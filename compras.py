import os 
import funcionalidades2.fecha_compra as fc
import funcionalidades2.elegir_productos as ep
def menuprincipal(op):
    os.system("cls")
    menuprincipalop = "1.fecha de la compra y nombre del provedor  \n2 i \n3 productos comprados \n4 volver   "
    if (op !=4):
        print ("menu de resgistro de compras")
        print (menuprincipalop)
        try:
            opcion = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menuprincipal(0)
        else: 
            match (opcion):
                case 1:
                    fc.fechacompra()
                case 2:
                    ep.menuprincipal(1)
                case 3:
                    print("2")
                case 4:
                    import prin
                    prin.menuprincipal