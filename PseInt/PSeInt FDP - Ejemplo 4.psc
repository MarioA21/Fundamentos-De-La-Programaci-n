Algoritmo dia_semana
	//Descripci�n: programa que indica el d�a seg�n la fecha ingresada
	//desarrollado por: Mario Andr�s
	//VERSI�N 1.0
	//�ltima actualizaci�n: 28/02/23
	Definir Nombre Como Caracter
	Definir d�a Como Entero
	Escribir "Ingrese su nombre: "
	Leer Nombre
	Escribir Nombre ", Ingrese la fecha: "
	leer d�a
	Seg�n d�a MOD 7 hacer;
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
	Escribir Nombre ", La fecha corresponde a un s�bado."
7:
	Escribir Nombre ", La fecha corresponde a un domingo."
FinSegun
FinAlgoritmo