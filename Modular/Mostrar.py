'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
26/10/2022


Objetivo del modulo: Muestra todos los productos registrados y el total de ganacias que se han hecho
en la ejecucion de venta de productos 

'''

#Librerias de python
import os

def MostrarDatos(dineroLista,nomLista,precioLista,cantLista): #Modulo que se encarga de imprimir los datos que se encuantran en el programa
    
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
    
    
    return (dineroLista,nomLista,precioLista,cantLista)