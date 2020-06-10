# Escribir una función buscarclave() que reciba como parámetros un diccionario y un valor, y devuelva una lista de claves que
# apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado.

def buscarClave(dic, valor):
    lista = []
    for dic,val in dic.items():
        if val == valor:
            lista.append(dic)
    return lista


dic = {"Juli":19,"Maria":56,"Juan":19}
print(buscarClave(dic,19))
    