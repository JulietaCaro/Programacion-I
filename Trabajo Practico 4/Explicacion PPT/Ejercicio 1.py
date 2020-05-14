# Leer una frase, invertir las palabras que contiene (sin invertir las letras) y
# mostrar la cadena invertida por pantalla
cad = input("Ingrese una frase: ")
lista = cad.split()
lista.reverse()
cad =' '.join(lista)
print(f"Cadena invertida: {cad}")
if cad.isalpha():
    print("La cadena es toda alfabética")
else:
    print("La cadena no es toda alfabética")
if cad.islower():
    print("Todos los elementos están en minusculas")
elif cad.isupper():
    print("Todos los elementos están en mayusculas")
else:
    print("Los elementos estan en mayusculas y minusculas")