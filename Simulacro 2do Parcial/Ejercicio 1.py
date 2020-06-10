# Se solicita leer el archivo de frases “frases.txt” y crear uno nuevo que contenga una palabra por registro, debe ser la palabra
# más larga pero sin considerar letras repetidas. Si alguna frase tiene más de una palabra más larga, es suficiente con guardar
# sólo una de ellas. No se permite cargar por completo el archivo de frases en memoria.
# Registro: “Bello es mejor que feo” Palabra más larga: mejor
# Resolver utilizando excepciones y creando al menos dos funciones. No se aceptan funciones que sólo cumplen una acción o
# instrucción, debe resolver correctametne un sub-problema.

#FUNCIONES
def limpiarPalabra(registro):
    '''Remplaza los simbolos .,¡!;¡¿? de un registro'''
    registro = registro.rstrip()
    registro = registro.lstrip()
    simbolos = [".",",","¡","!",";","¿","?"]
    for simbolo in simbolos:
        registro = registro.replace(simbolo,"")
    return registro  
    
def verificarLetrasRepetidas(palabra):
    '''Verifica que una palabra no contenga letras repetidas, retorna True o False'''
    palabra = palabra.lower()
    nueva = ""
    veri = False
    for letra in palabra:
        if letra not in nueva:
            nueva += letra
    if palabra == nueva:
        veri = True
    return veri
    
def palabraMasLarga():
    '''Abre un archivo con una frase y crea otro con las palabras mas largas sin letras repetidas'''
    try:
        archivo = open("frases.txt","r")
        arch = open("frasesLarga.txt","w")
    except IOError:
        print("Se produjo un error al abrir/crear el archivo")
    else:
        for registro in archivo:
            maximo = ""
            registro = registro.rstrip()
            listaPal = registro.split()
            for palabra in listaPal:
                palabra = limpiarPalabra(palabra)
                if palabra.isalpha():
                    if len(palabra)>len(maximo):
                        if verificarLetrasRepetidas(palabra):
                            maximo = palabra
                            
            arch.write(maximo+"\n")               
    finally:
        archivo.close()
        arch.close()
        
palabraMasLarga()