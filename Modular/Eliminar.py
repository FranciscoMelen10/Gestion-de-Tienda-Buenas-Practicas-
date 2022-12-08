'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
26/10/2022


Objetivo del modulo: Eliminar productos de la tien, ya se uno en especifico
o eliminar todos los productos registrados

'''

import os

def EliminarUnProducto(dineroLista,nomLista,precioLista,cantLista):
    
    if(nomLista):# Comprueba si no hay productos registrados

        print("PRODUCTOS REGISTRADOS")

        #Imprime todos los productos registrados
        for x in range(0,len(nomLista)):
            print("Producto#"+str(x+1)+":")
            print("NOMBRE:")
            print(nomLista[x])
            print("PRECIO:")
            print(precioLista[x])
            print("Cantidad:")
            print(cantLista[x])
            print()
            # Mostrar los productos registrados en el programa

        producto=int(input("Digite el numero del producto que desea eliminar: ")) # Seleccionar el producto a eliminar

        if(producto<=len(nomLista)): # comprueba si el usuario usa de manera correcta el programa para eliminar
            os.system("cls")
            print("Se ha eliminado el producto "+str(nomLista[producto-1])+" los elementos de la lista")
            nomLista.pop(producto-1)
            precioLista.pop(producto-1)
            cantLista.pop(producto-1)
            os.system("Pause")

        else: # comprueba si el usuario usa de manera incorrecta el programa para eliminar
            print()
            print("DIGITE UN NUMERO CORRECTO")
            os.system("Pause")

    else: # Comprueba si hay productos registrados
        print()
        print("NO SE ENCUENTRAN NINGUN PRODUCTO REGISTRADO")
        os.system("Pause")


    return (dineroLista,nomLista,precioLista,cantLista)




def EliminarTodo(dineroLista,nomLista,precioLista,cantLista):

    nomLista.clear() # Borra todos los productos registrados

    cantLista.clear() # Borra todos los productos registrados

    precioLista.clear() # Borra todos los productos registrados

    print("Se han eliminado todos los elementos de la lista")

    os.system("Pause")

    return (dineroLista,nomLista,precioLista,cantLista)
