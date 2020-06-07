# 2.Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.

def deBinarioADecimal(binario, exp=0):
    if binario==0:
        return 0
    else:
        return (binario%10)*2**exp + deBinarioADecimal(binario//10,exp+1)

print(deBinarioADecimal(10101101))