Algoritmo sin_titulo
	Definir dia, mes, anio como Entero
    Definir bisiesto como Logico
	
    // Entrada de datos
    Escribir "Ingrese una d�a "
    Leer dia
	Escribir "Ingrese un mes"
	Leer mes
	Escribir "Ingrese un a�o"
	Leer a�o
	
	Mientras (dia > 31 o dia < 0) o (mes > 12 o mes < 0) Hacer
		Escribir "Dato(s) invalido(s): ingrese nuevamente:."
		Escribir "  - Ingrese un d�a: "
		Leer dia
		Escribir "  - Ingrese un mes: "
		Leer mes
		Escribir "  - Ingrese un a�o: "
		Leer a�o
	FinMientras
	
    Si (dia >= 1 y dia <= 31) y (mes >= 1 y mes <= 12) y (a�o >= 1) Entonces
        bisiesto = (a�o mod 4 = 0 y (a�o mod 100 <> 0 o a�o mod 400 = 0))
        Si (mes = 2) y ((dia > 28 y no bisiesto) o (dia > 29 y bisiesto)) Entonces
            Escribir "------------- Resultado --------------"
			Escribir "   La fecha ingresada es incorrecta   "
			Escribir "--------------------------------------"
		Sino
			Si ((mes = 4 o mes = 6 o mes = 9 o mes = 11) y (dia > 30)) Entonces
				Escribir "------------- Resultado --------------"
				Escribir "   La fecha ingresada es incorrecta   "
				Escribir "--------------------------------------"
        Sino
            Escribir "------------- Resultado --------------"
			Escribir "     La fecha ingresada es v�lida     "
			Escribir "--------------------------------------"
        FinSi
    Si (dia < 1 y dia > 31) o (mes < 1 y mes > 12) y (a�o < 1) Entonces
        Escribir "Fecha inv�lida o anterior a al a�o 0"
    FinSi
FinSi
FinSi


	
FinAlgoritmo
