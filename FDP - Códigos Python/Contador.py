Contador = 0 
Num = int(input("Digite un número: "))
while Num > 0:
    Num = int(input("Digite nuevamente: "))
    Contador = Contador + 1
    if Num <= 0:
        print("Fin del proceso")
print("Usted digitó", Contador, "números.") 