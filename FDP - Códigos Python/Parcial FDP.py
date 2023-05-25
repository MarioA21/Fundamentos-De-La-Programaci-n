# -------- Procesos --------- #
#Menú ----
nom = input("Ingrese su nombre: ")
print(nom + ", ¿Que desea realizar hoy?")
print("------------------ MENU -----------------")
print("1) Calculo de Velocidad Media")
print("2) Calculo de Aceleración")
print("3) Calculo de Velocidad Final")
print("4) Calculo de Velocidad Final al cuadrado")
print("5) Calculo de Distancia recorrida")
print("6) Calculo de distancia recorrida sin Vf ")
print("------------------------------------------")
Cod = int(input(" 1 | 2 | 3 | 4 | 5 | 6 -> "))
# ----- Fin Menu ------ #
# ----- Velocidad Media ------ #
if Cod == 1:
        Vi = float(input(nom + ", Ingrese la Velocidad incial: "))
        Vf = int(float(input(nom + ", Ingrese la velocidad final: ")))
        print("----------- Resultados ------------")
        Vm = (Vf + Vi)/2
        print("Vm = ", Vm, "Km/h")
        print("-----------------------------------")
# ------ Aceleración ------ #
elif Cod == 2:
    Vi = float(input(nom + ", Ingrese la Velocidad incial: "))
    Vf = float(input(nom + ", Ingrese la velocidad final: "))
    t = float(input((nom + ", Ingrese el tiempo: ")))
    print("----------- Resultados ------------")
    Ac = (Vf - Vi)/t
    print("Aceleración = ", Ac,"m/s")
    print("-----------------------------------")
# ------ Velocidad Final ------- #
elif Cod == 3:
    Vi = float(input(nom + ", Ingrese la Velocidad incial: "))
    Ac = float(input(nom + ", Ingrese la aceleración: "))
    t = float(input((nom + ", Ingrese el tiempo: ")))
    print("----------- Resultados ------------")
    Vf = Vi + (Ac)*(t)
    print("Vf = ", Vf,"km/h")
    print("-----------------------------------")
elif Cod == 4:
    Vi = float(input(nom + ", Ingrese la Velocidad incial: "))
    Ac = float(input(nom + ", Ingrese la aceleración: "))
    t = float(input((nom + ", Ingrese el tiempo: ")))
    print("----------- Resultados ------------")
    Vf = (Vi * Vi) + 2*((Ac)*(t))
    print("Vf^2 = ", Vf,"(km/h)^2")
    print("-----------------------------------")
elif Cod == 5:
    Vi = float(input(nom + ", Ingrese la Velocidad incial: "))
    Vf = float(input(nom + ", Ingrese la velocidad final: "))
    t = float(input((nom + ", Ingrese el tiempo: ")))
    print("----------- Resultados ------------")
    D = ((Vf + Vi)/2) * t
    print("D = ", D,"m")
    print("-----------------------------------")
elif Cod == 6:
    Vi = float(input(nom + ", Ingrese la Velocidad incial: "))
    Ac = float(input(nom + ", Ingrese la aceleración: "))
    t = float(input((nom + ", Ingrese el tiempo: ")))
    print("----------- Resultados ------------")
    D = (Vi * t) + (1/2 * ((Ac)*(t*t)))
    print("D = ", D,"m")
    print("-----------------------------------")
    # ------- Fin ------- #
elif Cod < 1:
    print("Error: Ingresó una opción no admitida en el menú")
elif Cod > 6:
    print("Error: Ingresó una opción no admitida en el menú")