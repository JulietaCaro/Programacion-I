# 1.Desarrollar un programa para eliminar todos los comentarios de un programa  escrito en lenguaje Python. Tener en cuenta
# que los comentarios comienzan con el signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y
# que también se considera comentario a las cadenas de documentación (docstrings).

def main():
    try:
        comentarios = open("EjConComentarios.txt","r")
        sinComent = open("EjSinComentarios.txt","w")
    except IOError:
        print("Ocurrio un problema al abrir/crear el archivo")
    else:
        while True:
            registro = comentarios.readline()
            if registro == "":
                break
            if registro[0] != "#" and registro[0] != '"' and registro[0] != "'":
                if registro.count("#")!= 0:
                    regis = registro.split("#")
                    sinComent.write(regis[0]+"\n")
                elif registro.count("'") != 0:
                    regis = registro.split("'")
                    sinComent.write(regis[0]+"\n")
                elif registro.count('"')!= 0:
                    regis = registro.split('"')
                    sinComent = write(regis[0]+"\n")
                else:
                    sinComent.write(registro)
    finally:
        comentarios.close()
        sinComent.close()
        print("Se cerraron los archivos")

main()