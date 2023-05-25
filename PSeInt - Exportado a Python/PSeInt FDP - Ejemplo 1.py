# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripci�n: programa que imprime el resultado de una ecuaci�n de primer grado con reales
	# indica cuando su soluci�n es imposible o indeterminada
	# desarrollado por: Mario Andr�s
	# Versión 1.0
	# �ltima actualizaci�n: 28/02/23
	a = float()
	b = float()
	x = float()
	print("Ingrese el valor de a")
	a = float(input())
	print("Ingrese el valor de b")
	b = float(input())
	if a!=0:
		x = -b/a
		print("el valor de x es: ",x)
	else:
		if b!=0:
			print("Solución Imposible")
		else:
			print("Solución indeterminada")

