'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
26/10/2022


Objetivo del modulo:Es un menu para poder interactuar con el usuario de manera que se
repita hasta que el usuario digite el numero '6' para finalizar el programa

'''

#Librerias de python
import sys
import os

#Modulos del programa
import Agregar
import Venta
import Eliminar
import Mostrar


def menuGeneral(dineroLista,nomLista,precioLista,cantLista):
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
            Agregar.AgregarProducto(dineroLista,nomLista,precioLista,cantLista)
           
            

        elif(opc==2):#Realizar su venta
            os.system("cls")
            Venta.RealizarVenta(dineroLista,nomLista,precioLista,cantLista)
            

        elif(opc==3):#Borrar un producto
            os.system("cls")
            Eliminar.EliminarUnProducto(dineroLista,nomLista,precioLista,cantLista)
            

        elif(opc==4):#Borrar todos los productos
            os.system("cls")
            Eliminar.EliminarTodo(dineroLista,nomLista,precioLista,cantLista)


        elif(opc==5):#Mostrar productos registrados 
            os.system("cls")
            Mostrar.MostrarDatos(dineroLista,nomLista,precioLista,cantLista)
            

        elif(opc==6):#Salir del programa
            os.system("cls")
            print("Gracias por usar este programa\n")
            print("Clase: Algoritmos y estructuras de datos\n")
            print("Autor: Francisco De Jesús Melendez Simplina\n")
            print("Numero de carnet: 000033484\n")
            print("Universidad Centroamericana UCA\n")
            sys.exit()
            

        else: # por si se da uso del programa
            print("Digite una opcion correcta")
            os.system("Pause")
