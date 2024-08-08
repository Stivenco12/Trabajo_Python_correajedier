import os 
import ventas
import compras
def menuprincipal(op):
    os.system("cls")
    menuprincipalop = "1.ventas \n2 compras   "
    if (op !=2):
        print ("menu de PanCamp")
        print (menuprincipalop)
        try:
            opcion = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menuprincipal(0)
        else: 
            match (opcion):
                case 1:
                    ventas.menuprincipal(1)
                case 2:
                    compras.menuprincipal(1)
menuprincipal(1)