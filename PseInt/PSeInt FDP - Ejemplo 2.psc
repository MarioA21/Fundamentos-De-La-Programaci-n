Algoritmo salario
	//Descripción: programa que calcula el salario de un individuo y sus impuestos a pagar
	//desarrollado por: Mario Andrés
	//VERSIÓN 1.0
	//Última actualización: 28/02/23
	definir Nmbr como caracter
	definir hor_tbjd, trf, impst, slr_bruto, slr_neto como real
	escribir "Ingrese su nombre";
	leer Nmbr
	escribir Nmbr ", Ingrese sus horas trabajadas";
	leer hor_tbjd
	escribir Nmbr ", Ingrese el valor de la tarifa horaria";
	leer trf
	si hor_tbjd <= 35 Entonces
		slr_bruto = hor_tbjd * trf
	sino 
		slr_bruto = (35*trf)+(hor_tbjd-35)+(1.5*trf)
	FinSi
	si slr_bruto <= 2000 Entonces
		impst = 0
	SiNo
	si slr_bruto > 2000 y slr_bruto <= 2220 Entonces
		impst = (slr_bruto - 2000) * 0.20
	sino
		impst = (slr_bruto - 2220) * 0.30 + (220 * 0.20)
		FinSi
	FinSi
	slr_neto = slr_bruto - impst
	escribir Nmbr ", Los resultados son los siguientes:" 
	escribir "Su salario bruto es: " ,slr_bruto; 
	escribir "Sus impuestos a pagar son: " ,impst;
	escribir "Su salario neto es: " ,slr_neto;
FinAlgoritmo