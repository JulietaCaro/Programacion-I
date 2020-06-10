# Desarrollar un programa principal para ingresar dos palabras por teclado e informar las letras poseen en común. Permitir
# ingresar varias veces dos palabras hasta que la primera que se ingrese sea vacía. Para el ingreso de palabras, generar y
# gestionar una excepcion si se ingresan numeros, espacios o símbolos, aceptar solo palabras con caracteres alfabeticos.

def main():
    while True:
        try:
            pal1 = input("Ingrese una palabra: ")
            if pal1 == "":
                break
            assert(pal1.isalpha()), "Error al ingresar la palabra, debe tener caracteres alfabéticos"
            pal2 = input("Ingrese otra palabra: ")
            assert(pal2.isalpha()), "Error al ingresar la palabra, debe tener caracteres alfabéticos"
            
            con1 = set(pal1)
            con2 = set(pal2)
            comun = con1&con2
            print("Palabras en comun: ")
            for letra in comun:
                print(letra,end=" ")
            print()
            
        except AssertionError as mensaje:
            print(mensaje)
        
main()