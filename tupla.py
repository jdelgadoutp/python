
mytupla=("jairo","Juan",23,2,1981,13,13)
mylist=list(mytupla)

print (mytupla)
print (mylist)

mytupla=tuple(mylist)
print (mytupla)
print ("jairo" in mytupla)
print(mytupla.count(13))
print(len(mytupla))

mytupla1=("Jairo Andres","Delgado Lopez",17,2,1981)
nombre,apellido,dia,mes,año=mytupla1

print(nombre)
print(apellido)
print(dia)
print(mes)
print(año)



