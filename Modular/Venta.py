'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
26/10/2022


Objetivo del modulo: Realiza la venta de productos que se encuentran registrados en el programa
tambien hace una comprobacion si hay productos registrados y si el usuario quiere llevar una
productos cierta cantidad de productos para que solo se venda y se mantenga el producto en la 
ejecucion del programa

'''

#Librerias de python
import os

def RealizarVenta(dineroLista,nomLista,precioLista,cantLista):
    
    if(nomLista):   # Comprueba si no hay productos registrados

        print("PRODUCTOS DISPONIBLES")
        #Imprime todos los productos registrados
        for x in range(0,len(nomLista)):
            print()
            print("Producto#"+str(x+1)+":")
            print("NOMBRE:")
            print(nomLista[x])
            print("PRECIO:")
            print(precioLista[x])
            print("Cantidad:")
            print(cantLista[x])


            # Pedir al usuario el producto a comprar
        opcion=int(input("\nDigite el numero del producto a comprar: "))
        print()

            # Comprobar si el producto a vender es correcto
        if(opcion<=len(nomLista)):

            print("Producto a comprar: "    +   str(nomLista[opcion-1]))

            print("Precio: "    +   str(precioLista[opcion-1]))

            print("Producto a comprar: "    +   str(cantLista[opcion-1]))

            cantidad=int(input("Digite la cantidad de productos a comprar: "))
            os.system("cls")
                    
            # Comprobar si se encuentra la cantidad correcta del producto a eliminar es correcto
            if(cantidad==cantLista[opcion-1]):# Si se quiere llevar todos los productos

                aux=cantLista[opcion-1]*precioLista[opcion-1] # Suma todas los unidades de los productos registrados por el precio

                dineroLista.append(int(aux)) # auciliar para mantener la ganancias de estos productos

                print("El total de la compra es: "+str(aux))
                print("Se elimino el producto, por que adquieron todas las unidades")

                #Elimina el producto, por que el usuario se lleva todas las unidades del inventario
                nomLista.pop(opcion-1)
                precioLista.pop(opcion-1)
                cantLista.pop(opcion-1)
                os.system("Pause")

            elif(cantidad<cantLista[opcion-1]): # Si se quiere llevar una cierta cantidad de productos

                aux=cantidad*precioLista[opcion-1] # Sumar la cantidad de produtos que compro el usaurio con su precio

                dineroLista.append(int(aux)) # auciliar para mantener la ganancias de estos productos

                cantLista[opcion-1]=cantLista[opcion-1]-cantidad # Eliminar la cantidad total de productos antes guaradados con la cantidad de productos que desea el cliente
                        
                print("El total de la compra es: "+str(aux)) # Muestra el dinero total que se gana con el produto
                os.system("Pause")

            else:# Comprobar si la cantidad a comprar es correcto
                print()
                print("DIGITE LA CANTIDAD DE PRODUCTOS CORRECTO")
                os.system("Pause")

        else: # Comprueba si hay productos registrados
            print()
            print("NO SE ENCUENTRAN NINGUN PRODUCTO REGISTRADO")
            os.system("Pause")

    else: # Comprueba si hay productos registrados
        print()
        print("NO SE ENCUENTRAN NINGUN PRODUCTO REGISTRADO")
        os.system("Pause")    

    return (dineroLista,nomLista,precioLista,cantLista)