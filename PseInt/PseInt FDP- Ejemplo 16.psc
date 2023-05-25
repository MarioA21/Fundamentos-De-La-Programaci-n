Algoritmo sin_titulo
	definir Numero1, Numero2, Numero3 Como Real
	Escribir "Ingrese el primer dato"
	leer Numero1;
	Escribir "Ingrese el segundo dato"
	leer Numero2;
	Escribir "Ingrese el tercer dato"
	leer Numero3;
	
	Si Numero1 > Numero2 y Numero1>Numero3 Entonces
		Escribir "El número mayor es: ", Numero1;
	SiNo
		Si Numero2 > Numero1 y Numero2>Numero3 Entonces
		Escribir "El número mayor es: ", Numero2;
	SiNo
		Si Numero3 > Numero1 y Numero3>Numero2 Entonces
		Escribir "El número mayor es: ", Numero3;
	SiNo
		Si Numero1 = Numero2 y Numero1 = Numero3 Entonces
		Escribir "Todos los números son iguales";
	FinSi
finsi
FinSi
FinSi


FinAlgoritmo
