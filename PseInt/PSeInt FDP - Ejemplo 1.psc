Proceso Ecua1grado
	//Descripción: programa que imprime el resultado de una ecuación de primer grado con reales
	//indica cuando su solución es imposible o indeterminada
	//desarrollado por: Mario Andrés
	//vERSIÓN 1.0
	//Última actualización: 28/02/23
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
			escribir "Solución Imposible"
		sino 
			escribir "Solución indeterminada"
		FinSi
	FinSi
FinProceso