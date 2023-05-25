# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	nom = str()
	a = float()
	b = float()
	c = float()
	print("Ingrese su nombre: ")
	nom = input()
	print(nom,", Ingrese el primer valor: ")
	a = float(input())
	print(nom,", Ingrese el segundo valor: ")
	b = float(input())
	print(nom,", Ingrese el tercer valor: ")
	c = float(input())
	if a==b and a==c:
		print("Todos los valores son iguales, por favor ingresar valores distintos")
	else:
		if (a==b and a!=c) or (a==c and b!=c) or (b==c and a!=b):
			print("Hay dos valores iguales, por favor ingresar valores distintos")
		else:
			if a>b and a>c:
				print("El valor más grande es: ",a)
			else:
				if b>a and b>c:
					print("El valor más grande es: ",b)
				else:
					if c>a and c>b:
						print("El valor más grande es: ",c)

