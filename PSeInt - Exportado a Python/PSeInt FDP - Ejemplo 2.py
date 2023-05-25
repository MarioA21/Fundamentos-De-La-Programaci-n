# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Descripci�n: programa que calcula el salario de un individuo y sus impuestos a pagar
	# desarrollado por: Mario Andrés
	# VERSIÓN 1.0
	# Última actualización: 28/02/23
	nmbr = str()
	hor_tbjd = float()
	trf = float()
	impst = float()
	slr_bruto = float()
	slr_neto = float()
	print("Ingrese su nombre")
	nmbr = input()
	print(nmbr,", Ingrese sus horas trabajadas")
	hor_tbjd = float(input())
	print(nmbr,", Ingrese el valor de la tarifa horaria")
	trf = float(input())
	if hor_tbjd<=35:
		slr_bruto = hor_tbjd*trf
	else:
		slr_bruto = (35*trf)+(hor_tbjd-35)+(1.5*trf)
	if slr_bruto<=2000:
		impst = 0
	else:
		if slr_bruto>2000 and slr_bruto<=2220:
			impst = (slr_bruto-2000)*0.20
		else:
			impst = (220*0.20)+(slr_bruto-2220)
	slr_neto = slr_bruto-impst
	print(nmbr,", Los resultados son los siguientes:")
	print("Su salario bruto es: ",slr_bruto)
	print("Sus impuestos a pagar son: ",impst)
	print("Su salario neto es: ",slr_neto)

