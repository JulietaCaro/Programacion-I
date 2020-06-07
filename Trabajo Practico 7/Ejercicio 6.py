# 6.La función de Ackermann A(m,n) se define de la siguiente forma:
#     n+1 si m = 0
#     A(m-1,1) si n = 0
#     A(m-1,A(m,n-1)) de otro modo
# Imprimir un cuadro con los valores que adopta la función para valores de m entre 0 y 3 y de n entre 0 y 7.

def Ackermann (m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return Ackermann(m-1,1)
    else:
        return Ackermann(m-1,Ackermann(m,n-1))
    
print(Ackermann(3,2))