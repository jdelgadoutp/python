print("Tipo de musica")
tema=input("Genero : Valletanto;Salsa,Rock : ")

opcion=tema.lower()

if opcion in ("vallenato","salsa","rock"):
	print("Su genero seleccionado es : " + opcion)
else:
	print("No escogio una opcion valida")

print("Programa finalizado")	

