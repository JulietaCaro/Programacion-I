# 2. Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
# misma tiene 80 columnas.

# FUNCIONE
def main():
    cad = input("Ingrese una frase: ")
    cad1 = cad.center(80, " ")
    print(cad1)

#Programa principal
main()