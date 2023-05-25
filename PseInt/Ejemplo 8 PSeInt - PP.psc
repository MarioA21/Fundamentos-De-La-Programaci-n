Algoritmo sin_titulo
	Definir dia, mes, anio como Entero
    Definir bisiesto como Logico
	
    // Entrada de datos
    Escribir "Ingrese una día "
    Leer dia
	Escribir "Ingrese un mes"
	Leer mes
	Escribir "Ingrese un año"
	Leer año
	
	Mientras (dia > 31 o dia < 0) o (mes > 12 o mes < 0) Hacer
		Escribir "Dato(s) invalido(s): ingrese nuevamente:."
		Escribir "  - Ingrese un día: "
		Leer dia
		Escribir "  - Ingrese un mes: "
		Leer mes
		Escribir "  - Ingrese un año: "
		Leer año
	FinMientras
	
    Si (dia >= 1 y dia <= 31) y (mes >= 1 y mes <= 12) y (año >= 1) Entonces
        bisiesto = (año mod 4 = 0 y (año mod 100 <> 0 o año mod 400 = 0))
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
			Escribir "     La fecha ingresada es válida     "
			Escribir "--------------------------------------"
        FinSi
    Si (dia < 1 y dia > 31) o (mes < 1 y mes > 12) y (año < 1) Entonces
        Escribir "Fecha inválida o anterior a al año 0"
    FinSi
FinSi
FinSi


	
FinAlgoritmo
