'''
Estudiante:
Francisco de Jesus Melendez Simplina
Carnet:
000033484

Fecha de realizacion:
26/10/2022

Clase:
Algoritmos y Estructuras de Datos - Grupo: B124

Docente : 
César Marín López

Tema:
Buenas Practicas de Programación

Objetivo: Implementar las buenas prácticas de programación con programación modular 
para mejorar la calidad de los programas utilizando Python.

Modulos creados:
1)Menu
2)Agregar
3)Eliminar
4)Mostrar
5)Venta

'''

#Modulos del programa
import Menu 

def main():
   
    #Variables que usaremos en programa
    
    dineroLista=[] # Dinero total que se va ganando con cada venta 

    nomLista=[] # Almacena el nombre de cada producto

    precioLista=[] # Almacena el precio de cada producto

    cantLista=[] # Almacena la cantidad de productos que registra el usuario

    Menu.menuGeneral(dineroLista,nomLista,precioLista,cantLista) # Menu que ejecutara todos los modulos del programa
   

main()