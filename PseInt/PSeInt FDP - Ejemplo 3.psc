Algoritmo area_triangulo
	//Descripción: programa que calcula el area de un triangulo e indica si sus valores corresponden o no
	//desarrollado por: Mario Andrés
	//VERSIÓN 1.0
	//Última actualización: 28/02/23
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
		Escribir "los valores que ingresó no forman un triángulo"
	FinSi
FinAlgoritmo