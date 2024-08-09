import json
def panaderia(op):
    print (  "Pan de Bono: 700")
    print ("Pan de Queso: 800")   
    print ("Pan Cascarita: 500")   
    print("Pan de Yuca: 800")
    print("Calentano: 700")
    print("Rollito de Sal: 900")
    print("Pan Integral 700")
    print("Pan relleno de Arequipe: 1150")
    print("Pan con Salchicha: 1300")
    print("Pan recubierto de Chocolate: 1200")
    input ("nombra lo que quieres comprar = ")
    print ("añadido a la lista de productos")
    menuprincipal(1)

def pasteleria(op):
    bebidas: []
                "Coca-Cola": 3000,
        "Pepsi": 2900,
        "Red-Bull": 4000,
        "Gatorade": 3700,
        "Budweiser": 3200,
        "Hit": 2500,
        "Pony-Malta": 2300,
        "Sprite": 3200,
        "Monster": 3000,
        "Tropicana": 2400,
    
    bebidas















import os
def menuprincipal(op):
    os.system("cls")
    menuprincipalop = "n\1 padaneria \n2 pasteleria \n3 bebidas "
    if (op !=3):
        print ("elije que quieres comprar")
        print (menuprincipalop)
        try:
            opcion = int(input(":) "))
        except ValueError:
            print ("error en la opccion ingresada")
            menuprincipal(0)
        else: 
            match (opcion):
                case 1:
                    panaderia(1)
                case 2:
                    pasteleria(1)
                case 3:
                    print()