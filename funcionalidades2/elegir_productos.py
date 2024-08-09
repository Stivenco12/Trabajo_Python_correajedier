import os
import json
from os import system
import sys 
import json
from enum import Enum
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

    print ("añadido a la lista de productos")
    pausar_pantalla
    menuprincipal(1)

def pasteleria(op):  
    print (  "Pastel de Vainilla: 5000")
    print ("Pastel de Chocolate: 5500")   
    print ("Pastel de bodas: 10000 ")   
    print( "Glaseado de Vainilla: 3000")
    print("Glaseado de Chocolate: 3500 ")
    print("Rollito de Sal: 900")
    print("Pastel de Arequipe: 5700 ")
    print("Pastel de Oreo: 7000 ")
    print("Postre de Limon: 4300, ")
    print("Postre de Vainilla: 4000," )
    
    print ("añadido a la lista de productos")
    pausar_pantalla
    menuprincipal(1)

def bebidas(op):
    print("Coca-Cola: 3000")
    print("Pepsi: 2900")
    print("Red-Bull: 4000")
    print("Gatorade: 3700")
    print("Budweiser: 3200")
    print("Hit: 2500")
    print("Pony-Malta: 2300")
    print("Sprite: 3200")
    print("Monster: 3000")
    print("Tropicana: 2400")
    print("-Promociones-: Algunas promociones de la sección de Bebidas")
    print("1 Pan con Salchicha y 1 Pony Malta: 3000")
    print("1 Postre de Oreo y 1 Budweiser: 9000")
    
    print ("añadido a la lista de productos")
    pausar_pantalla
    menuprincipal(1)

def apartado_promocione(op):
    print("6 Panes Integrales: 4000")
    print("5 Panes recubiertos de Chocolate: 5500")
    print("3 Pasteles de Vainilla: 13000")
    print("4 Postres de Oreo: 25000")
    print("1 Pan con Salchicha y 1 Pony Malta: 3000")
    print("1 Postre de Oreo y 1 Budweiser: 9000")

    print ("añadido a la lista de productos")
    pausar_pantalla
    menuprincipal(1)

def pausar_pantalla():
    if sys.platform == "Linux" or sys.platform == "darwin":
        x=input("presione una tecla para continuar")
    else:
        system("pause")

def menuprincipal(op):
    os.system("cls")
    menuprincipalop = "n\1 padaneria \n2 pasteleria \n3 bebidas "
    if (op !=4):
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
                    
                    panaderia_producto=input ("nombra lo que quieres comprar = ")
                case 2:
                    pasteleria(1)
                    pausar_pantalla
                    pasteleria_produc=input ("nombra lo que quieres comprar = ")
                case 3:
                    bebidas(1)
                    pausar_pantalla
                    bebidas_produc = input ( "nombra lo que quieres comprar = " )
                case 4:
                    apartado_promocione(1)
                    pausar_pantalla
                    promocies_produc = input ( "nombra lo que quieres comprar = " )

    
    data1 = {
        'produc1' : panaderia_producto,
        'produc2' : pasteleria_produc,
        'produc3' : bebidas_produc,
        'produc4' : promocies_produc,
    }
    with open('guardar_informacion.json', 'w') as jf: 
        json.dump(data1, jf, ensure_ascii=False, indent=2)