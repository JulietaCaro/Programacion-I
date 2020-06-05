# Los campos están separados por el signo #.
# Pérez Juan#20080211#Corrientes 348
def formatoNombreYApellido(nombre, apell):
    nombre = nombre.lower()
    apell = apell.lower()
    nombre = nombre.rstrip()
    nombre = nombre.lstrip()
    apell = apell.rstrip()
    apell = apell.lstrip()
    cad = apell+" "+nombre
    cad = cad.title()
    return cad

def pedirDNI():
    while True:
        try:
            dni = int(input("Ingrese su DNI: "))
            while len(str(dni))>8 or len(str(dni))<7:
                dni = int(input("Error, reingrese su DNI: "))
            break
        except ValueError:
            print("Se esperaba el ingreso de un numero")
    return dni

def pedirDomicilio():
    domic = input("Ingrese su domicilio: ")
    dom = domic.replace(" ","")
    while not dom.isalnum():
        domic = input("Error, reingrese su domicilio: ")
    return domic.title()

def escribirArchivo():
    try:
        archivo = open("CamposConSeparador.txt","w")
    except IOError:
        print("Error al crear el archivo")
    else:
        while True:
            apellido = input("Ingrese su apellido: ")
            if apellido == "":
                break
            nombre = input("Ingrese su nombre: ")
            apynom = formatoNombreYApellido(nombre,apellido)
            dni = pedirDNI()
            domicilio = pedirDomicilio()
            cad = f"{apynom}#{dni}#{domicilio}"
            archivo.write(cad+"\n")
    finally:
        archivo.close()

def leerArchivo():
    try:
        archivo = open("CamposConSeparador.txt","r")
    except IOError:
        print("Error al abrir el archivo")
    else:
        while True:
            registro = archivo.readline()
            if registro == "":
                break
            registro = registro.rstrip()
            lista = registro.split("#")
            apynom,dni,dom = lista
            print(apynom,dni,dom)
    finally:
        archivo.close()

escribirArchivo()
leerArchivo()        
            
