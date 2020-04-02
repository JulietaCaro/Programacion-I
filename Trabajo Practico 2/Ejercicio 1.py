'''1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar
su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será
un número al azar de dos dígitos.
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a
eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].'''

from random import randint
import funciones
#FUNCIONES
'''def imprimirLista(lista):
    'Imprimir lista sin indice'
    for numero in lista:
        print(numero, end=" ")
    print()

def validarPositivo():
    numero = int(input("Ingrese un numero positivo: "))
    while numero < 1:
        numero = int(input("Reingrese un numero positivo: "))
    return numero'''
        
def funcionA(cantidad):
    'lista con numeros al azar de cuatro digitos'
    lista = []
    for i in range(cantidad):
        lista.append(randint(1000,9999))
    return lista

def funcionB(lista):
    'Suma todos los elementos de la lista'
    return sum(lista)

def funcionC(lista, valor):
    'Eliminar valor pasado por parametro'
    while valor in lista:
        lista.remove(valor)

def funcionD(lista):
    'Verificar si la lista es capicua'
    primeraParte = len(lista)-1
    segundaParte = primeraParte // 2
    capicua = False
    for i in range(0, segundaParte):
        if lista[i] == primeraParte:
            capicua = True
        else:
            capicua = False
        primeraParte = primeraParte - 1
    return capicua
        
def main():
    'Programa principal'
    cantElem = randint(10,99)
    lista = funcionA(cantElem)
    funciones.imprimirLista(lista)
    print("Suma de la lista: ",funcionB(lista))
    num = funciones.pedirYValidarNum()
    funcionC(lista,num)
    funciones.imprimirLista(lista)
    if funcionD(lista):
        print("Es capicua")
    else:
        print("No es capicua")
    
#PROGRAM PRINCIPAL
main()