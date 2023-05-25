Algoritmo factorial
	
	//Descripci�n: programa que calcula el producto de los primeros n�meros naturales
	//desarrollado por: Mario Andr�s
	//VERSI�N 1.0
	//�ltima actualizaci�n: 28/02/23
	
	Definir N1, N2 Como real
	Definir N, F Como Real
	
	N1 = 1
	N2 = 2
	
	Escribir "Ingrese el n�mero que quiere calcular (Natural): "
	Leer N
	
	Mientras N < 0 Hacer
		Escribir "Error: El n�mero ingresado no es natural, ingrese nuevamente: "
		Leer N
	FinMientras
	F = 1
	    Si N = 0 o N = 1
			Escribir "---------------------- Factorial ----------------------"
		    Escribir "El producto es: 1"
		    Escribir "-------------------------------------------------------"
	    Sino 
		    Para V = 1 Hasta N con paso 1 Hacer
			    F = F * V
		    FinPara
		    Escribir "---------------------- Factorial ----------------------"
		    Escribir "El producto es: " Pr = F
		    Escribir "-------------------------------------------------------"
		FinSi
		
		Mientras N <> 0 y N <> 1 Hacer
				Escribir "Desea ingresar otro valor?"
				Escribir "1: Si"
				Escribir "2: No"
				Leer Opc
				Si opc = N1 Entonces
					Leer N
				SiNo
					Si opc = N2
					Escribir "El proceso ha finalizado"
				FinSi
			FinSi
			FinMientras
FinAlgoritmo