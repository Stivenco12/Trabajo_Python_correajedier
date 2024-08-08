import os 

def menuprincipal(op):
    os.system("cls")
    menuprincipalop = "1.fecha de la compra  \n2 informacion del proevedor \n3 productos comprados \n4 volver   "
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
                    print("hasta")
                case 2:
                    print("hasta")
                case 3:
                    print("2")
                case 4:
                    import prin
                    prin.menuprincipal