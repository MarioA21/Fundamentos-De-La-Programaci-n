# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	a = float()
	b = float()
	c = float()
	x1 = float()
	x2 = float()
	r = float()
	v = float()
	i = float()
	print("Ingresa el valor de a: ")
	a = float(input())
	print("Ingresa el valor de b: ")
	b = float(input())
	print("Ingresa el valor de C: ")
	c = float(input())
	if a==0:
		print("No es una función de segundo grado")
	else:
		v = (b*b)-4*a*c
		if v==0:
			x1 = -b/(2*a)
			x2 = -b/(2*a)
			print(x1,x2)
		else:
			if v>0:
				x1 = -b+sqrt((b*b)-4*a*c)
				x2 = -b-sqrt((b*b)-4*a*c)
			else:
				if v<0:
					i = sqrt(abs(-v/(2*a)))
					r = -b/(2*a)
					print("Los resultados son: ")
					print(r," + ",i,"i")
					print(r," - ",i,"i")

