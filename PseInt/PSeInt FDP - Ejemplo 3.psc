Algoritmo area_triangulo
	//Descripci�n: programa que calcula el area de un triangulo e indica si sus valores corresponden o no
	//desarrollado por: Mario Andr�s
	//VERSI�N 1.0
	//�ltima actualizaci�n: 28/02/23
	definir a, b, c, p, area como real
	escribir "Ingresa el valor del lado a:"
	leer a;
	escribir "Ingresa el valor del lado b:"
	leer b;
	escribir "Ingresa el valor del lado c:"
	leer c;
	p = (a + b + c)/2
	si (p > a) y (p > b) y (p > c) Entonces
		area = RC(p * (p - a) * (p - b) * (p - c))
		Escribir "El area del triangulo es: " ,area;
	SiNo
		Escribir "los valores que ingres� no forman un tri�ngulo"
	FinSi
FinAlgoritmo