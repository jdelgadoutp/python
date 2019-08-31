for i in range(0,101,2):
	print("Hola # " + str(i),end=";") 

print("For con lista")

for h in ["Uno","Dos","Tres","Cuatro"]:
	print(h)	

print("For con el tamaño de un string")

email=False

for s in "j.delgado@utp.edu.co":
	print("Verica correo")
	if (s=="@"):
		email=True
		

if email:
	print("email correcto")
else:
	print("email incorrecto")

print("Otro for por bloque de 100")

for z in range(101):
	print("Hola señores de python # " + str(z))