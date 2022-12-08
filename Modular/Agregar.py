'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
26/10/2022


Objetivo del modulo: Regista un producto en el programa, en donde se pedira su nombre, precio y la cantidad 
de productos que se va guardar en la ejecucion del programa

'''


import os


def AgregarProducto(dineroLista,nomLista,precioLista,cantLista):

    print("Producto #"+str(len(nomLista)+1))

    print("AGREGANDO PRODUCTOS A LA TIENDA")

    nomLista.append(input("Digite el nombre del articulo: ")) # Agrega el nombre de producto 

    precioLista.append(int(input("Digite el precio de producto: "))) # Agrega la cantidad de producto 

    cantLista.append(int(input("Digite la cantidad de productos: "))) # Agrega la cantidad de producto 

    

    return (dineroLista,nomLista,precioLista,cantLista)

