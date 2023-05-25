import random
#===// Menú Opciones //===#
def menu():
    print("=======// Menú //=======")
    print("1 | Lista de valores aleatorios.")
    print("2 | Generar lista e intercambiar por -1.")
    print("3 | Eliminar número seleccionado por teclado")
    print("4 | Ingresar un valor y ordenarlo")
    print("5 | Generar la lista inicial de forma ordenada")
    print("6 | Salir del menú.")
    print("=======================")
    Opcion = int(input("| 1 | 2 | 3 | 4 | 5 | ----> "))
    return Opcion
while True:
    Opcion = menu()
#==============// 1 "Se genera una lista con valores aleatorios (1, 30)"
    if Opcion == 1:
        Lista = []
        print("=======================")
        Tmñ = int(input("Ingrese el tamaño que desea para su lista: "))
        for x in range(Tmñ):
            X = int(random.randint(0, 100))
            Lista.append(X)
        print("---------- Lista ----------")
        print(Lista)
        print("---------------------------")
#==============// 2 "El número ingresado si pertenece a la lista se cambia por -1"
    elif Opcion == 2:
        Lista2 = []
        print("=======================")
        Tamaño = int(input("Ingrese el tamaño que desea para su lista: "))
        for x in range(Tamaño):
            Valor = int(input("Ingrese el valor que desea añadir: "))
            Lista2.append(Valor)
        print("---------- Lista ----------")
        print(Lista2)
        print("---------------------------")
        val = int(input("Ingrese el(los) valor(es) que desea cambiar: "))
        while val not in Lista2:
            val = int(input("El valor no se encuentra en la lista, intente nuevamente: "))
            if val in Lista2:
                break
        while val in Lista2:
            indice = Lista2.index(val)
            Lista2[indice] = -1
        print("------ Nueva Lista ------")
        print(Lista2)    
        print("-------------------------")    
#=============// 3 Eliminar el número seleccionado por el usuario 
    elif Opcion == 3:
        Lista3 = []
        print("=======================")
        Tmño = int(input("Ingrese el tamaño que desea para su lista: "))
        for x in range(Tmño):
            Vlr = int(input("Ingrese el valor que desea añadir: "))
            Lista3.append(Vlr)
        print("---------- Lista ----------")
        print(Lista3)
        print("---------------------------")
        ValElm = int(input("Ingrese el(los) valor(es) que desea remover: "))
        while ValElm not in Lista3:
            ValElm = int(input("El valor no se encuentra en la lista, intente nuevamente: "))
            if ValElm in Lista3:
                break
        while ValElm in Lista3:
            Pos = Lista3.index(ValElm)
            Lista3.pop(Pos)
        print("------ Nueva Lista ------")
        print(Lista3)    
        print("-------------------------")   
#=============// 4 Ordenar el valor ingresado en la lista
    elif Opcion == 4:
        Lista4 = []
        print("=======================")
        Tamaño4 = int(input("Ingrese el tamaño que desea para su lista: "))
        for x in range(Tamaño4):
            Valor4 = int(input("Ingrese el valor que desea añadir: "))
            Lista4.append(Valor4)
        print("---------- Lista ----------")
        print(Lista4)
        print("---------------------------")
        ValIn = int(input("Ingrese el valor que desea añadir: "))
        Lista4.append(ValIn)
        Lista4.sort()
        print("------ Nueva Lista ------")
        print(Lista4)
        print("-------------------------")
#=============// 5 Ordenar datos ingresados por el usuario en una lista vacía
    elif Opcion == 5:
        Lista5 = []
        print("=======================")
        Tamaño5 = int(input("Ingrese el tamaño que desea para su lista: "))
        for x in range(Tamaño5):
            Valor5 = int(input("Ingrese el valor que desea añadir: "))
            Lista5.append(Valor5)
        Lista5.sort()
        print("---------- Lista ----------")
        print(Lista5)
        print("---------------------------")
#=============// Salir del menú
    elif Opcion == 6:
        print("==================================================")
        print("Gracias por utilizar el programa | Fin del proceso")
        print("==================================================")
        break
#=============// Opción no admitida/inexistente
    else:
        print("================================================================================")
        print("Error: Ingresó una opción no admitida en el menú. Ingrese nuevamente una opción:")
        print("================================================================================")
        continue
#=============// Continuar 
    if Opcion in [1, 2, 3, 4, 5]:
        respuesta = input("¿Desea continuar en el menú? | S | N | ----> ")
        if respuesta.upper() != "S":
            print("==================================================")
            print("Gracias por utilizar el programa | Fin del proceso")
            print("==================================================")
            break