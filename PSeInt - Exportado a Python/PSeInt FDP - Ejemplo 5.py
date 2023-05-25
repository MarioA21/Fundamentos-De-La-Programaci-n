# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	dia = int()
	dia_inicial = int()
	nombre = str()
	fecha = str()
	print("Ingrese su nombre: ")
	nombre = input()
	print(nombre,", Ingrese cual fue el primer día (Lunes, Martes, Miercoles, etc): ")
	fecha = input()
	print(nombre,", Ingrese la fecha la cual quiere conocer: ")
	dia = int(input())
	if fecha=="Lunes":
		dia_inicial = 0
	elif fecha=="Martes":
		dia_inicial = 1
	elif fecha=="Miercoles":
		dia_inicial = 2
	elif fecha=="Jueves":
		dia_inicial = 3
	elif fecha=="Viernes":
		dia_inicial = 4
	elif fecha=="Sábado":
		dia_inicial = 5
	elif fecha=="Domingo":
		dia_inicial = 6
	else:
		dia_inicial = -32
	dia = dia_inicial+dia
	if dia%7 hacer;==1:
		print(nombre,", La fecha corresponde a un: ","Lunes")
	elif dia%7 hacer;==2:
		print(nombre,", La fecha corresponde a un: ","Martes")
	elif dia%7 hacer;==3:
		print(nombre,", La fecha corresponde a un: ","Miercoles")
	elif dia%7 hacer;==4:
		print(nombre,", La fecha corresponde a un: ","Jueves")
	elif dia%7 hacer;==5:
		print(nombre,", La fecha corresponde a un: ","Viernes")
	elif dia%7 hacer;==6:
		print(nombre,", La fecha corresponde a un: ","Sábado")
	elif dia%7 hacer;==7:
		print(nombre,", La fecha corresponde a un: ","Domingo")

