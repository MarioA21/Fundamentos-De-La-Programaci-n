# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Descripción: programa que calcula el area de un triangulo e indica si sus valores corresponden o no
	# desarrollado por: Mario Andrés
	# VERSIÓN 1.0
	# Última actualización: 28/02/23
	a = float()
	b = float()
	c = float()
	p = float()
	area = float()
	print("Ingresa el valor del lado a:")
	a = float(input())
	print("Ingresa el valor del lado b:")
	b = float(input())
	print("Ingresa el valor del lado c:")
	c = float(input())
	p = (a+b+c)/2
	if (p>a) and (p>b) and (p>c):
		area = sqrt(p*(p-a)*(p-b)*(p-c))
		print("El area del triangulo es: ",area)
	else:
		print("los valores que ingresó no forman un triángulo")

