Proceso Ecua1grado
	//Descripci�n: programa que imprime el resultado de una ecuaci�n de primer grado con reales
	//indica cuando su soluci�n es imposible o indeterminada
	//desarrollado por: Mario Andr�s
	//vERSI�N 1.0
	//�ltima actualizaci�n: 28/02/23
	definir a,b,x Como Real
	escribir "Ingrese el valor de a"
	leer a;
	escribir "Ingrese el valor de b"
	leer b;
	si a <> 0 Entonces
		x <- -b/a
		escribir "el valor de x es: " ,x;
	SiNo
		si b <> 0 Entonces
			escribir "Soluci�n Imposible"
		sino 
			escribir "Soluci�n indeterminada"
		FinSi
	FinSi
FinProceso