Algoritmo num_masg
	
	//Descripci�n: programa que indica cual es el dato con mayor magnitud ingresado por el usuario
	//desarrollado por: Mario Andr�s
	//VERSI�N 1.0
	//�ltima actualizaci�n: 28/02/23
	
	Definir Nom Como Caracter
	Definir A, B, C Como Real
	Escribir "Ingrese su nombre: "
	leer Nom
	Escribir Nom ", Ingrese el primer valor: "
	Leer A
	Escribir Nom ", Ingrese el segundo valor: "
	Leer B
	Escribir Nom ", Ingrese el tercer valor: "
	Leer C
	
	Si A = B y A = C Entonces
		Escribir "Todos los valores son iguales, por favor ingresar valores distintos"
	SiNo
		Si (A = B y A <> C) o (A = C Y B <> C) o (B = C y A <> B) Entonces
			Escribir "Hay dos valores iguales, por favor ingresar valores distintos"
		SiNo
			Si A > B y A > C Entonces
		Escribir "El valor m�s grande es: " A;
	SiNo
		Si B > A y B > C Entonces
			Escribir "El valor m�s grande es: " B;
		SiNo
			Si C > A y C > B Entonces
				Escribir "El valor m�s grande es: " C;
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
