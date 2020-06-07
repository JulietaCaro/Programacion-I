# Desarrollar una función para contar cuantas vocales posee una cadena.

def contarVocales(cad):
    if len(cad) == 0:
        return  0
    else:
        letra = cad[0].lower()
        if letra in ("a","e","i","o","u"):
            return 1 + contarVocales(cad[1:])
        else:
            return 0 + contarVocales(cad[1:])

print(f"Cant vocales {contarVocales('Hola como estas? todo bien?')}")