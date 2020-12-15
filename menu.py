import hashlib
import os

def convertirMD5():

    print(hashlib.md5(cadena.encode('utf-8')).hexdigest())

def convertirFichMD5():
    with open(cadena, "rb") as f:
        print(hashlib.md5(f.read()).hexdigest())

def convertirSHA1():
    print(hashlib.sha1(cadena.encode('utf-8')).hexdigest())

def convertirFichSHA1():
    with open(cadena, "rb") as f:
        print(hashlib.sha1(f.read()).hexdigest())

def menu():
    opvalida = False
    num = 0
    while (not opvalida):
        try:
            num = int(input("Introduce un numero entero: \n"))
            opvalida = True
        except ValueError:
            print('Error!! Introduce un numero entero')

    return num


salir = False
opcion = 0

while not salir:

    print("1. Resumen de MD5 de una cadena")
    print("2. Resumen de MD5 de un fichero")
    print("3. Resumen de SHA1 de una cadena")
    print("4. Resumen de SHA1 de un fichero")
    print("5. Salir \n")

    print("Elige una opcion")

    opcion = menu()

    if opcion == 1:
        print("Resumen de MD5 de una cadena: \n")
        cadena=str(input("Introduce la cadena para realizar el resumen MD5: \n"))
        print("\n")
        convertirMD5()
        print("\n")
    elif opcion == 2:
        print("Resumen de MD5 de un fichero: \n")
        valido = False
        while valido == False:
            cadena=str(input("Introduce el fichero para obtener el resumen MD5: \n"))
            if os.path.isfile(cadena):
                valido = True
                convertirFichMD5()
                print("\n")
            else:
                print("El archivo especificado no existe \n")
    elif opcion == 3:
        print("Resumen de SHA1 de una cadena: \n")
        cadena=str(input("Introduce la cadena para realizar el resumen SHA1: \n"))
        convertirSHA1()
        print("\n")
    elif opcion == 4:
        print("Resumen de SHA1 de un fichero: \n")
        valido2 = False
        while valido2 == False:
            cadena = str(input("Introduce el fichero para obtener el resumen SHA1 \n"))
            if os.path.isfile(cadena):
                valido2 = True
                convertirFichSHA1()
                print("\n")
            else:
                print("El archivo especificado no existe \n")
    elif opcion == 5:
        salir = True
    else:
        print("Introduce un numero entre 1 y 4 \n")

print("\nSaliendo del menú...")