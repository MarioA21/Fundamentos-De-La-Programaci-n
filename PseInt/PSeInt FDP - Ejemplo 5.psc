Algoritmo Día_mes
	
	Definir día, dia_inicial Como entero
	Definir Nombre Como Caracter
	Definir Fecha Como Caracter
	Escribir "Ingrese su nombre: "
	Leer Nombre
	Escribir Nombre ", Ingrese cual fue el primer día (Lunes, Martes, Miercoles, etc): "
	Leer Fecha
	Escribir Nombre ", Ingrese la fecha la cual quiere conocer: "
	Leer día
	
	Segun Fecha hacer 
		"Lunes":
			dia_inicial = 0
		"Martes":
			dia_inicial = 1
		"Miercoles":
			dia_inicial = 2
		"Jueves":
			dia_inicial = 3
		"Viernes":
			dia_inicial = 4
		"Sábado":
			dia_inicial = 5
		"Domingo":
			dia_inicial = 6
		De Otro Modo:
			dia_inicial = -32
FinSegun

día = dia_inicial + día

	Según día MOD 7 hacer;
1:
	Escribir Nombre ", La fecha corresponde a un: " "Lunes"
2:
	Escribir Nombre ", La fecha corresponde a un: " "Martes"
3:
	Escribir Nombre ", La fecha corresponde a un: " "Miercoles"
4:
	Escribir Nombre ", La fecha corresponde a un: " "Jueves"
5:
	Escribir Nombre ", La fecha corresponde a un: " "Viernes"
6:
	Escribir Nombre ", La fecha corresponde a un: " "Sábado"
7:
	Escribir Nombre ", La fecha corresponde a un: " "Domingo"
FinSegun
FinAlgoritmo