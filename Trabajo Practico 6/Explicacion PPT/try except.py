try:
    arch = open(r"notas.txt","w")
    print("Se creó el archivo")
    
except IOError:
    print("No se pudo crear el archivo")

finally:
    arch.close()
    print("Se cerró el archivo")