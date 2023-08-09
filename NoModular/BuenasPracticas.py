'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
9/10/2022

Clase:
Algoritmos y Estructuras de Datos - Grupo: B124

Docente : 
César Marín López

Tema:
Buenas Practicas de Programación

Objetivo: Implementar las buenas prácticas de programación con programación no modular 
para mejorar la calidad de los programas utilizando Python, realizando un programa que administre
una tienda, en donde se pueda:

1)Navegar por el Menu
2)Agregar Productos
3)Eliminar Productos
4)Mostrar Productos
5)Venta Productos

'''


import os

nomLista=[] # Almacena el nombre de cada producto
precioLista=[] # Almacena el precio de cada producto
cantLista=[] # Almacena la cantidad de productos que registra el usuario
dineroLista=[] # Dinero total que se va ganando con cada venta 



def main():
    opc=0 # Elegir una opcion en el menú

    while(opc!=6): # Se repita el menu hasta que el usuario desee salir

        os.system("cls")
        print("MENU DE OPCIONES")
        print("1)Agregar un producto")
        print("2)Realizar su venta")
        print("3)Borrar un producto")
        print("4)Borrar todos los productos")
        print("5)Mostrar de información")
        print("6)salir")
        opc=int(input("DIGITE UN OPCION: "))

        if(opc==1):#Agregar un producto

            os.system("cls")
            print("Producto #"+str(len(nomLista)+1))

            print("AGREGANDO PRODUCTOS A LA TIENDA")

            nomLista.append(input("Digite el nombre del articulo: ")) # Agrega el nombre de producto 

            precioLista.append(int(input("Digite el precio de producto: "))) # Agrega la cantidad de producto 

            cantLista.append(int(input("Digite la cantidad de productos: "))) # Agrega la cantidad de producto 
            

        elif(opc==2):#Realizar su venta
            os.system("cls")

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

                    print("Cantidad de productos disponibles: "    +   str(cantLista[opcion-1]))

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
                        print("DIGITE LA CANTIDAD DE PRODUCTOS CORRECTA")
                        os.system("Pause")

                else: # Comprueba si hay productos registrados
                    print()
                    print("NO SE ENCUENTRAN NINGUN PRODUCTO REGISTRADO")
                    os.system("Pause")

            else: # Comprueba si hay productos registrados
                print()
                print("NO SE ENCUENTRAN NINGUN PRODUCTO REGISTRADO")
                os.system("Pause")    

                

        elif(opc==3):#Borrar un producto
            os.system("cls")

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
                    print("Se ha eliminado el producto "+str(nomLista[producto-1])+" en los elementos de la lista")
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

        elif(opc==4):#Borrar todos los productos
            os.system("cls")

            if(nomLista):# Comprueba si no hay productos 

                nomLista.clear() # Borra todos los productos registrados

                cantLista.clear() # Borra todos los productos registrados

                precioLista.clear() # Borra todos los productos registrados

                print("Se han eliminado todos los elementos de la lista")

                os.system("Pause")

            else: # Comprueba si hay productos registrados
                print()
                print("NO SE ENCUENTRAN NINGUN PRODUCTO REGISTRADO")
                os.system("Pause")


        elif(opc==5):#Mostrar productos registrados
            os.system("cls")

            if(len(nomLista)==0 and len(dineroLista)==0): #Comprueba si hay productos registrados y  no hay
                print("NO SE ENCUENTRA NINGUN PRODUCTO REGISTRADO\nSIN VENTAS")
                os.system("Pause")

            elif(len(nomLista)==0 and  len(dineroLista)>0): # Comprueba si no productos registrados pero hay un dinero ganado   
                print("SIN PRODUCTOS")
                print("TOTAL DE VENTAS:"+str(sum(dineroLista)))  
                os.system("Pause")           

            elif(len(nomLista)>0 or  len(dineroLista)>0): # Comprueba si hay productos registrados y tambien un dinero ganado   

                #Imprime todos los productos registrados en la ejecucion del programa
                for i in range(0,len(nomLista)):
                    print("Producto #"+str(i+1))
                    print("NOMBRE DEL PRODUCTO: "+str(nomLista[i]))
                    print("PRECIO DE PRODUCTO: "+str(precioLista[i]))
                    print("CANTIDAD DE PRODUCTO: "+str(cantLista[i]))
                    print()

                print("TOTAL DE VENTAS:"+str(sum(dineroLista))) # Total de ventas que se han realizado en la ejecucion del programa
                os.system("Pause")

        elif(opc==6):#Salir del programa

            os.system("cls")

            print("Gracias por usar este programa\n")
            print("Clase: Algoritmos y estructuras de datos\n")
            print("Autor: Francisco De Jesús Melendez Simplina\n")
            print("Numero de carnet: 000033484\n")
            print("Universidad Centroamericana UCA\n")

        else: # por si se da uso del programa
            print("Digite una opcion correcta")
            os.system("Pause")



main()