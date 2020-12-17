#corrección
import hashlib
import os
#mis funciones
def convertirMD5():

    print(hashlib.md5(cadena.encode('utf-8')).hexdigest())

def convertirFichMD5():
    with open(cadena, "rb") as f:
        print(hashlib.md5(f.read()).hexdigest())
    #rb se involucra en la lectura del fichero
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

#\n salto de linea para la ejecución, por estetica

salir = False
opcion = 0
#se muestra el menu, el while es un bucle que no termina hasta que pulsamos "5. Salir"
while not salir:

    print("1. Resumen MD5 en una cadena")
    print("2. Resumen MD5 en un fichero")
    print("3. Resumen SHA1 en una cadena")
    print("4. Resumen SHA1 en un fichero")
    print("5. Salir \n")

    print("Elige una opcion")

    opcion = menu()

    if opcion == 1:
        print("Resumen MD5 en una cadena: \n")
        cadena=str(input("Introduce la cadena para realizar el resumen MD5: \n"))
        print("\n")
        convertirMD5()
        print("\n")
    elif opcion == 2:
        print("Resumen MD5 en un fichero: \n")
        valido = False #bucles, se ejecuta mientras sea falso, cuando detecta el archivo, lo convierte en true
        while valido == False:
            cadena=str(input("Introduce el fichero para obtener el resumen MD5: \n")) #se encarga de añadir el fichero

            if os.path.isfile(cadena):
                valido = True
                convertirFichMD5()
                print("\n")
            else:
                print("El archivo no existe \n")
    elif opcion == 3:
        print("Resumen SHA1 en una cadena: \n")
        cadena=str(input("Introduce la cadena para realizar el resumen SHA1: \n"))
        convertirSHA1()
        print("\n")
    elif opcion == 4:
        print("Resumen SHA1 en un fichero: \n")
        valido2 = False
        while valido2 == False:
            cadena = str(input("Introduce el fichero para obtener el resumen SHA1 \n"))
            if os.path.isfile(cadena):
                valido2 = True
                convertirFichSHA1()
                print("\n")
            #este if es para poder atacar el contenido del fichero
            else:
                print("El archivo no existe \n")
    elif opcion == 5:
        salir = True
    else:
        print("Introduce un numero entre 1 y 5 \n")
    #si se indica un numero diferente entre 1-5, se hace un reset y nos indica la opcion valida
print("\nHas salido del menú!")
