def buscar(cad, subcad): #"uade"
    #paso las cadenas todo a minúscula.
    cad = cad.lower()
    subcad = subcad.lower()
    i=0
    cont=0
    ind=-1
    while i != -1:
       
        c=0
        while c < len(subcad) and i!= -1:
            ind = cad.find(subcad[c],ind+1) #c=0:"u" c=1:"a" ....
            c = c + 1
            i = ind
        if c == len(subcad):
            cont = cont + 1
      
    return cont
cad=input("Ingresar cadena")
subcadena=input("Ingresar sub-cadena")
p=buscar(cad, subcadena)
print(p)