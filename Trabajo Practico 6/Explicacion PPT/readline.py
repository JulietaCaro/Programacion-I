try:    
    arch = open("readline.txt")
except IOError:
    print("No se pudo abrir el archivo")
else:
    print("El archivo tiene",len(arch.readlines()),"registros")
finally:
    arch.close()
    print("Se cerro el archivo")