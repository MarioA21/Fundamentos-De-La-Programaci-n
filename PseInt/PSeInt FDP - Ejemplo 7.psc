Algoritmo Ec_segundogrado
	
	//Descripción: programa que resuelve una ecuación de segundo grado, dando soluciones con números imaginarios
	//desarrollado por: Mario Andrés
	//VERSIÓN 1.0
	//Última actualización: 28/02/23
	
	Definir A, B, C Como Real
	Definir X1, X2 Como Real
	Definir R, V  Como Real 
	Definir i Como Real
	
	Escribir "Ingresa el valor de a: "
	Leer A
	Escribir "Ingresa el valor de b: "
	Leer B
	Escribir "Ingresa el valor de C: "
	Leer C
	
	Mientras A = 0 Hacer
		Escribir "No es una función de segundo grado, ingrese nuevamente: "
		Escribir "El valor de a: "
		Leer A
		Escribir "El valor de b: "
		Leer B
		Escribir "El valor de c: "
		Leer C
	FinMientras
	Si a <> 0 Entonces
		V = (B * B) - 4 * A * C
		Si V = 0 Entonces
			X1 = -B / (2 * A)
			X2 = -B / (2 * A)
			Escribir X1, X2 
		SiNo
			Si V > 0 Entonces
				X1 = -B + RC ( (B * B)  - 4 * A * C) / (2 * A)
				X2 = -B - RC ( (B * B) - 4 * A * C) / (2 * A)
				Escribir "------------------------ Resultados ------------------------"
				Escribir "X1 = " X1
				Escribir "X2 = " X2
				Escribir "------------------------------------------------------------"
			SiNo
				Si V < 0 Entonces
					i = RC (abs(-V / (2 * A) ) )
					R = -B / (2 * A)
					Escribir "------------------------ Resultados ------------------------"
					Escribir R " + " I "i"
					Escribir R " - " I "i"
					Escribir "------------------------------------------------------------"
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo