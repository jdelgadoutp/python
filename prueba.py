
def textos():
	print ("Hola empezamos")
	print ("1")
	print ("2")


for i in range(0,10):
	textos()


mylist=["Juan","Villa verde",3245678]

mylist.append("Casa 1")
mylist.insert(1,"Conjunto villa verde")
mylist.extend(["Jairo Andres","Adriana"])
mylist.remove("Juan")
#elimina el ultimo dato de la lista
mylist.pop()

print(mylist[:])
print(mylist.index("Jairo Andres"))
print("Juan" in mylist)
print("Ana" in mylist)