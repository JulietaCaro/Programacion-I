# Ingresar por teclado el nombre de una entidad o institución y generar la sigla correspondiente,
# tomando la inicial de cada palabra.

nombre = input("Ingrese el nombre: ")
lista = nombre.split()
sigla = ""
for letras in lista:
    sigla = sigla + letras[0]

sigla.upper()
print(f"Sigla de {nombre}: {sigla}")