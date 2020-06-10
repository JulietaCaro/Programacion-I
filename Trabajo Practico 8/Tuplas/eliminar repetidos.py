lista = [5,4,9,5,3,5]
nueva = []
for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] != lista[j]:
            nueva.append(lista[i])
            
print(nueva)