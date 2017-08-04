"""
    Modelos de Programacion II
    Binario Recursivo

"""

def binario(x):

    #Si es un digito binario, se devuelve el mismo #
    if x>=0 and x<=1:
        return x

    #Si no es un digito#
    else:
        return x%2 + 10*binario(x//2)


if __name__ == "__main__":
    x = int(input("Ingrese un entero:"))
    print(binario(x))
    
