mydiccionario={"Risaralda":"Pereira","Caldas":"Manizales","Quindio":"Armenia"}
mydiccionario["Valle"]="Cali"

print(mydiccionario["Risaralda"])
print(mydiccionario["Caldas"])
print(mydiccionario)
mydiccionario["Valle"]="Cartago"
print(mydiccionario)
del mydiccionario["Valle"]
print(mydiccionario)

mytupla=("Risaralda","Caldas","Quindio","Valle")
mydiccionario1={mytupla[0]:"Pereira",mytupla[1]:"Manizales",mytupla[2]:"Armenia",mytupla[3]:"Cartago"}
print(mydiccionario1)

mydiccionario2={"Nombre":"Jairo Delgado","Declaraciones":[2017,2018,2019]}
print(mydiccionario2)
print(mydiccionario.keys())
print(mydiccionario.values())
print(len(mydiccionario))