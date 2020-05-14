# Pedir el pais y decir si es arg o no
pais = input("Ingrese el pais donde nacio: ")
minPais = pais.capitalize()
if minPais == "Argentina":
    print("Usted es argentino")
else:
    print("Usted no es argentino")