Algoritmo dia_semana
	//Descripción: programa que indica el día según la fecha ingresada
	//desarrollado por: Mario Andrés
	//VERSIÓN 1.0
	//Última actualización: 28/02/23
	Definir Nombre Como Caracter
	Definir día Como Entero
	Escribir "Ingrese su nombre: "
	Leer Nombre
	Escribir Nombre ", Ingrese la fecha: "
	leer día
	Según día MOD 7 hacer;
1:
	Escribir Nombre ", La fecha corresponde a un lunes."
2:
	Escribir Nombre ", La fecha corresponde a un martes."
3:
	Escribir Nombre ", La fecha corresponde a un miercoles."
4:
	Escribir Nombre ", La fecha corresponde a un jueves."
5:
	Escribir Nombre ", La fecha corresponde a un viernes."
6:
	Escribir Nombre ", La fecha corresponde a un sábado."
7:
	Escribir Nombre ", La fecha corresponde a un domingo."
FinSegun
FinAlgoritmo