# Escribe tus funciones abajo de esta línea
def pies_cm(pies):
    pass

def pulgadas_cm(pulgadas):
    pass

def yardas_cm(yardas):
    pass

def main():
    # Escribe tu código abajo de esta línea
    print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm") 
    opc = int(input("Introduce una opcion: "))
    valor = int(input("Introduce la cantidad: "))
    if valor >= 0:
        if opc == 1:
            print(pies_cm(valor))
        elif opc == 2:
            print(pulgadas_cm(valor))
        elif opc == 3:
            print(yardas_cm(valor))
        else:
            print("Error")
    else:
        print("Error")

if __name__ == '__main__':
    main()
