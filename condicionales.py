sunota=input("Digite su nota: ")

def evaluacion(nota):
	valoracion="No Aprovado"
	if nota>=3 and nota<=5:
		valoracion="Aprovado"
	return valoracion

print(evaluacion(int(sunota)))

edad=int(input("Digite su edad: "))

def caledad(n):
	if edad<18:
		print("No puedes ingresar")
	elif edad>100:
		print("Edad incorrecta")
	else:	
		print("Puedes ingresar")	

caledad(edad)
print("Finalización programa")